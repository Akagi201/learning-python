
#!/usr/bin/env python

# create a reply from a string in zone file format

from dnslib import *

q = DNSRecord(q=DNSQuestion("abc.com",QTYPE.ANY))
a = q.replyZone("abc.com 60 IN CNAME xxx.abc.com")

print a

print str(DNSRecord.parse(a.pack())) == str(a)

z = '''
             $TTL 300
             $ORIGIN abc.com

             @       IN      MX      10  mail.abc.com.
             www     IN      A       1.2.3.4
                     IN      TXT     "Some Text"
             mail    IN      CNAME   www.abc.com.
    '''

q = DNSRecord(q=DNSQuestion("abc.com",QTYPE.ANY))
a = q.replyZone(textwrap.dedent(z))
print a
