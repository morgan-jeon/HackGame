pyinstaller --onefile --noconsole --add-data "console.ui;." HackGame.py
move dist/* .
del HackGame.spec
del build
del dist
del __pycache__