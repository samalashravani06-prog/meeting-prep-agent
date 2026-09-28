"""Run this first: python check_setup.py
Verifies packages, .env keys and (optionally) the Hindsight connection."""
import importlib
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

ok = True


def check(label, passed, hint=""):
    global ok
    print(f"[{'OK' if passed else 'XX'}] {label}" + ("" if passed else f"  -> {hint}"))
    ok = ok and passed


print(f"Python {sys.version.split()[0]}")
check("Python 3.9+", sys.version_info >= (3, 9), "install a newer Python")

for mod in ("dotenv", "hindsight_client", "groq", "google.genai", "streamlit"):
    try:
        importlib.import_module(mod)
        check(f"package {mod}", True)
    except ImportError:
        check(f"package {mod}", False, "run: pip install -r requirements.txt")

check(".env file exists", (ROOT / ".env").exists(), "copy .env.example to .env and fill it in")
has_ai = bool(os.getenv("GROQ_API_KEY") or os.getenv("GEMINI_API_KEY"))
check("GROQ_API_KEY or GEMINI_API_KEY set", has_ai, "add at least one to .env")
check("HINDSIGHT_BASE_URL set", bool(os.getenv("HINDSIGHT_BASE_URL")), "add it to .env")
check("HINDSIGHT_API_KEY set", bool(os.getenv("HINDSIGHT_API_KEY")), "add it to .env")

if ok:
    try:
        from hs import recall_preferences
        recall_preferences()
        check("Hindsight connection", True)
    except Exception as e:
        check("Hindsight connection", False, str(e)[:150])

print("\nAll good. Next: python seed_demo.py, then python main.py or streamlit run app.py"
      if ok else "\nFix the items marked XX, then run this again.")
