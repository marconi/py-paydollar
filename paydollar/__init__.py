import logging
import hashlib


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('paydollar')


def generate_secure_hash(merchant_id, ref_num, curr, amount, pay_type,
    hash_secret):
    """
    Helper for generating secure hash.
    """
    param_list = [
        merchant_id,
        ref_num,
        curr,
        amount,
        pay_type,
        hash_secret
    ]
    logger.info('generating secure hash using: %s' % str(param_list))
    param_str = '|'.join(param_list)
    logger.debug(param_str)
    secure_hash = hashlib.sha1(param_str).hexdigest()
    logger.debug('secure hash: %s' % secure_hash)
    return secure_hash


def verify_secure_hash(src, prc, success_code, ref_num, pay_ref, curr, amount,
    payer_auth_stat, hash_secret, secure_hash):
    """
    Helper for verifying secure hash, should be called from datafeed.
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
        hash_secret
    ])
    return hashlib.sha1(param_str).hexdigest() == secure_hash


def flatten_response(response):
    """
    Convert single itemed-list to just the value itself.
    ie. 'Cur': [u'840'] => 'Cur': u'840'
    """
    for key, val in response.items():
        if isinstance(val, list) and len(val) == 1:
            response[key] = val[0]
    return response
