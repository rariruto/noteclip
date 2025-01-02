from django.db import models
from .models import User, Note,Class,Clip
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import generic
from django.http import Http404
import glob
import re
import csv
import pprint

class csv_process:
    def load_csv(request):
        note_data = Note.objects.all()

        for data in note_data:
            title = data.title[8:-4]
            print(title)
            with open("static/noteclipper/reference/cut_data/" + title + ".csv") as f:
                c_data = (re.findall('.+,.*,.*,.*,.*,.*,.*' ,f.read()))
                for check in c_data:
                    if check.find(title)>=0:
                        data_div = check.split(',')
                        print(data_div)
                        print(check)
                    
                        if float(data_div[4]) > 1500:
                            result = Clip(file= data_div[1] + "/" + data_div[0] + ".bmp", note=title, class_type=data_div[1], pos="0" )
                        else:
                            result = Clip(file= data_div[1] + "/" + data_div[0] + ".bmp", note=title, class_type=data_div[1], pos="1" )
                        result.save()

                        print(c_data)

        return redirect('noteclipper:home')