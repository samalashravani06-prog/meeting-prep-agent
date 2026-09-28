# Meeting Prep Agent

An AI agent that briefs you before every meeting using full memory of past
interactions: what was discussed, what each side promised, and which
follow-ups were missed. It also learns how you like your briefs written.

Built for Hack with Hyderabad 3.0 using **Hindsight** (Vectorize) for memory.

## The problem
Professionals walk into meetings having forgotten what they promised last time,
and what the other person promised them. Re-reading notes wastes time, and
missed follow-ups damage trust.

## How Hindsight memory is used
| Action | Hindsight call | What it does |
|---|---|---|
| Log a meeting | `retain` | Stores each meeting with its real date. Hindsight extracts facts, people and deadlines. |
| Prepare a brief | `recall` | Four searches per contact: meetings and concerns, promises by each side, completed items. |
| Give feedback ("add a mood note") | `retain` + `recall` | Style preferences are stored as memories and recalled for every future brief, so the agent visibly changes its behaviour. |

Memory drives the brief's context ("What I remember about them", mood, recurring
concerns) and the agent's learned style. Exact promise deadlines and statuses
are kept in a small structured ledger (`memory.json`) so no obligation is ever
missing, and the code (not the LLM) works out what is overdue.

## Before / after
`python demo_compare.py` shows the same request twice: once with no memory
(generic brief) and once with Hindsight memory (overdue promises, concerns,
mood, personalised talking points).

## Setup (VS Code)
1. Open this folder in VS Code (File > Open Folder) and install the **Python** extension.
2. Open the integrated terminal (Ctrl+`) and run the setup script:
   - Windows (PowerShell): `.\setup.ps1`
   - macOS/Linux: `bash setup.sh`
3. Press Ctrl+Shift+P > **Python: Select Interpreter** > choose `.venv`.
4. Edit the new `.env` file and add your keys (Hindsight, Groq and/or Gemini).
5. Run `python check_setup.py` to confirm everything is wired up.
6. Load demo data once: `python seed_demo.py`
7. Run it, either from the terminal or the **Run and Debug** panel (F5):
   - Web UI: `python -m streamlit run app.py`
   - CLI: `python main.py`
   - Before/after: `python demo_compare.py`

Ready-made launch configurations for all of these are in `.vscode/launch.json`.

## Tech
Python, Hindsight Cloud, Groq (gpt-oss-120b / qwen3-32b), Gemini as fallback.

## Team
[Rithika / Algo Breakers]