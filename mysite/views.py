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
    subkriteriaT = SubKriteria.objects.all()
    # total code untuk Matriks Perbandingan Kriteria
    arrSub1  = []
    arrSub2  = []
    arrSub3  = []
    arrSub4  = []
    totalarr = []
    for index, i in enumerate(subkriteriaT) :
        arrSub1.append(float(i.k1))
        arrSub2.append(float(i.k2))
        arrSub3.append(float(i.k3))
        arrSub4.append(float(i.k4))
    totalarr.extend([sum(arrSub1), sum(arrSub2), sum(arrSub3), sum(arrSub4)])  
    
    # Matriks bobot prioritas
    BPr1 = []
    BPr2 = []
    BPr3 = []
    BPr4 = []
    realBpr = []

    for index, j in enumerate(subkriteriaT):
        br1 = round(float(j.k1) / totalarr[0], 3)
        br2 = round(float(j.k2) / totalarr[1], 3)
        br3 = round(float(j.k3) / totalarr[2], 3)
        br4 = round(float(j.k4) / totalarr[3], 3)

        BPr1.append(float(br1))
        BPr2.append(float(br2))
        BPr3.append(float(br3))
        BPr4.append(float(br4))

    allBr = [BPr1, BPr2, BPr3, BPr4]

    transposed_allBr = list(map(list, zip(*allBr)))

    realBpr = [
        round(sum(transposed_allBr[0]) / 4, 3),
        round(sum(transposed_allBr[1]) / 4, 3),
        round(sum(transposed_allBr[2]) / 4, 3),
        round(sum(transposed_allBr[3]) / 4, 3)
    ]
    # print(realBpr)
    

  
    for j, br_data in zip(kriteria, transposed_allBr):
        boboPR, created = BobotPrioritas.objects.get_or_create(
            codeBF=j,
            defaults={
                'bobotPrio': 0,
                'k1': 0,
                'k2': 0,
                'k3': 0,
                'k4': 0,
            }
        )

        if br_data and len(br_data) == 4:
            boboPR, created = BobotPrioritas.objects.update_or_create(
                codeBF=j,
                defaults={
                    'k1': br_data[0],
                    'k2': br_data[1],
                    'k3': br_data[2],
                    'k4': br_data[3],
                }
            )

        boboPR.save()

    for a, b in zip(kriteria, realBpr):
        objects = BobotPrioritas.objects.filter(codeBF=a)
        for obj in objects:
            obj.bobotPrio = b
            obj.save()
    
        
    bprall = BobotPrioritas.objects.all()    
    
    #Matriks Konsistensi Kriteria
    
    prioritasCase = BobotPrioritas.objects.values('bobotPrio')
    listKons = []
    for h in prioritasCase:
        listKons.append(float(h["bobotPrio"]))
    
    
    for j, k in zip(kriteria,subkriteriaT):
        boboKN, created = BobotKonsistensi.objects.get_or_create(
            codeBKF=j,
            defaults={
                'k1': 0,
                'k2': 0,
                'k3': 0,
                'k4': 0,
                'bobotkons': 0,
            }
        )
        

        if not created :
            boboKN, created = BobotKonsistensi.objects.update_or_create(
                codeBKF=j,
                defaults={
                    'k1': round(float(k.k1)*listKons[0],3),
                    'k2': round(float(k.k2)*listKons[1],3),
                    'k3': round(float(k.k3)*listKons[2],3),
                    'k4': round(float(k.k4)*listKons[3],3),
                }
            )
        boboKN.save()
    bkonsen = BobotKonsistensi.objects.all()
    
    BKn1 = []
    BKn2 = []
    BKn3 = []
    BKn4 = []
    listBobotKon = []
    for index, k in enumerate(bkonsen):
        bn1 = float(k.k1)
        bn2 = float(k.k2)
        bn3 = float(k.k3)
        bn4 = float(k.k4)

        BKn1.append(float(bn1))
        BKn2.append(float(bn2))
        BKn3.append(float(bn3))
        BKn4.append(float(bn4))
    
    listBobotKon.extend([BKn1,BKn2,BKn3,BKn4])
    transposed_konsBot = list(map(list, zip(*listBobotKon)))
    
    
    
    realBKN = [
        round(sum(transposed_konsBot[0]) / listKons[0], 3),
        round(sum(transposed_konsBot[1]) / listKons[1], 3),
        round(sum(transposed_konsBot[2]) / listKons[2], 3),
        round(sum(transposed_konsBot[3]) / listKons[3], 3)
    ]
    
   
        
    for a, b in zip(kriteria, realBKN):
        objects = BobotKonsistensi.objects.filter(codeBKF=a)
        for obj in objects:
            obj.bobotkons = b
            obj.save()
    
    # perhitungan CI, RI, CR
    print(len(kriteria))
    lambdad = sum(realBKN)/len(kriteria)
    CI = round((lambdad-len(kriteria))/(len(kriteria)-1),3)
    if len(kriteria) == 1:
        R = 0
    elif len(kriteria) == 2:
        R = 0
    elif len(kriteria) == 3:
        R = 0.58
    elif len(kriteria) == 4:
        R = 0.9
    elif len(kriteria) == 5:
        R = 1.12
    elif len(kriteria) == 6:
        R = 1.24
    elif len(kriteria) == 7:
        R = 1.32
    elif len(kriteria) == 8:
        R = 1.41
    elif len(kriteria) == 9:
        R = 1.46
    elif len(kriteria) == 10:
        R = 1.49
    elif len(kriteria) == 11:
        R = 1.51
    elif len(kriteria) == 12:
        R = 1.48
    elif len(kriteria) == 13:
        R = 1.56
    elif len(kriteria) == 14:
        R = 1.57
    elif len(kriteria) == 15:
        R = 1.59
    
    CR = round(CI/R,3)
    print(CR)
        
            

  
    context = {
        'nama' : 'PERHITUNGAN',
        'kriteria' : kriteria,
        'subkriteria' : subkriteriaT,
        'total' : totalarr,
        'bprall' : bprall,
        "totalbpr" :realBpr,
        "bkonsen" : bkonsen,
        "CI" : CI,
        "R" : R,
        "CR" : CR
      
    }
    return render(request, template_name, context)



def login(request):
    template_name = "login.html"
    context = {
        'nama' : 'Form Input',
        
    }
    return render(request, template_name, context)
