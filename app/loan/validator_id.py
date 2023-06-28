import requests
from requests.auth import HTTPBasicAuth

STATE_APPROVE = 'approve'

def validate_dni(dni: int) -> bool:
    is_approve = True

    auth = HTTPBasicAuth('user', 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u')

    url = f'https://api.moni.com.ar/api/v4/scoring/pre-score/{dni}'
    result = requests.get(url, auth=auth)
    
    if result.json()['status'] is not STATE_APPROVE:
        is_approve = False

    return is_approve