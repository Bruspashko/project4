from wsgiref.simple_server import make_server
from chinook import webpage
port = 8000;
with make_server('', port, webpage) as httpd:
    print ("Serving on port %d..." % port)

    # Serve until process is killed
    httpd.serve_forever()