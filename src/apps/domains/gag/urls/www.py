from django.urls import path

from apps.domains.gag.views import www as views

app_name = 'apps.domains.gag'
urlpatterns = [
    path('', views.GagListView.as_view(), name='gag_list'),
]
