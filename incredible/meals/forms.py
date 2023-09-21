from django import forms
from .models import Meal

class AddMealForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = ['restaurant_name', 'entree_choice', 'entree_rating', 'notes']
