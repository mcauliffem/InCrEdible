from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Meal(models.Model):
    entree_choice = models.CharField(max_length=100)
    entree_rating = models.IntegerField(default=100)
    notes = models.TextField(default="")
    restaurant_name = models.CharField(max_length=100)
    date = models.DateTimeField("Date dined", default=timezone.now)
    eaten_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        retstr = str(self.entree_rating) + "/100 for " + str(self.entree_choice) + " at " + str(self.restaurant_name) + " on " + str(self.date)
        return retstr
    
    def get_absolute_url(self):
        return reverse('meals:meal-detail', kwargs={'pk': self.pk})


