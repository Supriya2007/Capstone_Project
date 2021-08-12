from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('home_reload', views.home_reload, name='home_reload'),
    path('filter', views.filter, name='filter'),
    path('get_data', views.get_data, name='get_data'),
    path('get_formal_struct', views.get_formal_struct, name='get_formal_struct'),
    path('get_prog_files', views.get_prog_files, name='get_prog_files'),
    path('get_selected_lib_rules', views.get_selected_lib_rules, name='get_selected_lib_rules'),
    path('start_again', views.start_again, name='start_again'),
    path('run_again', views.run_again, name='run_again'),
]
