# Generated by Django 3.2 on 2021-04-25 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dumbdash', '0004_auto_20210424_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurants',
            old_name='address',
            new_name='phone_number',
        ),
    ]
