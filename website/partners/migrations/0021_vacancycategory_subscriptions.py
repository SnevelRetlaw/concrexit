# Generated by Django 3.2.7 on 2021-10-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0039_remove_profile_language'),
        ('partners', '0020_auto_20211002_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancycategory',
            name='subscriptions',
            field=models.ManyToManyField(to='members.Member'),
        ),
    ]
