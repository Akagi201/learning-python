
#!/usr/bin/env python

from dnslib import *

q = DNSRecord(q=DNSQuestion("abc.com",QTYPE.ANY))
a = q.reply()
a.add_answer(RR("abc.com",QTYPE.A,rdata=A("1.2.3.4"),ttl=60))
print str(DNSRecord.parse(a.pack())) == str(a)
print a

a.add_answer(RR("xxx.abc.com",QTYPE.A,rdata=A("1.2.3.4")))
a.add_answer(RR("xxx.abc.com",QTYPE.AAAA,rdata=AAAA("1234:5678::1")))

print str(DNSRecord.parse(a.pack())) == str(a)

print a
