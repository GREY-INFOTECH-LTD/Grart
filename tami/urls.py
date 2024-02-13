from django.urls import path
from . import views

urlpatterns = [
    path('', views.tami, name='tami'),
    path('<artwork_id>', views.artwork_detail, name='artwork_detail'),
    path('add_tami/', views.add_tami, name='add_tami')
    ]
    