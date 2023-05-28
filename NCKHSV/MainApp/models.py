from django.db import models
# from django.conf import settings
# import os

# BASE_DIR = Path(__file__).resolve().parent.parent
# IMG_DIR = os.path.join(BASE_DIR, 'MainApp\\static\\assets\\img\\house_photo')
# save_img = os.path.join(settings.BASE_DIR, '\\house_photo')

# Create your models here.
# ! new models
class house_types(models.Model):
    house_type = models.CharField(max_length=255, null=False)


class districts(models.Model):
    district = models.CharField(max_length=255, null=False)
    
    
class wards(models.Model):
    ward = models.CharField(max_length=255, null=False)
    district = models.ForeignKey(districts, null=True, on_delete=models.CASCADE)
    
    
class houses_for_rent(models.Model):
    house_type = models.ForeignKey(house_types, null=False, on_delete=models.CASCADE, related_name='types')
    address = models.CharField(max_length=255, null=False)
    district = models.ForeignKey(districts, null=False, on_delete=models.CASCADE, related_name='districts')
    ward = models.ForeignKey(wards, null=False, on_delete=models.CASCADE, related_name='wards')
    price_per_month = models.FloatField(null=False)
    area = models.IntegerField(null=False)
    water_price = models.IntegerField(null=False)
    price_per_electric_num = models.IntegerField(null=False)
    junk_money = models.IntegerField(null=False)
    air_conditioner = models.IntegerField(null=False)
    wardrobe = models.IntegerField(null=False)
    fan = models.IntegerField(null=False)
    wc = models.IntegerField(null=False)
    electric_water_heater = models.IntegerField(null=True)
    cooking_area = models.IntegerField(null=False)
    parking_area = models.IntegerField(null=False)
    car_parking_area = models.IntegerField(null=False)
    pet_allow = models.IntegerField(null=False)
    description = models.TextField(null=False)
    thumbnail = models.FileField(upload_to='MainApp/static/assets/img/house_photo/thumbnail', null=True)
    
    # Update: add 2 fields "lat" & "lng" replace coordinates for storing coordinates of Inn:
    lat = models.CharField(max_length=255, null=True)
    lng = models.CharField(max_length=255, null=True)
    
    
class Image(models.Model):
    images = models.FileField(upload_to='MainApp/static/assets/img/house_photo', null=False)
    houses = models.ForeignKey(houses_for_rent, on_delete=models.CASCADE)
    
    
# Comment models
class comments(models.Model):
    name = models.CharField(max_length=255, null=False)
    mail = models.CharField(max_length=255, null=False)
    comment = models.TextField(null=False)
    phone = models.IntegerField(null=False)
    star_rating = models.IntegerField(null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    house = models.ForeignKey(houses_for_rent, on_delete=models.CASCADE)
    
    