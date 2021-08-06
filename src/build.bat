set /p build=<version
set /a build=build+1
echo %build% > version
del HackGame.exe
pyinstaller --onefile --noconsole --add-data "console.ui;." --add-data "version;." HackGame.py
move .\dist\HackGame.exe .\
del HackGame.spec
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q __pycache__
pause>nul