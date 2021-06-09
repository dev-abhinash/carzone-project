from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
class CarAdmim(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px"; >'.format(object.car_photo.url))

    thumbnail.short_description = 'car image'

    list_display = ('id', 'thumbnail', 'car_title', 'state', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    search_fields = ('id', 'car_title', 'state', 'city', 'model', 'body_style', 'fuel_type')
    list_editable = ('is_featured',)
    list_filter = ('city', 'model', 'body_style', 'fuel_type')

admin.site.register(Car, CarAdmim)
