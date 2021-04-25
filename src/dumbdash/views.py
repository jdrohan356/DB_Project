from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Users, Orders, Restaurants, Types


def orders_index(request):
    orders = Orders.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'orders_index.html', context)


def order_detail(request, pk):
    order = Orders.objects.get(pk=pk)
    context = {
        'order': order
    }
    return render(request, 'order_detail.html', context)


@csrf_exempt
def order_create(request):
    if request.method == 'GET':
        restaurants = Restaurants.objects.all()
        users = Users.objects.all()
        context = {
            'restaurants': restaurants,
            'users': users
        }
        return render(request, 'order_create.html', context)
    elif request.method == 'POST':
        restaurant = Restaurants.objects.get(pk=request.POST.get('restaurant'))
        user = Users.objects.get(pk=request.POST.get('user'))
        food_request = request.POST.get('food_request')
        price = request.POST.get('price')

        order = Orders(food_request=food_request, price=price,
                       user=user, restaurant=restaurant)
        order.save()
        orders = Orders.objects.all()
        context = {
            'orders': orders
        }
        return render(request, 'orders_index.html', context)


def users_modify(request):
    if request.method == 'GET':
        users = Users.objects.all()
        context = {
            'users': users
        }
    return render(request, 'users_modify.html', context)


def dumbdash(request):
    return render(request, 'index.html', {})
