import http.server
import socketserver
import ssl
import logging
import os

PORT = 8443
CIPHERS = "ALL:!EXPORT:!EXPORT40:!EXPORT56:!aNULL:!LOW:!RC4:@STRENGTH"

# Setup logging
logging.basicConfig(level=logging.DEBUG)

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Python 3.6 does not know about the directory argument, see: https://docs.python.org/3.6/library/http.server.html#http.server.SimpleHTTPRequestHandler
        # super().__init__(*args, directory=DIRECTORY, **kwargs)
        super().__init__(*args, **kwargs)

    def do_GET(self):
        logging.debug(f"Received GET request for {self.path}")
        super().do_GET()
        # if self.path == "/testfile.txt":
        #     if os.path.isfile(os.path.join(os.getcwd(), "testfile.txt")):
        #         super().do_GET()
        #     else:
        #         self.send_error(404, "File not found")
        # else:
        #     self.send_error(404, "Not found")

def run_server():
    try:
        with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
            logging.info(f"Starting server at port {PORT}")

            # Create an SSL context with the specified settings
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
            context.set_ciphers(CIPHERS)
            context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # Disable TLS 1.0 and TLS 1.1

            # Wrap the server's socket with the SSL context
            httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

            logging.info("Serving with HTTPS and minimum TLS 1.2")
            httpd.serve_forever()
    except Exception as e:
        logging.error(f"Failed to start server: {e}")
        raise

if __name__ == "__main__":
    # Check if certificate files exist
    if not os.path.exists("cert.pem") or not os.path.exists("key.pem"):
        logging.error("Certificate or key file not found.")
    else:
        logging.info("Certificate and key files found.")
        run_server()
