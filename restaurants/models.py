from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_24_hours = models.BooleanField(default=False)
    cuisine_type = models.CharField(max_length=50, blank=True, null=True)  # New field
    rating = models.FloatField(null=True, blank=True)  # New field
    location = gis_models.PointField(geography=True)
    date_added = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name