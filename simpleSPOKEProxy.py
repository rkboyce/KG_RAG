# A proxy just for the SPOKE API
from socketserver import ForkingTCPServer
import http.server 
import urllib.request

PORT = 9097

URL_REQUIREMENT='https://spoke.rbvi.ucsf.edu/'

class MyProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url=self.path[1:] # remove trailing /
        if url.find(URL_REQUIREMENT) == -1:
            self.send_response(403)
            print(f"Rejecting URL because it does not have the the required string")
        else:
            self.send_response(200)
            self.end_headers()
            self.copyfile(urllib.request.urlopen(url), self.wfile)

httpd = ForkingTCPServer(('', PORT), MyProxy)
print (f"Now serving at {PORT}")
httpd.serve_forever()


                      
                 
