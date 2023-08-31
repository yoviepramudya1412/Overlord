from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    
    
    # urlbaru
    path('export-to-excel/', views.export_to_excel, name='export_to_excel'),
    path('export-to-excelper/', views.export_to_excelper, name='export_to_excelper'),
    path('export_pengajuan_to_excel/', views.export_pengajuan_to_excel, name='export_pengajuan_to_excel'),
    path('export_kerusakan_to_excel/', views.export_kerusakan_to_excel, name='export_kerusakan_to_excel'),
    
    
    
    path('',views.beranda,name='beranda'),
    path('peta/',views.maps, name='maps'),
    path('jenisperlengkapan/',views.jenisperlengkapan, name='jenisperlengkapan'),
    # khuusus baru
    # path grafik
    
    
    # path('pengajuan/',views.pengajuan, name='pengajuan'),
    path('perlengkapanjalandata/',views.get_json_datafpj, name='perlengkapanjalandata'),
    path('get_jenis_perlengkapan/', views.get_jenis_perlengkapan, name='get_jenis_perlengkapan'),
    path('get_nama_fasilitas/', views.get_nama_fasilitas, name='get_nama_fasilitas'),
    path('create_pengajuan/', views.create_pengajuan, name='create_pengajuan'),
    path('laporkerusakan/', views.laporkerusakan, name='laporkerusakan'),
    
    # dashboard
    path('dashboard/',login_required(views.dashboardadmin), name='dashboardadmin'),
    path('Account/',views.Account, name='Account'),
    
    # peta
    path('petaadkerusakan/',views.petaadkerusakan, name='petaadkerusakan'),
    path('petaadpembangunan/',views.petaadpembangunan, name='petaadpembangunan'),
    path('petaadpengajuan/',views.petaadpengajuan, name='petaadpengajuan'),
    path('petaadperencanaan/',views.petaadperencanaan, name='petaadperencanaan'),
    path('petaroutingpengajuan/<int:pengajuan_id>/',views.petaroutingpengajuan, name='petaroutingpengajuan'),
    path('petaroutingpembangunan/<int:pembangunan_id>/',views.petaroutingpembangunan, name='petaroutingpembangunan'),
    path('petaroutingperencanaan/<int:pembangunan_id>/',views.petaroutingperencanaan, name='petaroutingperencanaan'),
    path('petaroutingkerusakan/<int:kerusakan_id>/',views.petaroutingkerusakan, name='petaroutingkerusakan'),
    
    # staistik
    path('statistikfasilitas/',views.statistikfasiltas, name='statistikfasilitas'),
    path('statistikkerusakan/',views.statistikkerusakan, name='statistikkerusakan'),
    path('statistikpembangunan/',views.statistikpembangunan, name='statistikpembangunan'),
    path('statistikpengajuan/',views.statistikpengajuan, name='statistikpengajuan'),
    path('statistikperencanaan/',views.statistikperencanaan, name='statistikperencanaan'),
    
    
    # data
    path('datafpj/',views.datafpj, name='datafpj'),
    path('datapembangunan/',views.datapembangunan, name='datapembangunan'),
    path('datapengajuan/',views.datapengajuan, name='datapengajuan'),
    path('delete_pengajuan/<int:pengajuan_id>/',views.delete_pengajuan, name='delete_pengajuan'),
    path('delete_pembangunan/<int:pembangunan_id>/',views.delete_pembangunan, name='delete_pembangunan'),
    path('delete_perencanaan/<int:pembangunan_id>/',views.delete_perencanaan, name='delete_perencanaan'),
    path('delete_fasilitas/<int:fasilitas_id>/',views.delete_fasilitas, name='delete_fasilitas'),
    path('delete_kerusakanringan/<int:kerusakanid>/',views.delete_kerusakanringan, name='delete_kerusakanringan'),
    path('delete_kerusakanberat/<int:kerusakanid>/',views.delete_kerusakanberat, name='delete_kerusakanberat'),
    path('delete_kerusakansedang/<int:kerusakanid>/',views.delete_kerusakansedang, name='delete_kerusakansedang'),
    path('dataperencanaan/',views.dataperencanaan, name='dataperencanaan'),
    
    # masukkan data admin
    path('masukdatapembangunan/',views.masukdatapembangunan, name='masukdatapembangunan'),
    path('masukdataperencanaan/',views.masukdataperencanaan, name='masukdataperencanaan'),
    path('editdatapembangunan/<int:pembangunan_id>/',views.editdatapembangunan, name='editdatapembangunan'),
    path('editdataperlengkapan/<int:fasilitas_id>/', views.editdataperlengkapan, name='editdataperlengkapan'),
    path('tambahdataperencanaan/<int:pengajuan_id>/',views.tambahdataperencanaan, name='tambahdataperencanaan'),
    path('masukdataperlengkapan/',views.masukdataperlengkapan, name='masukdataperlengkapan'),
    
    
    # seleksi
    path('seleksidibawah/',views.seleksidibawah, name='seleksidibawah'),
    path('seleksimemenuhi/',views.seleksimemenuhi, name='seleksimemenuhi'),
    
    # pelaporan
    path('pelaporan/',views.pelaporan, name='pelaporan'),
    
    # kerusakan
    path('kerusakanringan/',views.kerusakanringan, name='kerusakanringan'),
    path('kerusakansedang/',views.kerusakansedang, name='kerusakansedang'),
    path('kerusakanberat/',views.kerusakanberat, name='kerusakanberat'),
    
    # bantuan
    path('kontakoperator/',views.kontakoperator, name='kontakoperator'),
    path('layanandinas/',views.layanandinas, name='layanandinas'),
    path('permasalahan/',views.permasalahan, name='permasalahan'),
    
    # panduan
    path('pemandu/',views.pemandu, name='pemandu'),
    path('penggunaan/',views.penggunaan, name='penggunaan'),
    
    # login
    path('masuk/',views.login_view, name='masuk'),
    
    
    path('cadangan/',views.cadangan, name='cadangan'),
    path('logout/',views.logout_view, name='logout'),
]
