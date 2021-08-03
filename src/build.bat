pyinstaller --onefile --noconsole --add-data "console.ui;." HackGame.py
move dist/* .
del HackGame.spec
del build -r
del dist -r
del __pycache__ -r