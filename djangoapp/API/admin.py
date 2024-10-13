from django.contrib import admin
from API.models import*

# Register your models here.
@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin):
    list_display = "id", 'angle', 'description',
    list_per_page = 60
    list_max_show_all = 100
    list_display_links = "id", 'angle', 'description',

@admin.register(TubeDiameter)
class TubeDiameterAdmin(admin.ModelAdmin):
    list_display = "id", 'diameter_meters', 'diameter_inch', 'description',
    list_per_page = 60
    list_max_show_all = 100
    list_display_links = "id", 'diameter_meters', 'diameter_inch', 'description',

@admin.register(ConstantsB)
class ConstantsBAdmin(admin.ModelAdmin):
    list_display = "id", "reynolds_min","reynolds_max","layout","b1","b2","b3","b4",
    list_per_page = 60
    list_max_show_all = 100
    list_display_links = "id", "reynolds_min","reynolds_max","layout","b1","b2","b3","b4",

@admin.register(ConstantsA)
class ConstantsBAdmin(admin.ModelAdmin):
    list_display = "id", "reynolds_min","reynolds_max","layout","a1","a2","a3","a4",
    list_per_page = 60
    list_max_show_all = 100
    list_display_links = "id", "reynolds_min","reynolds_max","layout","a1","a2","a3","a4",

