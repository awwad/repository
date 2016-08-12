#!/usr/bin/env python

import random
import requests
import sys

from six.moves import xrange

def get(number_of_ecus):
    nonces = random.sample(xrange(sys.maxint), number_of_ecus)
    print nonces
    request = requests.post('https://uptane.umtri.umich.edu:24515/timeserver/', json=nonces)
    print "Request URL: " + request.url + "  \n"
    print "Request Text: " + request.text + " \n"
    assert request.status_code==200
    response = request.json()
    print response 
    # TODO: Check signatures.
    assert len(response)==number_of_ecus
    # Check all current times are equal: http://stackoverflow.com/a/3844948
    current_times = [v['signed']['current-time'] for v in response.values()]
    current_time = current_times[0]
    assert current_times.count(current_time)==len(current_times)
    print('The latest downloaded time is {}'.format(current_time))

if __name__ == '__main__':
    get(3)
