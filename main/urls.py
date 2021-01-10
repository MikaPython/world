from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', category_detail, name='category'),
    path('country-detail/<int:pk>', country_detail, name='detail'),
    path('add-country/', add_country, name='add-country'),
    path('update-country/<int:pk>/', update_country, name='update-country'),
]

