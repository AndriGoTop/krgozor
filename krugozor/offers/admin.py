from django.contrib import admin
from .models import Offers


class OffersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city')


admin.site.register(Offers, OffersAdmin)
