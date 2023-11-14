from django.db import models, IntegrityError
from django.contrib.auth.models import User
# Create your models here.


class Kriteria(models.Model):
    codeK = models.TextField(unique=True)
    namaK = models.TextField()
    
    def __str__(self):
        return self.codeK + ' - ' + self.namaK
    
    class Meta:
        verbose_name_plural = 'Kriteria'
        constraints = [
            models.UniqueConstraint(fields=['codeK'], name='unique_codeK')
        ]
        
class Alternatif(models.Model):
    nimA = models.TextField()
    namaA = models.TextField()
    
    def __str__(self):
        return self.nimA + ' - ' + self.namaA
    
    class Meta:
        verbose_name_plural = 'Alternatif'
        

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