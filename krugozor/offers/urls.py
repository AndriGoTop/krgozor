from django.urls import path
from .views import index, index_city, all_offers, content

urlpatterns = [
    path('', index, name='home'),
    path('city/<int:city_id>/', index_city, name='city'),
    path('all_offers/<int:city_id>/', all_offers, name='all_offers'),
    path('content/<int:content_id>/', content, name='content'),
]
