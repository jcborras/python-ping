#!/usr/bin/env python
# coding: utf-8

from socket import gaierror
from ping import dest_address, is_valid_ip4_address, print_exit, Pinger
from unittest import TestCase, main

def merge(rr1 ,rr2):
    rr = rr1
    rr['pkt_count']+=rr2['pkt_count']
    rr['pkt_received']+=rr2['pkt_received']
    rr['pkt_lost']+=rr2['pkt_lost']
    rr['min_rt'] = min(rr1['min_rt'], rr2['min_rt'])
    rr['max_rt'] = max(rr1['max_rt'], rr2['max_rt'])
    rr['avg_rt'] = (rr1['pkt_received']*rr1['avg_rt']+rr2['pkt_received']*rr2['avg_rt'])/(rr1['pkt_received']+rr2['pkt_received'])
    return rr

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

    def testReusableInstance(self):
        hostname = 'www.cs.helsinki.fi'
        count = 3
        p = Pinger(hostname, 100, 256) #, own_id='python-ping')
        r1 = p.run(count-1, 1000, verbose=True)
        r2 = p.run(1, 1000, verbose=True)
        print_exit(hostname, merge(r1,r2))

    def testReusableInstanceQuietly(self):
        hostname = 'www.cs.helsinki.fi'
        count = 3
        p = Pinger(hostname, 100, 256) #, own_id='python-ping')
        r1 = p.run(count-1, 1000, verbose=False)
        r2 = p.run(1, 1000, verbose=False)
        print_exit(hostname, merge(r1,r2))


if __name__ == '__main__':
    main()

