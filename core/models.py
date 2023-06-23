from django.db import models





# Pemabagian inti dari core
class Status(models.Model):
    STATUS_CHOICES = (
        ('DIAJUKAN', 'Masih Diajukan'),
        ('DIPROSES', 'Masih Diproses'),
        ('PERENCANAAN', 'Perencanaan'),
        ('PEMBANGUNAN', 'Pembangunan'),
    )
    statusid = models.CharField(max_length=200 , primary_key=True)
    tipestatus = models.CharField(max_length=50,unique=True, choices=STATUS_CHOICES,default='DIAJUKAN')
    
class Location(models.Model):
    locationid= models.CharField(max_length=200 , primary_key=True)
    status =  models.OneToOneField(Status, on_delete=models.CASCADE)
    latitude= models.FloatField()
    longitude= models.FloatField()
    
    
# Bagan khusus.
class Perlengkapan_jalan(models.Model):
    perlengkapanid = models.CharField(max_length=200 , primary_key= True)
    jenis_perlengkapan = models.CharField(max_length=200 , unique=True)
    deskrpsi = models.TextField(blank=True,null=True)
    
class Fasilitas_perlengkapan(models.Model):
    fasilitasid = models.CharField(max_length=200 , primary_key=True)
    status= models.ForeignKey(Status,on_delete=models.CASCADE,to_field="tipestatus")
    nama_fasilitas= models.CharField(max_length=200)
    kondisi= models.CharField(max_length=200)
    volume= models.IntegerField()
    jenis_perlengkapan = models.ForeignKey(Perlengkapan_jalan, on_delete=models.CASCADE, to_field="jenis_perlengkapan")    
    gambar = models.ImageField(upload_to="fasilitas/",null=True)
    
    
# User form.
class Masyarakat(models.Model):
    masyarakatid = models.CharField(max_length=200 , primary_key=True)
    nama= models.CharField(max_length=200)
    notelepon= models.IntegerField()
    alamat= models.CharField(max_length=200)
    
class Pengajuan(models.Model):
    pengajuanid = models.CharField(max_length=200 , primary_key=True)
    masyarakatid = models.ManyToManyField(Masyarakat)
    perlengkapanid = models.ManyToManyField(Perlengkapan_jalan)
    nama_fasilitas = models.ManyToManyField(Fasilitas_perlengkapan)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    statuspengajuan = models.ForeignKey(Status,on_delete=models.CASCADE)
    
    
    
# tabel function users   
class Pembangunan(models.Model):
    pembangunanid = models.CharField(max_length=200 , primary_key=True)
    tanggal_bangun = models.DateField()
    konstruksi_selesai = models.DateField()
    deskripsi = models.TextField(blank=True,null=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    
class Penyeleksian(models.Model):
    penyeleksianid = models.CharField(max_length=200 , primary_key=True)
    pembangunanid = models.ManyToManyField(Pembangunan)
    adminid = models.CharField(max_length=200)
    pengajuanid = models.CharField(max_length=200)
    perencanaanid = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, to_field="tipestatus") 
    location = models.OneToOneField(Location, on_delete=models.CASCADE)   
    tggl_terima = models.DateTimeField()
    
    
class Perencanaan(models.Model):
    perencanaanid = models.CharField(max_length=200 , primary_key=True)
    pembangunanid = models.ForeignKey(Pembangunan, on_delete=models.CASCADE, to_field="pembangunanid")    
    fasilitasid = models.ForeignKey(Fasilitas_perlengkapan, on_delete=models.CASCADE, to_field="fasilitasid")    
    nama_perencanaan = models.CharField(max_length=200)
    status_pengajuan = models.ForeignKey(Status, on_delete=models.CASCADE, to_field="tipestatus") 
    location = models.OneToOneField(Location, on_delete=models.CASCADE)   

# tabel skala/pendamping    
class Admin(models.Model):
    adminid = models.CharField(max_length=200 , primary_key=True)
    nama_admin = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    ditambahkan = models.DateField(auto_now_add=True)
    divisi = models.CharField(max_length=200)
    kedinasan = models.CharField(max_length=200)
    
    
class Beranda(models.Model):        
    folioid = models.CharField(max_length=200 , primary_key=True)
    konstruksi_selesai = models.ForeignKey(Pembangunan, on_delete=models.CASCADE)    
    nama_perencanaan = models.ForeignKey(Perencanaan, on_delete=models.CASCADE)    
    jenis_perlengkapan = models.ForeignKey(Perlengkapan_jalan, on_delete=models.CASCADE, to_field="jenis_perlengkapan")    
    deskripsi = models.TextField(blank=True,null=True)
    
    
            