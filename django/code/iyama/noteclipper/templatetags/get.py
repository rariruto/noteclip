from django import template
from django.shortcuts import render
from django.views import generic
from django.db import models, connection
import glob
#from .forms import ImageForm
register = template.Library()

@register.filter(name="get_note")
def get_note():
    files = glob.glob("static/noteclipper/reference/org_img/*")
    for file in files:
        models.Notes.objects.create(title=file)
    print(OK)
    return render("noteclipper:main")
