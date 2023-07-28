from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import os
import uuid
#Admin

def common(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"akunadmin/{unique_filename}"

class Admin(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    nama_admin = models.CharField(max_length=200)
    divisi = models.CharField(max_length=200)
    kedinasan = models.CharField(max_length=200)
    email = models.EmailField(("Email Admin"), max_length=254)
    gambar = models.ImageField(upload_to=common,null=True, blank=True)
    USERNAME_FIELD = "username"
    
        
    def __str__(self):
        return self.username


# Pemabagian inti dari core
class Status(models.Model):
    STATUS_CHOICES = (
        ('DIAJUKAN', 'Masih Diajukan'),
        ('PERENCANAAN', 'Perencanaan'),
        ('PEMBANGUNAN', 'Pembangunan'),
    )
    statusid = models.BigAutoField(primary_key=True)
    tipestatus = models.CharField(max_length=50, choices=STATUS_CHOICES,default='DIAJUKAN')
    
class Kondisi(models.Model):
    KONDISI_CHOICES = (
        ('BAIK', 'Kondisi Baik'),
        ('BURUK','Kondisi Buruk'),
    )
    
    Kondisiid = models.BigAutoField(primary_key=True)
    tipekondisi = models.CharField(max_length=50, choices=KONDISI_CHOICES,default='BAIK')
    
class Location(models.Model):
    locationid= models.BigAutoField(primary_key=True)
    latitude= models.FloatField()
    longitude= models.FloatField()
    
    
class Rusak(models.Model):
    RUSAK_CHOICES = (
        ('RUSAK BERAT','Kerusakan Berat'),
        ('RUSAK SEDANG', 'Kerusakan Sedang'), 
        ('RUSAK RINGAN','Kerusakan Ringan'),
    )    
    rusakid= models.BigAutoField(primary_key=True)
    tiperusak= models.CharField(max_length=50, choices=RUSAK_CHOICES,default='RUSAK RINGAN')
    deskrpsi = models.TextField(null=True, blank=True)
    
# Bagan khusus.
class Perlengkapan_jalan(models.Model):
    perlengkapanid = models.BigAutoField(primary_key= True)
    jenis_perlengkapan = models.CharField(max_length=200 , unique=True)
    deskrpsi = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.jenis_perlengkapan


def upload_to(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"fasilitas/{unique_filename}"

class Fasilitas_perlengkapan(models.Model):
    fasilitasid = models.BigAutoField(primary_key=True)
    tipekhusus = models.CharField(max_length=200,blank=True,null=True)
    namakhusus = models.CharField(max_length=200,blank=True,null=True)
    nama_fasilitas = models.CharField(max_length=200,unique=True,blank=True,null=True)
    tanggal_ditambahkan = models.CharField(max_length=200,blank=True,null=True)
    volume= models.IntegerField(blank=True)
    jenis_perlengkapan = models.ForeignKey(Perlengkapan_jalan, on_delete=models.CASCADE, to_field="jenis_perlengkapan")    
    gambar = models.ImageField(upload_to=upload_to,null=True, blank=True)
    color = models.CharField(max_length=30,null=True, blank=True)
    deskrpsi = models.TextField(blank=True,null=True)
    
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
    gambar = models.ImageField(upload_to=mirage,null=True, blank=True)
    
    # Menyimpan objek Pengajuan
    
# tabel function users   
def cringe(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"pembangunan/{unique_filename}"

class Pembangunan(models.Model):
    pembangunanid = models.BigAutoField(primary_key=True)
    tanggal_bangun = models.CharField(max_length=200,null=True,blank=True)
    konstruksi_selesai = models.CharField(max_length=200,null=True,blank=True)
    ruasjalan = models.CharField(max_length=400,null=True,blank=True)
    nama_fasilitas = models.ForeignKey(Fasilitas_perlengkapan,on_delete=models.CASCADE,to_field="nama_fasilitas",blank=True)
    jenis_perlengkapan = models.ForeignKey(Perlengkapan_jalan, on_delete=models.CASCADE, to_field="jenis_perlengkapan",blank=True)    
    kondisi= models.ForeignKey(Kondisi, on_delete=models.CASCADE,blank=True) 
    volume= models.IntegerField(null=True,blank=True)
    deskripsi = models.TextField(blank=True,null=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE,null=True,blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE,null=True,blank=True) 
    gambar = models.ImageField(upload_to=cringe,blank=True,null=True)
    

    

def demonslayer(instance, filename):
    _, file_extension = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{file_extension}"
    return f"kerusakan/{unique_filename}" 

class Kerusakan(models.Model):
    kerusakanid = models.BigAutoField(primary_key=True)
    masyarakatid = models.ForeignKey(Masyarakat,on_delete=models.CASCADE)
    nama_fasilitas = models.ForeignKey(Fasilitas_perlengkapan,on_delete=models.CASCADE,to_field="nama_fasilitas",null=True,blank=True)
    jenis_perlengkapan = models.ForeignKey(Perlengkapan_jalan, on_delete=models.CASCADE, to_field="jenis_perlengkapan",null=True,blank=True)    
    deskripsi = models.TextField(null=True, blank=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE,null=True,blank=True)
    rusak = models.ForeignKey(Rusak, on_delete=models.CASCADE,null=True,blank=True) 
    gambar = models.ImageField(upload_to=demonslayer,null=True, blank=True)
    
    
# tabel skala/pendamping    

    
    
class Beranda(models.Model):        
    folioid = models.BigAutoField(primary_key=True)
    konstruksi_selesai = models.ForeignKey(Pembangunan, on_delete=models.CASCADE)    
    kerusakan= models.ForeignKey(Kerusakan, on_delete=models.CASCADE)    
    jenis_perlengkapan = models.ForeignKey(Perlengkapan_jalan, on_delete=models.CASCADE, to_field="jenis_perlengkapan")    
    deskripsi = models.TextField(blank=True,null=True)
    
    
            