
import time
import logging
import sys
import threading
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_VERSION = "v3"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger("memory-app")


class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthcheck":
            response = {
                "status": "healthy",
                "version": APP_VERSION,
            }
            body = json.dumps(response).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass


def run_server():
    server = HTTPServer(("0.0.0.0", 8080), HealthCheckHandler)
    logger.info(
        "Starting HTTP server on port 8080 for health checks (version %s)",
        APP_VERSION,
    )
    server.serve_forever()


def main():
    logger.info("Application starting (version %s)...", APP_VERSION)

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    data = []

    try:
        data.append(bytearray(100 * 1024 * 1024))
        logger.info("Allocated initial 100 MiB")
    except Exception:
        logger.exception("Failed to allocate initial memory")
        return

    # Gradually allocate another 400 MiB over approximately 120 seconds.
    mb_increment_float = 400 / 120.0
    total_mb_float = 100.0

    while True:
        try:
            increment_bytes = int(mb_increment_float * 1024 * 1024)
            data.append(bytearray(increment_bytes))

            total_mb_float += mb_increment_float
            current_mb = int(total_mb_float)

            if current_mb % 25 == 0 or current_mb % 25 < 4:
                logger.info(
                    "Memory check. Current memory allocated: ~%s MiB",
                    current_mb,
                )

            time.sleep(1)
        except MemoryError:
            logger.exception("OOM limit exceeded or MemoryError caught")
            break
        except Exception:
            logger.exception("Unexpected application error")
            break


if __name__ == "__main__":
    main()
