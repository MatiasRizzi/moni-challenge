from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loan-create',views.create_loan, name='loan_create'),
    path('loan-list', views.list_loan, name='loan_list'),
    path('loan-update/<int:id>', views.update_loan, name='loan_update'),
    path('loan-delete/<int:id>', views.delete_loan, name='loan_delete'),
]