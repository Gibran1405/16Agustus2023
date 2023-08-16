from django.forms import ModelForm,TextInput, Select, Textarea
from app_sitani.models import KelompokTani, Profile, TokoPertanian, UsulanBantuanPoktan, BeritaPertanian, BarangDariPemerintah, Golongan, Jabatan
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


#Form Keltan
class FormKeltan(ModelForm): 
    class Meta:
        model = KelompokTani
        fields = ['Nama_Poktan', 'Kecamatan', 'Desa', 'Ketua','NIK_Ketua', 'KTP_Ketua','Sekretaris', 'Bendahara','Pemilik_Lahan','Surat_Lahan', 'No_Telephone', 'Komoditas','Score', 'Luas_Areal_HA', 'Tanggal_Pembentukan', 'Jumlah_Anggota', 'Status_Poktan', 'Kelas_Poktan']
        widgets = {
        'Nama_Poktan': forms.TextInput(attrs={'class': 'form-control'}),
        'Kecamatan': forms.TextInput(attrs={'class': 'form-control', 'value': 'Pagaden Barat', 'readonly': 'readonly'}),
        'Desa': forms.Select(attrs={'class': 'form-control'}),
        'Ketua': forms.TextInput(attrs={'class': 'form-control'}),
        'NIK_Ketua': forms.NumberInput(attrs={'class': 'form-control'}),
        'Sekretaris': forms.TextInput(attrs={'class': 'form-control'}),
        'Bendahara': forms.TextInput(attrs={'class': 'form-control'}),
        'Pemilik_Lahan': forms.TextInput(attrs={'class': 'form-control'}),
        'No_Telephone': forms.NumberInput(attrs={'class': 'form-control'}),
        'Score': forms.NumberInput(attrs={'class': 'form-control'}),
        'Luas_Areal_HA': forms.NumberInput(attrs={'class': 'form-control'}),
        'Tanggal_Pembentukan': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'Jumlah_Anggota': forms.NumberInput(attrs={'class': 'form-control'}),
        'Status_Poktan': forms.Select(attrs={'class': 'form-control'}),
        'Kelas_Poktan': forms.Select(attrs={'class': 'form-control'}),
        }  

#Form Golongan
class FormGolongan(ModelForm):
    class Meta:
        model = Golongan 
        fields = ['Golongan','Jabatan_Fungsional']
        widgets = {
            'Golongan' : forms.TextInput(attrs={'class': 'form-control'}),
            'Jabatan_Fungsional' : forms.TextInput(attrs={'class': 'form-control'}),
        }

#Form Jabatan
class FormJabatan(ModelForm):
    class Meta:
        model = Jabatan
        fields = ['Nama_Jabatan']
        widgets = {
            'Nama_Jabatan' : forms.TextInput(attrs={'class': 'form-control'}),
        }
     
