from django.conf import settings
from django.shortcuts import redirect, render
from requests import request
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.serializers import serialize


# Masyarakat


def maps(request):
    return render(request, 'masyarakat/maps.html')


def beranda(request):
    return render(request, 'masyarakat/landingpage.html')

def jenisperlengkapan(request):
    return render(request, 'masyarakat/jenis perlengkapan.html')


# def pengajuan(request):
#     qs = Perlengkapan_jalan.objects.all()
#     return render(request, 'masyarakat/pengajuan.html', {'qs': qs})

def get_json_datafpj(request):
    qs_val = list(Perlengkapan_jalan.objects.values())
    return JsonResponse({'data': qs_val})

def get_jenis_perlengkapan(request):
    jenis_perlengkapan_list = Perlengkapan_jalan.objects.values_list('jenis_perlengkapan', flat=True)
    return JsonResponse(list(jenis_perlengkapan_list), safe=False)

def get_nama_fasilitas(request):
    jenis_perlengkapan = request.GET.get('jenis_perlengkapan')
    nama_fasilitas_list = Fasilitas_perlengkapan.objects.filter(jenis_perlengkapan__jenis_perlengkapan=jenis_perlengkapan).values_list('nama_fasilitas', flat=True)
    return JsonResponse(list(nama_fasilitas_list), safe=False)





def create_pengajuan(request):
    if request.method == 'POST':
        pengajuan_form = PengajuanForm(request.POST)

        if pengajuan_form.is_valid():
            # Membuat objek Masyarakat dan mengisi kolom-kolomnya
            masyarakat = Masyarakat.objects.create(
                nama=request.POST['nama'],
                notelepon=request.POST['notelepon'],
                alamat=request.POST['alamat']
            )

            # Mengisi kolom-kolom pada objek Pengajuan
            pengajuan = pengajuan_form.save(commit=False)
            pengajuan.masyarakatid = masyarakat
            pengajuan.nama_fasilitas = Fasilitas_perlengkapan.objects.get(nama_fasilitas=request.POST['nama_fasilitas'])
            pengajuan.jenis_perlengkapan = Perlengkapan_jalan.objects.get(jenis_perlengkapan=request.POST['jenis_perlengkapan'])
            pengajuan.Fasilitas_khusus = request.POST['Fasilitas_khusus']
            pengajuan.gambar = request.FILES['gambar']

            # Simpan objek pengajuan
            pengajuan.save()

            # Dapatkan objek Status dengan nilai 'DIAJUKAN'
            status = Status.objects.create(tipestatus='DIAJUKAN')

            # Menghubungkan objek pengajuan dengan objek status
            pengajuan.statuspengajuan = status
            pengajuan.save()

            # Buat objek Location dan hubungkan dengan objek Pengajuan
            location = Location.objects.create(
                latitude=request.POST['latitudeA'],
                longitude=request.POST['longitudeB'],
            )
            pengajuan.location = location
            pengajuan.save()

            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('create_pengajuan')  # Ganti 'peta' dengan URL halaman peta

        else:
            errors = pengajuan_form.errors
            print(errors)
            messages.error(request, 'Terjadi kesalahan dalam menambahkan data.')

    else:
        pengajuan_form = PengajuanForm()

    return render(request, 'masyarakat/pengajuan.html', {'pengajuan_form': pengajuan_form})







# percobaan
@login_required(login_url=settings.LOGIN_URL)
def cadangan(request):
    return render(request, 'masyarakat/cadangan.html')
# percobaan





# Peta admin
@login_required(login_url=settings.LOGIN_URL)
def petaadkerusakan(request):
    return render(request, 'peta/peta kerusakan.html')

@login_required(login_url=settings.LOGIN_URL)
def petaadpembangunan(request):
    return render(request, 'peta/peta pembangunan.html')

@login_required(login_url=settings.LOGIN_URL)
def petaadpengajuan(request):
    pengajuan_data = Pengajuan.objects.exclude(location=None)
    markers = []
    for pengajuan in pengajuan_data:
        marker = {
            'lat': pengajuan.location.latitude,
            'lng': pengajuan.location.longitude,
            'nama': pengajuan.masyarakatid.nama,
            'notelepon': pengajuan.masyarakatid.notelepon,
            'alamat': pengajuan.masyarakatid.alamat,
            'gambar': pengajuan.gambar.url if pengajuan.gambar else None,
        }
        markers.append(marker)

    context = {
        'markers': markers
    }
    return render(request, 'peta/peta pengajuan.html',context)

