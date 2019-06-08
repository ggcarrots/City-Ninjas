from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class HulajnogaPost(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    coordinateX = models.FloatField()
    coordinateY = models.FloatField()
    review_body = models.TextField()


    def __str__(self):
        return self.review_body[:50]

    def get_absolute_url(self):
        return reverse('review-detail', args=[str(self.id)])
