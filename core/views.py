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
from django.shortcuts import get_object_or_404

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

def laporkerusakan(request):
    rusak_choices = Rusak.RUSAK_CHOICES
    if request.method == 'POST':
        kerusakan_form = KerusakanForm(request.POST, request.FILES)

        if kerusakan_form.is_valid():
            # Membuat objek Masyarakat dan mengisi kolom-kolomnya
            masyarakat = Masyarakat.objects.create(
                nama=request.POST['nama'],
                notelepon=request.POST['notelepon'],
                alamat=request.POST['alamat']
            )

            # Mengisi kolom-kolom pada objek Pengajuan
            kerusakan = kerusakan_form.save(commit=False)
            kerusakan.masyarakatid = masyarakat
            kerusakan.nama_fasilitas = Fasilitas_perlengkapan.objects.get(nama_fasilitas=request.POST['nama_fasilitas'])
            kerusakan.jenis_perlengkapan = Perlengkapan_jalan.objects.get(jenis_perlengkapan=request.POST['jenis_perlengkapan'])
            kerusakan.deskripsi = request.POST['deskripsi']
            if 'gambar' in request.FILES:
                kerusakan.gambar = request.FILES['gambar']

            # Simpan objek kerusakan
            kerusakan.save()

            # Dapatkan objek Status dengan nilai 'DIAJUKAN'
            tipe_rusak = request.POST.get('tipe_rusak')
            rusak = Rusak.objects.create(tiperusak=tipe_rusak)
            kerusakan.rusak = rusak
            # Menghubungkan objek kerusakan dengan objek status
            

            # Buat objek Location dan hubungkan dengan objek kerusakan
            location = Location.objects.create(
                latitude=request.POST['latitudeA'],
                longitude=request.POST['longitudeB'],
            )
            kerusakan.location = location
            kerusakan.save()

            messages.success(request, 'Data berhasil dilaporkan')
            return redirect('laporkerusakan')  # Ganti 'peta' dengan URL halaman peta

        else:
            errors = kerusakan_form.errors
            print(errors)
            messages.error(request, 'Terjadi kesalahan dalam menambahkan data.')

    else:
        kerusakan_form = KerusakanForm()

    
    
    context={
        'rusak_choices':rusak_choices,
        'kerusakan_form':kerusakan_form,
    }
    return render(request, 'masyarakat/lapor kerusakan.html',context)


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
            if 'gambar' in request.FILES:
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

            messages.success(request, 'Berhasil diajukan')
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


# khusus akun
@login_required(login_url=settings.LOGIN_URL)
def Account(request):
    admin = Admin.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil berhasil diperbarui.')
            return redirect('Account')
        else:
            errors = form.errors
            print(errors)
            messages.error(request, 'Terjadi kesalahan pada sistem')
    else:
        form = EditProfileForm(instance=admin)

    context = {
        'form': form
    }
    return render(request, 'core/Akun.html',context)
# khusus akun


# Peta admin
@login_required(login_url=settings.LOGIN_URL)
def petaadkerusakan(request):
    kerusakan_data = Kerusakan.objects.all().exclude(location=None)
    markers = []
    for kerusakan in kerusakan_data:
        if kerusakan.location is not None:
            marker = {
                'lat': kerusakan.location.latitude,
                'lng': kerusakan.location.longitude,
                'nama': kerusakan.masyarakatid.nama,
                'notelepon': kerusakan.masyarakatid.notelepon,
                'alamat': kerusakan.masyarakatid.alamat,
                'nama_fasilitas': kerusakan.nama_fasilitas,
                'tiperusak':kerusakan.rusak.tiperusak,
            }
            if kerusakan.gambar:
                marker['gambar'] = kerusakan.gambar.url
            else:
                marker['gambar'] = None
            markers.append(marker)
    context = {
        'markers': markers
    }
    return render(request, 'peta/peta kerusakan.html', context)

