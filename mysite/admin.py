from django.contrib import admin
from .models import *
# Register your models here.

class KriteriaAdmin(admin.ModelAdmin):
    list_display = ['codeK', "namaK"]

class SubKriteriaAdmin(admin.ModelAdmin):
    list_display = ['codeKF', "k1", "k2", "k3", "k4"]

class AlternatifAdmin(admin.ModelAdmin):
    list_display = ['nimA', "namaA"]
    
admin.site.register(Kriteria, KriteriaAdmin)
admin.site.register(SubKriteria, SubKriteriaAdmin)
admin.site.register(Alternatif, AlternatifAdmin)