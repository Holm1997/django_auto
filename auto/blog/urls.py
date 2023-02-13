from django.urls import path

from .views import *

urlpatterns = [
    path('', CarsList.as_view(), name='main'),
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('about/', about, name='about'),
    path('add/', AddCar.as_view(), name='addcar'),
    path('contact/', contact, name='contact'),
    path('car/<slug:car_slug>', ShowCar.as_view(), name='car'),
    path('brand/<slug:brands_slug>', CarBrands.as_view(), name='brands'),
]

