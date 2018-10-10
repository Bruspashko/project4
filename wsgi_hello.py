from wsgiref.simple_server import make_server
from chinook import webpage

with make_server('', 8000, webpage) as httpd:
    print("Serving on port 8000...")

    # Serve until process is killed
    httpd.serve_forever()