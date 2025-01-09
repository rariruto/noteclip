from django.urls import path, re_path
from . import views
from . import csv_set

app_name = 'noteclipper'

urlpatterns = [
    #path('home/', views.MainView.as_view(), name='home'),
    path('', views.LoginView.as_view(), name='login'),
    path('new/', views.NewAccountView.as_view(), name='new'),
    path('home', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.MainView.as_view(), name='main'),
    path('up/<int:pk>', views.MainUpView.as_view(), name='main_up'),
    path('bottom/<int:pk>', views.MainBottomView.as_view(), name='main_bottom'),
    path('clip/', csv_set.csv_process.load_csv, name='clip'),
    #path('//', views.ClipView.as_view(), name='clip'),
    path('activate/', views.ActivateView.as_view(), name='activate'),
    path('update/', views.update, name='update'),
    #path('activate/<int:pk>', views.ActivateView.as_view(), name='activate'),
    path('setting/', views.SettingView.as_view(), name='setting'),
    path('information', views.InformationView.as_view(), name='information'),
    path('change_name', views.ChangeNameView.as_view(), name='chango_u'),
    path('change_passwd', views.ChangePasswdView.as_view(), name='change_p'),
]

handler404 = views.error_404page
