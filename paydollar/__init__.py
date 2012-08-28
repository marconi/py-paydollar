import hashlib
import logging
import requests
import urllib
from paydollar import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('paydollar')


def ss_direct(params, url=settings.SS_DIRECT_PROD_URL, secure=False):
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
            params['payType'])

    logger.info('posting to PayDollar...')
    response = requests.post(url, data=params)
    logger.debug(response.status_code)
    logger.debug(response.url)
    logger.debug(response.text)
    return urllib.parse.parse_qs(response.text)


def ss_data_feed(url_params):
    """
    API for processing data feed, meant to be called inside a url handler.

    Parameters:
    url_params: posted url coming from PayDollar
    """
    logger.info('processing data feed...')
    decoded = urllib.parse.parse_qs(url_params)
    logger.debug(decoded)


def generate_secure_hash(merchant_id, ref_num, curr, amount, pay_type):
    """
    Helper for generating secure hash.
    """
    logger.info('generating secure hash...')
    param_str = '|'.join([
        merchant_id,
        ref_num,
        curr,
        amount, pay_type,
        settings.SECURE_HASH_SECRET
    ])
    logger.debug(param_str)
    secure_hash = hashlib.sha1(param_str).hexdigest()
    logger.debug('secure hash: %s' % secure_hash)
    return secure_hash


def verify_secure_hash(src, prc, success_code, ref_num, pay_ref, curr, amount,
    payer_auth_stat, paydollar_secure_hash):
    """
    Helper for verifying secure hash.
    """
    param_str = '|'.join([
        src,
        prc,
        success_code,
        ref_num,
        pay_ref,
        curr,
        amount,
        payer_auth_stat,
        settings.SECURE_HASH_SECRET
    ])
    return hashlib.sha1(param_str).hexdigest() == paydollar_secure_hash
