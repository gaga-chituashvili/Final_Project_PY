from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    thumbnil = models.ImageField(upload_to="final_project_python/", blank=True, null=True)
    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(default=0.00, max_digits=3, decimal_places=2)
    # stock = models.IntegerField(default=0) 
    # discount = models.DecimalField(
    #     default=0.00,
    #     max_digits=5,
    #     decimal_places=2,
    #     validators=[MinValueValidator(0.0), MaxValueValidator(100.00)]
    # )


