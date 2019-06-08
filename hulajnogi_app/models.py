from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class HulajnogaPost(models.Model):
    # HC = 'HC'
    # CB = 'CB'
    # PT = 'PT'
    # DT = 'DT'
    # SR = 'SR'
    # MP = 'MP'
    # GS = 'GS'
    # WR = 'WR'
    # OR = 'OR'
    # POSSIBLE_STATES = [
    #     (HC, 'High Curb'),
    #     (CB, 'Cobblestones'),
    #     (PT, 'Potholes'),
    #     (DT, 'Dangerous Turn'),
    #     (SR, 'Slippery Road'),
    #     (MP, 'Many Pedestrians'),
    #     (GS, 'Good Surface'),
    #     (WR, 'Wide Road'),
    #     (OR, 'Other'),
    # ]
    POSSIBLE_STATES = [
        ('High Curb', 'High Curb'),
        ('Cobblestones', 'Cobblestones'),
        ('Potholes', 'Potholes'),
        ('Dangerous Turn', 'Dangerous Turn'),
        ('Slippery Road', 'Slippery Road'),
        ('Many Pedestrians', 'Many Pedestrians'),
        ('Good Surface', 'Good Surface'),
        ('Wide Road', 'Wide Road'),
        ('Other', 'Other'),
    ]

    creation_date = models.DateTimeField(auto_now_add=True)

    coordinateX = models.FloatField()
    coordinateY = models.FloatField()

    ideas_category = models.CharField(
        max_length=20,
        choices=POSSIBLE_STATES,
        default='Other',
    )

    review_body = models.TextField()

    adress = models.TextField()

    influence_points = models.IntegerField(default=0)


    def __str__(self):
        return self.review_body[:50]

    def get_absolute_url(self):
        return reverse('review-detail', args=[str(self.id)])
