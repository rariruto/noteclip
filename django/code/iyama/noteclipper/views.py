from django.shortcuts import render, redirect
from django.views import generic
from django.http import Http404
from .models import User, Note,Class
import glob
import re
#from .forms import ImageForm

# Create your views here
class HomeView(generic.ListView):
    model = Note
    check = True
    template_name = 'noteclipper/home.html'
    all_data = Note.objects.all()
    title_c = "aaa"
    files = glob.glob("static/noteclipper/reference/org_img/*")
    print(files)

    for file in files:
        title_c = (re.findall('org_img/.*.jpg',file))[0]
        for check in all_data:
            if title_c==check.title:
                check=False
        if check==True:
            test = Note(title=title_c, done='1')
            test.save()

class LoginView(generic.ListView):
    model = User
    template_name = 'noteclipper/login.html'

class NewAccountView(generic.ListView):
    model = User
    template_name = 'noteclipper/new.html'
    fields = '__all__'

class MainView(generic.DetailView):
    model = Note
    template_name = 'noteclipper/main.html'

    def get_context_data(self, **kwargs):
        bmp_a = []
        bmp_b = glob.glob('static/noteclipper/reference/cut_img/*/*/*')

        for i in bmp_b:
            bmp_a.append((re.search(('/\w*/\w*/\w*.bmp'), i))[0])


        context = super(MainView, self).get_context_data(**kwargs)
        context.update({'object_list2':Class.objects.all(),})
        context.update({'object_list3':bmp_a})
        return context

    def get_queryset(self):
        return Note.objects.all()

#class ClipView(generic.DetailView):
#    model = Note
#    template_name = 'noteclipper/clip.html'

#    def get_context_data(self, **kwargs):
#        bmp_a = []
#        bmp_b = glob.glob('static/noteclipper/reference/cut_img/*/*/*')

#        for i in bmp_b:
#            bmp_a.append((re.search(('/\w*/\w*/\w*.bmp'), i))[0])


#        context = super(ClipView, self).get_context_data(**kwargs)
#        context.update({'object_list2':Class.objects.all(),})
#        context.update({'object_list3':bmp_a})
#        return context

#    def get_queryset(self):
#        return Note.objects.all()

class ActivateView(generic.ListView):
    model = Class
    template_name = 'noteclipper/activate.html'
    field='__all__'

    http_method_names = ['get', 'post']

#class ActivateView(generic.edit.UpdateView):
#    model = Class
#    template_name = 'noteclipper/activate.html'
#    fields = '__all__'
    
class SettingView(generic.ListView):
    model = Note
    template_name = 'noteclipper/setting.html'

class InformationView(generic.ListView):
    model = User
    template_name = 'noteclipper/information.html'

class ChangeNameView(generic.ListView):
    model = User
    template_name = 'noteclipper/change_u.html'

class ChangePasswdView(generic.ListView):
    model = User
    template_name = 'noteclipper/change_p.html'

def error_404page(request, exception):
    raise render(request, 'noteclipper/404.html', status=404)

def list_func(request):
    object_list = Note.objects.all()
    context = {'object_list': object_list}
    return render(request, 'noteclipper/main.html', context) 


def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'noteclipper/main.html', context)

def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            post = form.save(commit==False)
            post.image = request.FILES['image']
            post.save()
            return redirect('noteclipper:main')

def update(request):
    class_type = Class.objects.all()

    if request.method == 'POST':
        selecteds = request.POST.getlist('class[]')

        for data in class_type:
            article = Class.objects.get(name=data.name)
            article.activate = False
            article.save()
      
        for value in selecteds:
            article = Class.objects.get(name=value)
            article.activate = True 
            article.save()
            
        return redirect('noteclipper:activate')

    return render(request, "noteclipper/activate.html")