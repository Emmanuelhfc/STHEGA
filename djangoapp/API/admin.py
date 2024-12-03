from collections.abc import Sequence
from typing import Any
from django.contrib import admin
from django.db.models.fields import Field
from django.forms.fields import TypedChoiceField
from django.http import HttpRequest
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

@admin.register(LiLo)
class LiLoAdmin(admin.ModelAdmin):
    list_per_page = 60
    list_max_show_all = 100
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    def get_list_display_links(self, request: HttpRequest, list_display: Sequence[str]) -> Sequence[str] | None:
        return [field.name for field in self.model._meta.fields]

@admin.register(TubeCount)
class TubeCountAdmin(admin.ModelAdmin):
    list_per_page = 300
    list_max_show_all = 600
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    def get_list_display_links(self, request: HttpRequest, list_display: Sequence[str]) -> Sequence[str] | None:
        return [field.name for field in self.model._meta.fields]
    
@admin.register(Pitch)
class PitchAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    def get_list_display_links(self, request: HttpRequest, list_display: Sequence[str]) -> Sequence[str] | None:
        return [field.name for field in self.model._meta.fields]

@admin.register(DeltaSB)
class DeltaSBAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    def get_list_display_links(self, request: HttpRequest, list_display: Sequence[str]) -> Sequence[str] | None:
        return [field.name for field in self.model._meta.fields]

@admin.register(NozzleDiameter)
class NozzleDiameterAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    def get_list_display_links(self, request: HttpRequest, list_display: Sequence[str]) -> Sequence[str] | None:
        return [field.name for field in self.model._meta.fields]
    
@admin.register(InputsShellAndTube)
class InputsShellAndTubeAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    def get_list_display_links(self, request: HttpRequest, list_display: Sequence[str]) -> Sequence[str] | None:
        return [field.name for field in self.model._meta.fields]

    def formfield_for_choice_field(self, db_field, request: HttpRequest | None, **kwargs: Any) -> TypedChoiceField:
        if db_field.name == "Ds_inch":
            kwargs['choices'] = [(value, value) for value in TubeCount.objects.values_list('Ds_inch', flat=True).distinct()]
        return super().formfield_for_choice_field(db_field, request, **kwargs)
    
@admin.register(TubeInternDiameter)
class TubeInternDiameterAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    def get_list_display_links(self, request: HttpRequest, list_display: Sequence[str]) -> Sequence[str] | None:
        return [field.name for field in self.model._meta.fields]
    
@admin.register(TubeMaterial)
class TubeMaterialsAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    def get_list_display_links(self, request: HttpRequest, list_display: Sequence[str]) -> Sequence[str] | None:
        return [field.name for field in self.model._meta.fields]
    
@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    def get_list_display_links(self, request: HttpRequest, list_display: Sequence[str]) -> Sequence[str] | None:
        return [field.name for field in self.model._meta.fields]