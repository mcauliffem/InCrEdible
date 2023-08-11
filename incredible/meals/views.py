from django.shortcuts import render, get_object_or_404

from .models import Meal

def index(request):
    latest_meal_list = Meal.objects.order_by("-date")[:5]
    context = {"latest_meal_list": latest_meal_list}
    return render(request, "meals/index.html", context)

def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    return render(request, "meals/detail.html", {"meal": meal})


