from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

from .models import Meal

class MealListView(ListView):
    model = Meal
    template_name = 'meals/home.html'
    context_object_name = 'meal_list'
    ordering = ['-date']
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super(MealListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-date")
        if self.request.user.is_authenticated:
            qs.filter(eaten_by = self.request.user)
        return qs
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(MealListView, self).get_context_data(**kwargs)
        context['scope'] = "all"
        return context
    
class MealSearchView(ListView):
    model = Meal
    template_name = 'meals/search.html'
    context_object_name = 'all_search_results'
    paginate_by = 10
    ordering=['entree_choice']

    def get_queryset(self):
        scope = self.kwargs['scope']
        result = super(MealSearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if scope == "my":
            if self.request.user.is_authenticated:
                result = Meal.objects.filter(eaten_by= self.request.user)
            else:
                return []
        else:
            result = Meal.objects.all()
        if query:
            result.filter(entree_choice__icontains=query)
        return result
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(MealSearchView, self).get_context_data(**kwargs)
        context['scope'] = self.kwargs['scope']
        return context
    
class RestaurantSearchView(ListView):
    model = Meal
    template_name = 'meals/restaurantsearch.html'
    context_object_name = 'all_search_results'
    paginate_by = 10

    def get_queryset(self):
        scope = self.kwargs['scope']
        result = super(RestaurantSearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if scope == "my":
            if self.request.user.is_authenticated:
                result = Meal.objects.filter(eaten_by= self.request.user).values_list('restaurant_name', flat=True).distinct()
            else:
                return []
        else:
            result = Meal.objects.values_list('restaurant_name', flat=True).distinct()
        if query:
            result.filter(restaurant_name__icontains=query)
        return result
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(RestaurantSearchView, self).get_context_data(**kwargs)
        context['scope'] = self.kwargs['scope']
        return context

class MealDetailView(DetailView):
    model = Meal
    template_name = 'meals/detail.html'

class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['restaurant_name', 'entree_choice', 'entree_rating', 'notes']
    template_name = 'meals/add.html'
    
    def form_valid(self, form):
        form.instance.eaten_by = self.request.user
        form.instance.entree_choice = form.instance.entree_choice.lower().title()
        form.instance.restaurant_name = form.instance.restaurant_name.lower().title()
        return super().form_valid(form)

class RestaurantMealList(ListView):
    model = Meal
    template_name = 'meals/search.html'
    context_object_name = 'all_search_results'
    paginate_by = 10
    ordering=['entree_choice']

    def get_queryset(self):
        result = super(RestaurantMealList, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Meal.objects.filter(restaurant_name=self.kwargs['restaurant_name']).filter(entree_choice__icontains=query)
            result = postresult
        else:
            result = Meal.objects.filter(restaurant_name=self.kwargs['restaurant_name'])
        return result
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(RestaurantMealList, self).get_context_data(**kwargs)
        context['type'] = 'restaurant'
        context['r_name'] = self.kwargs['restaurant_name']
        context['scope'] = self.kwargs['scope']
        return context
