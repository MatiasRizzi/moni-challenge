from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get', views.controller, name='proxy'),
    path('loan-create',views.create_loan, name='create_loan')
]