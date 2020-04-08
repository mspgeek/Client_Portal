from __future__ import unicode_literals

import unittest

from templatetags.phonenumber_filter import (
    phonenumber, phonenumber_international, phonenumber_e164)


class PhoneNumberFilterTestCase(unittest.TestCase):
    def test_bad_phonenumber(self):
        self.assertEqual('123', phonenumber('123'))
        self.assertEqual('', phonenumber(''))
        self.assertEqual('abc', phonenumber('abc'))
        self.assertEqual('222125551212', phonenumber('222125551212'))

    def test_phonenumber(self):
        self.assertEqual('(212) 867-5309', phonenumber('2128675309'))
        self.assertEqual('(212) 867-5309', phonenumber('12128675309'))

    def test_phonenumber_international(self):
        self.assertEqual('+1 212-867-5309', 
                         phonenumber_international('2128675309'))
        self.assertEqual('+1 212-867-5309', 
                         phonenumber_international('12128675309'))

    def test_phonenumber_e164(self):
        self.assertEqual('+12128675309', phonenumber_e164('2128675309'))
        self.assertEqual('+12128675309', phonenumber_e164('12128675309'))

