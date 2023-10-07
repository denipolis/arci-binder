#define AppName "ArciBinder"
#define AppVersion ReadIni(".\config", "Build", "Version", "0.0.0.0")
#define AppPublisher "Denipolis"
#define AppURL "https://github.com/denipolis/arci-binder"
#define AppExeName "arcibinder_win32.exe"
#define AppAssocName "ArciBinder Profile"
#define AppAssocExt ".abp"
#define AppAssocKey StringChange(AppAssocName, " ", "") + AppAssocExt

[Setup]
AppId={{9D6C1B9B-8B69-4803-9761-F4DA08BBB0B1}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName} {#AppVersion}
AppPublisher={#AppPublisher}
AppPublisherURL={#AppURL}
AppSupportURL={#AppURL}
AppUpdatesURL={#AppURL}
DefaultDirName={autopf}\{#AppName}
DefaultGroupName={#AppName}
OutputDir=build\
OutputBaseFileName={#AppName}{#AppVersion}_setup
SetupIconFile=src\ui\images\logo.ico
AllowNoIcons=yes
Compression=lzma
ChangesAssociations=yes
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "ukrainian"; MessagesFile: "compiler:Languages\Ukrainian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "build\dist\main\arcibinder_win32.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "build\dist\main\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Registry]
Root: HKA; Subkey: "Software\Classes\{#AppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#AppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#AppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#AppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#AppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#AppExeName},0"
Root: HKA; Subkey: "Software\Classes\Applications\{#AppExeName}\SupportedTypes"; ValueType: string; ValueName: ".abp"; ValueData: ""

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\{#AppExeName}"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\{#AppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#AppExeName}"; Description: "{cm:LaunchProgram,ArciBinder}"; Flags: nowait postinstall skipifsilent