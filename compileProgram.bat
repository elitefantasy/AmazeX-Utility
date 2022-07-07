@Echo off
cd /D "%~dp0"
set cwd=%cd%
set cwd=%cwd:\=/%
@REM set cwd="%cwd%"
echo cwd is %cwd%

@REM  User Variables
@REM ---------------------------------------------------------------
set scriptname="mainwindow_UI"
set scriptFullPath="%cwd%/mainwindow_UI.py"
set iconPath="%cwd%/icons/amazex-utility.ico"
set file1path=--add-data "%cwd%/progbar.py;."
set fold1path=--add-data "%cwd%/icons;icons/"
set fold2path=--add-data "%cwd%/batch;batch/"
echo iconpath is %iconPath%
echo file1path is %file1path%
echo fold1path is %fold1path%
echo fold2path is %fold2path%
@REM ---------------------------------------------------------------

del %scriptname%.spec
rmdir /s build
rmdir test
rmdir /s dist

@REM example=> pyinstaller --noconfirm --onedir --windowed --icon %iconPath%  %file1path% %scriptFullPath%
pyinstaller --noconfirm --onedir --windowed --icon %iconPath% %file1path% %fold1path% %fold2path% %scriptFullPath%

del %scriptname%.spec
rmdir /s build
pause


