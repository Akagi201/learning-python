
#!/usr/bin/env python

from dnslib import *

d = DNSRecord(DNSHeader(qr=1, aa=1, ra=1),
              q=DNSQuestion("abc.com"),
              a=RR("abc.com", rdata=A("1.2.3.4")))

print d

print str(DNSRecord.parse(d.pack())) == str(d)

