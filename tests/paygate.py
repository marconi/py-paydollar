import time
import unittest

from paydollar import paygate, settings, logger


class ServerSideDirectTest(unittest.TestCase):
    def _generate_payload(self):
        return {
            'orderRef': ('%d' % time.time()),
            'amount': ('%.2f' % 10.50),
            'currCode': '840',
            'lang': 'E',
            'merchantId': settings.MERCHANT_ID,
            'pMethod': 'VISA',
            'epMonth': settings.VISA_EXPIRY_MONTH,
            'epYear': settings.VISA_EXPIRY_YEAR,
            'cardNo': settings.VISA_CARDNO,
            'cardHolder': 'Marconi Moreto',
            'securityCode': settings.VISA_CVV,
            'payType': 'N'
        }

    def test_post_secure(self):
        result = paygate.ss_direct(self._generate_payload(),
                                   settings.PAYGATE_SS_DIRECT_TEST_URL, True)
        logger.debug(result)
        self.assertEqual(result['successcode'], '0')


if __name__ == '__main__':
    unittest.main()
