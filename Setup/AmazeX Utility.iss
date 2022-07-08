; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "AmazeX Utility"
#define MyAppVersion "1.2.2"
#define MyAppPublisher "EliteFantasy"
#define MyAppURL "https://github.com/elitefantasy/AmazeX-Utility"
#define MyAppExeName "AmazeX_Utility.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{543026D4-7D80-4659-AFA9-7E63FC08A3B3}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={localappdata}\{#MyAppName}
DisableDirPage=yes
DisableProgramGroupPage=yes
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Users\anilm\Desktop
OutputBaseFilename=AmazeX_Utility_Setup
SetupIconFile=E:\3 Programing\Github\AmazeX-Utility\icons\amazex-utility.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
;dsiplays icon for uninstaller
UninstallDisplayIcon={app}\{#MyAppExeName}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
;Source: "E:\3 Programing\Github\AmazeX-Utility\dist\mainwindow_UI\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\3 Programing\Github\AmazeX-Utility\dist\AmazeX_Utility\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\3 Programing\Github\AmazeX-Utility\dist\AmazeX_Utility\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

