from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *

# Create your views here.

def main(request):
    return render(request, 'Home.html')

def index(request):
    return render(request, 'index.html')

def upload(request):
    filter_house = house_types.objects.all()
    filter_province = provinces.objects.all()
    filter_district = districts.objects.all()
    filter_ward = wards.objects.all()
    if request.method == "POST":
        uploadForm = UploadForm(request.POST, request.FILES)
        if uploadForm.is_valid():
            house_type = request.POST.get('house_type')
            address = request.POST.get('address')
            province = request.POST.get('province')
            district = request.POST.get('district')
            ward = request.POST.get('ward')
            price_per_month = request.POST.get('price_per_month')
            area = request.POST.get('area')
            images = request.FILES.getlist('images')
            description = request.POST.get('description')
            price_per_water_num = request.POST.get('price_per_water_num')
            price_per_electric_num = request.POST.get('price_per_electric_num')
            junk_money = request.POST.get('junk_money')
            air_conditioner = request.POST.get('air_conditioner')
            wardrobe = request.POST.get('wardrobe')
            fan = request.POST.get('fan')
            wc = request.POST.get('wc')
            cooking_area = request.POST.get('cooking_area')
            parking_area = request.POST.get('parking_area')
            car_parking_area = request.POST.get('car_parking_area')
            pet_allow = request.POST.get('pet_allow')
            
            save_house = houses_for_rent.objects.create(house_type=house_type, address=address, province=province, district=district, ward=ward,
                                                        price_per_month=price_per_month, area=area, description=description, 
                                                        price_per_water_num=price_per_water_num, price_per_electric_num=price_per_electric_num,
                                                        junk_money=junk_money, air_conditioner=air_conditioner, wardrobe=wardrobe, fan=fan, wc=wc,
                                                        cooking_area=cooking_area, parking_area=parking_area, car_parking_area=car_parking_area,
                                                        pet_allow=pet_allow, coordinates=None)
            save_house.save()
            
            for image in images:
                name_img = image.name
                save_img = Image.objects.create(images=name_img, houses=save_house)
                save_img.save()
            return render(request,'Home.html')
        else:
            print(house_type)
            print(uploadForm.errors)
    else:
        uploadForm = UploadForm()
    return render(request, 'upload.html', {'uploadForm': uploadForm, 'house_types': filter_house, 'provinces': filter_province, 'districts': filter_district, 'wards': filter_ward})