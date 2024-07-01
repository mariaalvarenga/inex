from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.contrib import admin
from .models import Servicos

admin.site.register(Servicos)
