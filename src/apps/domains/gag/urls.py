from django.urls import path

from apps.domains.gag import views

app_name = 'apps.domains.gag'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
