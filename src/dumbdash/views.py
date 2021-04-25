from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Users, Orders, Restaurants, Types


@csrf_exempt
def orders_index(request):
    if request.method == 'POST':
        if request.POST.get('intent') == "rm":
            order = Orders.objects.get(pk=request.POST.get('id'))
            order.delete()
    orders = Orders.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'orders_index.html', context)


@csrf_exempt
def order_detail(request, pk):
    if request.method == 'GET':
        order = Orders.objects.get(pk=pk)
        restaurants = Restaurants.objects.all()
        users = Users.objects.all()
        context = {
            'order': order,
            'users': users,
            'restaurants': restaurants
        }
        return render(request, 'order_detail.html', context)
    elif request.method == 'POST':
        order = Orders(id=request.POST.get('id'),
                       food_request=request.POST.get('food_request'),
                       price=request.POST.get('price'),
                       user=Users.objects.get(pk=request.POST.get('user')),
                       restaurant=Restaurants.objects.get(pk=request.POST.get('restaurant')))
        order.save()
        return redirect('orders')


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
        order = Orders(food_request=request.POST.get('food_request'),
                       price=request.POST.get('price'),
                       user=Users.objects.get(pk=request.POST.get('user')),
                       restaurant=Restaurants.objects.get(pk=request.POST.get('restaurant')))
        order.save()
        return redirect('orders')


@csrf_exempt
def users_index(request):
    if request.method == 'POST':
        if request.POST.get('intent') == "rm":
            user = Users.objects.get(pk=request.POST.get('id'))
            user.delete()
    users = Users.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users_index.html', context)


@csrf_exempt
def user_detail(request, pk):
    if request.method == 'GET':
        user = Users.objects.get(pk=pk)
        orders = Orders.objects.filter(user=user)
        types = Types.objects.all()
        context = {
            'user': user,
            'orders': orders,
            'types': types
        }
        return render(request, 'user_detail.html', context)
    elif request.method == 'POST':
        user = Users(id=request.POST.get('id'),
                     first_name=request.POST.get('first_name'),
                     last_name=request.POST.get('last_name'),
                     username=request.POST.get('username'),
                     password=request.POST.get('password'),
                     address=request.POST.get('address'),
                     phone_number=request.POST.get('phone_number'),
                     email=request.POST.get('email'),
                     venmo=request.POST.get('venmo'),
                     account_type=Types.objects.get(pk=request.POST.get('account_type')))
        user.save()
        return redirect('users')


@csrf_exempt
def restaurants_index(request):
    if request.method == 'POST':
        if request.POST.get('intent') == "rm":
            restaurant = Restaurants.objects.get(pk=request.POST.get('id'))
            restaurant.delete()
    restaurants = Restaurants.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants_index.html', context)


@csrf_exempt
def restaurant_detail(request, pk):
    if request.method == 'GET':
        restaurant = Restaurants.objects.get(pk=pk)
        orders = Orders.objects.filter(restaurant=restaurant)
        context = {
            'restaurant': restaurant,
            'orders': orders
        }
        return render(request, 'restaurant_detail.html', context)
    elif request.method == 'POST':
        restaurant = Restaurants(id=request.POST.get('id'),
                                 name=request.POST.get('name'),
                                 phone_number=request.POST.get('phone_number'))
        restaurant.save()
        return redirect('restaurants')
