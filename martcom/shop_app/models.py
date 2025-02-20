from django.db import models
from django.utils.text import slugify

# Create your models here.


class Product(models.Model):

    CATEGORY_CHOICES = (
        ("Electronics", "Electronics"),
        ("Fashion", "Fashion"),
        ("Grocery", "Grocery"),
        ("Stationary", "Stationary"),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="products")
    slug = models.SlugField(blank=True, null=True)
    category = models.CharField(
        choices=CATEGORY_CHOICES, max_length=20, blank=True, null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            if Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)
