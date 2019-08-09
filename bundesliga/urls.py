from django.urls import path
from .views import bundeslig_detail

urlpatterns  = [
    path('', bundeslig_detail, name='bundeslig')
]