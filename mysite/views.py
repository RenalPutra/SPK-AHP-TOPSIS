from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    template_name = "index.html"
    context = {
        'nama': 'SPK AHP-TOPSIS'
        }
    return render(request, template_name, context)

def kriteriaTabel(request):
    template_name = "kriteria.html"
    kriteria = Kriteria.objects.all()
    context = {
        'nama' : 'KRITERIA',
        'kriteria' : kriteria
    }
    return render(request, template_name, context)

def subkriteriaTabel(request):
    template_name = "subkriteria.html"
    kriteria = Kriteria.objects.all()
    subkriteriaT = SubKriteria.objects.all()
    
    if request.method == 'POST':
        kolom = request.POST.get('kolom')
        bobot = int(request.POST.get('bobot'))
        baris = request.POST.get('baris')
       
        matrix_baris = SubKriteria.objects.get(codeKF=baris)

        if kolom == 'K1':
            if baris == 'K2':
                matrix_baris.k1 = round(int(subkriteriaT[0].k1)/int(bobot), 3)
                messages.success(request, "Congratulations, petak berhasil diubah")
            elif baris == 'K3':
                matrix_baris.k1 = round(int(subkriteriaT[0].k1)/int(bobot), 3)
                messages.success(request, "Congratulations, petak berhasil diubah")
            elif baris == 'K4':
                matrix_baris.k1 = round(int(subkriteriaT[0].k1)/int(bobot), 3)
                messages.success(request, "Congratulations, petak berhasil diubah")
            elif baris == 'K1':
                messages.error(request, "Sorry, petak ini tidak bisa diubah")
        elif kolom == 'K2':
            if baris == 'K3':
                matrix_baris.k2 = round(int(subkriteriaT[1].k2)/int(bobot), 3)
                messages.success(request, "Congratulations, petak berhasil diubah")
            elif baris == 'K4':
                matrix_baris.k2 = round(int(subkriteriaT[1].k2)/int(bobot), 3)
                messages.success(request, "Congratulations, petak berhasil diubah")
            elif baris == 'K2':
                messages.error(request, "Sorry, petak ini tidak bisa diubah")
            elif baris == 'K1':
                messages.error(request, "Sorry, petak ini tidak bisa diubah")
        elif kolom == 'K3':
            if baris == 'K4':
                matrix_baris.k3 = round(int(subkriteriaT[2].k3)/int(bobot), 3)
                messages.success(request, "Congratulations, petak berhasil diubah")
            elif baris == 'K1':
                messages.error(request, "Sorry, petak ini tidak bisa diubah")
            elif baris == 'K3':
                messages.error(request, "Sorry, petak ini tidak bisa diubah")
            elif baris == 'K2':
                messages.error(request, "Sorry, petak ini tidak bisa diubah")
        elif kolom == 'K4':
            if baris == 'K1':
                messages.error(request, "Sorry, petak ini tidak bisa diubah")
            elif baris == 'K2':
                messages.error(request, "Sorry, petak ini tidak bisa diubah")
            elif baris == 'K3':
                messages.error(request, "Sorry, petak ini tidak bisa diubah")
            elif baris == 'K4':
                messages.error(request, "Sorry, petak ini tidak bisa diubah")
       
        
        matrix_baris.save()
        
        return redirect(subkriteriaTabel)
    
    context = {
        'nama' : 'SUB-KRITERIA',
        'kriteria' : kriteria,
        'subkriteria' : subkriteriaT,
    }
    return render(request, template_name, context)

def formKriteria(request):
    template_name = "formKriteria.html"
    if request.method == 'POST':
        namaCode = request.POST.get('namaCode')
        namaKriteria = request.POST.get('namaKriteria')
   
        Kriteria.objects.create(
           codeK=namaCode,
           namaK=namaKriteria, 
        )
        return redirect(kriteriaTabel)
    context = {
        'nama' : 'Form Input Kriteria'
    }
    return render(request, template_name, context)

