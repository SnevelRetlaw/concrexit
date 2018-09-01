# Generated by Django 2.0.8 on 2018-09-01 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0023_auto_20180819_1542'),
        ('activemembers', '0026_auto_20180203_2151'),
        ('mailinglists', '0012_auto_20180203_2304'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('events', '0027_merge_20180618_1438'),
        ('members', '0023_auto_20180819_1542'),
    ]

    operations = [
        migrations.RenameModel(old_name='CommitteeMembership', new_name='MemberGroupMembership'),
        migrations.RenameField(old_name='committee', new_name='group', model_name='membergroupmembership'),
        migrations.AlterModelOptions(
            name='membergroupmembership',
            options={'verbose_name': 'group membership', 'verbose_name_plural': 'group memberships'},
        ),
        migrations.AlterField(
            model_name='membergroupmembership',
            name='since',
            field=models.DateField(default=datetime.date.today, help_text='The date this member joined in this role', verbose_name='Member since'),
        ),
        migrations.AlterField(
            model_name='membergroupmembership',
            name='until',
            field=models.DateField(blank=True, help_text="A member until this time (can't be in the future).", null=True, verbose_name='Member until'),
        ),
    ]
