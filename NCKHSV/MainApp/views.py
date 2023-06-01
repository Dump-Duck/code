from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import resolve
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.db.models import Q
from .forms import *
from .models import *
from .utils import *
import random 

# Create your views here.
def main(request):
    # add random Inn: (enable while want to create more Inn for website)
    # x = 0
    # images = ["MainApp/static/assets/img/house_photo/img3.jpg", "MainApp/static/assets/img/house_photo/thumbnail/img1.jpg", "MainApp/static/assets/img/house_photo/thumbnail/img2.jpg"]
    # while x < 100:
    #     house_for_rent = houses_for_rent.objects.create(house_type=house_types.objects.get(id=random.randrange(1, 3)), address=random.randrange(1, 1000), district=districts.objects.get(id=random.randrange(1, 3)), ward=wards.objects.get(id=random.randrange(1, 5)), price_per_month=random.uniform(1.0, 20.0), area=random.randrange(15, 100), water_price=random.randrange(15, 100, 5), price_per_electric_num=random.randrange(2500, 6000, 500), junk_money=random.randrange(0, 24000, 6000), air_conditioner=random.choice([0, 1]), wardrobe=random.choice([0, 1]), fan=random.choice([0, 1]), wc=random.choice([0, 1]), electric_water_heater=random.choice([0, 1]), cooking_area=random.choice([0, 1]), parking_area=random.choice([0, 1]), car_parking_area=random.choice([0, 1]), pet_allow=random.choice([0, 1]), description="Cho thuê nhà trọ", thumbnail="MainApp/static/assets/img/house_photo/thumbnail/img3.jpg", lat=random.uniform(20.53, 21.23), lng=random.uniform(105.44, 106.02))
    #     for image in images:
    #         save_img = Image.objects.create(images=image, houses=house_for_rent)
    #         save_img.save()
    #     x += 1
    house_type = house_types.objects.all()
    district = districts.objects.all()
    ward = wards.objects.all()
    house_posts = houses_for_rent.objects.prefetch_related('house_type', 'district', 'ward').all()
    image = Image.objects.all()

    # Phân trang:
    paginator = Paginator(house_posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Home.html', {'types': house_type, 'districts': district, 'wards': ward, 'images': image, 'page_obj': page_obj})


# Search by text:
def search(request):
    if request.method == "POST":
        search_text = request.POST.get('search_text')
        search_result = houses_for_rent.objects.filter(Q(house_type__house_type__icontains=search_text) | Q(district__district__icontains=search_text) | Q(ward__ward__icontains=search_text) | Q(address__icontains=search_text) | Q(area__icontains=search_text) | Q(price_per_month__icontains=search_text))
        house_type = house_types.objects.all()
        district = districts.objects.all()
        ward = wards.objects.all()

        # Phân trang:
        paginator = Paginator(search_result, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'Home.html', {'types': house_type, 'districts': district, 'wards': ward, 'page_obj': page_obj, 'searches': search_result})

# Filter
def filter(request):
    if request.method == 'POST':
        house_type_filter = request.POST.get('house_type')
        district_filter = request.POST.get('district')
        ward_filter = request.POST.get('ward')
        price = request.POST.get('price')
        area = request.POST.get('area')
                
        filters = {}
        if house_type_filter:
            filters['house_type'] = house_type_filter
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
        district = districts.objects.all()
        ward = wards.objects.all()
        
        # Phân trang:
        paginator = Paginator(search_result, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'Home.html', {'types': house_type, 'districts': district, 'wards': ward, 'page_obj': page_obj, 'searches': search_result})


# Infomation of Inn what has show by id
def index(request, id):
    house_infomation = houses_for_rent.objects.prefetch_related('house_type', 'district', 'ward').get(id=id)
    images = Image.objects.filter(houses=id)
    all_comments = comments.objects.filter(house=id).order_by('date_time')
    all_replies = replies.objects.all()
    
    if request.method == 'POST':
        if 'comment' in request.POST:
            name = request.POST.get('full-name')
            email = request.POST.get('email')
            comment = request.POST.get('subject')
            phone = request.POST.get('phone')
            star_rating = request.POST.get('rating')
            house = houses_for_rent.objects.get(id=id)
            
            save_comment = comments.objects.create(name=name, mail=email, comment=comment, phone=phone, star_rating=star_rating, house=house)
            save_comment.save()
            return render(request, 'index.html', {'house_infomation': house_infomation, 'images': images, 'all_comments': all_comments, 'all_replies': all_replies})
        
        elif 'reply' in request.POST:
            comment_id = comments.objects.get(id=request.POST.get('data-comment-id'))
            content = request.POST.get('content')
            
            save_reply = replies.objects.create(comment_id=comment_id, content=content)
            save_reply.save()
            return render(request, 'index.html', {'house_infomation': house_infomation, 'images': images, 'all_comments': all_comments, 'all_replies': all_replies})
    
    return render(request, 'index.html', {'house_infomation': house_infomation, 'images': images, 'all_comments': all_comments, 'all_replies': all_replies})

# Upload new post of Inn information
def upload(request):
    filter_house = house_types.objects.all()
    filter_district = districts.objects.all()
    filter_ward = wards.objects.all()
    if request.method == "POST":
        uploadForm = UploadForm(request.POST, request.FILES)
        if uploadForm.is_valid():
            house_type = house_types.objects.get(id=request.POST.get('house_type'))
            address = request.POST.get('address')
            district = districts.objects.get(id=request.POST.get('district'))
            ward = wards.objects.get(id=request.POST.get('ward'))
            price_per_month = request.POST.get('price_per_month')
            area = request.POST.get('area')
            images = request.FILES.getlist('images')
            description = request.POST.get('description')
            water_price = request.POST.get('water_price')
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
            lat = request.POST.get('lat')
            lng = request.POST.get('lng')
            
            
            save_house = houses_for_rent.objects.create(house_type=house_type, address=address, district=district, ward=ward,
                                                        price_per_month=price_per_month, area=area, description=description, 
                                                        water_price=water_price, price_per_electric_num=price_per_electric_num,
                                                        junk_money=junk_money, air_conditioner=air_conditioner, wardrobe=wardrobe, fan=fan, wc=wc, electric_water_heater=electric_water_heater,
                                                        cooking_area=cooking_area, parking_area=parking_area, car_parking_area=car_parking_area,
                                                        pet_allow=pet_allow, coordinates=None, thumbnail=images[0], lat=lat, lng=lng)
            save_house.save()
            
            for image in images:
                save_img = Image.objects.create(images=image, houses=save_house)
                save_img.save()
            return redirect('/')
        else:
            print(uploadForm.errors)
    else:
        uploadForm = UploadForm()
    return render(request, 'upload.html', {'uploadForm': uploadForm, 'house_types': filter_house, 'districts': filter_district, 'wards': filter_ward})

# Update
def update(request, id):
    filter_house = house_types.objects.all()
    filter_district = districts.objects.all()
    filter_ward = wards.objects.all()
    house_for_rent = houses_for_rent.objects.prefetch_related('house_type', 'district', 'ward').get(id=id)
    if request.method == "POST":
        updateForm = UpdateForm(id, request.POST, request.FILES)
        if updateForm.is_valid():
            house_for_rent.house_type = house_types.objects.get(id=request.POST.get('house_type'))
            house_for_rent.address = request.POST.get('address')
            house_for_rent.district = districts.objects.get(id=request.POST.get('district'))
            house_for_rent.ward = wards.objects.get(id=request.POST.get('ward'))
            house_for_rent.price_per_month = request.POST.get('price_per_month')
            house_for_rent.area = request.POST.get('area')
            house_for_rent.description = request.POST.get('description')
            house_for_rent.water_price = request.POST.get('water_price')
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
            house_for_rent.lat = request.POST.get('lat')
            house_for_rent.lng = request.POST.get('lng')
            house_for_rent.save()
            return redirect('/')
        else:
            print(updateForm.errors)
    else:
        updateForm = UpdateForm(id)
    return render(request, 'update.html', {'updateForm': updateForm, 'house_types': filter_house,'districts': filter_district, 'wards': filter_ward, 'oldData': house_for_rent})

# Delete
def delete(request, id):
    house_post = houses_for_rent.objects.get(id=id)
    if request.method == 'POST':
        house_post.delete()
        return redirect('/manage')
    return render(request, 'delete.html', {'house_post':house_post})

# Manage all posts of Inn
def manage(request):
    all_posts = houses_for_rent.objects.prefetch_related('house_type', 'district', 'ward').all()
    image = Image.objects.all()
    return render(request, 'manage.html', {'allPosts': all_posts, 'images': image})

# Contact
def contact(request):
    return render(request, 'contact.html')

# Map
def map(request):
    all_houses = houses_for_rent.objects.all()
    return render(request, 'map.html', {'houses': all_houses})

# Show info about Inn when user right click into marker in map
def info_content(request, id):
    information = houses_for_rent.objects.prefetch_related('house_type', 'district', 'ward').get(id=id)
    info_images = Image.objects.filter(houses=id)
    return render(request, 'info.html', {'information': information, 'images': info_images})
















