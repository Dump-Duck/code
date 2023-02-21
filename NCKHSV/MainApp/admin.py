from django.contrib import admin
from .models import *

# Register your models here.

# ! old admin signature
# admin.site.register(houseType)
# admin.site.register(userType)
# admin.site.register(accounts)
# admin.site.register(college)
# admin.site.register(accountInformations)
# admin.site.register(houseInformations)                                            

#  new admin signature
admin.site.register(house_types)
admin.site.register(provinces)
admin.site.register(districts)
admin.site.register(wards)
admin.site.register(streets)
admin.site.register(houses_for_rent)
admin.site.register(Image)