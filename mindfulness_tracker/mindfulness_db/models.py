from django.db import models


class MeditationMetrics(models.Model):
    total_time = models.IntegerField()
