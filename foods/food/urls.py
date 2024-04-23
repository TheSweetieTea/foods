from django.urls import path
from food import views


urlpatterns = [
    path('', views.FoodAPIView.as_view())
]
