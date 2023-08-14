from django.urls import path

from . import views

app_name = "meals"
urlpatterns = [
    path("", views.home, name="home"),
    path("restaurant/<int:meal_id>", views.restaurant, name="restaurant"),
    path("<int:meal_id>/", views.detail, name="detail"),
    path("add/", views.add, name="add")
]
