from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
import requests
from requests.auth import HTTPBasicAuth

from loan.models import Loan

STATE_APPROVE = 'approve'

def index(request):
    return HttpResponse("Test")

def controller(request):
    '''
    intermediate endpoint. Response json with aprove or disallow loan
    '''
    auth = HTTPBasicAuth('user', 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u')
    #TODO manage variable dni and add it the end to url
    dni = 30156149

    url = f'https://api.moni.com.ar/api/v4/scoring/pre-score/{dni}'
    result = requests.get(url, auth=auth)

    response = {'state':result.json()['status']}
    return JsonResponse(result)