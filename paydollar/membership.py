"""
Membership APIs
"""

import requests
import urllib
from lxml import etree

from . import settings, logger


def query_membership():
    pass


def add_membership(merchant_id, merchant_api_id, merchant_api_password,
    member_id, first_name, last_name, url=settings.MEMBERSHIP_API_PROD_URL):
    """
    API for adding membership.
    """
    params = {
        'merchantId': merchant_id,
        'merchantApiId': merchant_api_id,
        'password': merchant_api_password,
        'actionType': 'Add',
        'memberId': member_id,
        'firstName': first_name,
        'lastName': last_name,
        'status': 'A'
    }
    params = urllib.urlencode(params)
    logger.info('adding membership...')
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=params, headers=headers, verify=True)
    dom = etree.fromstring(response.text)

    status_code = dom.find('.//responsecode').text
    status_message = dom.find('.//responsemessage').text
    result = {'status_code': status_code,
              'status_message': status_message}
    if status_message == 'OK':
        result['static_token'] = dom.find('.//statictoken').text
    return result


def update_membership():
    pass


def delete_membership():
    pass


def verify_membership():
    pass
