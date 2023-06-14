from django.db import models
from realtors.models import Realtor
from datetime import datetime
from django.utils import timezone

# Our Custom Model Manager
class PublishManager(models.Manager):
    use_for_related_fields = True
    def listed(self, **kwargs):
        return self.filter(list_date__lte=timezone.now(), **kwargs)
    def builded(self, **kwargs):
        return self.filter(build_year__lte=timezone.now(), **kwargs)

# Create your models here.


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    descriptions = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    # bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    area = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    types = models.CharField(max_length=50)
    build_year = models.DateTimeField(default=datetime.now, blank=True)
    rate = models.CharField(max_length=30, blank=True)


    STAT = (
        ("soldout", "product soldout"),
        ("on bid", "product on bidding"),
        ("available", "product available")
    )
    status = models.CharField(max_length=20, choices=STAT)

    objects = PublishManager()

    def __str__(self):
        return self.title
