import requests
from requests.auth import HTTPBasicAuth

STATE_APPROVE = 'approve'

def validate_dni(dni: int) -> bool:
    auth = HTTPBasicAuth('user', 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u')

    url = f'https://api.moni.com.ar/api/v4/scoring/pre-score/{dni}'
    result = requests.get(url, auth=auth)

    #TODO manage exceptions Key Value
    is_approve = result.json()['status'] == STATE_APPROVE

    return is_approve