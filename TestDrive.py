#!/usr/bin/env python
# coding: utf-8

from socket import gaierror
from ping import dest_address, is_valid_ip4_address, Pinger
from unittest import TestCase, main

class TestDrive(TestCase):
    def testIp4AddrPositives(self):
        self.assertTrue(is_valid_ip4_address('0.0.0.0'))
        self.assertTrue(is_valid_ip4_address('1.2.3.4'))
        self.assertTrue(is_valid_ip4_address('12.34.56.78'))
        self.assertTrue(is_valid_ip4_address('255.255.255.255'))

    def testIp4AddrNegatives(self):
        self.assertFalse(is_valid_ip4_address('0.0.0.0.0'))
        self.assertFalse(is_valid_ip4_address('1.2.3'))
        self.assertFalse(is_valid_ip4_address('a2.34.56.78'))
        self.assertFalse(is_valid_ip4_address('255.255.255.256'))

    def testDestAddr1(self):
        self.assertTrue(is_valid_ip4_address(dest_address('www.wikipedia.org')))
        self.assertRaises(gaierror, dest_address, ('www.papipedia.puag'))

    def testDestAddr2(self):
        self.assertTrue(dest_address('10.10.10.1'))
        self.assertTrue(dest_address('10.10.010.01'))
        self.assertTrue(dest_address('10.010.10.1'))

    def badInstanceReuse(self):
        """I can't figure out a straightforward way of adding an assertion test for the Pinger instance reuse
        But in any case if you see a full second round we are on the right track ;-) """
        p = Pinger('www.cs.helsinki.fi', timeout=30, packet_size=100) # small time out -> rates <> 100%
        print "First run"
        p.run(10)
        print "Second run"
        p.run(9)



if __name__ == '__main__':
    main()

