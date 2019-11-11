from django.urls import path
from .views import RegisterView, validate, index


urlpatterns = [
    path('validate/<codigo_participante>', validate, name='validate-attendance'),
    path('', RegisterView.as_view(), name='index'),
    path('test/', index, name='test'),
]
