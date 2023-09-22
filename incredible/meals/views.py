from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Meal

class MealListView(ListView):
    model = Meal
    template_name = 'meals/home.html'
    context_object_name = 'meal_list'
    paginate_by = 5
    order_by = '-date'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(MealListView, self).get_context_data(**kwargs)
        context['scope'] = "all"
        context['starvalues'] = [20,40,60,80,100]
        return context
    
class MealSearchView(ListView):
    model = Meal
    template_name = 'meals/search.html'
    context_object_name = 'all_search_results'
    paginate_by = 4

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
            print("flitering by query:")
            print(query)
            result = result.filter(entree_choice__icontains=query)
        result = result.order_by('entree_choice')
        return result
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(MealSearchView, self).get_context_data(**kwargs)
        context['scope'] = self.kwargs['scope']
        context['starvalues'] = [20,40,60,80,100]
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
            result = result.filter(restaurant_name__icontains=query)
        result = result.order_by('restaurant_name')
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

class MealUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Meal
    fields = ['restaurant_name', 'entree_choice', 'entree_rating', 'notes']
    template_name = 'meals/add.html'
    
    def form_valid(self, form):
        form.instance.eaten_by = self.request.user
        form.instance.entree_choice = form.instance.entree_choice.lower().title()
        form.instance.restaurant_name = form.instance.restaurant_name.lower().title()
        return super().form_valid(form)
    
    def test_func(self):
        meal = self.get_object()
        if self.request.user == meal.eaten_by:
            return True
        return False
    
class MealDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Meal
    success_url = '/'

    def test_func(self):
        meal = self.get_object()
        if self.request.user == meal.eaten_by:
            return True
        return False


class RestaurantMealList(ListView):
    model = Meal
    template_name = 'meals/search.html'
    context_object_name = 'all_search_results'
    paginate_by = 10

    def get_queryset(self):
        scope = self.kwargs['scope']
        result = super(RestaurantMealList, self).get_queryset()
        query = self.request.GET.get('search')
        if scope == "my":
            if self.request.user.is_authenticated:
                result = Meal.objects.filter(eaten_by= self.request.user).filter(restaurant_name=self.kwargs['restaurant_name'])
            else:
                return []
        else:
            result = Meal.objects.all().filter(restaurant_name=self.kwargs['restaurant_name'])
        if query:
            result = result.filter(entree_choice__icontains=query)
        result = result.order_by('entree_choice')
        return result
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(RestaurantMealList, self).get_context_data(**kwargs)
        context['type'] = 'restaurant'
        context['r_name'] = self.kwargs['restaurant_name']
        context['scope'] = self.kwargs['scope']
        context['starvalues'] = [20,40,60,80,100]
        return context
