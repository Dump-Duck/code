from django import forms
from .models import *
from django.forms import ModelForm
    
class UploadForm(forms.Form):
    house_type = forms.CharField(label='Kiểu nhà')
    address = forms.CharField(max_length=255, label='Địa chỉ')
    province = forms.CharField(label='Tỉnh/Thành phố')
    district = forms.CharField(label='Quân/Huyện')
    ward = forms.CharField(label='Xã/Phường')
    price_per_month = forms.FloatField(label='Giá tiền 1 tháng', help_text='VND/Tháng')
    area = forms.IntegerField(label='Diện tích', help_text='m2')
    images = forms.FileField(label='Hình ảnh')
    description = forms.CharField(label='Mô tả')
    price_per_water_num = forms.IntegerField(label='Giá 1 số nước', help_text='VND/Số')
    price_per_electric_num = forms.IntegerField(label='Giá 1 số điện', help_text='VND/Số')
    junk_money = forms.IntegerField(label='Phí môi trường', help_text='VND/Người')
    air_conditioner = forms.IntegerField(label='Điều hòa')
    wardrobe = forms.IntegerField(label='Tủ quần áo')
    fan = forms.IntegerField(label='Quạt')
    wc = forms.IntegerField(label='WC')
    electric_water_heater = forms.IntegerField(label='Nóng lạnh')
    cooking_area = forms.IntegerField(label='Khu vực nấu ăn')
    parking_area = forms.IntegerField(label='Bãi để xe (xe máy, xe đạp)')
    car_parking_area = forms.IntegerField(label='Bãi đỗ ô tô')
    pet_allow = forms.IntegerField(label='Cho phép nuôi thú')

class UpdateForm(forms.Form):
    house_type = forms.CharField(label='Kiểu nhà')
    address = forms.CharField(max_length=255, label='Địa chỉ')
    province = forms.CharField(label='Tỉnh/Thành phố')
    district = forms.CharField(label='Quân/Huyện')
    ward = forms.CharField(label='Xã/Phường')
    price_per_month = forms.FloatField(label='Giá tiền 1 tháng', help_text='VND/Tháng')
    area = forms.IntegerField(label='Diện tích', help_text='m2')
    images = forms.FileField(label='Hình ảnh')
    description = forms.CharField(label='Mô tả')
    price_per_water_num = forms.IntegerField(label='Giá 1 số nước', help_text='VND/Số')
    price_per_electric_num = forms.IntegerField(label='Giá 1 số điện', help_text='VND/Số')
    junk_money = forms.IntegerField(label='Phí môi trường', help_text='VND/Người')
    air_conditioner = forms.IntegerField(label='Điều hòa')
    wardrobe = forms.IntegerField(label='Tủ quần áo')
    fan = forms.IntegerField(label='Quạt')
    wc = forms.IntegerField(label='WC')
    electric_water_heater = forms.IntegerField(label='Nóng lạnh')
    cooking_area = forms.IntegerField(label='Khu vực nấu ăn')
    parking_area = forms.IntegerField(label='Bãi để xe (xe máy, xe đạp)')
    car_parking_area = forms.IntegerField(label='Bãi đỗ ô tô')
    pet_allow = forms.IntegerField(label='Cho phép nuôi thú')
    
    def __init__(self, id,*args, **kwargs):
        super().__init__(*args, **kwargs)
        data = houses_for_rent.objects.prefetch_related('house_type', 'province', 'district', 'ward').get(id=id)
        img_data = Image.objects.filter(houses=id)
        self.fields['house_type'].initial = data.house_type.house_type
        self.fields['address'].initial = data.address
        self.fields['province'].initial = data.province.province
        self.fields['district'].initial = data.district.district
        self.fields['ward'].initial = data.ward.ward
        self.fields['price_per_month'].initial = data.price_per_month
        self.fields['area'].initial = data.area
        # self.fields['images'].widget['value'] = img_data.images
        list_imgs = []
        for image in img_data:
            list_imgs.append(image.images.__str__())
            
        self.fields['images'].initial = list_imgs
        self.fields['description'].initial = data.description
        self.fields['price_per_water_num'].initial = data.price_per_water_num
        self.fields['price_per_electric_num'].initial = data.price_per_electric_num
        self.fields['junk_money'].initial = data.junk_money
        self.fields['air_conditioner'].initial = data.air_conditioner
        self.fields['wardrobe'].initial = data.wardrobe
        self.fields['fan'].initial = data.fan
        self.fields['wc'].initial = data.wc
        self.fields['electric_water_heater'].initial = data.electric_water_heater
        self.fields['cooking_area'].initial = data.cooking_area
        self.fields['parking_area'].initial = data.parking_area
        self.fields['car_parking_area'].initial = data.car_parking_area
        self.fields['pet_allow'].initial = data.pet_allow