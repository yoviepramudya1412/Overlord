from django.conf import settings
from django.shortcuts import redirect, render
from requests import request
from .forms import *
from django.contrib.auth import authenticate, login, logout
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
    return render(request, 'peta/peta pengajuan.html')

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
    return render(request, 'datatables/pengajuan.html')

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