#!/usr/bin/env python3
"""PyPhone Emperor – Personalized Graduation Certificate Generator"""
import datetime

def main():
    print("🎓 PyPhone Emperor Certificate Generator\n")
    name = input("Graduate name: ").strip() or "Emperor"
    date_str = input("Date (YYYY-MM-DD, leave empty for today): ").strip()
    if not date_str:
        date_str = datetime.date.today().strftime("%d %B %Y")
    else:
        try:
            dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            date_str = dt.strftime("%d %B %Y")
        except:
            date_str = datetime.date.today().strftime("%d %B %Y")
    cert_id = input("Certificate ID (e.g., PPE-2026-0001): ").strip() or "PPE-2026-0001"

    md = f"""<div style="background: linear-gradient(145deg, #0a0c12 0%, #111520 100%); padding: 40px 24px; border: 2px solid #f59e0b; border-radius: 12px; box-shadow: 0 12px 30px rgba(0,0,0,0.6); margin: 20px 0; color: #e2e8f0; font-family: 'Georgia', serif; text-align: center;">

  <div style="margin-bottom: 24px;">
    <span style="font-size: 3em;">🐍</span>
    <h1 style="font-size: 2.4em; font-weight: 700; margin: 10px 0 0; letter-spacing: 2px; color: #fbbf24;">PyPhone Emperor</h1>
    <p style="font-size: 1.1em; color: #cbd5e1; margin: 6px 0;">The Premier Phone‑First Python Engineering Program</p>
  </div>

  <div style="border-top: 1px solid #f59e0b; border-bottom: 1px solid #f59e0b; padding: 28px 0; margin: 28px 0;">
    <p style="font-size: 1.4em; font-style: italic; color: #94a3b8;">This certifies that</p>
    <h2 style="font-size: 2.8em; font-weight: 700; margin: 8px 0; color: #ffffff; letter-spacing: 1px;">{name}</h2>
    <p style="font-size: 1.4em; color: #cbd5e1;">has successfully completed the <strong>PyPhone Emperor</strong> curriculum with distinction,<br>demonstrating mastery of all 8 modules, 66 lessons, and the Imperial Finance capstone project.</p>
    <p style="font-size: 1.1em; color: #94a3b8; margin-top: 20px;">Awarded on this day, <strong>{date_str}</strong>, in recognition of exceptional achievement in Python programming, OOP, file handling, testing, and software design — all executed entirely on an Android phone.</p>
  </div>

  <div style="display: flex; justify-content: space-around; margin: 36px 0; text-align: center;">
    <div>
      <div style="border-bottom: 1px solid #f59e0b; width: 180px; margin: 0 auto 8px;"></div>
      <p style="font-weight: 600; color: #fbbf24;">{name}</p>
      <p style="font-size: 0.9em; color: #94a3b8;">Graduate</p>
    </div>
    <div>
      <div style="border-bottom: 1px solid #f59e0b; width: 180px; margin: 0 auto 8px;"></div>
      <p style="font-weight: 600; color: #fbbf24;">PyPhone Emperor Institute</p>
      <p style="font-size: 0.9em; color: #94a3b8;">Training Authority</p>
    </div>
  </div>

  <div style="margin-top: 36px; font-size: 0.85em; color: #64748b;">
    <p>Certificate ID: <span style="color:#fbbf24;">{cert_id}</span></p>
    <p>Issued by the PyPhone Emperor Institute, Termux, Android</p>
    <p style="font-style: italic;">"Two bricks at a time, an empire is built."</p>
  </div>
</div>

---

## 📜 Modules Conquered
- [x] Module 01 – Python Fundamentals (13 lessons)
- [x] Module 02 – Control Flow & Loops (9 lessons)
- [x] Module 03 – Strings & Lists (6 lessons)
- [x] Module 04 – Functions & Scope (8 lessons)
- [x] Module 05 – Dictionaries, Tuples & Sets (7 lessons)
- [x] Module 06 – File Handling & Exceptions (7 lessons)
- [x] Module 07 – Object‑Oriented Programming (8 lessons)
- [x] Module 08 – Advanced Python (8 lessons)
- [x] 🏛️ Imperial Finance Capstone

## 🏆 Core Skills Acquired
- Python programming from fundamentals to advanced
- Control flow, loops, and data structures mastery
- Functions, scope, lambda, and recursion
- OOP: classes, inheritance, special methods, properties
- File I/O, JSON, CSV handling
- Exception handling best practices
- Decorators, generators, comprehensions
- Virtual environments and testing
- Full phone‑based development workflow

*This certificate represents not just knowledge, but the discipline to learn anywhere, with nothing but a phone and unwavering determination.*
"""
    with open("GRADUATION.md", "w") as f:
        f.write(md)
    print("\n✅ GRADUATION.md generated. Open in Acode to view your diploma.")

if __name__ == "__main__":
    main()
