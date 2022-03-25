
from django.urls import path
from . import views

app_name = 'inputform'
urlpatterns = [
    path('client/',views.client, name='client'),
    path('client/complete/', views.complete, name='complete'),
]
