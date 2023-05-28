# import requests
import json
from django.conf import settings

def get_coordinates(generalAddress):
    """
    Lấy tọa độ từ địa chỉ bằng Google Maps Geocoding API
    """
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(generalAddress, settings.GOOGLE_MAPS_API_KEY)
    response = requests.get(url)
    data = json.loads(response.text)
    
    print(data)
    if data['status'] == 'OK':
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        return (lat, lng)
    else:
        return None
    