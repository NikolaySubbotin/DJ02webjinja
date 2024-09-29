from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new_view, name='new'),
    path('test/', views.test_view, name='test'),
    path('contacts/', views.contacts_view, name='contacts'),
]