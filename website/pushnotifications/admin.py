from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from pushnotifications import models
from pushnotifications.models import Message
from utils.translation import TranslatedModelAdmin


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'active', 'date_created')
    list_filter = ('active', 'type')
    actions = ('enable', 'disable')
    ordering = ('user__first_name', )
    search_fields = ('registration_id', 'user__username',
                     'user__first_name', 'user__last_name')

    def enable(self, request, queryset):
        queryset.update(active=True)
    enable.short_description = _('Enable selected devices')

    def disable(self, request, queryset):
        queryset.update(active=False)
    disable.short_description = _('Disable selected devices')

    def name(self, obj):
        return '{} ({})'.format(obj.user.get_full_name(), obj.user.username)
    name.short_description = _('Name')
    name.admin_order_field = 'user__first_name'


@admin.register(models.Message)
class MessageAdmin(TranslatedModelAdmin):
    list_display = ('title', 'body', 'category', 'sent', 'success', 'failure')
    filter_horizontal = ('users',)
    list_filter = ('sent', 'category')

    def get_fields(self, request, obj=None):
        if obj and obj.sent:
            return ('users', 'title_nl', 'title_en', 'body_nl', 'body_en',
                    'category', 'success', 'failure')
        return ('users', 'title_nl', 'title_en', 'body_nl', 'body_en',
                'category')

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.sent:
            return ('users', 'title_nl', 'title_en', 'body_nl', 'body_en',
                    'category', 'success', 'failure')
        return super().get_readonly_fields(request, obj)

    def change_view(self, request, object_id, form_url='', **kwargs):
        obj = Message.objects.filter(id=object_id)[0]
        return super(MessageAdmin, self).change_view(
            request, object_id, form_url, {'message': obj})


@admin.register(models.ScheduledMessage)
class ScheduledMessageAdmin(TranslatedModelAdmin):
    list_display = ('title', 'body', 'time', 'category', 'sent', 'success',
                    'failure')
    date_hierarchy = 'time'
    filter_horizontal = ('users',)
    list_filter = ('sent', 'category')

    def get_fields(self, request, obj=None):
        if obj and obj.sent:
            return ('users', 'title_nl', 'title_en', 'body_nl', 'body_en',
                    'category', 'success', 'failure', 'time', 'task_id')
        return ('users', 'title_nl', 'title_en', 'body_nl', 'body_en',
                'category', 'time', 'task_id')

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.sent:
            return ('users', 'title_nl', 'title_en', 'body_nl', 'body_en',
                    'category', 'success', 'failure', 'time', 'task_id')
        return 'task_id',
