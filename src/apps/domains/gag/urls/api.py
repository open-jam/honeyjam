from django.urls import path

from apps.domains.gag.views import api as views

app_name = 'apps.domains.gag'
urlpatterns = [
    path('add/', views.GagAddView.as_view(), name='gag_add'),
    path('<int:gag_id>/', views.GagView.as_view(), name='gag'),
]
