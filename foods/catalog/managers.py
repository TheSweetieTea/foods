from django.db import models


class CategoryManager(models.Manager):
    def published(self):
        categories = self.get_queryset().annotate(
            food_count=models.Count(
                'food',
                filter=models.Q(food__is_publish=True)
            )
        ).filter(food_count__gt=0)

        return categories
