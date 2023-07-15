from django import forms
from . models import *


class FasilitasForm(forms.ModelForm):
    gambar = forms.ImageField(required=False)
    class Meta:
        model = Fasilitas_perlengkapan
        fields = ['tipekhusus', 'namakhusus', 'nama_fasilitas', 'tanggal_ditambahkan', 'volume', 'jenis_perlengkapan', 'gambar', 'deskrpsi']

class PengajuanForm(forms.ModelForm):
    gambar = forms.ImageField(required=False)
    
    masyarakatid = forms.ModelChoiceField(queryset=Masyarakat.objects.all(), required=False)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), required=False)
    statuspengajuan = forms.ModelChoiceField(queryset=Status.objects.all(), required=False)

    class Meta:
        model = Pengajuan
        fields = [ 'nama_fasilitas', 'jenis_perlengkapan', 'Fasilitas_khusus', 'gambar', 'masyarakatid', 'location', 'statuspengajuan']

    


class PembangunanForm(forms.ModelForm):
    gambar = forms.ImageField(required=False)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), required=False)
    kondisi = forms.ModelChoiceField(queryset=Kondisi.objects.all(), required=False)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False)
    
    class Meta:
        model = Pembangunan
        fields = ['nama_fasilitas', 'jenis_perlengkapan', 'tanggal_bangun', 'konstruksi_selesai', 'kondisi', 'volume', 'deskripsi', 'location', 'status', 'gambar']
    
    

    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            # Periksa kecocokan username dan password dengan model Admin
            admin = Admin.objects.filter(username=username).first()
            if admin is None or not admin.check_password(password):
                raise forms.ValidationError('Username atau password salah')
        
        return cleaned_data