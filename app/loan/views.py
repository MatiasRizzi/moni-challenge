from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
import requests
from requests.auth import HTTPBasicAuth

from loan.serializers import LoanSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from loan.models import Loan
from .forms import LoanForm

from django.contrib.auth.decorators import login_required

STATE_APPROVE = 'approve'

def index(request):
    return HttpResponse("Test")

@api_view(http_method_names=["post"])
def create_loan(request):

    if request.method == 'GET':
        return HttpResponseNotAllowed()
    
    #Handle POST
    serializer = LoanSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    loan = serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

#@login_required(login_url='admin_login')
def list_loan(request):
    loans = Loan.objects.all()  
    return render(request,"loan-list.html",{'loans':loans}) 

#@login_required(login_url='admin_login')
def update_loan(request, id):  
    loan = Loan.objects.get(id=id)
    form = LoanForm(initial={'name': loan.name, 'surname': loan.surname, 'gender': loan.gender, 'email': loan.email, 'requested_amount':loan.requested_amount})
    if request.method == "POST":  
        form = LoanForm(request.POST, instance=loan)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/loan-list')  
            except Exception as e: 
                pass    
    return render(request,'loan-update.html',{'form':form})  

#@login_required(login_url='admin_login')
def delete_loan(request, id):
    loan = Loan.objects.get(id=id)
    try:
        loan.delete()
    except:
        pass
    return redirect('loan-list')

@login_required(login_url='admin_login')
def admin_home(request):
    return render(request, 'admin/home.html')    