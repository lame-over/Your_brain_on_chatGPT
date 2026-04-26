from django.urls import path, re_path
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    path('', views.questions, name='questions'),
]