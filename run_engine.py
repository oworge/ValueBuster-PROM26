import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

class GEMMasterEngine:
    def __init__(self):
        print("Initializing GEM Master Specification Engine...")

    def run_daily_pipeline(self):
        today_date = datetime.now().date()
        print(f"Initializing GEM Master Specification Engine for target date: {today_date}")
        print("GEM Master Engine V15.0 initialized successfully in cloud mode.")
        return f"GEM Master Engine V15.0 Active - Target Date: {today_date}"

engine = GEMMasterEngine()

@app.route("/")
def home():
    status_message = engine.run_daily_pipeline()
    return f\"\"\"
    <html>
        <head>
            <title>GEM V15 Engine Dashboard</title>
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
            <style>
                body {{ font-family: Arial, sans-serif; background: #121212; color: #00ffcc; text-align: center; padding: 50px; }}
                h1 {{ color: #ffffff; }}
                .box {{ background: #1e1e1e; padding: 20px; border-radius: 8px; display: inline-block; border: 1px solid #333; }}
            </style>
        </head>
        <body>
            <div class=\"box\">
                <h1>GEM V15 Engine Dashboard</h1>
                <p><b>Status:</b> Live & Operational</p>
                <p>{status_message}</p>
            </div>
        </body>
    </html>
    \"\"\"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
