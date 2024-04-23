from rest_framework.response import Response
from rest_framework.views import APIView
from food.models import FoodCategory, Food
from food.serializers import FoodListSerializer
from django.db.models import Prefetch, Count


class FoodAPIView(APIView):
    def get(self, request):
        categories = FoodCategory.objects.prefetch_related(
            Prefetch(
                'food',
                Food.objects.filter(is_publish=True).defer('is_publish')
            )
        )
        not_empty_categories = (
            categories
            .annotate(food_count=Count('food'))
            .filter(food_count__gt=0)
        )
        result = FoodListSerializer(not_empty_categories, many=True)
        return Response(result.data)
