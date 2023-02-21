from django import forms
from .models import *

class LoginForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    
    
class UploadForm(forms.Form):
    house_type = forms.ChoiceField(label='Kiểu nhà')
    address = forms.CharField(max_length=255, label='Địa chỉ')
    province = forms.ChoiceField(label='Tỉnh/Thành phố')
    district = forms.ChoiceField(label='Quân/Huyện')
    ward = forms.ChoiceField(label='Xã/Phường')
    price_per_month = forms.IntegerField(label='Giá tiền 1 tháng')
    area = forms.IntegerField(label='Diện tích')
    images = forms.ImageField(label='Hình ảnh')
    description = forms.CharField(label='Mô tả')
    price_per_water_num = forms.IntegerField(label='Giá 1 số nước')
    price_per_electric_num = forms.IntegerField(label='Giá 1 số điện')
    junk_money = forms.IntegerField(label='Phí môi trường')
    air_conditioner = forms.IntegerField(label='Điều hòa')
    wardrobe = forms.IntegerField(label='Tủ quần áo')
    fan = forms.IntegerField(label='Quạt')
    wc = forms.IntegerField(label='WC')
    cooking_area = forms.IntegerField(label='Khu vực nấu ăn')
    parking_area = forms.IntegerField(label='Bãi để xe (xe máy, xe đạp)')
    car_parking_area = forms.IntegerField(label='Bãi đỗ ô tô')
    pet_allow = forms.IntegerField(label='Cho phép nuôi thú')
    