from django.contrib import admin
from food import models

# Register your models here.
admin.site.register(models.Food)
admin.site.register(models.FoodCategory)
