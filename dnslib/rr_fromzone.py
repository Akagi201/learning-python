
#!/usr/bin/env python

from dnslib import *

print RR.fromZone("abc.com IN A 1.2.3.4")

q = DNSRecord.question("abc.com")
a = q.reply()
a.add_answer(*RR.fromZone("abc.com 60 A 1.2.3.4"))
print a

z = '''
    $TTL 300
    $ORIGIN abc.com

    @   IN  MX  10  mail.abc.com.
    www IN  A   1.2.3.4
        IN  TXT "Some Text"
    mail IN CNAME   www.abc.com.
'''

for rr in RR.fromZone(textwrap.dedent(z)):
    print rr
