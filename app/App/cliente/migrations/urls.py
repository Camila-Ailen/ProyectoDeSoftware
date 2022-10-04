from django.urls import path
from App.views import mysecondview

from .views import myfirstview

from . import views

app_name = 'cliente'

urlpatterns = [
    path('uno/', myfirstview, name='vista1'),
    path('dos/', mysecondview, name='vista2'),

]


