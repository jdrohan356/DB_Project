# Generated by Django 3.2 on 2021-04-25 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dumbdash', '0007_remove_orders_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dumbdash.users'),
        ),
    ]