@login_required(login_url=settings.LOGIN_URL)
def petaadpembangunan(request):
    pembangunan_perencanaan = Pembangunan.objects.filter(status__tipestatus='PEMBANGUNAN').exclude(location=None)
    markers = []
    for pembangunan in pembangunan_perencanaan:
        if pembangunan.location is not None:
            marker = {
                'lat': pembangunan.location.latitude,
                'lng': pembangunan.location.longitude,
                'nama_fasilitas': pembangunan.nama_fasilitas,
                'konstruksi_selesai': pembangunan.konstruksi_selesai,
                
            }
            if pembangunan.gambar:
                marker['gambar'] = pembangunan.gambar.url
            else:
                marker['gambar'] = None
            markers.append(marker)
    context = {
        'markers': markers
    }
    return render(request, 'peta/peta pembangunan.html',context)

@login_required(login_url=settings.LOGIN_URL)
def petaadpengajuan(request):
    pengajuan_data = Pengajuan.objects.exclude(location=None)
    markers = []

    for pengajuan in pengajuan_data:
        if pengajuan.location is not None:
            fasilitas = pengajuan.nama_fasilitas
            color = fasilitas.color  # Mengambil warna dari fasilitas perlengkapan
            

            marker = {
                'lat': pengajuan.location.latitude,
                'lng': pengajuan.location.longitude,
                'nama': pengajuan.masyarakatid.nama,
                'notelepon': pengajuan.masyarakatid.notelepon,
                'alamat': pengajuan.masyarakatid.alamat,
                'nama_fasilitas': pengajuan.nama_fasilitas,
                'color': color,  # Menambahkan warna ke data marker
            }

            if pengajuan.gambar:
                marker['gambar'] = pengajuan.gambar.url
            else:
                marker['gambar'] = None

            markers.append(marker)

    context = {
        'markers': markers
    }

    return render(request, 'peta/peta pengajuan.html', context)


@login_required(login_url=settings.LOGIN_URL)
def petaadperencanaan(request):
    pembangunan_perencanaan = Pembangunan.objects.filter(status__tipestatus='PERENCANAAN').exclude(location=None)
    markers = []
    for pembangunan in pembangunan_perencanaan:
        if pembangunan.location is not None:
            marker = {
                'lat': pembangunan.location.latitude,
                'lng': pembangunan.location.longitude,
                'nama_fasilitas': pembangunan.nama_fasilitas,
                'konstruksi_selesai': pembangunan.konstruksi_selesai,
                
            }
            if pembangunan.gambar:
                marker['gambar'] = pembangunan.gambar.url
            else:
                marker['gambar'] = None
            markers.append(marker)
    context = {
        'markers': markers
    }
    return render(request, 'peta/peta perencanaan.html',context)



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
    fasilitas_data = Fasilitas_perlengkapan.objects.all()
    success_messages = messages.get_messages(request)
    success_message = next((m.message for m in success_messages if m.level == messages.SUCCESS), None)
    error_messages = messages.get_messages(request)
    error_message = next((m.message for m in error_messages if m.level == messages.ERROR), None)
    context = {
        'success_message': success_message,
        'error_message': error_message,
        'fasilitas_data': fasilitas_data,
    }
    return render(request, 'datatables/data fpj.html',context)

@login_required(login_url=settings.LOGIN_URL)
def datapembangunan(request):
    pembangunan_data = Pembangunan.objects.filter(status__tipestatus='PEMBANGUNAN')
    success_messages = messages.get_messages(request)
    success_message = next((m.message for m in success_messages if m.level == messages.SUCCESS), None)
    error_messages = messages.get_messages(request)
    error_message = next((m.message for m in error_messages if m.level == messages.ERROR), None)
    context = {
        'pembangunan_data': pembangunan_data,
        'success_message': success_message,
        'error_message': error_message,
    }
    
    return render(request, 'datatables/pembangunan.html',context)

@login_required(login_url=settings.LOGIN_URL)
def datapengajuan(request):
    pengajuan_data = Pengajuan.objects.all()
    success_messages = messages.get_messages(request)
    success_message = next((m.message for m in success_messages if m.level == messages.SUCCESS), None)
    error_messages = messages.get_messages(request)
    error_message = next((m.message for m in error_messages if m.level == messages.ERROR), None)
    context = {
        'pengajuan_data': pengajuan_data,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'datatables/pengajuan.html',context)

