from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, path
from django.utils import timezone
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from pizzas import admin_views
from utils.admin import DoNextModelAdmin
from .models import Order, PizzaEvent, Product
from events.models import Event
from events.services import is_organiser


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available', 'restricted')


@admin.register(PizzaEvent)
class PizzaEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'orders')
    exclude = ('end_reminder',)

    def orders(self, obj):
        url = reverse('admin:pizzas_pizzaevent_details', kwargs={'pk': obj.pk})
        return format_html('<a href="{url}">{text}</a>',
                           url=url, text=_("Orders"))

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "event":
            kwargs["queryset"] = Event.objects.filter(
                end__gte=timezone.now())
        return super(PizzaEventAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/details/',
                 self.admin_site.admin_view(
                     admin_views.PizzaOrderDetails.as_view(admin=self)),
                 name='pizzas_pizzaevent_details'),
            path('<int:pk>/overview/',
                 self.admin_site.admin_view(
                     admin_views.PizzaOrderSummary.as_view(admin=self)),
                 name='pizzas_pizzaevent_overview'),
        ]
        return custom_urls + urls


@admin.register(Order)
class OrderAdmin(DoNextModelAdmin):
    list_display = ('pizza_event', 'member_first_name',
                    'member_last_name', 'product', 'payment')
    exclude = ('payment', )

    def save_model(self, request, obj, form, change):
        if not is_organiser(request.member, obj.pizza_event.event):
            raise PermissionDenied
        return super().save_model(request, obj, form, change)

    def has_view_permission(self, request, order=None):
        """Only give view permission if the user is an organiser"""
        if (order is not None and
                not is_organiser(request.member, order.pizza_event.event)):
            return False
        return super().has_view_permission(request, order)

    def has_change_permission(self, request, order=None):
        """Only give change permission if the user is an organiser"""
        if (order is not None and
                not is_organiser(request.member, order.pizza_event.event)):
            return False
        return super().has_change_permission(request, order)

    def has_delete_permission(self, request, order=None):
        """Only give delete permission if the user is an organiser"""
        if (order is not None and
                not is_organiser(request.member, order.pizza_event.event)):
            return False
        return super().has_delete_permission(request, order)
