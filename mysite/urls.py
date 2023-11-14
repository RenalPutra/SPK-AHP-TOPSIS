from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('kriteria/', kriteriaTabel, name='kriteria'),
    path('kriteria/form/', formKriteria, name='formKriteria'),
    path('kriteria/form/edit/<int:id>', formEditKriteria, name='formEditKriteria'),
    path('kriteria/form/delete/<int:id>', deleteKriteria, name='deleteKriteria'),
    path('subkriteria/', subkriteriaTabel, name='subkriteria'),
    path('alternatif/', alternatifTabel, name='alternatif'),
    path('alternatif/form/', formAlternatif, name='formAlternatif'),
    path('alternatif/form/edit/<int:id>', formEditAlternatif, name='formEditAlternatif'),
    path('alternatif/form/delete/<int:id>', deleteAlternatif, name='deleteAlternatif'),
    path('login', login, name='login'),
]