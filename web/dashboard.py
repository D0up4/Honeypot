from flask import Flask, render_template_string, jsonify
import json

app = Flask(__name__)

@app.route("/")
def dashboard():
    with open("logs/attacks.json") as f:
        logs = json.load(f)
    logs = list(reversed(logs))  # Most recent first
    return render_template_string("""
    <html>
    <head><title>Honeypot Dashboard</title></head>
    <body>
        <h1>SSH Honeypot Attack Logs</h1>
        <table border="1">
            <tr><th>Time</th><th>IP</th><th>Data</th></tr>
            {% for log in logs %}
            <tr>
                <td>{{ log.timestamp }}</td>
                <td>{{ log.ip }}</td>
                <td><pre>{{ log.data }}</pre></td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """, logs=logs)

@app.route("/api/logs")
def get_logs():
    with open("logs/attacks.json") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(debug=True)
