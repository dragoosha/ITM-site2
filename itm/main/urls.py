from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path("impressum/", impressum, name='impressum'),
    path("privacy/", privacy, name='privacy'),
]