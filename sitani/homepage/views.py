from django.shortcuts import render, redirect
from app_tani.models import KelompokTani 
from app_tani.models import Profile
from app_tani.models import TokoPertanian
from app_tani.models import UsulanBantuanPoktan
from app_tani.models import BeritaPertanian
from app_tani.forms import FormBantuanPoktan
from app_tani.forms import FormKeltan
from app_tani.forms import FormBerita
from app_tani.forms import FormToko
from app_tani.forms import FormProfilePegawai
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect

# Create your views here

def toko (request):
    return HttpResponse('services.html')
def pegawai (request):
    return HttpResponse('coach.html')
def contact (request):
    return HttpResponse('contact.html')
def blog (request):
    return HttpResponse('blog.html')
def berita (request):
    return HttpResponse('blog-single.html')