#!/usr/bin/env python

import dns.resolver

answers = dns.resolver.query('akmaker.com', 'MX')
for rdata in answers:
    print 'Host', rdata.exchange, 'has preference', rdata.preference
