from django.shortcuts import render
from django.http import JsonResponse

import time

# Create your views here.
def index(request):
    nonces = request.GET.getlist('nonce')

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
