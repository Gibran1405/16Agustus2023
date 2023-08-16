"""sitani URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_sitani.views import *
from django.contrib.auth.views import LogoutView
from app_sitani import views
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import *


urlpatterns = [
#login admin django
    path('admin/', admin.site.urls),
#homepage
    path('',views.home , name='home'),
    path('home/',views.home , name = 'home'),
    path('blog/', views.blog , name ='blog'),
    path('blogsingle/<int:Id_Berita>/', blog_single, name='blogsingle'),
    path('struktur/',views.struktur, name ='struktur'),
    path('toko/', views.toko , name ='toko'),
    path('perban/', perban, name='perban'),
#dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
#login dan logout serta register
    path('login/',login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('lupasandi/', lupasandi, name='lupasandi'),
#kelola kelompok tani
    path('keltan/', keltan, name='keltan'),
    path('tambah_keltan/', tambah_keltan, name='tambah_keltan'),
    path('keltan/ubah/<str:Nama_Poktan>/', ubah_keltan, name='ubah_keltan'),
    path('keltan/hapus/<str:Nama_Poktan>/',hapus_keltan, name='hapus_keltan'),
#kelola data pegawai
    path('datapegawai/', datapegawai, name='datapegawai'),
    path('tambah_datapegawai/', tambah_datapegawai, name='tambah_datapegawai'),
    path('datapegawai/ubah/<str:Nama>/', ubah_datapegawai, name='ubah_datapegawai'),
    path('datapegawai/hapus/<str:Nama>/',hapus_datapegawai, name='hapus_datapegawai'),
#kelola toko pertanian
    path('tokopertanian/', tokopertanian, name='tokopertanian'),
    path('tambah_tokopertanian/', tambah_tokopertanian, name='tambah_tokopertanian'),
    path('tokopertanian/ubah/<str:Nama_Toko>/', ubah_tokopertanian, name='ubah_tokopertanian'),
    path('tokopertanian/hapus/<str:Nama_Toko>/', hapus_tokopertanian, name='hapus_tokopertanian'),
#kelola bantuan
    path('bantuan/', bantuan, name='bantuan'),
    path('tambah_bantuan/', tambah_bantuan, name='tambah_bantuan'),
    path('bantuan/ubah/<int:Id_Bantuan>/', ubah_bantuan, name='ubah_bantuan'),
    path('bantuan/hapus/<int:Id_Bantuan>/', hapus_bantuan, name='hapus_bantuan'),
#kelola bantuan dari pemerintah
    path('banpemtan/', banpemtan, name='banpemtan'),
    path('tambah_banpemtan/', tambah_banpemtan, name='tambah_banpemtan'),
    path('banpemtan/ubah/<str:Nama_Barang>/', ubah_banpemtan, name='ubah_banpemtan'),
    path('banpemtan/hapus/<str:Nama_Barang>/', hapus_banpemtan, name='hapus_banpemtan'),
#kelola berita
    path('beritapertanian/', beritapertanian, name='beritapertanian'),
    path('tambah_berita/', tambah_berita, name='tambah_berita'),
    path('beritapertanian/ubah/<str:Judul_Berita>/', ubah_berita, name='ubah_berita'),
    path('beritapertanian/hapus/<str:Judul_Berita>/', hapus_berita, name='hapus_berita'),
#kelola Golongan
    path('golongan/', golongan, name='golongan'),
    path('tambah_golongan/', tambah_golongan, name='tambah_golongan'),
    path('golongan/ubah/<int:Id_Golongan>/', ubah_golongan, name='ubah_golongan'),
    path('golongan/hapus/<int:Id_Golongan>/',hapus_golongan, name='hapus_golongan'),
#kelola Jabatan
    path('jabatan/', jabatan, name='jabatan'), 
    path('tambah_jabatan/', tambah_jabatan, name='tambah_jabatan'),
    path('jabatan/ubah/<str:Nama_Jabatan>/', ubah_jabatan, name='ubah_jabatan'),
    path('jabatan/hapus/<str:Nama_Jabatan>/',hapus_jabatan, name='hapus_jabatan'),
#kelola pdf
    path('bantuan_excel/',usulanbantuan_excel, name='bantuan_excel'),
    path('Status_bantuan_pdf/',statusbantuan_pdf, name='bantuan_pdf'),
    path('bantuanpemerintah_pdf/', bantuanpemerintah_pdf, name='bantuanpemerintah_pdf'),
#kelola User
    path('user/', user, name='user'),
    path('tambah_user/', tambah_user, name='tambah_user'),
#   path('user/ubah/<int:id>/', ubah_user, name='ubah_user'),
    path('user/hapus/<int:id>/', hapus_user, name='hapus_user'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

