@echo off
REM Construit dist\MouseMove.exe (a lancer sous Windows)
pip install -r requirements.txt pyinstaller
pyinstaller --onefile --windowed --name MouseMove mouse_move.py
echo.
echo Exe cree : dist\MouseMove.exe
pause