@login_required(login_url=settings.LOGIN_URL)
def delete_fasilitas(request,fasilitas_id):
    fasilitas = Fasilitas_perlengkapan.objects.get(pk=fasilitas_id)

    if request.method == 'POST':
        try:
            
            # Hapus objek fasilitas
            fasilitas.delete()
            
            messages.success(request, 'Data berhasil dihapus.')
            return redirect('datafpj')
        
        except Exception as e:
            messages.error(request, 'Terjadi kesalahan saat menghapus data.')
            print(str(e))
        context = {
        'fasilitas': fasilitas
    }
    return render(request, 'datatables/data fpj.html',context)

@login_required(login_url=settings.LOGIN_URL)
def delete_pembangunan(request, pembangunan_id):
    pembangunan = Pembangunan.objects.get(pk=pembangunan_id)
    
    # Menampilkan SweetAlert konfirmasi penghapusan
    if request.method == 'POST':
        try:
            # Hapus data yang berelasi
            pembangunan.location.delete()
            pembangunan.status.delete()
            pembangunan.kondisi.delete()
            
            # Hapus objek pembangunan
            pembangunan.delete()
            
            messages.success(request, 'Data berhasil dihapus.')
            return redirect('datapembangunan')
        
        except Exception as e:
            messages.error(request, 'Terjadi kesalahan saat menghapus data.')
            print(str(e))
        context = {
        'pembangunan': pembangunan
    }
    return render(request, 'datatables/pembangunan.html', context)

@login_required(login_url=settings.LOGIN_URL)
def delete_perencanaan(request, pembangunan_id):
    pembangunan = Pembangunan.objects.get(pk=pembangunan_id)
    
    # Menampilkan SweetAlert konfirmasi penghapusan
    if request.method == 'POST':
        try:
            # Hapus data yang berelasi
            pembangunan.location.delete()
            pembangunan.status.delete()
            pembangunan.kondisi.delete()
            
            # Hapus objek pembangunan
            pembangunan.delete()
            
            messages.success(request, 'Data berhasil dihapus.')
            return redirect('dataperencanaan')
        
        except Exception as e:
            messages.error(request, 'Terjadi kesalahan saat menghapus data.')
            print(str(e))
        context = {
        'pembangunan': pembangunan
    }
    return render(request, 'datatables/perencanaan.html', context)


@login_required(login_url=settings.LOGIN_URL)
def delete_kerusakanringan(request, kerusakanid):
    kerusakan = Kerusakan.objects.get(pk=kerusakanid)
    
    if request.method == 'POST':
        try:
            # Hapus data yang berelasi
            kerusakan.location.delete()
            kerusakan.rusak.delete()
            kerusakan.masyarakatid.delete()
            
            # Hapus objek kerusakan
            kerusakan.delete()
            
            messages.success(request, 'Data berhasil dihapus.')
            return redirect('kerusakanringan')
        
        except Exception as e:
            messages.error(request, 'Terjadi kesalahan saat menghapus data.')
            print(str(e))
    
    context = {
        'kerusakan': kerusakan
    }
    return render(request, 'kerusakan/ringan.html', context)

@login_required(login_url=settings.LOGIN_URL)
def delete_kerusakansedang(request, kerusakanid):
    kerusakan = Kerusakan.objects.get(pk=kerusakanid)
    
    if request.method == 'POST':
        try:
            # Hapus data yang berelasi
            kerusakan.location.delete()
            kerusakan.rusak.delete()
            kerusakan.masyarakatid.delete()
            
            # Hapus objek kerusakan
            kerusakan.delete()
            
            messages.success(request, 'Data berhasil dihapus.')
            return redirect('kerusakansedang')
        
        except Exception as e:
            messages.error(request, 'Terjadi kesalahan saat menghapus data.')
            print(str(e))
    
    context = {
        'kerusakan': kerusakan
    }
    return render(request, 'kerusakan/sedang.html', context)

@login_required(login_url=settings.LOGIN_URL)
def delete_kerusakanberat(request, kerusakanid):
    kerusakan = Kerusakan.objects.get(pk=kerusakanid)
    
    if request.method == 'POST':
        try:
            # Hapus data yang berelasi
            kerusakan.location.delete()
            kerusakan.rusak.delete()
            kerusakan.masyarakatid.delete()
            
            # Hapus objek kerusakan
            kerusakan.delete()
            
            messages.success(request, 'Data berhasil dihapus.')
            return redirect('kerusakanberat')
        
        except Exception as e:
            messages.error(request, 'Terjadi kesalahan saat menghapus data.')
            print(str(e))
    
    context = {
        'kerusakan': kerusakan
    }
    return render(request, 'kerusakan/berat.html', context)


