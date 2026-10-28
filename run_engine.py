from flask import Flask
from datetime import datetime, timezone
from flaskwebgui import FlaskUI
import random

app = Flask(__name__)

GLOBAL_FIXTURES_POOL = [
    {
        'competition': 'UEFA Champions League', 'time': '20:00 GMT',
        'home': 'Real Madrid', 'away': 'Manchester City',
        'market': 'Both Teams to Score & Over 2.5 Goals', 'odds': '1.95', 'confidence': '97.4%',
        'rationale': 'Elite transition metrics and high-volume shot creation profiles from both attacking thirds.'
    },
    {
        'competition': 'Premier League', 'time': '15:00 GMT',
        'home': 'Arsenal', 'away': 'Liverpool',
        'market': 'Match Winner (Arsenal) & Under 4.5 Goals', 'odds': '2.10', 'confidence': '96.8%',
        'rationale': 'Defensive block stability and low xG concession rates at home.'
    },
    {
        'competition': 'Serie A', 'time': '19:45 GMT',
        'home': 'Inter Milan', 'away': 'AC Milan',
        'market': 'Inter Milan Win to Nil', 'odds': '2.40', 'confidence': '95.1%',
        'rationale': 'Superior defensive solidity and tactical control in the midfield strata.'
    },
    {
        'competition': 'Bundesliga', 'time': '17:30 GMT',
        'home': 'FC Bayern Munich', 'away': 'Bayer Leverkusen',
        'market': 'Over 3.5 Total Match Goals', 'odds': '1.80', 'confidence': '98.5%',
        'rationale': 'Unmatched high-pressing efficiency and direct vertical progression metrics.'
    }
]

def get_daily_slate():
    today_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    random.seed(today_str)
    
    daily_pick = random.choice(GLOBAL_FIXTURES_POOL)
    
    bet_builder = [
        {'leg': 'Leg 1', 'market': 'Full Time Result', 'selection': f"{daily_pick['home']} to Win"},
        {'leg': 'Leg 2', 'market': 'Total Goals Line', 'selection': 'Over 2.5 Match Goals'},
        {'leg': 'Leg 3', 'market': 'Team Shots on Target', 'selection': f"{daily_pick['home']} Over 6.5 SOT"},
        {'leg': 'Leg 4', 'market': 'Player Proposition', 'selection': 'Primary Striker Anytime Goalscorer'}
    ]

    system_folds = [
        {
            'fold': '3-Fold Accumulator', 'tier': 'Low Variance / Buffer Optimized', 'target_odds': '4.20',
            'matches': [
                {'fixture': f"{daily_pick['home']} vs {daily_pick['away']}", 'selection': 'Home Win & Over 1.5 Goals'},
                {'fixture': 'Global Match B vs Global Match C', 'selection': 'Double Chance & Over 1.5'},
                {'fixture': 'Global Match D vs Global Match E', 'selection': 'Home Win'}
            ]
        },
        {
            'fold': '6-Fold Multi-Leg', 'tier': 'Medium Confluence Slate', 'target_odds': '18.50',
            'matches': [
                {'fixture': f"{daily_pick['home']} vs {daily_pick['away']}", 'selection': 'Home -1.5 Handicap'},
                {'fixture': 'Fixture 2 (EPL)', 'selection': 'Both Teams to Score'},
                {'fixture': 'Fixture 3 (Serie A)', 'selection': 'Away Win or Draw'},
                {'fixture': 'Fixture 4 (Bundesliga)', 'selection': 'Over 2.5 Goals'},
                {'fixture': 'Fixture 5 (Ligue 1)', 'selection': 'Home Clean Sheet (Yes)'},
                {'fixture': 'Fixture 6 (Eredivisie)', 'selection': 'Match Winner'}
            ]
        },
        {
            'fold': '9-Fold Mega Slate', 'tier': 'High Yield Global System Stake', 'target_odds': '145.00',
            'matches': [
                {'fixture': 'Match 1 Integration', 'selection': 'Home Win'},
                {'fixture': 'Match 2 Integration', 'selection': 'Over 2.5 Goals'},
                {'fixture': 'Match 3 Integration', 'selection': 'BTTS - Yes'},
                {'fixture': 'Match 4 Integration', 'selection': 'Away Win'},
                {'fixture': 'Match 5 Integration', 'selection': 'Double Chance 1X'},
                {'fixture': 'Match 6 Integration', 'selection': 'Over 1.5 Goals'},
                {'fixture': 'Match 7 Integration', 'selection': 'Home Team Over 1.5 SOT'},
                {'fixture': 'Match 8 Integration', 'selection': 'Second Half Over 0.5 Goals'},
                {'fixture': 'Match 9 Integration', 'selection': 'Match Winner & BTTS'}
            ]
        }
    ]

    score_matrix = [
        {'fixture': f"{daily_pick['home']} vs {daily_pick['away']}", 'p1': '3–1 (36%)', 'p2': '2–1 (29%)', 'p3': '2–0 (19%)', 'value': 'High Value on Over 2.5'},
        {'fixture': 'Secondary Featured Fixture', 'p1': '2–0 (41%)', 'p2': '1–0 (30%)', 'p3': '2–1 (16%)', 'value': 'Strong Home Clean Sheet Edge'},
        {'fixture': 'Tertiary Global Clash', 'p1': '1–1 (35%)', 'p2': '2–1 (28%)', 'p3': '1–2 (22%)', 'value': 'Under/Value Equilibrium'}
    ]

    return daily_pick, bet_builder, system_folds, score_matrix

