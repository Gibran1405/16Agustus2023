from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta
from multiselectfield import MultiSelectField
# Create your models here.
    
#kelompok Tani    
class KelompokTani(models.Model):
    Komoditas_Choise = (
        ('Padi','Padi'),
        ('Palawija','Palawija'),
        ('Cabai','Cabai'),
        ('Jamur','Jamur'),
        ('Ternak','Ternak'),
        ('Sapi Potong','Sapi Potong'),
        ('KWT','KWT'),
        ('Pemuda Tani','Pemuda Tani'),
    )
    Desa_Choise = (
        ('Cidahu','Cidahu'),
        ('Balingbing','Balingbing'),
        ('Cidadap','Cidadap'),
        ('Pangsor','Pangsor'),
        ('Bendungan','Bendungan'),
        ('Munjul','Munjul'),
        ('Margahayu','Margahayu'),
        ('Mekarwangi','Mekarwangi'),
    )
    Kelas_Choise = (
        ('Pemula','Pemula'),
        ('Lanjut','Lanjut'),
        ('Madya','Madya'),
        ('Utama','Utama'),
    )
    Status_Choise = (
        ('Aktif','Aktif'),
        ('Tidak Aktif','Tidak Aktif'),
    )
    Id_Poktan = models.AutoField(primary_key=True)
    Nama_Poktan = models.CharField(max_length=25)
    Kecamatan = models.CharField (max_length=30)
    Desa = models.CharField(choices=Desa_Choise, max_length=100, null=True)
    Ketua = models.CharField(max_length=25)
    NIK_Ketua = models.CharField(max_length=16)
    KTP_Ketua = models.ImageField(upload_to='ktp/%Y/%m/%d/', null=True, blank=True)
    Sekretaris = models.CharField(max_length=25)
    Bendahara = models.CharField(max_length=25)
    Pemilik_Lahan = models.CharField(max_length=25, null=True)
    Surat_Lahan = models.ImageField(upload_to='surat/%Y/%m/%d/', null=True, blank=True)
    No_Telephone = models.CharField(max_length=13)
    Komoditas = MultiSelectField(choices= Komoditas_Choise, max_choices=10,max_length=100)
    Score = models.IntegerField(null=True)
    Luas_Areal_HA = models.IntegerField(null=True)
    Jumlah_Anggota = models.IntegerField(null=True)
    Tanggal_Pembentukan = models.DateField(blank=True)
    Status_Poktan = models.CharField(choices=Status_Choise, max_length=100, null=True)
    Kelas_Poktan = models.CharField(choices=Kelas_Choise, max_length=100, null=True)
    
    def __str__(self):
        return self.Nama_Poktan

    
#Golongan
class Golongan(models.Model):
    Id_Golongan = models.AutoField(primary_key=True)
    Golongan = models.CharField(max_length=6, default='IA')
    Jabatan_Fungsional = models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.Golongan}-{self.Jabatan_Fungsional}'

    
#Jabatan
class Jabatan(models.Model):
    Id_Jabatan = models.AutoField(primary_key=True)
    Nama_Jabatan = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Nama_Jabatan


#Profile  
class Profile(models.Model):
    NIP = models.CharField(max_length=18, primary_key=True, null=False)
    Nama = models.CharField(max_length=100)
    Id_Jabatan = models.ForeignKey('Jabatan', on_delete=models.CASCADE, null=True)
    Id_Golongan = models.ForeignKey('Golongan', on_delete=models.CASCADE, null=True)
    Foto_Profile = models.ImageField(upload_to='images/%Y/%m/%d/', null=True, blank=True)
    Alamat = models.TextField()
  
    def __str__(self):
        return self.NIP

    
#Toko Pertanian
class TokoPertanian(models.Model):
    Id_Toko = models.AutoField(primary_key=True)
    Nama_Toko = models.CharField(max_length=50)
    Nama_Pemilik = models.CharField(max_length=50, null=True)
    Foto_Toko = models.ImageField(upload_to='toko/%Y/%m/%d/', null=True, blank=True)
    Deskripsi = models.CharField(max_length=100, null=True)
    Alamat = models.TextField()
    Jam_Buka = models.TimeField()
    Jam_Tutup = models.TimeField()

    def __str__(self):
        return self.Id_Toko
 
    
