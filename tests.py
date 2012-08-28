import unittest
import paydollar
from paydollar import settings


class ServerSideDirectTest(unittest.TestCase):
    def test_post(self):
        payload = {
            'orderRef': 1234,
            'amount': 10.50,
            'currCode': '840',
            'lang': 'E',
            'merchantId': '',
            'pMethod': 'VISA',
            'epMonth': 04,
            'epYear': 2015,
            'cardNo': '4111111111111111',
            'cardHolder': 'Marconi Moreto',
            'securityCode': '111',
            'payType': 'N'
        }
        result = paydollar.ss_direct(
            payload, settings.SS_DIRECT_TEST_URL, True)
        print result


if __name__ == '__main__':
    unittest.main()
