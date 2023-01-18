from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('search_map/',views.search_map,name='search_map'),
    path('bung_list/',views.create_bung,name='bung_list'),
]

