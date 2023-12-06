from django.shortcuts import render
from .models import Offers, City


def index(request):
    offers = Offers.objects.all()
    offers_filter = Offers.objects.filter(city=1)
    context = {
        'offers': offers,
        'offers_filter': offers_filter,
    }
    return render(request, 'offers/index.html', context)


def index_city(request, city_id):
    offers = Offers.objects.all()
    offers_filter = Offers.objects.filter(city=city_id)
    city = City.objects.get(id=city_id)
    context = {
        'offers': offers,
        'offers_filter': offers_filter,
        'city': city,
    }
    return render(request, 'offers/index_city.html', context)


def all_offers(request, city_id):
    offers = Offers.objects.filter(city=city_id)
    offers_filter = Offers.objects.filter(city=city_id)
    city = City.objects.get(id=city_id)
    context = {
        'offers': offers,
        'offers_filter': offers_filter,
        'city': city,
    }
    return render(request, 'offers/all_offers.html', context)


def content(request, content_id):
    offers = Offers.objects.all()
    offers_get = Offers.objects.get(id=content_id)
    context = {
        'offers': offers,
        'offers_get': offers_get,
    }
    return render(request, 'offers/content.html', context)