def formEditKriteria(request, id):
    kriteria_id = Kriteria.objects.get(id=id)
    template_name = "formKriteria.html"
    if request.method == 'POST':
        namaCode = request.POST.get('namaCode')
        namaKriteria = request.POST.get('namaKriteria')
        
        kriteria_id.codeK = namaCode
        kriteria_id.namaK = namaKriteria
        kriteria_id.save()
        
        return redirect(kriteriaTabel)
    context = {
        'nama' : 'Form Edit Kriteria',
        'krit_value' : kriteria_id,
    }
    return render(request, template_name, context)

def deleteKriteria(request, id):
    Kriteria.objects.get(id=id).delete()
    return redirect(kriteriaTabel)

def alternatifTabel(request):
    template_name = "alternatif.html"
    alternatif = Alternatif.objects.all()
    context = {
        'nama' : 'ALTERNATIF',
        'alternatif' : alternatif
    }
    return render(request, template_name, context)

def formAlternatif(request):
    template_name = "formAlternatif.html"
    if request.method == 'POST':
        nimA = request.POST.get('nimA')
        namaA = request.POST.get('namaA')
   
        Alternatif.objects.create(
           nimA=nimA,
           namaA=namaA, 
        )
        return redirect(alternatifTabel)
    context = {
        'nama' : 'Form Input Alternatif'
    }
    return render(request, template_name, context)

def formEditAlternatif(request, id):
    alter_id = Alternatif.objects.get(id=id)
    template_name = "formAlternatif.html"
    if request.method == 'POST':
        nimA = request.POST.get('nimA')
        namaA = request.POST.get('namaA')
   
        alter_id.nimA = nimA
        alter_id.namaA =namaA
        alter_id.save()
        return redirect(alternatifTabel)
    context = {
        'nama' : 'Form Input Alternatif',
        'alter_value' : alter_id,
    }
    return render(request, template_name, context)

def deleteAlternatif(request, id):
    Alternatif.objects.get(id=id).delete()
    return redirect(alternatifTabel)

def subAlternatifTabel(request):
    template_name = "subalternatif.html"
    alternatif_objects = Alternatif.objects.all()
    
    for d in alternatif_objects:
        sub_alternatif, created = SubAlternatif.objects.get_or_create(
            codeNim=d,
            defaults={'namaSA': d.namaA}
        )
        
    
        if not created and sub_alternatif.namaSA != d.namaA:
            sub_alternatif.namaSA = d.namaA
            sub_alternatif.save()
    
    sub_alternatif_objects = SubAlternatif.objects.all()
    
    context = {
        'nama': 'SUB-ALTERNATIF',
        'subAlternatif': sub_alternatif_objects
    }
    return render(request, template_name, context)

def formEditSubAlternatif(request, id):
    subalter_id = SubAlternatif.objects.get(id=id)
    template_name = "subalternatifedit.html"
    if request.method == 'POST':
        k1 = request.POST.get('K1')
        k2 = request.POST.get('K2')
        k3 = request.POST.get('K3')
        k4 = request.POST.get('K4')
   
        subalter_id.k1sa = k1
        subalter_id.k2sa = k2
        subalter_id.k3sa = k3
        subalter_id.k4sa = k4
        subalter_id.save()
        return redirect(subAlternatifTabel)
    context = {
        'nama' : 'Edit Sub-Alternatif',
        'subalter_value' : subalter_id,
    }
    return render(request, template_name, context)

def hasilahptopsis(request):
    template_name = "hasilahptopsis.html"
    kriteria = Kriteria.objects.all()
    context = {
        'nama' : 'AHP',
        'kriteria' : kriteria
    }
    return render(request, template_name, context)



def login(request):
    template_name = "login.html"
    context = {
        'nama' : 'Form Input',
        
    }
    return render(request, template_name, context)
