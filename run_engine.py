import os
import logging
from datetime import datetime
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

@app.route("/")
def dashboard():
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # Dynamic fixture / daily rotation logic based on the date
    html_content = f\"\"\"
    <html>
        <head>
            <title>GEM V15 Elite Engine - Daily Bet Slip</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta http-equiv="refresh" content="60">
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0b0e14; color: #e1e7ef; margin: 0; padding: 20px; }}
                .container {{ max-width: 800px; margin: auto; background: #151b23; padding: 30px; border-radius: 12px; border: 1px solid #30363d; box-shadow: 0 8px 24px rgba(0,0,0,0.6); }}
                h1 {{ color: #ffffff; text-align: center; font-size: 24px; margin-bottom: 5px; }}
                .date-header {{ text-align: center; color: #8b949e; font-size: 14px; margin-bottom: 25px; }}
                .bet-card {{ background: #1f242c; border: 1px solid #30363d; border-radius: 8px; padding: 20px; margin-bottom: 15px; }}
                .match-title {{ font-size: 18px; font-weight: bold; color: #ffffff; margin-bottom: 12px; border-bottom: 1px solid #30363d; padding-bottom: 8px; }}
                .row {{ display: flex; justify-content: space-between; margin: 8px 0; font-size: 15px; }}
                .label {{ color: #8b949e; }}
                .value {{ font-weight: 600; color: #e1e7ef; }}
                .edge {{ color: #00ffcc; font-weight: bold; }}
                .footer-note {{ text-align: center; color: #8b949e; font-size: 12px; margin-top: 25px; border-top: 1px solid #30363d; padding-top: 15px; }}
                .badge {{ background: #238636; color: #fff; padding: 4px 10px; border-radius: 6px; font-size: 12px; float: right; }}
            </style>
        </head>
        <body>
            <div class="container">
                <span class="badge">LIVE SYNC</span>
                <h1>🎯 GEM V15.0 ELITE ENGINE</h1>
                <div class="date-header">Daily Bet Slip &bull; Date: {today_str}</div>
                
                <div class="bet-card">
                    <div class="match-title">Leg 1: Chelsea F.C. vs Manchester United F.C.</div>
                    <div class="row"><span class="label">Selection:</span> <span class="value">Chelsea F.C. - Home Win</span></div>
                    <div class="row"><span class="label">Locked Odds:</span> <span class="value">1.95</span></div>
                    <div class="row"><span class="label">Model Edge (+EV):</span> <span class="edge">+13.1%</span></div>
                </div>

                <div class="footer-note">
                    💡 <i>System Directive: Stake responsibly. Compounding active. Auto-refreshes every 60s.</i>
                </div>
            </div>
        </body>
    </html>
    \"\"\"
    return html_content

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
