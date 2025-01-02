from django.db import models
#from models import User, Note,Class
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import generic
from django.http import Http404
import glob
import re
import csv
import pprint

def load_csv():
    with open("static/noteclipper/reference/cut_data/SKM_C360i23092810090_0102.csv") as f:
        print(f.read())