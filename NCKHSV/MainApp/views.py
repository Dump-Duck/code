from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import resolve
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .forms import *
from .models import *

# Create your views here.
def main(request):
    house_type = house_types.objects.all()
    province = provinces.objects.all()
    district = districts.objects.all()
    ward = wards.objects.all()
    house_posts = houses_for_rent.objects.prefetch_related('house_type', 'province', 'district', 'ward').all()
    image = Image.objects.all()

    # Phân trang:
    paginator = Paginator(house_posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Home.html', {'types': house_type, 'provinces': province, 'districts': district, 'wards': ward, 'images': image, 'page_obj': page_obj})


# Search by text:
def search(request):
    if request.method == "POST":
        search_text = request.POST.get('search_text')
        search_result = houses_for_rent.objects.filter(Q(house_type__house_type__icontains=search_text) | Q(province__province__icontains=search_text) | Q(district__district__icontains=search_text) | Q(ward__ward__icontains=search_text) | Q(address__icontains=search_text) | Q(area__icontains=search_text) | Q(price_per_month__icontains=search_text))
        house_type = house_types.objects.all()
        province = provinces.objects.all()
        district = districts.objects.all()
        ward = wards.objects.all()

        # Phân trang:
        paginator = Paginator(search_result, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'Home.html', {'types': house_type, 'provinces': province, 'districts': district, 'wards': ward, 'page_obj': page_obj, 'searches': search_result})

# Filter
def filter(request):
    if request.method == 'POST':
        house_type_filter = request.POST.get('house_type')
        province_filter = request.POST.get('province')
        district_filter = request.POST.get('district')
        ward_filter = request.POST.get('ward')
        price = request.POST.get('price')
        area = request.POST.get('area')
                
        filters = {}
        if house_type_filter:
            filters['house_type'] = house_type_filter
        if province_filter:
            filters['province'] = province_filter
        if district_filter:
            filters['district'] = district_filter
        if ward_filter:
            filters['ward'] = ward_filter
        if price:
            if price == '1':
                filters['price_per_month__lt'] = 3
            elif price == '2':
                filters['price_per_month__gte'] = 3
                filters['price_per_month__lt'] = 5
            elif price == '3':
                filters['price_per_month__gte'] = 5
                filters['price_per_month__lt'] = 7
            elif price == '4':
                filters['price_per_month__gt'] = 7
        if area:
            if area == '1':
                filters['area__lt'] = 30
            elif area == '2':
                filters['area__gte'] = 30
                filters['area__lt'] = 50
            elif area == '3':
                filters['area__gt'] = 50
                
        if filters:
            q_objects = Q()
            for key, value in filters.items():
                q_objects &= Q(**{key: value})
            
            search_result = houses_for_rent.objects.filter(q_objects)
        
        house_type = house_types.objects.all()
        province = provinces.objects.all()
        district = districts.objects.all()
        ward = wards.objects.all()
        
        # Phân trang:
        paginator = Paginator(search_result, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'Home.html', {'types': house_type, 'provinces': province, 'districts': district, 'wards': ward, 'page_obj': page_obj, 'searches': search_result})


# Infomation of Inn what has show by id
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

# Update
def update(request, id):
    filter_house = house_types.objects.all()
    filter_province = provinces.objects.all()
    filter_district = districts.objects.all()
    filter_ward = wards.objects.all()
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

# Service
def services(request):
    return render(request, 'services.html')

# Contact
def contact(request):
    return render(request, 'contact.html')



















