from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from . import views

app_name = 'api_services'

urlpatterns = [
    path('one-random-line/', views.get_one_line, name='one_random_line'),
    path('one-random-line-backwards/', views.one_random_line_backwards, name='one_random_line_backwards'),
    path('hundreds-longest-lines/', views.hundreds_longest_line, name='hundreds_longest_lines'),
    path('twenty-longest-lines/', views.twenty_longest_line_of_last_file, name='twenty_longest_lines'),
]

drf_spectacular_urls = [
    path('api/schema/', SpectacularAPIView.as_view(urlconf=urlpatterns), name='api_schema'),
    path('api/docs/swagger-ui/', SpectacularSwaggerView.as_view(url_name='api_services:api_schema'), name='api_sa'),
    path('api/docs/', SpectacularRedocView.as_view(url_name='api_services:api_schema'), name='api_'),
]

urlpatterns += drf_spectacular_urls
