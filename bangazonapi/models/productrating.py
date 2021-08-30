from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .customer import Customer

# from .product import Product -- this line and the line below were in the deleted ratings model, which this model replicates (other than these two differences)
# product = models.ForeignKey(Product, on_delete=models.DO_NOTHING,)



class ProductRating(models.Model):

    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="ratings")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

class Meta:
    verbose_name = ("productrating")
    verbose_name_plural = ("productratings")

def __str__(self):
    return self.rating
