# Generated by Django 2.2 on 2019-05-08 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pushnotifications', '0013_auto_20181111_1319'),
        ('photos', '0010_merge_20170510_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='new_album_notification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pushnotifications.ScheduledMessage'),
        ),
    ]
