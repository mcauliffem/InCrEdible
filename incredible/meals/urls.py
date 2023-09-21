from django.urls import path
from . import views
from .views import (
    MealListView,
    MealSearchView,
    RestaurantSearchView,
    MealDetailView,
    MealCreateView,
    RestaurantMealList
)

app_name = "meals"
urlpatterns = [
    path("", MealListView.as_view(), name="home"),
    path("meals/search/meals/<str:scope>/", MealSearchView.as_view(), name="mealsearch"),
    path("meals/search/restaurants/<str:scope>/", RestaurantSearchView.as_view(), name="restaurantsearch"),
    path("restaurant/<str:restaurant_name>/<str:scope>/", RestaurantMealList.as_view(), name="restaurant"),
    path("meals/<int:pk>/", MealDetailView.as_view(), name="meal-detail"),
    path("meals/new/", MealCreateView.as_view(), name="meal-create")
]
