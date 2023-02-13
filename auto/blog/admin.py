from django.contrib import admin

from .models import *

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brd', 'title', 'photo', 'btype', 'carcl', 'birthday', 'published')
    list_display_links = ('id', 'brd', 'title')
    search_fields = ('btype_id', 'brd', 'carcl')
    list_filter = ('brd', 'btype', 'carcl')
    prepopulated_fields = {'slug': ('title',)}


class BrandAdmin(admin.ModelAdmin):
   list_display = ('id','title')
   list_display_links = ('id', 'title')
   prepopulated_fields = {'slug': ('title',)}


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Specification)
admin.site.register(Country)
admin.site.register(CarClass)
admin.site.register(BodyType)