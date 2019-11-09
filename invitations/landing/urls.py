from django.urls import path
from .views import RegisterView, validate, finish


urlpatterns = [
    path('', RegisterView.as_view(), name='index'),
    path('validate/<codigo_participante>/', validate, name='validate-attendance'),
    path('finish/<codigo>/', finish, name="finish"),
]