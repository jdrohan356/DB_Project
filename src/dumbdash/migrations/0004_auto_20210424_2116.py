# Generated by Django 3.2 on 2021-04-25 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dumbdash', '0003_auto_20210424_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='order',
            new_name='food_request',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='restaurants',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='users',
            name='zip_code',
        ),
    ]
