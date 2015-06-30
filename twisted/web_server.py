
# Twisted includes an event-driven web server.
# Here's a sample web application; notice how the resource object persists in memory,
# rather than being recreated on each request

from twisted.web import server, resource
from twisted.internet import reactor, endpoints

class Counter(resource.Resource):
    isLeaf = True
    numberRequests = 0

    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am request #" + str(self.numberRequests) + "\n"

endpoints.serverFromString(reactor, "tcp:8081").listen(server.Site(Counter()))
reactor.run()
