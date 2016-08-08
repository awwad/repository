#!/usr/bin/env python

import requests

VIN = '1M8GDM9A_KP042788'
PRIMARY_SERIAL_NUMBER = 'VWZ7Z0F7185451'
FULL_SECONDARY_SERIAL_NUMBER = 'VWZ7Z0F7185452'
PARTIAL_SECONDARY_SERIAL_NUMBER = 'VWZ7Z0F7185453'

def get_ecu_version_manifest(serial_number, previous_time, current_time,
                             current_bootloader, current_image,
                             freeze_attack_detected=False):
    assert isinstance(current_bootloader, dict)
    assert 'unencrypted-file-path' in current_bootloader
    assert 'unencrypted-file-hashes' in current_bootloader

    assert isinstance(current_image, dict)
    assert 'unencrypted-file-path' in current_image
    assert 'unencrypted-file-hashes' in current_image

    signed = {
        'serial-number': serial_number,
        'previous-time': previous_time,
        'current-time': current_time,
        'freeze-attack-detected': freeze_attack_detected,
        'current-bootloader': current_bootloader,
        'current-image': current_image
    }
    # TODO: Attach signatures.
    signatures = [{
        'keyid': None,
        'method': 'ed25519',
        'signature': None
    }]
    ecu_version_manifest = {
        serial_number : {
            'signatures': signatures,
            'signed': signed
        }
    }

    return ecu_version_manifest

def post():
    previous_time = 1466654400
    current_time = 1466930108

    current_bootloader = {
        'unencrypted-file-path': '2f3caffd6aeec967a7d71eb7abec0993d036430691e66'
                                 '8a8710248df4541111e.ldr',
        'unencrypted-file-hashes': {
            'sha256': '2f3caffd6aeec967a7d71eb7abec0993d036430691e668a8710248df'
                      '4541111e'
        }
    }

    current_image = {
        'unencrypted-file-path': '20e24ade0e9aa41d7ee9d094bb2e31ac12115ad7b9fd6'
                                 '6a9692ebb07dfaa9512.img',
        'unencrypted-file-hashes': {
            'sha256': '20e24ade0e9aa41d7ee9d094bb2e31ac12115ad7b9fd66a9692ebb07'
                      'dfaa9512'
        }
    }

    installed = {
        PRIMARY_SERIAL_NUMBER: get_ecu_version_manifest(PRIMARY_SERIAL_NUMBER,
                                                        previous_time,
                                                        current_time,
                                                        current_bootloader,
                                                        current_image)
    }

    signed = {
        '_type': 'Vehicle',
        'VIN': VIN,
        'primary-serial-number': PRIMARY_SERIAL_NUMBER,
        'installed' : installed
    }
    # TODO: Attach signatures.
    signatures = [{
        'keyid': None,
        'method': 'ed25519',
        'signature': None
    }]
    vehicle_version_manifest = {
        'signatures': signatures,
        'signed': signed
    }

    request = requests.post('http://127.0.0.1:8000/director/',
                            json=vehicle_version_manifest)
    assert request.status_code==200

if __name__ == '__main__':
    post()
