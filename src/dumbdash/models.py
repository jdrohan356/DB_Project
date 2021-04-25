from django.db import models

# Create your models here.


class Restaurants(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()


class Types(models.Model):
    account_type = models.CharField(max_length=200)


class Users(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    venmo = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    email = models.EmailField()

    account_type = models.ForeignKey(Types, on_delete=models.DO_NOTHING)


class Orders(models.Model):
    food_request = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.DO_NOTHING)
