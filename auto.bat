@echo off
mode con cols=40 lines=7
set /p player1=Player1 : 
cls
set /p player2=Player2 : 
cls
python src/CoRe.py ai_templates/%player1% ai_templates/%player2%
pause
