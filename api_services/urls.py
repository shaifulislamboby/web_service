from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = 'api_services'

urlpatterns = [
    path('one-random-line/', views.get_one_line, name='one_random_line'),
    path('one-random-line-backwards/', views.one_random_line_backwards, name='one_random_line_backwards'),
    path('hundreds-longest-lines/', views.hundreds_longest_line, name='hundreds_longest_lines'),
    path('twenty-longest-lines/', views.twenty_longest_line_of_last_file, name='twenty_longest_lines'),
]
