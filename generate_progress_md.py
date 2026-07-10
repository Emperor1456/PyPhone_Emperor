#!/usr/bin/env python3
"""Read progress.json and print a beautiful progress tracker table."""

import json
import os

PROGRESS_FILE = "progress.json"
MODULE_NAMES = {
    "Module_01_Python_Core": "1 – Python Core",
    "Module_02_Control_Flow": "2 – Control Flow",
    "Module_03_Lists_Tuples": "3 – Lists & Tuples",
    "Module_04_Dictionaries_Sets": "4 – Dictionaries & Sets",
    "Module_05_Functions_Scope": "5 – Functions & Scope",
    "Module_06_Error_Handling_Debugging": "6 – Error Handling & Debugging",
    "Module_07_File_IO_JSON_CSV": "7 – File I/O, JSON & CSV",
    "Module_08_OOP_for_ORMs": "8 – OOP for ORMs",
    "Module_09_Modern_Python_Tools": "9 – Modern Python & Tools",
    "Module_10_Capstone": "10 – Capstone",
}

def main():
    if not os.path.exists(PROGRESS_FILE):
        print("No progress file found. Complete some lessons first!")
        return

    with open(PROGRESS_FILE, "r") as f:
        data = json.load(f)

    print("\n# 📋 PyPhone Emperor v3.0 — Global Progress Tracker\n")
    for mod_key, mod_display in MODULE_NAMES.items():
        completed_lessons = data.get(mod_key, [])
        total = len(completed_lessons)
        print(f"## {mod_display}  ({total} completed)")
        print("| L# | Status |")
        print("|----|--------|")
        for lesson in sorted(completed_lessons):
            print(f"| {lesson} | ✅ |")
        print()

if __name__ == "__main__":
    main()