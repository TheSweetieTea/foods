from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.FoodAPIView.as_view(), name='foods')
]
