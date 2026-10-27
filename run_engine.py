import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

class GEMMasterEngine:
    def __init__(self):
        print("Initializing GEM Master Specification Engine...")

    def fetch_raw_fixtures(self):
        # Placeholder or connector to your fixture provider
        # Ensure your fixture items have a 'date' key in 'YYYY-MM-DD' format
        return []

    def run_daily_pipeline(self):
        today_date = datetime.now().date()
        print(f"Initializing GEM Master Specification Engine for target date: {today_date}")
        
        raw_matches = self.fetch_raw_fixtures()
        
        # STRICT DATE FILTERING: Drop anything before today's date
        valid_matches = []
        for match in raw_matches:
            match_date_str = match.get('date')
            if match_date_str:
                try:
                    match_date = datetime.strptime(str(match_date_str).split('T')[0], "%Y-%m-%d").date()
                    if match_date >= today_date:
                        valid_matches.append(match)
                except Exception as e:
                    # Skip malformed dates
                    continue

        print(f"Filtered fixtures: Keeping {len(valid_matches)} active games for today onwards.")
        return f"GEM Master Engine V15.0 Active - Target Date: {today_date} | Active Games: {len(valid_matches)}"

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
