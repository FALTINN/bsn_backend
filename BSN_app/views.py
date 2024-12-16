from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import json


class MainView(TemplateView):
  template_name = "main.html"

class CatalogView(TemplateView):
  template_name = "catalog.html"
  
class StoreView(TemplateView):
  template_name = "store.html"