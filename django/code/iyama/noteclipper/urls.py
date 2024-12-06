from django.urls import path, re_path
from . import views

app_name = 'noteclipper'

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('new/', views.NewAccountView.as_view(), name='new'),
    path('<int:pk>/', views.ClipView.as_view(), name='clip'),
    path('activate_home/', views.ActivateHomeView.as_view(), name='activate_home'),
    path('activate/<int:pk>', views.ActivateView.as_view(), name='activate'),
    path('setting/', views.SettingView.as_view(), name='setting'),
    path('information', views.InformationView.as_view(), name='information'),
    path('change_name', views.ChangeNameView.as_view(), name='chango_u'),
    path('change_passwd', views.ChangePasswdView.as_view(), name='change_p'),

]

handler404 = views.error_404page
