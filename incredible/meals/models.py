from django.db import models

# Create your models here.

class User(models.Model):
    fname_text = models.CharField(max_length=200)
    lname_text = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    def __str__(self):
        return self.user_name

class Meal(models.Model):
    entree_choice_text = models.CharField(max_length=200)
    entree_rating = models.IntegerField(default=100)
    notes = models.CharField(max_length=500, default="")
    restaurant_name_text = models.CharField(max_length=200)
    date = models.DateTimeField("Date dined")
    # eaten_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        retstr = str(self.entree_rating) + "/100 for " + str(self.entree_choice_text) + " at " + str(self.restaurant_name_text) + " on " + str(self.date)
        return retstr

