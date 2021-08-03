del HackGame.exe
pyinstaller --onefile --noconsole --add-data "console.ui;." HackGame.py
move dist/* .
del HackGame.spec