@login_required(login_url=settings.LOGIN_URL)
def delete_pengajuan(request, pengajuan_id):
    pengajuan = Pengajuan.objects.get(pk=pengajuan_id)
    
    # Menampilkan SweetAlert konfirmasi penghapusan
    if request.method == 'POST':
        try:
            # Hapus data yang berelasi
            pengajuan.location.delete()
            pengajuan.statuspengajuan.delete()
            pengajuan.masyarakatid.delete()
            
            # Hapus objek Pengajuan
            pengajuan.delete()
            
            messages.success(request, 'Data berhasil dihapus.')
            return redirect('datapengajuan')
        
        except Exception as e:
            messages.error(request, 'Terjadi kesalahan saat menghapus data.')
            print(str(e))
    
    context = {
        'pengajuan': pengajuan
    }
    return render(request, 'datatables/pengajuan.html', context)



@login_required(login_url=settings.LOGIN_URL)
def dataperencanaan(request):
    pembangunan_data = Pembangunan.objects.filter(status__tipestatus='PERENCANAAN')
    success_messages = messages.get_messages(request)
    success_message = next((m.message for m in success_messages if m.level == messages.SUCCESS), None)
    error_messages = messages.get_messages(request)
    error_message = next((m.message for m in error_messages if m.level == messages.ERROR), None)
    context = {
        'pembangunan_data': pembangunan_data,
        'success_message': success_message,
        'error_message': error_message,
    }
    
    return render(request, 'datatables/perencanaan.html',context)

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
    kerusakan_data = Kerusakan.objects.filter(rusak__tiperusak="RUSAK BERAT")
    success_messages = messages.get_messages(request)
    success_message = next((m.message for m in success_messages if m.level == messages.SUCCESS), None)
    error_messages = messages.get_messages(request)
    error_message = next((m.message for m in error_messages if m.level == messages.ERROR), None)
    context = {
        'kerusakan_data':kerusakan_data,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'kerusakan/berat.html',context)

@login_required(login_url=settings.LOGIN_URL)
def kerusakansedang(request):
    kerusakan_data = Kerusakan.objects.filter(rusak__tiperusak="RUSAK SEDANG")
    success_messages = messages.get_messages(request)
    success_message = next((m.message for m in success_messages if m.level == messages.SUCCESS), None)
    error_messages = messages.get_messages(request)
    error_message = next((m.message for m in error_messages if m.level == messages.ERROR), None)
    context = {
        'kerusakan_data':kerusakan_data,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'kerusakan/sedang.html',context)

@login_required(login_url=settings.LOGIN_URL)
def kerusakanringan(request):
    kerusakan_data = Kerusakan.objects.filter(rusak__tiperusak="RUSAK RINGAN")
    success_messages = messages.get_messages(request)
    success_message = next((m.message for m in success_messages if m.level == messages.SUCCESS), None)
    error_messages = messages.get_messages(request)
    error_message = next((m.message for m in error_messages if m.level == messages.ERROR), None)
    context = {
        'kerusakan_data':kerusakan_data,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'kerusakan/ringan.html',context)

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
    kondisi_choices = Kondisi.KONDISI_CHOICES
    status_choices = Status.STATUS_CHOICES

    if request.method == 'POST':
        pembangunan_form = PembangunanForm(request.POST, request.FILES)
        
        if pembangunan_form.is_valid():
            pembangunan = pembangunan_form.save(commit=False)
            pembangunan.nama_fasilitas = Fasilitas_perlengkapan.objects.get(nama_fasilitas=request.POST['nama_fasilitas'])
            pembangunan.jenis_perlengkapan = Perlengkapan_jalan.objects.get(jenis_perlengkapan=request.POST['jenis_perlengkapan'])
            pembangunan.tanggal_bangun = request.POST['tanggal_bangun']
            pembangunan.konstruksi_selesai = request.POST['konstruksi_selesai']
            pembangunan.volume = request.POST['volume']
            pembangunan.ruasjalan = request.POST['RuasJalan']
            pembangunan.deskripsi = request.POST['deskripsi']
            if 'gambar' in request.FILES:
                pembangunan.gambar = request.FILES['gambar']
            
            tipe_kondisi = request.POST['kondisi_id']
            tipe_status = request.POST['status_id']
            
            kondisi = Kondisi.objects.create(tipekondisi=tipe_kondisi)
            status = Status.objects.create(tipestatus=tipe_status)
            
            pembangunan.kondisi = kondisi
            pembangunan.status = status
            
            location = Location.objects.create(
                latitude=request.POST['latitude'],
                longitude=request.POST['longitude'],
            )
            pembangunan.location = location

            pembangunan.save()
            
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('masukdatapembangunan')  # Ganti 'masukdatapembangunan' dengan URL yang sesuai
            
        else:
            errors = pembangunan_form.errors
            print(errors)
            messages.error(request, 'Terjadi kesalahan dalam menambahkan data.')
    else:
        pembangunan_form = PembangunanForm()
    
    context = {
        'pembangunan_form': pembangunan_form,
        'kondisi_choices': kondisi_choices,
        'status_choices': status_choices,
    }
    
    return render(request, 'create/Pembangunan.html', context)

