from django.contrib import admin
from django.urls import path, include

from addjobs import views

app_name = 'addjobs'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('addjob/', views.addjob, name='addjob'),
    path('signup/', views.signup, name='signup'),
    path('jobview/', views.jobview, name='jobview'),

]