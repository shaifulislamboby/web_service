from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'file_upload'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('file-upload/', views.file_upload_via_model_form, name='file-upload'),
]
