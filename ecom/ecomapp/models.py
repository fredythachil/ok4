from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    dicription = models.TextField()
    image = models.ImageField(upload_to='categories_image')

    def __str__(self):
        return (self.name)
class Product(models.Model):
    name = models.CharField(unique=True, blank=True, max_length=100)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    discription = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='product_images')
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)




