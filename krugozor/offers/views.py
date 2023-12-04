from django.shortcuts import render
from .models import Offers


def index(requst):
    offers = Offers.objects.all()
    context = {
        'offers': offers,
    }
    return render(requst, 'offers/index.html', context)
