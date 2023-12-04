from django.contrib import admin
from .models import *


class OffersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city')
    list_filter = ('city',)
    search_fields = ('city',)
    list_display_links = ('id', 'title')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'stars', 'content', 'id_offer')
    list_filter = ('stars',)
    list_display_links = ('id',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
    list_display_links = ('id', 'title')


class StarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')


admin.site.register(Offers, OffersAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Stars, StarsAdmin)
