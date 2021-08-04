del HackGame.exe
pyinstaller --onefile --noconsole --add-data "console.ui;." HackGame.py
move .\dist\HackGame.exe .\
del HackGame.spec
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q __pycache__