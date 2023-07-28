from django.contrib import admin
from core.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

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

class KerusakanAdmin(admin.ModelAdmin):
    pass
class Adminadmin(admin.ModelAdmin):
    pass
class BerandaAdmin(admin.ModelAdmin):
    pass
class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(Admin,CustomUserAdmin)
admin.site.register(Fasilitas_perlengkapan,FasilitasAdmin)
admin.site.register(Status,Statusadmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Perlengkapan_jalan,PerlengkapanJalanAdmin)
admin.site.register(Masyarakat,MasyarakatAdmin)
admin.site.register(Pengajuan,PengajuanAdmin)
admin.site.register(Pembangunan,PembangunanAdmin)

admin.site.register(Kerusakan,KerusakanAdmin)
# admin.site.register(Admin,Adminadmin)
admin.site.register(Beranda,BerandaAdmin)

