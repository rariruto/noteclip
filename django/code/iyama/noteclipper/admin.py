from django.contrib import admin
from .models import Class, User, Note, Clip

# Register your models here.
admin.site.register(Class)
admin.site.register(User)
admin.site.register(Note)
admin.site.register(Clip)
