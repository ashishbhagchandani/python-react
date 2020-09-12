from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.TextField(max_length=50)
    description = models.TextField(max_length=50)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