@login_required(login_url=settings.LOGIN_URL)
def editdatapembangunan(request,pembangunan_id):
    kondisi_choices = Kondisi.KONDISI_CHOICES
    status_choices = Status.STATUS_CHOICES
    pembangunan = Pembangunan.objects.get(pk=pembangunan_id)

    if request.method == 'POST':
        form = PembangunanForm(request.POST, request.FILES,instance=pembangunan)
        if form.is_valid():
            pembangunan = form.save(commit=False)
            pembangunan.nama_fasilitas = Fasilitas_perlengkapan.objects.get(nama_fasilitas=request.POST['nama_fasilitas'])
            pembangunan.jenis_perlengkapan = Perlengkapan_jalan.objects.get(jenis_perlengkapan=request.POST['jenis_perlengkapan'])
            pembangunan.tanggal_bangun = request.POST['tanggal_bangun']
            pembangunan.konstruksi_selesai = request.POST['konstruksi_selesai']
            pembangunan.ruasjalan = request.POST['RuasJalan']
            pembangunan.volume = request.POST['volume']
            pembangunan.deskripsi = request.POST['deskripsi']
            if 'gambar' in request.FILES:
                pembangunan.gambar = request.FILES['gambar']
            
            tipe_kondisi = request.POST['kondisi_id']
            tipe_status = request.POST['status_id']
            
            kondisi = Kondisi.objects.create(tipekondisi=tipe_kondisi)
            status = Status.objects.create(tipestatus=tipe_status)
            
            pembangunan.kondisi = kondisi
            pembangunan.status = status
            
            location = Location.objects.create(
                latitude=request.POST['latitude'],
                longitude=request.POST['longitude'],
            )
            pembangunan.location = location

            pembangunan.save()

            messages.success(request, 'Data berhasil diubah dari data sebelumnya')
            return redirect('datapembangunan')  # Ganti 'nama_halaman' dengan URL halaman yang sesuai
        else:
            messages.error(request, 'Terjadi kesalahan dalam menyimpan data.')
    else:
        form = PembangunanForm(initial={
            'latitude': pembangunan.location.latitude,
            'longitude': pembangunan.location.longitude,
            'kondisi': pembangunan.kondisi.tipekondisi,
            'status': pembangunan.status.tipestatus,
            'deskripsi': pembangunan.deskripsi,
            'volume': pembangunan.volume,
            'tanggal_bangun':pembangunan.tanggal_bangun,
            'konstruksi_selesai': pembangunan.konstruksi_selesai,
            'nama_fasilitas': pembangunan.nama_fasilitas,
            'jenis_perlengkapan': pembangunan.jenis_perlengkapan,
            'ruasjalan':pembangunan.ruasjalan,
        })
        context = {
        'pembangunan': pembangunan,
        'form': form,
        'kondisi_choices': kondisi_choices,
        'status_choices': status_choices,
    }
    return render(request, 'create/Edit data.html', context)

    
