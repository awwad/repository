from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import json
import time

@csrf_exempt
def index(request):
    assert request.method == 'POST'
    vehicle_version_manifest = json.loads(request.body)

    # Sanity-check manifest.
    # TODO: check signatures based on VIN and primary serial number.
    signatures = vehicle_version_manifest['signatures']
    signed = vehicle_version_manifest['signed']
    VIN = signed['VIN']
    # TODO: Lookup vehicle in DB based on its VIN. If fail, return 403.
    installed = signed['installed']
    # TODO: Assert that every ECU known in DB is in @installed.
    # TODO: Lookup public key of every ECU.
    # TODO: Check signature of every ECU version manifest.

    director_metadata = {}

    # TODO: Dependency resolution.
    targets = {}

    # Send back what to install.
    director_metadata['signed'] = {
        '_type': 'Director',
        'VIN': VIN,
        'version': int(round(time.time())),
        # TODO: Expiration timestamp.
        'expires': None,
        'targets': targets
    }

    # TODO: Attach director's signatures.
    director_metadata['signatures'] = [{
        'keyid': None,
        'method': 'ed25519',
        'signature': None
    }]

    # TODO: Actually, return the timestamp metadata, which points to the
    # release metadata, which points to the director metadata specific to this
    # vehicle and request.
    return JsonResponse(director_metadata)
