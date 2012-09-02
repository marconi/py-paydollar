"""
PayGate APIs
"""

import requests
import urllib
import urlparse

from . import settings, logger, generate_secure_hash, flatten_response


def ss_direct(params, url=settings.PAYGATE_SS_DIRECT_PROD_URL, secure=False):
    """
    API for Server Side Direct Connection.

    Parameters:
    url: PayDollar post url
    params: dictionary of parameters to be posted to PayDollar
    secure: Boolean, wether or not we should generate secure hash
    """

    if secure:
        params['secureHash'] = generate_secure_hash(
            params['merchantId'],
            params['orderRef'],
            params['currCode'],
            params['amount'],
            params['payType'],
            settings.SECURE_HASH_SECRET)

    params = urllib.urlencode(params)
    logger.info('posting to paydollar...')
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=params, headers=headers, verify=True)
    return flatten_response(urlparse.parse_qs(response.text))
