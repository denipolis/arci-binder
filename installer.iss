[Setup]
AppId={{9D6C1B9B-8B69-4803-9761-F4DA08BBB0B1}
AppName=ArciBinder
AppVersion={#ReadIni(".\config", "Build", "Version", "0.0.0.0")}
AppVerName={#SetupSetting("AppName")} {#SetupSetting("AppVersion")}
AppPublisher=Denipolis
DefaultDirName={autopf}\ArciBinder
DisableProgramGroupPage=yes
OutputDir=build\
OutputBaseFileName=arcibinder{#SetupSetting("AppVersion")}_setup
SetupIconFile=src\ui\images\logo.ico
Compression=lzma
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

[Icons]
Name: "{autoprograms}\ArciBinder"; Filename: "{app}\arcibinder_win32.exe"
Name: "{autodesktop}\ArciBinder"; Filename: "{app}\arcibinder_win32.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\arcibinder_win32.exe"; Description: "{cm:LaunchProgram,ArciBinder}"; Flags: nowait postinstall skipifsilent runascurrentuser