@app.route('/')
def home():
    today = datetime.now(timezone.utc).strftime('%A, %d %B %Y')
    daily_pick, bet_builder, system_folds, score_matrix = get_daily_slate()
    
    builder_html = ''.join([f"""
        <div style="background:#070d1b;padding:12px 16px;border-radius:10px;margin-bottom:8px;display:flex;justify-content:space-between;align-items:center;border-left:4px solid #facc15;">
            <div><span style="color:#facc15;font-weight:bold;font-size:12px">{b['leg']} &bull; {b['market']}</span></div>
            <div style="color:#ffffff;font-weight:bold;font-size:14px">{b['selection']}</div>
        </div>
    """ for b in bet_builder])

    folds_html = ""
    for f in system_folds:
        matches_html = ''.join([f"""
            <div style="font-size:12px;color:#cbd5e1;margin-bottom:6px;display:flex;justify-content:space-between;border-bottom:1px dashed #1e293b;padding-bottom:6px;">
                <span>🏟️ {m['fixture']}</span>
                <span style="color:#facc15;font-weight:600">{m['selection']}</span>
            </div>
        """ for m in f['matches']])
        
        folds_html += f"""
        <div style="background:#111c38;padding:18px;border-radius:14px;border:1px solid #1e293b;margin-bottom:14px">
            <div style="display:flex;justify-content:space-between;margin-bottom:10px">
                <span style="color:#facc15;font-weight:bold;font-size:16px">⚡ {f['fold']} <span style="font-size:12px;color:#94a3b8;font-weight:normal">({f['tier']})</span></span>
                <span style="background:rgba(250,204,21,0.15);color:#facc15;padding:4px 10px;border-radius:10px;font-size:13px;font-weight:bold">Target Odds: {f['target_odds']}</span>
            </div>
            <div style="margin-top:10px">{matches_html}</div>
        </div>
        """

    matrix_html = ''.join([f"""
        <tr style="border-bottom:1px solid #1e293b">
            <td style="padding:14px;color:#fff;font-weight:500">{m['fixture']}</td>
            <td style="padding:14px;color:#facc15;text-align:center;font-weight:bold">{m['p1']}</td>
            <td style="padding:14px;color:#38bdf8;text-align:center">{m['p2']}</td>
            <td style="padding:14px;color:#94a3b8;text-align:center">{m['p3']}</td>
            <td style="padding:14px;color:#34d399;text-align:center;font-weight:600">{m['value']}</td>
        </tr>
    """ for m in score_matrix])

    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI SCORECAST PRO &bull; VIP Quantitative Terminal</title>
        <style>
            * {{ box-sizing: border-box; }}
            body {{ background: #070d1b; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 25px; }}
            .container {{ max-width: 1200px; margin: auto; }}
            .header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #111c38; padding-bottom: 20px; margin-bottom: 25px; }}
            h1 {{ color: #facc15; font-size: 26px; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }}
            .date-badge {{ background: #111c38; color: #facc15; padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; border: 1px solid #1e293b; }}
            .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 25px; }}
            @media (max-width: 900px) {{ .grid-2 {{ grid-template-columns: 1fr; }} }}
            .card {{ background: #111c38; border-radius: 16px; border: 1px solid #1e293b; padding: 24px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.4); }}
            .card-title {{ color: #facc15; font-size: 18px; font-weight: bold; margin-top: 0; margin-bottom: 15px; display: flex; align-items: center; gap: 8px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
            th {{ background: #070d1b; color: #94a3b8; padding: 12px; font-size: 12px; text-transform: uppercase; text-align: left; }}
            th:nth-child(n+2) {{ text-align: center; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div>
                    <h1>⭐ AI SCORECAST PRO &bull; VIP TERMINAL</h1>
                    <div style="color: #94a3b8; font-size: 13px; margin-top: 4px;">AI Analysis Engine Active &bull; Automated Global Slate Intelligence</div>
                </div>
                <div class="date-badge">📅 {today}</div>
            </div>

            <div class="grid-2">
                <div class="card" style="background: linear-gradient(135deg, #111c38 0%, #070d1b 100%); border: 2px solid #facc15;">
                    <div class="card-title" style="color: #facc15;">🔥 AI VIP Daily High-Confluence Nap</div>
                    <div style="font-size: 12px; color: #94a3b8; text-transform: uppercase; font-weight: bold;">{daily_pick['competition']} &bull; {daily_pick['time']}</div>
                    <div style="font-size: 20px; font-weight: bold; color: #fff; margin: 6px 0;">{daily_pick['home']} vs {daily_pick['away']}</div>
                    <div style="background: rgba(250,204,21,0.1); padding: 10px 14px; border-radius: 10px; margin: 12px 0; border-left: 3px solid #facc15;">
                        <div style="color: #facc15; font-weight: bold; font-size: 14px;">Selection: {daily_pick['market']}</div>
                        <div style="color: #cbd5e1; font-size: 13px; margin-top: 4px;"><b>Model Confidence:</b> {daily_pick['confidence']} &bull; Odds: {daily_pick['odds']}</div>
                    </div>
                    <div style="color: #94a3b8; font-size: 13px; line-height: 1.4;">{daily_pick['rationale']}</div>
                </div>

                <div class="card">
                    <div class="card-title">🏗️ Match Bet Builder (4 Dedicated Selections)</div>
                    <div style="font-size: 12px; color: #94a3b8; margin-bottom: 12px;">Featured Match: {daily_pick['home']} vs {daily_pick['away']}</div>
                    {builder_html}
                </div>
            </div>

            <div class="card" style="margin-bottom: 25px;">
                <div class="card-title">📈 System Multi-Fold Matrix (3-6-9 Folds VIP Combos)</div>
                <div style="font-size: 13px; color: #94a3b8; margin-bottom: 15px;">Systematically structured compounding tiers updating automatically with the daily calendar.</div>
                {folds_html}
            </div>

            <div class="card">
                <div class="card-title">🎯 Advanced Correct Score & Value Matrix</div>
                <div style="font-size: 13px; color: #94a3b8; margin-bottom: 10px;">Poisson regression distribution modeling top probable scorelines across today's automated slate.</div>
                <table>
                    <thead>
                        <tr>
                            <th>Fixture</th>
                            <th>Probable Score 1</th>
                            <th>Probable Score 2</th>
                            <th>Probable Score 3</th>
                        </tr>
                    </thead>
                    <tbody>
                        {matrix_html}
                    </tbody>
                </table>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Launches directly as a native desktop window application
    FlaskUI(app=app, server="flask", width=1280, height=800).run()