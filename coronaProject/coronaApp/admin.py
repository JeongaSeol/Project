from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(coronaDate)

class CoronaDateAdmin(admin.ModelAdmin):
    list_display = ('date','confirmed')

admin.site.register(coronaDate, CoronaDateAdmin)

class CoronaDistrictAdmin(admin.ModelAdmin):
    list_display = ('district','confirmed')

admin.site.register(coronaDistrict, CoronaDistrictAdmin)

class VaccineRateAdmin(admin.ModelAdmin):
    list_display=('district','rate')

admin.site.register(vaccineRate, VaccineRateAdmin)

class VaccinepercoronaAdmin(admin.ModelAdmin):
    list_display=('district','rate')

admin.site.register(vaccinepercorona, VaccinepercoronaAdmin)

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','content')
admin.site.register(Board, BoardAdmin)
