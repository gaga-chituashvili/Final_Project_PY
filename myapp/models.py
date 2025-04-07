from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User

class Product(models.Model):
    thumbnil = models.ImageField(upload_to="final_project_python/", blank=True, null=True)
    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def rating(self):
        reviews = self.review_set.all()
        if reviews:
            return sum([review.rating for review in reviews]) / len(reviews)
        return ""
    
    def get_stars(self):
         rating = self.rating() 
    
         if not rating: 
            return ""

         return ' <i class="fa-solid fa-star font-red"></i>' * int(self.rating()) + '<i class="fa-solid fa-star-half"></i>' *  (self.rating() % 1 > 0 ) + '<i class="fa-regular fa-star"></i>' * (4 - int(self.rating()))



class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    rating = models.DecimalField(
        max_digits=3,  
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True,null=True)



    

