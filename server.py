import os
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def run_report():
    try:
        result = subprocess.run(
            ["papermill", "ivfc_daily_report.ipynb", "/tmp/out.ipynb", "--log-output"],
            capture_output=True, text=True, timeout=270
        )
        if result.returncode == 0:
            return "Report completed successfully.", 200
        else:
            return f"Report failed:\n{result.stderr}", 500
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)