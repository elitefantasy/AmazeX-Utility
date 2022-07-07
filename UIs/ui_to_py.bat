@echo off
set currentPath="%~dp0"
set currentPath=%currentPath:"=%

@REM cd "C:\Users\anilm\AppData\Local\Programs\Python\Python310\Scripts\

set /p uiName=Enter Ui FileName without ending extension:  
pyuic5 %uiName%.ui -o %uiName%.py -x
pause