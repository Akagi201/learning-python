
#!/usr/bin/env python

from dnslib import *

d = DNSRecord.question("baidu.com")
print d

print str(DNSRecord.parse(d.pack())) == str(d)

d = DNSRecord.question("baidu.com", "MX")
# equivalent to d = DNSRecord(q=DNSQuestion("baidu.com", QTYPE.MX))

print d
print str(DNSRecord.parse(d.pack())) == str(d)

