from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.beranda,name='beranda'),
    path('peta/',views.maps, name='maps'),
    path('jenisperlengkapan/',views.jenisperlengkapan, name='jenisperlengkapan'),
    # khuusus baru
    # path('pengajuan/',views.pengajuan, name='pengajuan'),
    path('perlengkapanjalandata/',views.get_json_datafpj, name='perlengkapanjalandata'),
    path('get_jenis_perlengkapan/', views.get_jenis_perlengkapan, name='get_jenis_perlengkapan'),
    path('get_nama_fasilitas/', views.get_nama_fasilitas, name='get_nama_fasilitas'),
    path('create_pengajuan/', views.create_pengajuan, name='create_pengajuan'),
    
    # dashboard
    path('dashboard/',login_required(views.dashboardadmin), name='dashboardadmin'),
    path('Account/',views.Account, name='Account'),
    
    # peta
    path('petaadkerusakan/',views.petaadkerusakan, name='petaadkerusakan'),
    path('petaadpembangunan/',views.petaadpembangunan, name='petaadpembangunan'),
    path('petaadpengajuan/',views.petaadpengajuan, name='petaadpengajuan'),
    path('petaadperencanaan/',views.petaadperencanaan, name='petaadperencanaan'),
    
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
    path('dataperencanaan/',views.dataperencanaan, name='dataperencanaan'),
    
    # masukkan data admin
    path('masukdatapembangunan/',views.masukdatapembangunan, name='masukdatapembangunan'),
    path('masukdataperencanaan/',views.masukdataperencanaan, name='masukdataperencanaan'),
    path('tambahdataperencanaan/<int:pengajuan_id>/',views.tambahdataperencanaan, name='tambahdataperencanaan'),
    path('masukdataperlengkapan/',views.masukdataperlengkapan, name='masukdataperlengkapan'),
    
    
    # seleksi
    path('seleksidibawah/',views.seleksidibawah, name='seleksidibawah'),
    path('seleksimemenuhi/',views.seleksimemenuhi, name='seleksimemenuhi'),
    
    # pelaporan
    path('pelaporan/',views.pelaporan, name='pelaporan'),
    
    # kerusakan
    path('kerusakanringan/',views.kerusakanringan, name='kerusakanringan'),
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
