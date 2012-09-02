import os

# paygate urls
PAYGATE_SS_DIRECT_TEST_URL = 'https://test.paydollar.com/b2cDemo/eng/directPay/payComp.jsp'
PAYGATE_SS_DIRECT_PROD_URL = 'https://www.paydollar.com/b2c2/eng/directPay/payComp.jsp'

# membership urls
MEMBERSHIP_SS_DIRECT_TEST_URL = PAYGATE_SS_DIRECT_TEST_URL
MEMBERSHIP_SS_DIRECT_PROD_URL = PAYGATE_SS_DIRECT_PROD_URL
MEMBERSHIP_API_TEST_URL = 'https://test.paydollar.com/b2cDemo/merchant/api/MembershipApi.jsp'
MEMBERSHIP_API_PROD_URL = 'https://www.paydollar.com/b2c2/eng/merchant/api/MembershipApi.jsp'

# memberpay urls
MEMBERPAY_API_TEST_URL = 'https://test.paydollar.com/b2cDemo/eng/merchant/api/MemberPayApi.jsp'
MEMBERPAY_API_PROD_URL = 'https://www.paydollar.com/b2c2/eng/merchant/api/MemberPayApi.jsp'

# production credentials
MERCHANT_ID = ''
MERCHANT_API_ID = ''
MERCHANT_API_PASSWORD = ''
SECURE_HASH_SECRET = ''

# testing credentials
VISA_CARDNO = ''
VISA_EXPIRY_MONTH = ''
VISA_EXPIRY_YEAR = ''
VISA_CVV = ''

_locals = locals()

# pickup overrides from environment
for key in _locals.keys():
    if key.isupper():
        value = os.environ.get(key, None)
        if value:
            _locals[key] = value
