from django.http import JsonResponse, HttpResponse

from director.models import ECU

import json
import time

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


def Enroll(request):
    #todo: Check if exists? 
    print request.GET['serial']
    return HttpResponse("Enroll? I don't think so, Tim.") #Satisfy the request to calm down the ajax request
    ## VALIDATE ME -- this breaks. What's the ID? Gotta look up the latest? 
    newecu = ECU(serial_number=request.GET['serial'], public_key=request.GET['key']) 
    newecu.save()
    return 0 # because we messed up.

def List(request):
    all_entries = ECU.objects.all()
    returnstr = "<br />Found " + str(all_entries.count()) + " records."  
    returnstr += "<table class=\"fancytable\">" 
    returnstr += "<tr><td>Serial</td><td>Pub Key</td><td>Crypto</td><td>is Primary?</td></tr>"
    for x in range(0, all_entries.count()):
        returnstr += "<tr>"
        returnstr += "<td>" + str(all_entries[x].serial_number) + "</td>" 
        returnstr += "<td>" + str(all_entries[x].public_key) + "</td> "
        returnstr += "<td>" +  "</td>" 
        returnstr += "<td>" + str(all_entries[x].primary) + "</td>" 
        returnstr += "</tr>"

    returnstr += "</table>"
    return HttpResponse(returnstr) 
