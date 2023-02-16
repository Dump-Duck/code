from django.db import models

# Create your models here.

class houseType(models.Model):
    type = models.CharField(max_length=255, null=False)
    
    
class userType(models.Model):
    type = models.CharField(max_length=150, null=False)
    
    
class accounts(models.Model):
    userName = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=150, null=False)
    accountType = models.ForeignKey(userType, related_name='account_type', on_delete=models.CASCADE)
    
    
class college(models.Model):
    collegeName = models.CharField(max_length=255, null=False)
    acronym = models.CharField(max_length=50, null=False, primary_key=True)
    location = models.TextField(null=False)
    
    
class accountInformations(models.Model):
    accountID = models.ForeignKey(accounts, related_name='ID', null=False, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=255, null=False)
    phoneNumber = models.IntegerField(null=False)
    
    
class houseInformations(models.Model):
    accountID = models.ForeignKey(accounts, null=False, on_delete=models.CASCADE)
    houseType = models.ForeignKey(houseType, null=False, on_delete=models.CASCADE)
    location = models.TextField(null=False)
    price = models.IntegerField(null=False)
    userType = models.ForeignKey(userType, null=False, on_delete=models.CASCADE)
    
    def upload_photo(self, filename):
        return f'{self.accountID}{self.uploadDate}/{filename}'
    
    image = models.ImageField(upload_to=upload_photo, null=False)
    uploadDate = models.DateTimeField(null=False)
    area = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)