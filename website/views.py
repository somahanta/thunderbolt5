from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


# Create your views here.
class MainView(TemplateView):
    template_name = "website/main.html"
class TeamView(TemplateView):
    template_name = "website/team.html"

class GalleryView(TemplateView):
    template_name = "website/gallery.html"
class SponsView(TemplateView):
    template_name = "website/sponsors.html"
class ContactView(TemplateView):
    template_name = "website/contact.html"
