from django.contrib import admin
from app_sitani.models import KelompokTani, Profile, TokoPertanian, UsulanBantuanPoktan, BeritaPertanian

class KeltanAdmin(admin.ModelAdmin):
    list_display = ['Id_Poktan','Nama_Poktan','Kecamatan','Desa','Ketua','Sekretaris','Bendahara','Pemilik_Lahan','Surat_Lahan','Kelas_Poktan','Tanggal_Pembentukan','Kelas_Poktan','Status_Poktan']
    search_fields = ['Nama_Poktan','Ketua','Luas_Areal_HA']
    list_filter = ['Id_Poktan']
    list_per_page = 4

admin.site.register(KelompokTani, KeltanAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['NIP','Nama','Foto_Profile','Alamat','Id_Jabatan','Id_Golongan']
    search_fields = ['Nama','Id_Alamat','Id_Jabatan']
    list_filter = ['NIP']
    list_per_page = 4

admin.site.register(Profile, ProfileAdmin)


class TokoAdmin(admin.ModelAdmin):
    list_display = ['Id_Toko','Foto_Toko','Nama_Toko','Alamat','Jam_Buka','Jam_Tutup']
    search_fields = ['Nama_Toko','Jam_Buka','Jam_tutup']
    list_filter = ['Id_Toko']
    list_per_page = 4

admin.site.register(TokoPertanian, TokoAdmin)

class BantuanPoktanAdmin(admin.ModelAdmin):
    list_display = ['Id_Bantuan','Id_Poktan','Id_Banpem','Ketua','Jumlah_Bantuan','Satuan_Bantuan','Tanggal_Bantuan','Gambar_Lokasi']
    search_fields = ['Id_Poktan','Id_Banpem','Nama_Poktan']
    list_filter = ['Id_Bantuan']
    list_per_page = 4

admin.site.register(UsulanBantuanPoktan, BantuanPoktanAdmin)

class BeritaAdmin(admin.ModelAdmin):
    list_display = ['Id_Berita','Judul_Berita','Foto_Berita','Isi_Berita','Jam_Update','Tanggal_Update']
    search_fields = ['Judul_Berita','Isi_Berita','Jam_Update']
    list_filter = ['Id_Berita']
    list_per_page = 4

admin.site.register(BeritaPertanian, BeritaAdmin)
