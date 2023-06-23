from django.shortcuts import redirect, render
from requests import request
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Masyarakat

def maps(request):
    return render(request, 'masyarakat/maps.html')

def beranda(request):
    return render(request, 'masyarakat/landingpage.html')

def jenisperlengkapan(request):
    return render(request, 'masyarakat/jenis perlengkapan.html')

def pengajuan(request):
    return render(request, 'masyarakat/pengajuan.html')


# percobaan
def cadangan(request):
    return render(request, 'masyarakat/cadangan.html')
# percobaan



# Admin
def dashboardadmin(request):
    return render(request, 'core/dashboard.html')


# Peta admin
def petaadkerusakan(request):
    return render(request, 'peta/peta kerusakan.html')

def petaadpembangunan(request):
    return render(request, 'peta/peta pembangunan.html')

def petaadpengajuan(request):
    return render(request, 'peta/peta pengajuan.html')

def petaadperencanaan(request):
    return render(request, 'peta/peta perencanaan.html')

# Peta statistik
def statistikfasiltas(request):
    return render(request, 'statistik/statistik fasilitas.html')

def statistikkerusakan(request):
    return render(request, 'statistik/statistik kerusakan.html')

def statistikpembangunan(request):
    return render(request, 'statistik/statistik pembangunan.html')

def statistikpengajuan(request):
    return render(request, 'statistik/statistik pengajuan.html')

def statistikperencanaan(request):
    return render(request, 'statistik/statistik perencanaan.html')

# Data tables
def datafpj(request):
    return render(request, 'datatables/data fpj.html')

def datapembangunan(request):
    return render(request, 'datatables/pembangunan.html')

def datapengajuan(request):
    return render(request, 'datatables/pengajuan.html')

def dataperencanaan(request):
    return render(request, 'datatables/perencanaan.html')

# seleksi
def seleksidibawah(request):
    return render(request, 'seleksi/dibawah standar.html')

def seleksimemenuhi(request):
    return render(request, 'seleksi/memenuhi standar.html')

# pelaporan 
def pelaporan(request):
    return render(request, 'kerusakan/pelaporan.html')

# kerusakan
def kerusakanberat(request):
    return render(request, 'kerusakan/berat.html')

def kerusakanringan(request):
    return render(request, 'kerusakan/ringan.html')

# bantuan
def kontakoperator(request):
    return render(request, 'bantuan/kontak operator.html')

def layanandinas(request):
    return render(request, 'bantuan/layanandinas.html')

def permasalahan(request):
    return render(request, 'bantuan/pengajuan permasalahan.html')

# panduan 
def pemandu(request):
    return render(request, 'panduan/pemandu penambahan.html')

def penggunaan(request):
    return render(request, 'panduan/penggunaan.html')

def login(request):
    return render(request, 'core/login.html')




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Autentikasi pengguna
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Login berhasil, lakukan login dan redirect ke halaman yang diinginkan
                login(request, user)
                return redirect('dashboard')  # Ganti 'dashboard' dengan URL halaman dashboard Anda
            else:
                # Login gagal, tampilkan pesan error
                messages.error(request, 'Username atau password salah')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})