#Form Profile
class FormProfilePegawai(ModelForm):
    class Meta:
        model = Profile
        fields = ['NIP', 'Nama', 'Id_Jabatan', 'Id_Golongan','Foto_Profile', 'Alamat']
        widgets = {
            'NIP': forms.TextInput(attrs={'class': 'form-control'}),
            'Nama': forms.TextInput(attrs={'class': 'form-control'}),
            'Id_Jabatan': forms.Select(attrs={'class': 'form-control'}),
            'Id_Golongan': forms.Select(attrs={'class': 'form-control'}),
            'Alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

#Form Toko        
class FormToko(ModelForm): 
    class Meta:
        model = TokoPertanian
        fields =['Nama_Toko','Nama_Pemilik','Foto_Toko','Jam_Buka','Jam_Tutup','Deskripsi','Alamat']
        widgets = {
            'Nama_Toko' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Nama_Pemilik' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Jam_Buka' : forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'Jam_Tutup' : forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'Deskripsi' :forms.Textarea(attrs={'class' : 'form-control','row': 4}),
            'Alamat' : forms.Textarea(attrs={'class' : 'form-control','row': 4}),
        }
 
 #Form Bantuan       
class FormBantuanPoktan(ModelForm):
    class Meta:
        model = UsulanBantuanPoktan
        fields = ['Id_Poktan', 'Id_Banpem', 'Jumlah_Bantuan', 'Satuan_Bantuan', 'Tanggal_Bantuan', 'Gambar_Lokasi', 'Status']
        widgets = {
            'Id_Poktan': forms.Select(attrs={'class': 'form-control'}),
            'Id_Banpem': forms.Select(attrs={'class': 'form-control'}),
            'Jumlah_Bantuan': forms.NumberInput(attrs={'class': 'form-control'}),
            'Satuan_Bantuan': forms.TextInput(attrs={'class': 'form-control'}),
            'Tanggal_Bantuan': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Status': forms.Select(attrs={'class': 'form-control'}),
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.Id_Banpem and instance.Jumlah_Bantuan:
            barang = instance.Id_Banpem
            if barang.Jumlah_Barang >= instance.Jumlah_Bantuan:
                if commit:
                    instance.save()  # Simpan objek BantuanPoktan ke database sebelum mengurangi Jumlah_Barang
                difference = instance.Jumlah_Bantuan - self.cleaned_data['Jumlah_Bantuan']
                barang.Jumlah_Barang -= difference
                barang.save()  # Simpan perubahan pada Jumlah_Barang setelah pengurangan

                return instance
            else:
                self.add_error('Jumlah_Bantuan', 'Jumlah bantuan melebihi jumlah barang yang tersedia.')
        else:
            if commit:
                instance.save()
        
        if instance.status == "Dapat Bantuan":
            next_year = datetime.now().year + 1
            kelompok_tani = KelompokTani.objects.filter(Nama_Poktan=instance.Nama_Poktan, tahun__gte=next_year)
            kelompok_tani.update(tampilkan=False)
            message = "Kelompok Tani ini Sudah Mendapatkan Bantuan di tahun sekarang."
            self.add_error(None, message)
        
        return instance

    def delete(self):
        instance = self.instance
        if instance.Id_Banpem and instance.Jumlah_Bantuan:
            barang = instance.Id_Banpem
            barang.Jumlah_Barang += instance.Jumlah_Bantuan
            barang.save()
        instance.delete()
    
#Form Barang
class FormBarangDariPemerintah(ModelForm):
    class Meta:
        model = BarangDariPemerintah
        fields = ['Nama_Barang', 'Jumlah_Barang', 'Satuan', 'Tanggal']
        widgets = {
            'Nama_Barang': forms.TextInput(attrs={'class': 'form-control'}),
            'Jumlah_Barang': forms.NumberInput(attrs={'class': 'form-control'}),
            'Satuan': forms.TextInput(attrs={'class': 'form-control'}),
            'Tanggal': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }


#Form Register
class FormRegister(UserCreationForm):
    is_staff = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2','is_staff']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'is_staff': forms.TextInput(attrs={'class': 'form-control'}),
        }


#Form Berita
class FormBerita(ModelForm):
    class Meta:
        model = BeritaPertanian
        fields = ['Penulis','Judul_Berita','Foto_Berita','Isi_Berita','Jam_Update','Tanggal_Update']
        widgets = {
            'Penulis' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Judul_Berita' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Isi_Berita': forms.Textarea(attrs={'class' : 'form-control','row':10}),
            'Jam_Update' : forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'Tanggal_Update': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }


#Form Lupa Sandi
class LupaSandi(SetPasswordForm):
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()
    class Meta:
        fields = ['new_password1','new_password2']
        widgets = {
            'new_password1': forms.TextInput({'class': 'form-control'}),
            'new_password2': forms.TextInput({'class': 'form-control'}),
        }

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        # Tambahkan validasi tambahan sesuai kebutuhan Anda
        return new_password2
    
              