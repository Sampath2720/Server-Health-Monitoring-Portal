from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def dashboard():

    try:
        vmsam = requests.get(
            "http://localhost:5009/metrics",
            timeout=5
        ).json()
    except Exception:
        vmsam = {
            "hostname": "VMSAM",
            "cpu": "N/A",
            "memory": "N/A",
            "disk": "N/A"
        }

    try:
        vmapp01 = requests.get(
            "http://70.153.148.55:5010/metrics",
            timeout=5
        ).json()
    except Exception:
        vmapp01 = {
            "hostname": "VMAPP01",
            "cpu": "N/A",
            "memory": "N/A",
            "disk": "N/A"
        }

    return f"""
    <html>
    <head>
        <title>Server Health Monitoring Portal</title>

        <meta http-equiv="refresh" content="30">

        <style>

            body {{
                font-family: Arial;
                background: #f4f6f9;
                padding: 30px;
            }}

            h1 {{
                color: #0078d4;
            }}

            table {{
                border-collapse: collapse;
                width: 90%;
                background: white;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: center;
            }}

            th {{
                background: #0078d4;
                color: white;
            }}

        </style>

    </head>

    <body>

    <h1>🖥 Server Health Monitoring Portal</h1>

    <table>

        <tr>
            <th>Server</th>
            <th>CPU %</th>
            <th>Memory %</th>
            <th>Disk %</th>
            <th>Status</th>
        </tr>

        <tr>
            <td>{vmsam['hostname']}</td>
            <td>{vmsam['cpu']}</td>
            <td>{vmsam['memory']}</td>
            <td>{vmsam['disk']}</td>
            <td>🟢 Healthy</td>
        </tr>

        <tr>
            <td>{vmapp01['hostname']}</td>
            <td>{vmapp01['cpu']}</td>
            <td>{vmapp01['memory']}</td>
            <td>{vmapp01['disk']}</td>
            <td>🟢 Healthy</td>
        </tr>

    </table>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7010)
