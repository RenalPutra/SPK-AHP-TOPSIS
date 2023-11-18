from django.contrib import admin
from .models import *
# Register your models here.

class KriteriaAdmin(admin.ModelAdmin):
    list_display = ['codeK', "namaK"]

class SubKriteriaAdmin(admin.ModelAdmin):
    list_display = ['codeKF', "k1", "k2", "k3", "k4"]

class AlternatifAdmin(admin.ModelAdmin):
    list_display = ['nimA', "namaA"]

class SubAlternatifAdmin(admin.ModelAdmin):
    list_display = ['codeNim', 'namaSA',"k1sa", "k2sa", "k3sa", "k4sa"]
class BobotPrioritasAdmin(admin.ModelAdmin):
    list_display = ['codeBF', 'bobotPrio',"k1", "k2", "k3", "k4"]

class BobotKonsistensiAdmin(admin.ModelAdmin):
    list_display = ['codeBKF',"k1", "k2", "k3", "k4", "bobotkons"]
    
admin.site.register(Kriteria, KriteriaAdmin)
admin.site.register(SubKriteria, SubKriteriaAdmin)
admin.site.register(Alternatif, AlternatifAdmin)
admin.site.register(SubAlternatif, SubAlternatifAdmin)
admin.site.register(BobotPrioritas, BobotPrioritasAdmin)
admin.site.register(BobotKonsistensi, BobotKonsistensiAdmin)