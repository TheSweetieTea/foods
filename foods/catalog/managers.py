from django.db import models
from catalog import models as catalog_models


class CategoryManager(models.Manager):
    def published(self):
        categories = catalog_models.FoodCategory.objects.prefetch_related(
            models.Prefetch(
                'food',
                catalog_models.Food.objects.filter(is_publish=True)
            )
        )

        not_empty_categories = [
            category
            for category in categories
            if category.food.count() > 0
        ]

        return not_empty_categories
