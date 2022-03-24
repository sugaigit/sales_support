
from django.urls import path
from . import views

app_name = 'inputform'
urlpatterns = [
    path('', views.index, name='index'),
    path('input_form/',views.input_form, name='input_form'),
    path('input_form/input/complete/', views.complete, name='complete'),
]
