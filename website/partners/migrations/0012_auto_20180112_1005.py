# Generated by Django 2.0.1 on 2018-01-12 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0011_auto_20170912_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnerevent',
            name='other_partner',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='partnerevent',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='partners.Partner'),
        ),
    ]
