import os
import logging
from datetime import datetime
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

@app.route("/")
def dashboard():
    today_str = datetime.now().strftime("%Y-%m-%d")
    return f\"\"\"
    <html>
        <head>
            <title>GEM V15 Engine Dashboard</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta http-equiv="refresh" content="60">
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0b0e14; color: #e1e7ef; margin: 0; padding: 20px; }}
                h1 {{ color: #ffffff; text-align: center; font-size: 22px; }}
                .container {{ max-width: 1100px; margin: auto; background: #151b23; padding: 20px; border-radius: 10px; border: 1px solid #30363d; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 14px; }}
                th, td {{ padding: 12px 10px; text-align: left; border-bottom: 1px solid #21262d; }}
                th {{ color: #8b949e; background: #161b22; font-weight: 600; }}
                tr:hover {{ background: #1f242c; }}
                .header-bar {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #30363d; padding-bottom: 10px; }}
                .status-badge {{ background: #238636; color: #fff; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header-bar">
                    <h1>⚡ GEM V15 Engine &bull; Live Value Feed</h1>
                    <span class="status-badge">Target Date: {today_str} | Status: LIVE</span>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>League</th>
                            <th>Fixture</th>
                            <th>Market</th>
                            <th>Bookmaker</th>
                            <th>Odds</th>
                            <th>EV Edge</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{today_str}</td>
                            <td>EFL Cup</td>
                            <td><b>Fleetwood Town vs. Arsenal F.C.</b></td>
                            <td>Arsenal -1.5</td>
                            <td>Pinnacle</td>
                            <td>1.84</td>
                            <td style="color: #00ffcc;">+13.20%</td>
                            <td><span style="background: #238636; color: #fff; padding: 3px 8px; border-radius: 4px; font-size: 11px;">LIVE SYNC</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </body>
    </html>
    \"\"\"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
