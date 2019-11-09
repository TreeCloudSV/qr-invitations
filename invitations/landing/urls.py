from django.urls import path
from .views import RegisterView


urlpatterns = [
    path('', views.index, name='index'),
    path('validate/<codigo_participante>', views.validate, name='validate-attendance'),
    path('', RegisterView.as_view(), name='index'),
]