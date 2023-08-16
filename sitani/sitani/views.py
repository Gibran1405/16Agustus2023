from django.shortcuts import render, redirect
from app_sitani.models import KelompokTani 
from app_sitani.models import Profile
from app_sitani.models import TokoPertanian
from app_sitani.models import UsulanBantuanPoktan
from app_sitani.models import BeritaPertanian
from app_sitani.forms import FormBantuanPoktan
from app_sitani.forms import FormKeltan
from app_sitani.forms import FormBerita
from app_sitani.forms import FormToko
from app_sitani.forms import FormProfilePegawai
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
def home (request):
    return HttpResponse('index.html')
def login (request):
   return HttpResponse('login.html')


