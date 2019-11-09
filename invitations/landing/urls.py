from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.index, name='index'),
    path('validate/<codigo_participante>', views.validate, name='validate-attendance'),
]