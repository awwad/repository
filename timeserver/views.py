from django.http import JsonResponse

import json
import time

def index(request):
    # NO, both posts and gets work. 
    #assert request.method == 'GET'
    nonces = json.loads(request.body)
    print nonces
    print json.loads(request.body)
    assert isinstance(nonces, list)

    response = {}
    current_time = int(round(time.time()))

    for nonce in nonces:
        response[nonce] = {
            "signatures": [{
                "keyid": None,
                "method": "ed25519",
                "signature": None
            }],
            "signed": {
                "nonce": nonce,
                "current-time": current_time
            }
        }

    return JsonResponse(response)
