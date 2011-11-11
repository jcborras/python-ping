#!/usr/bin/env python
# coding: utf-8

from socket import gaierror
from ping import dest_address, is_valid_ip4_address
from unittest import TestCase, main

class Ip4Addr(TestCase):
    def testPositives(self):
        self.assertTrue(is_valid_ip4_address('0.0.0.0'))
        self.assertTrue(is_valid_ip4_address('1.2.3.4'))
        self.assertTrue(is_valid_ip4_address('12.34.56.78'))
        self.assertTrue(is_valid_ip4_address('255.255.255.255'))

    def testNegatives(self):
        self.assertFalse(is_valid_ip4_address('0.0.0.0.0'))
        self.assertFalse(is_valid_ip4_address('1.2.3'))
        self.assertFalse(is_valid_ip4_address('a2.34.56.78'))
        self.assertFalse(is_valid_ip4_address('255.255.255.256'))


class DestAddr(TestCase):
    def test1(self):
        self.assertTrue(is_valid_ip4_address(dest_address('www.github.com')))
        self.assertRaises(gaierror, dest_address, ('asafsfas.asfasdf.asdf'))

    def test2(self):
        self.assertTrue(dest_address('10.10.10.1'))
        self.assertTrue(dest_address('10.10.010.01'))
        self.assertTrue(dest_address('10.010.10.1'))

if __name__ == '__main__':
    main()

