from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Meal(models.Model):
    entree_choice_text = models.CharField(max_length=100)
    entree_rating = models.IntegerField(default=100)
    notes = models.TextField(default="")
    restaurant_name_text = models.CharField(max_length=100)
    date = models.DateTimeField("Date dined", default=timezone.now)
    eaten_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        retstr = str(self.entree_rating) + "/100 for " + str(self.entree_choice_text) + " at " + str(self.restaurant_name_text) + " on " + str(self.date)
        return retstr

