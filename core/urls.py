from django.urls import path
from . import views

urlpatterns = [
    path('',views.beranda,name='beranda'),
    path('peta/',views.maps, name='maps'),
    path('jenisperlengkapan/',views.jenisperlengkapan, name='jenisperlengkapan'),
    path('pengajuan/',views.pengajuan, name='pengajuan'),
    
    # dashboard
    path('dashboard/',views.dashboardadmin, name='dashboardadmin'),
    
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
    path('dataperencanaan/',views.dataperencanaan, name='dataperencanaan'),
    
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
    path('login/',views.login, name='login'),
    
    
    path('cadangan/',views.cadangan, name='cadangan'),
]
