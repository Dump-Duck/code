import os
from django.db import models
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = os.path.join(BASE_DIR, 'MainApp/static/assets/img/house_photo')

# Create your models here.

# !old models
# class houseType(models.Model):
#     type = models.CharField(max_length=255, null=False)
    
    
# class userType(models.Model):
#     type = models.CharField(max_length=150, null=False)
    
    
# class accounts(models.Model):
#     userName = models.CharField(max_length=255, null=False)
#     password = models.CharField(max_length=150, null=False)
#     accountType = models.ForeignKey(userType, related_name='account_type', on_delete=models.CASCADE)
    
    
# class college(models.Model):
#     collegeName = models.CharField(max_length=255, null=False)
#     acronym = models.CharField(max_length=50, null=False, primary_key=True)
#     location = models.TextField(null=False)
    
    
# class accountInformations(models.Model):
#     accountID = models.ForeignKey(accounts, related_name='ID', null=False, on_delete=models.CASCADE)
#     fullName = models.CharField(max_length=255, null=False)
#     phoneNumber = models.IntegerField(null=False)
    
    
# class houseInformations(models.Model):
#     accountID = models.ForeignKey(accounts, null=False, on_delete=models.CASCADE)
#     houseType = models.ForeignKey(houseType, null=False, on_delete=models.CASCADE)
#     location = models.TextField(null=False)
#     price = models.IntegerField(null=False)
#     userType = models.ForeignKey(userType, null=False, on_delete=models.CASCADE)
    
#     def upload_photo(self, filename):
#         return f'{self.accountID}{self.uploadDate}/{filename}'
    
#     image = models.ImageField(upload_to=upload_photo, null=False)
#     uploadDate = models.DateTimeField(null=False)
#     area = models.CharField(max_length=255, null=False)
#     description = models.TextField(null=False)


# ! new models
class house_types(models.Model):
    house_type = models.CharField(max_length=255, null=False)
    

class streets(models.Model):
    street = models.CharField(max_length=255, null=False)
    
    
class wards(models.Model):
    ward = models.CharField(max_length=255, null=False)
    streets = models.ManyToManyField(streets, null=False)
    
    
class districts(models.Model):
    district = models.CharField(max_length=255, null=False)
    wards = models.ManyToManyField(wards, null=False)
    
    
class provinces(models.Model):
    province = models.CharField(max_length=255, null=False)
    districts = models.ManyToManyField(districts, null=False)
    
    
class houses_for_rent(models.Model):
    house_type = models.ForeignKey(house_types, null=False, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=False)
    province = models.ForeignKey(provinces, null=False, on_delete=models.CASCADE)
    district = models.ForeignKey(districts, null=False, on_delete=models.CASCADE)
    ward = models.ForeignKey(wards, null=False, on_delete=models.CASCADE)
    street = models.ForeignKey(streets, null=False, on_delete=models.CASCADE)
    price_per_month = models.IntegerField(null=False)
    area = models.IntegerField(null=False)
    images = models.ManyToManyField('Image')
    description = models.TextField(null=False)
    price_per_water_num = models.IntegerField(null=False)
    price_per_electric_num = models.IntegerField(null=False)
    junk_money = models.IntegerField(null=False)
    air_conditioner = models.IntegerField(null=False)
    wardrobe = models.IntegerField(null=False)
    fan = models.IntegerField(null=False)
    wc = models.IntegerField(null=False)
    cooking_area = models.IntegerField(null=False)
    parking_area = models.IntegerField(null=False)
    car_parking_area = models.IntegerField(null=False)
    pet_allow = models.IntegerField(null=False)
    coordinates = models.CharField(max_length=255, null=False)
    
    
class Image(models.Model):
    
    def upload_photo(self, filename):
        return f'{IMG_DIR}/{filename}'
    
    images = models.ImageField(upload_to=upload_photo, null=False)
    
    
class admin_account(models.Model):
    admin_account_name = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)