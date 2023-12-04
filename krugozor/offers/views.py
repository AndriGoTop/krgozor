from django.shortcuts import render


def index(requst):
    return render(requst, 'offers/index.html')