@login_required(login_url=settings.LOGIN_URL)
def masukdataperencanaan(request):
    kondisi_choices = Kondisi.KONDISI_CHOICES
    status_choices = Status.STATUS_CHOICES

    if request.method == 'POST':
        pembangunan_form = PembangunanForm(request.POST, request.FILES)
        
        if pembangunan_form.is_valid():
            pembangunan = pembangunan_form.save(commit=False)
            pembangunan.nama_fasilitas = Fasilitas_perlengkapan.objects.get(nama_fasilitas=request.POST['nama_fasilitas'])
            pembangunan.jenis_perlengkapan = Perlengkapan_jalan.objects.get(jenis_perlengkapan=request.POST['jenis_perlengkapan'])
            pembangunan.tanggal_bangun = request.POST['tanggal_bangun']
            pembangunan.konstruksi_selesai = request.POST['konstruksi_selesai']
            pembangunan.volume = request.POST['volume']
            pembangunan.ruasjalan = request.POST['RuasJalan']
            pembangunan.deskripsi = request.POST['deskripsi']
            if 'gambar' in request.FILES:
                pembangunan.gambar = request.FILES['gambar']
            
            tipe_kondisi = request.POST['kondisi_id']
            tipe_status = request.POST['status_id']
            
            kondisi = Kondisi.objects.create(tipekondisi=tipe_kondisi)
            status = Status.objects.create(tipestatus=tipe_status)
            
            pembangunan.kondisi = kondisi
            pembangunan.status = status
            
            location = Location.objects.create(
                latitude=request.POST['latitude'],
                longitude=request.POST['longitude'],
            )
            pembangunan.location = location

            pembangunan.save()
            
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('masukdataperencanaan')  # Ganti 'masukdatapembangunan' dengan URL yang sesuai
            
        else:
            errors = pembangunan_form.errors
            print(errors)
            messages.error(request, 'Terjadi kesalahan dalam menambahkan data.')
    else:
        pembangunan_form = PembangunanForm()
    
    context = {
        'pembangunan_form': pembangunan_form,
        'kondisi_choices': kondisi_choices,
        'status_choices': status_choices,
    }
    return render(request, 'create/Perencanaan.html',context)


@login_required(login_url=settings.LOGIN_URL)
def tambahdataperencanaan(request,pengajuan_id):
    kondisi_choices = Kondisi.KONDISI_CHOICES
    status_choices = Status.STATUS_CHOICES
    pengajuan = Pengajuan.objects.get(pk=pengajuan_id)

    if request.method == 'POST':
        form = PembangunanForm(request.POST, request.FILES)
        if form.is_valid():
            pembangunan = form.save(commit=False)
            pembangunan.nama_fasilitas = Fasilitas_perlengkapan.objects.get(nama_fasilitas=request.POST['nama_fasilitas'])
            pembangunan.jenis_perlengkapan = Perlengkapan_jalan.objects.get(jenis_perlengkapan=request.POST['jenis_perlengkapan'])
            pembangunan.tanggal_bangun = request.POST['tanggal_bangun']
            pembangunan.konstruksi_selesai = request.POST['konstruksi_selesai']
            pembangunan.volume = request.POST['volume']
            pembangunan.ruasjalan = request.POST['RuasJalan']
            pembangunan.deskripsi = request.POST['deskripsi']
            if 'gambar' in request.FILES:
                pembangunan.gambar = request.FILES['gambar']
            
            tipe_kondisi = request.POST['kondisi_id']
            tipe_status = request.POST['status_id']
            
            kondisi = Kondisi.objects.create(tipekondisi=tipe_kondisi)
            status = Status.objects.create(tipestatus=tipe_status)
            
            pembangunan.kondisi = kondisi
            pembangunan.status = status
            
            location = Location.objects.create(
                latitude=request.POST['latitude'],
                longitude=request.POST['longitude'],
            )
            pembangunan.location = location

            pembangunan.save()

            messages.success(request, 'Data berhasil disimpan.')
            return redirect('tambahdataperencanaan')  # Ganti 'nama_halaman' dengan URL halaman yang sesuai
        else:
            messages.error(request, 'Terjadi kesalahan dalam menyimpan data.')
    else:
        form = PembangunanForm(initial={
            'nama': pengajuan.masyarakatid.nama,
            'notelepon':pengajuan.masyarakatid.notelepon,
            'nama_fasilitas': pengajuan.nama_fasilitas.nama_fasilitas,
            'jenis_perlengkapan': pengajuan.jenis_perlengkapan.jenis_perlengkapan,
            'latitude': pengajuan.location.latitude,
            'longitude': pengajuan.location.longitude,
        })

    context = {
        'pengajuan': pengajuan,
        'form': form,
        'kondisi_choices': kondisi_choices,
        'status_choices': status_choices,
    }
    return render(request, 'create/Edit Perencanaan.html', context)



