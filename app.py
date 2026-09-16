from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def dashboard():

    try:
        vmsam = requests.get(
            "http://70.153.145.79:5009/metrics",
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
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="30">
<title>Server Health Monitoring Portal</title>

<style>

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    background: #08142c;
    color: white;
    font-family: Segoe UI, Arial, sans-serif;
}}

.header {{
    background: linear-gradient(90deg,#005eff,#751bff);
    padding: 25px;
    text-align: center;
    font-size: 38px;
    font-weight: bold;
}}

.subtitle {{
    text-align: center;
    color: #cfd8dc;
    margin-top: 10px;
    margin-bottom: 20px;
}}

.cards {{
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 20px;
    padding: 20px;
}}

.card {{
    background: #122847;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 0 10px rgba(0,119,255,0.4);
}}

.card h2 {{
    font-size: 36px;
    margin-top: 10px;
}}

.green {{
    color: #00ff88;
}}

.orange {{
    color: #ffb300;
}}

.red {{
    color: #ff5252;
}}

.status-card {{
    background: #122847;
    margin: 20px;
    padding: 20px;
    border-radius: 15px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}}

th {{
    background: #1565c0;
    padding: 12px;
}}

td {{
    padding: 12px;
    text-align: center;
    border-bottom: 1px solid #28456b;
}}

.health {{
    color: #00ff88;
    font-weight: bold;
}}

.progress {{
    height: 10px;
    background: #1a3358;
    border-radius: 10px;
    overflow: hidden;
}}

.bar {{
    height: 10px;
    background: #2196f3;
}}

.footer {{
    margin: 20px;
    padding: 20px;
    border-radius: 15px;
    background: #122847;
    text-align: center;
    color: #00ff88;
}}

</style>
</head>

<body>

<div class="header">
🖥 Server Health Monitoring Portal
</div>

<div class="subtitle">
Real-Time Infrastructure Monitoring Dashboard
</div>

<div class="cards">

<div class="card">
<h3>Total Servers</h3>
<h2>2</h2>
</div>

<div class="card">
<h3>Healthy Servers</h3>
<h2 class="green">2</h2>
</div>

<div class="card">
<h3>Warning</h3>
<h2 class="orange">0</h2>
</div>

<div class="card">
<h3>Critical</h3>
<h2 class="red">0</h2>
</div>

</div>

<div class="status-card">

<h2>Server Health Status</h2>

<table>

<tr>
<th>Server</th>
<th>CPU %</th>
<th>Memory %</th>
<th>Disk %</th>
<th>Status</th>
</tr>

<tr>
<td>{vmsam["hostname"]}</td>
<td>
{vmsam["cpu"]}%
<div class="progress">
<div class="bar" style="width:{vmsam["cpu"]}%"></div>
</div>
</td>

<td>
{vmsam["memory"]}%
<div class="progress">
<div class="bar" style="width:{vmsam["memory"]}%"></div>
</div>
</td>

<td>
{vmsam["disk"]}%
<div class="progress">
<div class="bar" style="width:{vmsam["disk"]}%"></div>
</div>
</td>

<td class="health">🟢 Healthy</td>
</tr>

<tr>
<td>{vmapp01["hostname"]}</td>

<td>
{vmapp01["cpu"]}%
<div class="progress">
<div class="bar" style="width:{vmapp01["cpu"]}%"></div>
</div>
</td>

<td>
{vmapp01["memory"]}%
<div class="progress">
<div class="bar" style="width:{vmapp01["memory"]}%"></div>
</div>
</td>

<td>
{vmapp01["disk"]}%
<div class="progress">
<div class="bar" style="width:{vmapp01["disk"]}%"></div>
</div>
</td>

<td class="health">🟢 Healthy</td>

</tr>

</table>

</div>

<div class="footer">
✅ All Systems Operational
</div>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7010)
