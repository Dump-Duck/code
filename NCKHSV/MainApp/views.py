from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import resolve
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *

# Create your views here.

def main(request):
    house_type = house_types.objects.all()
    province = provinces.objects.all()
    district = districts.objects.all()
    ward = wards.objects.all()
    house_posts = houses_for_rent.objects.prefetch_related('house_type', 'province', 'district', 'ward').all()
    
    paginator = Paginator(house_posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    image = Image.objects.all()
    return render(request, 'Home.html', {'types': house_type, 'provinces': province, 'districts': district, 'wards': ward, 'images': image, 'page_obj': page_obj})

def index(request, id):
    house_infomation = houses_for_rent.objects.prefetch_related('house_type', 'province', 'district', 'ward').get(id=id)
    images = Image.objects.filter(houses=id)
    return render(request, 'index.html', {'house_infomation': house_infomation, 'images': images})

# Upload new post of Inn information
def upload(request):
    filter_house = house_types.objects.all()
    filter_province = provinces.objects.all()
    filter_district = districts.objects.all()
    filter_ward = wards.objects.all()
    if request.method == "POST":
        uploadForm = UploadForm(request.POST, request.FILES)
        if uploadForm.is_valid():
            house_type = house_types.objects.get(id=request.POST.get('house_type'))
            address = request.POST.get('address')
            province = provinces.objects.get(id=request.POST.get('province'))
            district = districts.objects.get(id=request.POST.get('district'))
            ward = wards.objects.get(id=request.POST.get('ward'))
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
            electric_water_heater = request.POST.get('electric_water_heater')
            cooking_area = request.POST.get('cooking_area')
            parking_area = request.POST.get('parking_area')
            car_parking_area = request.POST.get('car_parking_area')
            pet_allow = request.POST.get('pet_allow')
            
            save_house = houses_for_rent.objects.create(house_type=house_type, address=address, province=province, district=district, ward=ward,
                                                        price_per_month=price_per_month, area=area, description=description, 
                                                        price_per_water_num=price_per_water_num, price_per_electric_num=price_per_electric_num,
                                                        junk_money=junk_money, air_conditioner=air_conditioner, wardrobe=wardrobe, fan=fan, wc=wc, electric_water_heater=electric_water_heater,
                                                        cooking_area=cooking_area, parking_area=parking_area, car_parking_area=car_parking_area,
                                                        pet_allow=pet_allow, coordinates=None, thumbnail=images[0])
            save_house.save()
            
            for image in images:
                save_img = Image.objects.create(images=image, houses=save_house)
                save_img.save()
            return redirect('/')
        else:
            print(uploadForm.errors)
    else:
        uploadForm = UploadForm()
    return render(request, 'upload.html', {'uploadForm': uploadForm, 'house_types': filter_house, 'provinces': filter_province, 'districts': filter_district, 'wards': filter_ward})

def update(request, id):
    filter_house = house_types.objects.all()
    filter_province = provinces.objects.all()
    filter_district = districts.objects.all()
    filter_ward = wards.objects.all()
    image_data = Image.objects.filter(houses=id)
    house_for_rent = houses_for_rent.objects.prefetch_related('house_type', 'province', 'district', 'ward').get(id=id)
    if request.method == "POST":
        updateForm = UpdateForm(id, request.POST, request.FILES)
        if updateForm.is_valid():
            house_for_rent.house_type = house_types.objects.get(id=request.POST.get('house_type'))
            house_for_rent.address = request.POST.get('address')
            house_for_rent.province = provinces.objects.get(id=request.POST.get('province'))
            house_for_rent.district = districts.objects.get(id=request.POST.get('district'))
            house_for_rent.ward = wards.objects.get(id=request.POST.get('ward'))
            house_for_rent.price_per_month = request.POST.get('price_per_month')
            house_for_rent.area = request.POST.get('area')
            images_upload = request.FILES.getlist('images')
            house_for_rent.description = request.POST.get('description')
            house_for_rent.price_per_water_num = request.POST.get('price_per_water_num')
            house_for_rent.price_per_electric_num = request.POST.get('price_per_electric_num')
            house_for_rent.junk_money = request.POST.get('junk_money')
            house_for_rent.air_conditioner = request.POST.get('air_conditioner')
            house_for_rent.wardrobe = request.POST.get('wardrobe')
            house_for_rent.fan = request.POST.get('fan')
            house_for_rent.wc = request.POST.get('wc')
            house_for_rent.electric_water_heater = request.POST.get('electric_water_heater')
            house_for_rent.cooking_area = request.POST.get('cooking_area')
            house_for_rent.parking_area = request.POST.get('parking_area')
            house_for_rent.car_parking_area = request.POST.get('car_parking_area')
            house_for_rent.pet_allow = request.POST.get('pet_allow')
            house_for_rent.save()
            
            for i in image_data:
                for j in images_upload:
                    i.images = j
                    i.save()
            return redirect('/')
        else:
            print(updateForm.errors)
    else:
        updateForm = UpdateForm(id)
    return render(request, 'update.html', {'updateForm': updateForm, 'house_types': filter_house, 'provinces': filter_province, 'districts': filter_district, 'wards': filter_ward, 'oldData': house_for_rent})

# Delete
def delete(request, id):
    house_post = houses_for_rent.objects.get(id=id)
    if request.method == 'POST':
        house_post.delete()
        return redirect('/manage')
    return render(request, 'delete.html', {'house_post':house_post})

# Manage all posts of Inn
def manage(request):
    all_posts = houses_for_rent.objects.prefetch_related('house_type', 'province', 'district', 'ward').all()
    image = Image.objects.all()
    return render(request, 'manage.html', {'allPosts': all_posts, 'images': image})


def load_img(request):
    house_posts = houses_for_rent.objects.prefetch_related('house_type', 'province', 'district', 'ward').all()
    image = Image.objects.all()
    return render(request, 'load_img.html', {'housePosts': house_posts, 'images': image})





















