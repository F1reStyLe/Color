from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *


class ProductionList(ListView):
    model = Product
    template_name = 'index.html'