@login_required(login_url=settings.LOGIN_URL)
def petaadperencanaan(request):
    return render(request, 'peta/peta perencanaan.html')

# Peta statistik
@login_required(login_url=settings.LOGIN_URL)
def statistikfasiltas(request):
    return render(request, 'statistik/statistik fasilitas.html')

@login_required(login_url=settings.LOGIN_URL)
def statistikkerusakan(request):
    return render(request, 'statistik/statistik kerusakan.html')

@login_required(login_url=settings.LOGIN_URL)
def statistikpembangunan(request):
    return render(request, 'statistik/statistik pembangunan.html')

@login_required(login_url=settings.LOGIN_URL)
def statistikpengajuan(request):
    return render(request, 'statistik/statistik pengajuan.html')

@login_required(login_url=settings.LOGIN_URL)
def statistikperencanaan(request):
    return render(request, 'statistik/statistik perencanaan.html')

# Data tables
@login_required(login_url=settings.LOGIN_URL)
def datafpj(request):
    return render(request, 'datatables/data fpj.html')

@login_required(login_url=settings.LOGIN_URL)
def datapembangunan(request):
    return render(request, 'datatables/pembangunan.html')

@login_required(login_url=settings.LOGIN_URL)
def datapengajuan(request):
    pengajuan_data = Pengajuan.objects.all()
    context = {
        'pengajuan_data': pengajuan_data
    }
    return render(request, 'datatables/pengajuan.html',context)

@login_required(login_url=settings.LOGIN_URL)
def dataperencanaan(request):
    return render(request, 'datatables/perencanaan.html')

# seleksi
@login_required(login_url=settings.LOGIN_URL)
def seleksidibawah(request):
    return render(request, 'seleksi/dibawah standar.html')

@login_required(login_url=settings.LOGIN_URL)
def seleksimemenuhi(request):
    return render(request, 'seleksi/memenuhi standar.html')

# pelaporan 
@login_required(login_url=settings.LOGIN_URL)
def pelaporan(request):
    return render(request, 'kerusakan/pelaporan.html')

# kerusakan
@login_required(login_url=settings.LOGIN_URL)
def kerusakanberat(request):
    return render(request, 'kerusakan/berat.html')

@login_required(login_url=settings.LOGIN_URL)
def kerusakanringan(request):
    return render(request, 'kerusakan/ringan.html')

# bantuan
@login_required(login_url=settings.LOGIN_URL)
def kontakoperator(request):
    return render(request, 'bantuan/kontak operator.html')

@login_required(login_url=settings.LOGIN_URL)
def layanandinas(request):
    return render(request, 'bantuan/layanandinas.html')

@login_required(login_url=settings.LOGIN_URL)
def permasalahan(request):
    return render(request, 'bantuan/pengajuan permasalahan.html')

# masukkan data buat admin
@login_required(login_url=settings.LOGIN_URL)
def masukdatapembangunan(request):
    return render(request, 'create/Pembangunan.html')

@login_required(login_url=settings.LOGIN_URL)
def masukdatapengajuan(request):
    return render(request, 'create/Pengajuan.html')

@login_required(login_url=settings.LOGIN_URL)
def masukdataperencanaan(request):
    return render(request, 'create/Perencanaan.html')

@login_required(login_url=settings.LOGIN_URL)
def masukdataperlengkapan(request):
    return render(request, 'create/Perlengkapan jalan.html')






# panduan 
@login_required(login_url=settings.LOGIN_URL)
def pemandu(request):
    return render(request, 'panduan/pemandu penambahan.html')

@login_required(login_url=settings.LOGIN_URL)
def penggunaan(request):
    return render(request, 'panduan/penggunaan.html')

# def login(request):
#     return render(request, 'core/login.html')

# Admin
@login_required(login_url=settings.LOGIN_URL)
def dashboardadmin(request):
    context = {'user': request.user}
    return render(request, 'core/dashboard.html',context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboardadmin')
        else:
            error_message = "Invalid username or password"
            return render(request, 'core/login.html', {'error_message': error_message})
    else:
        return render(request, 'core/login.html')
    
def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('masuk')