def editdataperlengkapan(request, fasilitas_id):
    fasilitas = get_object_or_404(Fasilitas_perlengkapan, pk=fasilitas_id)
    perlengkapan_list = Perlengkapan_jalan.objects.values_list('jenis_perlengkapan', flat=True)

    if request.method == 'POST':
        fasilitas_form = FasilitasForm(request.POST, request.FILES, instance=fasilitas)
        if fasilitas_form.is_valid():
            nama_fasilitas = fasilitas_form.cleaned_data['nama_fasilitas']
            if Fasilitas_perlengkapan.objects.exclude(pk=fasilitas_id).filter(nama_fasilitas=nama_fasilitas).exists():
                if fasilitas.nama_fasilitas != nama_fasilitas:
                    messages.error(request, 'Nama fasilitas sudah ada di database.')
                else:
                    fasilitas_form.save()
                    messages.success(request, 'Data berhasil diubah')
            else:
                fasilitas_form.save()
                messages.success(request, 'Data berhasil diubah')
                return redirect('datafpj')
        else:
            errors = fasilitas_form.errors
            print(errors)
            messages.error(request, 'Terjadi kesalahan dalam menyimpan data.')
    else:
        # Isi form dengan data yang ada untuk diedit
        fasilitas_form = FasilitasForm(instance=fasilitas)

    context = {
        'fasilitas': fasilitas,
        'fasilitas_form': fasilitas_form,
        'perlengkapan_list': perlengkapan_list,
    }
    return render(request, 'create/Edit data Perlengkapan.html', context)

        
@login_required(login_url=settings.LOGIN_URL)
def masukdataperlengkapan(request):
    perlengkapan_list = Perlengkapan_jalan.objects.values_list('jenis_perlengkapan', flat=True)
    if request.method == 'POST':
        fasilitas_form = FasilitasForm(request.POST, request.FILES)
        if fasilitas_form.is_valid():
            fasilitas = fasilitas_form.save(commit=False)
            fasilitas.nama_fasilitas = request.POST['nama_fasilitas']
            fasilitas.tipekhusus =request.POST['tipekhusus']
            fasilitas.namakhusus =request.POST['namakhusus']
            fasilitas.tanggal_ditambahkan =request.POST['tanggal_bangun']
            fasilitas.volume =request.POST['volume']
            fasilitas.color =request.POST['color']
            fasilitas.jenis_perlengkapan = Perlengkapan_jalan.objects.get(jenis_perlengkapan=request.POST['jenis_perlengkapan'])
            fasilitas.deskripsi =request.POST['deskripsi']
            if 'gambar' in request.FILES:
                fasilitas.gambar = request.FILES['gambar']
            
            fasilitas.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('masukdataperlengkapan')  # Ganti 'masukdatapembangunan' dengan URL yang sesuai
            
        else:
            errors = fasilitas_form.errors
            print(errors)
            messages.error(request, 'Terjadi kesalahan dalam menambahkan data.')
    else:
        fasilitas_form = FasilitasForm()
            
        
    context = {
        'fasilitas_form': fasilitas_form,
        'perlengkapan_list': perlengkapan_list,
    }
    return render(request, 'create/Perlengkapan jalan.html',context)






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
    jumlah_data = Pengajuan.objects.count()
    kerusakan = Kerusakan.objects.count()
    data_perencanaan = Pembangunan.objects.filter(status__tipestatus='PERENCANAAN').count()
    data_pembangunan = Pembangunan.objects.filter(status__tipestatus='PEMBANGUNAN').count()
    admin = request.user
    context = {
        'data_perencanaan' : data_perencanaan,
        'data_pembangunan' : data_pembangunan,
        'jumlah_data': jumlah_data,
        'kerusakan': kerusakan,
        'admin': admin,
        }
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