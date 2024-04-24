from rest_framework import generics
from catalog.serializers import FoodListSerializer
from catalog.models import FoodCategory


class FoodAPIView(generics.ListAPIView):
    queryset = FoodCategory.objects.published()
    serializer_class = FoodListSerializer
