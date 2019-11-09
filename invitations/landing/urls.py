from django.urls import path
from .views import RegisterView, validate, index


urlpatterns = [
    path('', index, name='index'),
    path('validate/<codigo_participante>', validate, name='validate-attendance'),
    path('', RegisterView.as_view(), name='index'),
]