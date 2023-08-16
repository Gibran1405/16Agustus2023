from django.shortcuts import render, redirect
from app_sitani.models import KelompokTani, BeritaPertanian, UsulanBantuanPoktan,TokoPertanian, Profile, BarangDariPemerintah, Golongan, Jabatan
from app_sitani.forms import FormBantuanPoktan,FormProfilePegawai, FormRegister, FormKeltan, FormBerita, FormToko, FormBarangDariPemerintah, LupaSandi, FormGolongan, FormJabatan
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest,HttpResponseForbidden
from django.http import FileResponse
from django.core.exceptions import ValidationError


# Create your views here.
def dashboard (request):
    return HttpResponse('dashboard.html')
