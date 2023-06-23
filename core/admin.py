from django.contrib import admin
from core.models import *
# Register your models here.
class Perencanaanadmin(admin.ModelAdmin):
    pass
class FasilitasAdmin(admin.ModelAdmin):
    pass
class Statusadmin(admin.ModelAdmin):
    pass
class LocationAdmin(admin.ModelAdmin):
    pass
class PerlengkapanJalanAdmin(admin.ModelAdmin):
    pass
class MasyarakatAdmin(admin.ModelAdmin):
    pass
class PengajuanAdmin(admin.ModelAdmin):
    pass
class PembangunanAdmin(admin.ModelAdmin):
    pass
class PenyeleksianAdmin(admin.ModelAdmin):
    pass
class PerencanaanAdmin(admin.ModelAdmin):
    pass
class Adminadmin(admin.ModelAdmin):
    pass
class BerandaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Fasilitas_perlengkapan,FasilitasAdmin)
admin.site.register(Status,Statusadmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Perlengkapan_jalan,PerlengkapanJalanAdmin)
admin.site.register(Masyarakat,MasyarakatAdmin)
admin.site.register(Pengajuan,PengajuanAdmin)
admin.site.register(Pembangunan,PembangunanAdmin)
admin.site.register(Penyeleksian,PenyeleksianAdmin)
admin.site.register(Perencanaan,PerencanaanAdmin)
admin.site.register(Admin,Adminadmin)
admin.site.register(Beranda,BerandaAdmin)

