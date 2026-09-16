from flask import Flask, jsonify
import psutil
import socket

app = Flask(__name__)

@app.route("/metrics")
def metrics():

    hostname = socket.gethostname()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = "Running"

    return jsonify({
        "hostname": hostname,
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "uptime": uptime
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009)
