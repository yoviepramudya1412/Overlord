from django.shortcuts import redirect, render
from requests import request
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


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

# def login(request):
#     return render(request, 'core/login.html')

# Admin
@login_required(login_url='login')
def dashboardadmin(request):
    return render(request, 'core/dashboard.html')





def login(request):
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