class UsulanBantuanPoktan(models.Model):
    Status_Choices = (
        ('Dapat Bantuan', 'Dapat Bantuan'),
        ('Tidak Dapat', 'Tidak Dapat'),
        ('Diajukan', 'Diajukan'),
    )
    Id_Bantuan = models.AutoField(primary_key=True)
    Id_Poktan = models.ForeignKey('KelompokTani', on_delete=models.CASCADE, null=True)
    Id_Banpem = models.ForeignKey('BarangDariPemerintah', on_delete=models.CASCADE, null=True)
    Jumlah_Bantuan = models.IntegerField()
    Satuan_Bantuan = models.CharField(max_length=50)
    Tanggal_Bantuan = models.DateField(blank=True)
    Gambar_Lokasi = models.ImageField(upload_to='bantuan/%Y/%m/%d/', null=True, blank=True)
    Status = models.CharField(choices=Status_Choices, max_length=100, null=True)
    
    def Ketua(self):
        if self.Id_Poktan:
            return self.Id_Poktan.Ketua
        return None
    
    def NIK_Ketua(self):
        if self.Id_Poktan:
            return self.Id_Poktan.NIK_Ketua
        return None
    
    def No_Telephone(self):
        if self.Id_Poktan:
            return self.Id_Poktan.No_Telephone
        return None

    def Kecamatan(self):
        if self.Id_Poktan:
            return self.Id_Poktan.Kecamatan
        return None
    
    def Desa(self):
        if self.Id_Poktan:
            return self.Id_Poktan.Desa
        return None
    
    def Jumlah_Anggota(self):
        if self.Id_Poktan:
            return self.Id_Poktan.Jumlah_Anggota
        return None 
    
    def Komoditas(self):
        if self.Id_Poktan:
            return self.Id_Poktan.Komoditas
        return None
    
    def Luas_Areal_HA(self):
        if self.Id_Poktan:
            return self.Id_Poktan.Luas_Areal_HA
        return None

    def Status_Poktan(self):
        if self.Id_Poktan:
            return self.Id_Poktan.Status_Poktan
        return None

    def Kelas_Poktan(self):
        if self.Id_Poktan:
            return self.Id_Poktan.Kelas_Poktan
        return None
    
        
    def delete(self, *args, **kwargs):
        if self.Id_Banpem and self.Jumlah_Bantuan:
            barang = self.Id_Banpem
            barang.Jumlah_Barang += self.Jumlah_Bantuan
            barang.save()

        super().delete(*args, **kwargs)
        
    from datetime import datetime, timedelta

def save(self, *args, **kwargs):
    if self.Id_Banpem and self.Jumlah_Bantuan:
        barang = self.Id_Banpem
        if barang.Jumlah_Barang == 0:
            message = "Tidak dapat menambahkan BantuanPoktan karena Jumlah_Barang pada Id_Banpem sudah mencapai 0."
            raise Exception(message)

        if self.Jumlah_Bantuan > barang.Jumlah_Barang:
            message = "Tidak dapat menambahkan BantuanPoktan karena Jumlah_Bantuan melebihi Jumlah_Barang pada Id_Banpem."
            raise Exception(message)

        super().save(*args, **kwargs)  # Simpan objek BantuanPoktan ke database

        # Ambil objek BantuanPoktan yang sudah disimpan untuk mendapatkan Id_Bantuan yang terbaru
        instance = UsulanBantuanPoktan.objects.get(Id_Bantuan=self.Id_Bantuan)

        if self.Jumlah_Bantuan > instance.Jumlah_Bantuan:
            # Pengurangan yang dilakukan hanya jika self.Jumlah_Bantuan lebih besar daripada instance.Jumlah_Bantuan
            difference = self.Jumlah_Bantuan - instance.Jumlah_Bantuan
            barang.Jumlah_Barang -= difference
            barang.save()
    else:
        super().save(*args, **kwargs)
        
        # Tambahkan logika untuk mengecualikan kelompok tani dengan status "Dapat Bantuan" dari daftar tahun berikutnya
        if self.status == "Dapat Bantuan":
            next_year = datetime.now().year + 1
            kelompok_tani = KelompokTani.objects.filter(Nama_Poktan=self.Nama_Poktan, tahun__gte=next_year)
            kelompok_tani.update(tampilkan=False)
            message = "Kelompok Tani ini Sudah Mendapatkan Bantuan di tahun sekarang."
            self.add_error(None, message)


    def __str__(self):
        return self.Id_Bantuan
       
#Barang Dari Pemerintah
class BarangDariPemerintah(models.Model):
    Id_Banpem = models.AutoField(primary_key=True)
    Nama_Barang = models.CharField(max_length=100)
    Jumlah_Barang = models.IntegerField()
    Satuan = models.CharField(max_length=100)
    Tanggal = models.DateField(blank=True)
    
    def __str__(self):
        return self.Nama_Barang
    

#Berita Pertanian 
class BeritaPertanian(models.Model):
    Id_Berita = models.AutoField(primary_key=True)
    Penulis = models.CharField(max_length=30, null=True)
    Judul_Berita = models.CharField(max_length=100)
    Foto_Berita = models.ImageField(upload_to='berita/%Y/%m/%d/', null=True, blank=True)
    Isi_Berita = models.TextField()
    Jam_Update = models.TimeField()
    Tanggal_Update = models.DateField(blank=True)

    def __str__(self):
        return self.Id_Berita