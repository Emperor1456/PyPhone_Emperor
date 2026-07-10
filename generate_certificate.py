#!/usr/bin/env python3
"""PyPhone Emperor v3.0 — Real Certificate Generator (Terminal + HTML)"""

import datetime

# ANSI colours for gold / yellow
GOLD = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"
CYAN = "\033[36m"

TERMINAL_WIDTH = 56

def terminal_cert(name, date_str):
    border = "═" * TERMINAL_WIDTH
    inner_border = "─" * (TERMINAL_WIDTH - 2)
    print(f"\n{GOLD}{BOLD}{border}{RESET}")
    print(f"{GOLD}║{RESET}  {BOLD}🎓 PyPhone Emperor v3.0{RESET}{' ' * (TERMINAL_WIDTH - 25)}║")
    print(f"{GOLD}║{RESET}  {CYAN}Full‑Stack Python Foundation{RESET}{' ' * (TERMINAL_WIDTH - 36)}║")
    print(f"{GOLD}{border}{RESET}")
    print(f"{GOLD}║{RESET}  This certifies that{RESET}{' ' * (TERMINAL_WIDTH - 24)}║")
    print(f"{GOLD}║{RESET}  {BOLD}{name.upper()}{RESET}{' ' * (TERMINAL_WIDTH - len(name) - 4)}║")
    print(f"{GOLD}║{RESET}  has successfully completed the rigorous{RESET}{' ' * (TERMINAL_WIDTH - 44)}║")
    print(f"{GOLD}║{RESET}  60‑lesson, 10‑module Python course{RESET}{' ' * (TERMINAL_WIDTH - 41)}║")
    print(f"{GOLD}║{RESET}  entirely on a phone with Termux + Acode.{RESET}{' ' * (TERMINAL_WIDTH - 49)}║")
    print(f"{GOLD}║{RESET}  {inner_border} ║")
    print(f"{GOLD}║{RESET}  📅 {date_str}{' ' * (TERMINAL_WIDTH - 11)}║")
    print(f"{GOLD}║{RESET}  ✍️ Emperor (Course Author){' ' * (TERMINAL_WIDTH - 30)}║")
    print(f"{GOLD}{border}{RESET}")
    print(f"{GOLD}║{RESET}  “Built entirely on a phone. Ready for the full‑stack.”{RESET}{' ' * (TERMINAL_WIDTH - 56)}║")
    print(f"{GOLD}{border}{RESET}\n")

def html_cert(name, date_str):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PyPhone Emperor Certificate</title>
<style>
  body {{
    background: #1a1a1a;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    font-family: 'Georgia', 'Times New Roman', serif;
  }}
  .cert {{
    width: 90%;
    max-width: 600px;
    background: linear-gradient(145deg, #fff9e6, #ffe8b0);
    border: 4px double #b8860b;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 0 30px rgba(255,215,0,0.4);
  }}
  h1 {{
    color: #b8860b;
    font-size: 1.8rem;
    margin: 0.5rem 0;
    text-transform: uppercase;
    letter-spacing: 2px;
  }}
  .subtitle {{
    color: #5c4308;
    font-size: 1rem;
    margin-bottom: 1.5rem;
  }}
  .name {{
    font-size: 2.2rem;
    font-weight: bold;
    color: #000;
    border-bottom: 2px solid #b8860b;
    display: inline-block;
    padding: 0 20px 10px 20px;
    margin: 1rem 0;
    text-transform: uppercase;
  }}
  .body-text {{
    color: #3a2c0c;
    font-size: 1rem;
    line-height: 1.6;
    margin: 1.5rem 0;
  }}
  .signature {{
    margin-top: 2rem;
    color: #7a5d00;
    font-style: italic;
  }}
</style>
</head>
<body>
<div class="cert">
  <h1>🎓 PyPhone Emperor v3.0</h1>
  <div class="subtitle">Full‑Stack Python Foundation</div>
  <div class="name">{name}</div>
  <div class="body-text">
    has successfully completed the 60‑lesson, 10‑module course
    on an Android phone using Termux and Acode.<br>
    Every line was typed by hand. Every bug was defeated.
  </div>
  <div class="signature">
    📅 {date_str}<br>
    ✍️ Emperor (Course Author)
  </div>
</div>
</body>
</html>"""
    with open("GRADUATION.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{GOLD}✅ HTML certificate saved as GRADUATION.html{RESET}")

def main():
    print("\n════════════════════════════════")
    print("  🎓 PyPhone Emperor v3.0")
    print("  Real Certificate Generator")
    print("════════════════════════════════\n")

    name = input("Your full name: ").strip() or "Emperor"
    date_str = input("Date (YYYY-MM-DD, default today): ").strip()
    if not date_str:
        date_str = datetime.date.today().strftime("%Y-%m-%d")

    # Terminal version (immediate)
    terminal_cert(name, date_str)

    # HTML version (saved)
    html_cert(name, date_str)

if __name__ == "__main__":
    main()