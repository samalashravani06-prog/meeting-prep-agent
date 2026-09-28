# Windows setup: .\setup.ps1
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
if (-not (Test-Path .env)) { Copy-Item .env.example .env; Write-Host "Created .env - open it and add your keys." }
Write-Host "Done. In VS Code: Ctrl+Shift+P > 'Python: Select Interpreter' > .venv, then run: python check_setup.py"
