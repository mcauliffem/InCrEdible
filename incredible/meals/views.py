from django.shortcuts import render, get_object_or_404

from .models import Meal

def home(request):
    latest_meal_list = Meal.objects.order_by("-date")[:5]
    context = {"meal_list": latest_meal_list, "type":"latest"}
    return render(request, "meals/home.html", context)

def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    return render(request, "meals/detail.html", {"meal": meal})

def add(request):
    return render(request, "meals/add.html")

def restaurant(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    restaurant_name = meal.restaurant_name_text
    restaurant_meal_list = Meal.objects.filter(restaurant_name_text=restaurant_name)
    context = {"meal_list": restaurant_meal_list, "type":"restaurant", "restaurant_name":restaurant_name}
    return render(request, "meals/home.html", context)
