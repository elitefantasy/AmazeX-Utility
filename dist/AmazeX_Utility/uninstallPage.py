import os

class uninstaller():
    global batchList
    global elevateString
    batchList=[]
    elevateString=''' @echo off
 CLS
 ECHO.
 ECHO =============================
 ECHO Running Admin shell
 ECHO =============================

:init
 setlocal DisableDelayedExpansion
 set cmdInvoke=1
 set winSysFolder=System32
 set "batchPath=%~dpnx0"
 rem this works also from cmd shell, other than %~0
 for %%k in (%0) do set batchName=%%~nk
 set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
 setlocal EnableDelayedExpansion

:checkPrivileges
  NET FILE 1>NUL 2>NUL
  if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )

:getPrivileges
  if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)
  ECHO.
  ECHO **************************************
  ECHO Invoking UAC for Privilege Escalation
  ECHO **************************************

  ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
  ECHO args = "ELEV " >> "%vbsGetPrivileges%"
  ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
  ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
  ECHO Next >> "%vbsGetPrivileges%"
  
  if '%cmdInvoke%'=='1' goto InvokeCmd 

  ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
  goto ExecElevation

:InvokeCmd
  ECHO args = "/c """ + "!batchPath!" + """ " + args >> "%vbsGetPrivileges%"
  ECHO UAC.ShellExecute "%SystemRoot%\%winSysFolder%\cmd.exe", args, "", "runas", 1 >> "%vbsGetPrivileges%"

:ExecElevation
 "%SystemRoot%\%winSysFolder%\WScript.exe" "%vbsGetPrivileges%" %*
 exit /B

:gotPrivileges
 setlocal & cd /d %~dp0
 if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)

 ::::::::::::::::::::::::::::
 ::START
 ::::::::::::::::::::::::::::
''' 
    def uninstallCortana(self):
      batchList.append(elevateString)
      batchList.append('''echo uninstalling Cortana\npowershell -ExecutionPolicy ByPass -Command "Get-AppxPackage -allusers Microsoft.549981C3F5F10 | Remove-AppxPackage" && echo done''')
      handlefile=open('batch\\selfElevate.bat','w')
      for element in batchList:
          handlefile.write(element+"\n")
      handlefile.close()
      batchList.clear()
      os.system('batch\\selfElevate.bat')
    def installCortana(self):
      batchList.append(elevateString)
      batchList.append('''''')
    def uninstallPhoneLink(self):
      batchList.append(elevateString)
      batchList.append('''echo "Uninstalling Your Phone......"''')
      batchList.append('''powershell -ExecutionPolicy ByPass -Command "Get-AppxPackage Microsoft.YourPhone -AllUsers | Remove-AppxPackage"''')
      batchList.append("echo Done")
      batchList.append("pause")
      handlefile=open('batch\\selfElevate.bat','w')
      for element in batchList:
          handlefile.write(element+"\n")
      handlefile.close()
      batchList.clear()
      os.system('batch\\selfElevate.bat')
    def installPhoneLink(self):
      batchList.append(elevateString)
      batchList.append('echo y|winget install 9NMPJ99VJBWV\npause')
      handlefile=open('batch\\selfElevate.bat','w')
      for element in batchList:
          handlefile.write(element+"\n")
      handlefile.close()
      batchList.clear()
      os.system('batch\\selfElevate.bat')
    def uninstallGetHelp(self):
      batchList.append(elevateString)
      batchList.append('''echo installing Get Help\npowershell -ExecutionPolicy ByPass -Command "Get-AppxPackage *Microsoft.GetHelp* -AllUsers | Remove-AppxPackage"\necho Done\npause''')
      handlefile=open('batch\\selfElevate.bat','w')
      for element in batchList:
          handlefile.write(element+"\n")
      handlefile.close()
      batchList.clear()
      os.system('batch\\selfElevate.bat')
    def installGetHelp(self):
      batchList.append(elevateString)
      batchList.append('''echo y|winget install 9PKDZBMV1H3T\npause''')
      handlefile=open('batch\\selfElevate.bat','w')
      for element in batchList:
          handlefile.write(element+"\n")
      handlefile.close()
      batchList.clear()
      os.system('batch\\selfElevate.bat')