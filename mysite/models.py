from django.db import models, IntegrityError
from django.contrib.auth.models import User
# Create your models here.


class Kriteria(models.Model):
    codeK = models.TextField(unique=True)
    namaK = models.TextField()
    kelasK = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.codeK + ' - ' + self.namaK
    
    class Meta:
        verbose_name_plural = 'Kriteria'
        constraints = [
            models.UniqueConstraint(fields=['codeK'], name='unique_codeK')
        ]
        
class Alternatif(models.Model):
    nimA = models.TextField(unique=True)
    namaA = models.TextField()
    
    
    def __str__(self):
        return self.nimA
    
    class Meta:
        verbose_name_plural = 'Alternatif'
        constraints = [
            models.UniqueConstraint(fields=['nimA'], name='unique_nimA')
        ]
        
class SubAlternatif(models.Model):
    codeNim = models.ForeignKey(Alternatif, on_delete=models.CASCADE)
    namaSA = models.CharField(max_length=255)
    k1sa = models.CharField(max_length=100 ,blank=True, null=True)
    k2sa = models.CharField(max_length=100 ,blank=True, null=True)
    k3sa = models.CharField(max_length=100 ,blank=True, null=True)
    k4sa = models.CharField(max_length=100 ,blank=True, null=True)
    
    def __str__(self):
        return self.namaSA
    
    class Meta:
        verbose_name_plural = 'sub-Alternatif'
        

class SubKriteria(models.Model):
    codeKF = models.ForeignKey(Kriteria, on_delete=models.CASCADE, to_field='codeK', unique=False)
    k1 = models.TextField(blank=True, null=True)
    k2 = models.TextField(blank=True, null=True)
    k3 = models.TextField(blank=True, null=True)
    k4 = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.codeKF.codeK
    
    class Meta:
        verbose_name_plural = 'sub-Kriteria'
        
# AHP
class BobotPrioritas(models.Model):
    codeBF = models.ForeignKey(Kriteria, on_delete=models.CASCADE, to_field='codeK', unique=False)
    bobotPrio = models.TextField(blank=True, null=True)
    k1 = models.TextField(blank=True, null=True)
    k2 = models.TextField(blank=True, null=True)
    k3 = models.TextField(blank=True, null=True)
    k4 = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.codeBF.codeK
    
    class Meta:
        verbose_name_plural = 'Bobot-Prioritas'

class BobotKonsistensi(models.Model):
    codeBKF = models.ForeignKey(Kriteria, on_delete=models.CASCADE)
    k1 = models.FloatField(default=0, blank=True, null=True)
    k2 = models.FloatField(default=0, blank=True, null=True)
    k3 = models.FloatField(default=0, blank=True, null=True)
    k4 = models.FloatField(default=0, blank=True, null=True) 
    bobotkons = models.FloatField(default=0, blank=True, null=True)
  

    def __str__(self):
        return self.codeBF.namaK
    
    class Meta:
        verbose_name_plural = 'Bobot-konsistensi'
# Topsis
class NormalisasiTopsis(models.Model):
    namaAlter = models.ForeignKey(SubAlternatif, on_delete=models.CASCADE)
    k1 = models.FloatField(default=0, blank=True, null=True)
    k2 = models.FloatField(default=0, blank=True, null=True)
    k3 = models.FloatField(default=0, blank=True, null=True)
    k4 = models.FloatField(default=0, blank=True, null=True)  

    def __str__(self):
        return self.namaAlter.namaSa
    
    class Meta:
        verbose_name_plural = 'Normalisasi-Topsis'

class NormalBobotTopsis(models.Model):
    nimAlter = models.ForeignKey(Alternatif, on_delete=models.CASCADE, to_field='nimA', unique=False)
    k1 = models.FloatField(default=0, blank=True, null=True)
    k2 = models.FloatField(default=0, blank=True, null=True)
    k3 = models.FloatField(default=0, blank=True, null=True)
    k4 = models.FloatField(default=0, blank=True, null=True)  

    def __str__(self):
        return self.nimAlter
    
    class Meta:
        verbose_name_plural = 'Normalisasi-Bobot-Topsis'

class TopsisSolusi(models.Model):
    status = models.CharField(max_length=255)
    k1 = models.FloatField(default=0, blank=True, null=True)
    k2 = models.FloatField(default=0, blank=True, null=True)
    k3 = models.FloatField(default=0, blank=True, null=True)
    k4 = models.FloatField(default=0, blank=True, null=True)  

    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name_plural = 'Topsis-Solusi'
        
class JarakPrefTopsis(models.Model):
    nimAlter = models.ForeignKey(Alternatif, on_delete=models.CASCADE, to_field='nimA', unique=False)
    positif = models.FloatField(default=0, blank=True, null=True)
    negatif = models.FloatField(default=0, blank=True, null=True)
    preferensi = models.FloatField(default=0, blank=True, null=True)  

    def __str__(self):
        return self.nimAlter
    
    class Meta:
        verbose_name_plural = 'Jarak-Pref-Topsis'
        
class RankingTopsis(models.Model):
    nimAlter = models.ForeignKey(Alternatif, on_delete=models.CASCADE, to_field='nimA', unique=False)
    preferensi = models.FloatField(default=0, blank=True, null=True)
    rank = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.nimAlter 
    
    class Meta:
        verbose_name_plural = 'Ranking-Topsis'