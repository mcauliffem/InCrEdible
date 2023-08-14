from django.shortcuts import render, get_object_or_404

from .models import Meal

def home(request):
    latest_meal_list = Meal.objects.order_by("-date")[:5]
    context = {"latest_meal_list": latest_meal_list}
    return render(request, "meals/home.html", context)

def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    return render(request, "meals/detail.html", {"meal": meal})

def add(request):
    return render(request, "meals/add.html")
