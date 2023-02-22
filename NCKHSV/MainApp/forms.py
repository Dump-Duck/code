from django import forms
from betterforms.multiform import MultiModelForm
from .models import *
from django.forms import ModelForm
    
class UploadForm(forms.Form):
    house_type = forms.CharField(label='Kiểu nhà')
    address = forms.CharField(max_length=255, label='Địa chỉ')
    province = forms.CharField(label='Tỉnh/Thành phố')
    district = forms.CharField(label='Quân/Huyện')
    ward = forms.CharField(label='Xã/Phường')
    price_per_month = forms.IntegerField(label='Giá tiền 1 tháng', help_text='VND/Tháng')
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
    cooking_area = forms.IntegerField(label='Khu vực nấu ăn')
    parking_area = forms.IntegerField(label='Bãi để xe (xe máy, xe đạp)')
    car_parking_area = forms.IntegerField(label='Bãi đỗ ô tô')
    pet_allow = forms.IntegerField(label='Cho phép nuôi thú')

# class HouseForm(ModelForm):
#     class Meta:
#         model = houses_for_rent
#         fields = ['house_type', 'address', 'province', 'district', 'ward', 'price_per_month', 'area', 'description', 'price_per_water_num', 'price_per_electric_num', 'junk_money', 'air_conditioner', 'wardrobe', 'fan', 'wc', 'cooking_area', 'parking_area', 'car_parking_area', 'pet_allow']

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
            
# class ImageUploadForm(ModelForm):
#     class Meta:
#         model = Image
#         fields = ['images']
        
# class UploadForm(MultiModelForm):
#     form_classes = {
#         'house': HouseForm,
#         'image': ImageUploadForm,
#     }