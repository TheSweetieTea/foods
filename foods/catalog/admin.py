from django.contrib import admin
from catalog import models


admin.site.register(models.Food)
admin.site.register(models.FoodCategory)
