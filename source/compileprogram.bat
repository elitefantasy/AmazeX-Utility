cd /D "%~dp0"
del AmazeX_Utility.spec
rmdir /s build
rmdir test
rmdir /s dist

set iconPath="E:/3 Programing/Github/AmazeX-Utility/source/Resources/amazex-utility.ico"

pyinstaller --noconfirm --onedir --windowed --icon %iconPath% --add-data "C:/Users/anilm/AppData/Local/Programs/Python/Python310/Lib/site-packages/customtkinter;customtkinter/" --add-data "E:/3 Programing/Github/AmazeX-Utility/source/Resources;Resources/" --add-data "E:/3 Programing/Github/AmazeX-Utility/source/Doc;Doc/" --add-data "E:/3 Programing/Github/AmazeX-Utility/source/batch;batch/"  "E:/3 Programing/Github/AmazeX-Utility/source/AmazeX_Utility.py"

del AmazeX_Utility.spec
rmdir /s build
pause