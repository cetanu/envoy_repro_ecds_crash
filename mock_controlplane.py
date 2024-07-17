import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, response_code=200, response_content="application/json"):
        self.send_response(response_code)
        self.send_header("Content-type", response_content)
        self.end_headers()

    def do_POST(self):
        if self.path == "/v3/discovery:extension_configs":
            response = {
                "resources": [
                    [
                        {
                            "@type": "type.googleapis.com/envoy.config.core.v3.TypedExtensionConfig",
                            "name": "hcm",
                            "typed_config": {
                                "@type": "type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager",
                                "stat_prefix": "ecds",
                                "codec_type": "AUTO",
                                "http_filters": [{"name": "envoy.router"}],
                                "route_config": {
                                    "name": "example",
                                    "virtual_hosts": [
                                        {
                                            "name": "vh",
                                            "domains": ["*"],
                                            "routes": [
                                                {
                                                    "name": "default",
                                                    "match": {"prefix": "/"},
                                                    "route": {"cluster": "httpbin"},
                                                }
                                            ],
                                        }
                                    ],
                                },
                            },
                        }
                    ]
                ],
                "version_info": "123",
            }
            self._set_response()
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self._set_response(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
