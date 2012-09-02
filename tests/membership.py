import time
import unittest

from paydollar import membership, settings


class MembershipAPITest(unittest.TestCase):
    def test_add_membership(self):
        result = membership.add_membership(
            merchant_id=settings.MERCHANT_ID,
            merchant_api_id=settings.MERCHANT_API_ID,
            merchant_api_password=settings.MERCHANT_API_PASSWORD,
            member_id=('%d' % time.time()),
            first_name='Marconi',
            last_name='Moreto',
            url=settings.MEMBERSHIP_API_TEST_URL)
        self.assertEqual(result['status_code'], '0')
        self.assertEqual(result['status_message'], 'OK')


if __name__ == '__main__':
    unittest.main()
