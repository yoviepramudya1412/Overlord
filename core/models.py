from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import os
import uuid
#Admin


class Admin(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    nama_admin = models.CharField(unique=True,max_length=200)
    divisi = models.CharField(max_length=200)
    kedinasan = models.CharField(max_length=200)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['nama_admin', 'kedinasan']
        
    def __str__(self):
        return self.username


# Pemabagian inti dari core
class Status(models.Model):
    STATUS_CHOICES = (
        ('DIAJUKAN', 'Masih Diajukan'),
        ('DIPROSES', 'Masih Diproses'),
        ('PERENCANAAN', 'Perencanaan'),
        ('PEMBANGUNAN', 'Pembangunan'),
    )
    statusid = models.BigAutoField(primary_key=True)
    tipestatus = models.CharField(max_length=50, choices=STATUS_CHOICES,default='DIAJUKAN')
    
class Location(models.Model):
    locationid= models.BigAutoField(primary_key=True)
    latitude= models.FloatField()
    longitude= models.FloatField()
    
    
# Bagan khusus.
class Perlengkapan_jalan(models.Model):
    perlengkapanid = models.BigAutoField(primary_key= True)
    jenis_perlengkapan = models.CharField(max_length=200 , unique=True)
    deskrpsi = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.jenis_perlengkapan


def upload_to(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"fasilitas/{unique_filename}"
   
class Fasilitas_perlengkapan(models.Model):
    fasilitasid = models.BigAutoField(primary_key=True)
    tipekhusus = models.CharField(max_length=200)
    nama_fasilitas = models.CharField(max_length=200,unique=True)
    kondisi= models.CharField(max_length=200,blank=True)
    volume= models.IntegerField(blank=True)
    jenis_perlengkapan = models.ForeignKey(Perlengkapan_jalan, on_delete=models.CASCADE, to_field="jenis_perlengkapan")    
    gambar = models.ImageField(upload_to=upload_to,blank=True)
    
    def __str__(self):
        return self.nama_fasilitas
    
# User form.
class Masyarakat(models.Model):
    masyarakatid = models.BigAutoField(primary_key=True)
    nama= models.CharField(max_length=200)
    notelepon= models.CharField(max_length=30)
    alamat= models.CharField(max_length=200)
    

def mirage(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"pengajuan/{unique_filename}"

class Pengajuan(models.Model):
    pengajuanid = models.BigAutoField(primary_key=True)
    masyarakatid = models.ForeignKey(Masyarakat,on_delete=models.CASCADE)
    nama_fasilitas = models.ForeignKey(Fasilitas_perlengkapan,on_delete=models.CASCADE,to_field="nama_fasilitas",blank=True)
    jenis_perlengkapan = models.ForeignKey(Perlengkapan_jalan, on_delete=models.CASCADE, to_field="jenis_perlengkapan",blank=True)    
    Fasilitas_khusus=models.CharField(max_length=200,blank=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE,null=True,blank=True)
    statuspengajuan = models.OneToOneField(Status,on_delete=models.CASCADE,null=True,blank=True)
    gambar = models.ImageField(upload_to=mirage,blank=True)
    
    # Menyimpan objek Pengajuan
    
# tabel function users   
def cringe(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"pembangunan/{unique_filename}"

class Pembangunan(models.Model):
    pembangunanid = models.BigAutoField(primary_key=True)
    tanggal_bangun = models.DateField()
    konstruksi_selesai = models.DateField()
    nama_fasilitas = models.ForeignKey(Fasilitas_perlengkapan,on_delete=models.CASCADE,to_field="nama_fasilitas",blank=True)
    jenis_perlengkapan = models.ForeignKey(Perlengkapan_jalan, on_delete=models.CASCADE, to_field="jenis_perlengkapan",blank=True)    
    kondisi= models.CharField(max_length=200,blank=True)
    volume= models.IntegerField(blank=True)
    deskripsi = models.TextField(blank=True,null=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    status = models.OneToOneField(Status, on_delete=models.CASCADE) 
    gambar = models.ImageField(upload_to=cringe,blank=True)
    
class Penyeleksian(models.Model):
    penyeleksianid = models.BigAutoField(primary_key=True)
    pembangunanid = models.ManyToManyField(Pembangunan)
    adminid = models.CharField(max_length=200)
    pengajuanid = models.CharField(max_length=200)
    perencanaanid = models.CharField(max_length=200)
    status = models.OneToOneField(Status, on_delete=models.CASCADE) 
    location = models.OneToOneField(Location, on_delete=models.CASCADE)   
    tggl_terima = models.DateTimeField()
    

def demonslayer(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"perencanaan/{unique_filename}" 

class Perencanaan(models.Model):
    perencanaanid = models.BigAutoField(primary_key=True)
    pembangunanid = models.ForeignKey(Pembangunan, on_delete=models.CASCADE, to_field="pembangunanid")    
    fasilitasid = models.ForeignKey(Fasilitas_perlengkapan, on_delete=models.CASCADE, to_field="fasilitasid")    
    nama_perencanaan = models.CharField(max_length=200)
    status_pengajuan = models.OneToOneField(Status, on_delete=models.CASCADE) 
    location = models.OneToOneField(Location, on_delete=models.CASCADE)   
    gambar = models.ImageField(upload_to=demonslayer,blank=True)
    
    
# tabel skala/pendamping    

    
    
class Beranda(models.Model):        
    folioid = models.BigAutoField(primary_key=True)
    konstruksi_selesai = models.ForeignKey(Pembangunan, on_delete=models.CASCADE)    
    nama_perencanaan = models.ForeignKey(Perencanaan, on_delete=models.CASCADE)    
    jenis_perlengkapan = models.ForeignKey(Perlengkapan_jalan, on_delete=models.CASCADE, to_field="jenis_perlengkapan")    
    deskripsi = models.TextField(blank=True,null=True)
    
    
            