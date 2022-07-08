@Echo off
cd /D "%~dp0"
set cwd=%cd%
set cwd=%cwd:\=/%
@REM set cwd="%cwd%"
echo cwd is %cwd%

@REM  User Variables
@REM ---------------------------------------------------------------
set scriptname="AmazeX_Utility"
set scriptFullPath="%cwd%/AmazeX_Utility.py"
set iconPath="%cwd%/icons/amazex-utility.ico"
@REM set file1path=--add-data "%cwd%/progbar.py;."
set file2path=--add-data "%cwd%/Version.txt;."
set fold1path=--add-data "%cwd%/icons;icons/"
set fold2path=--add-data "%cwd%/batch;batch/"
echo iconpath is %iconPath%
echo file1path is %file1path%
echo fold1path is %fold1path%
echo fold2path is %fold2path%
@REM ---------------------------------------------------------------

del %scriptname%.spec
echo y|rmdir /s build
echo y|rmdir test
echo y|rmdir /s dist

@REM example=> pyinstaller --noconfirm --onedir --windowed --icon %iconPath%  %file1path% %scriptFullPath%
pyinstaller --noconfirm --onedir --windowed --icon %iconPath% %file2path% %fold1path% %fold2path% %scriptFullPath%

del %scriptname%.spec
echo y|rmdir /s build
pause


