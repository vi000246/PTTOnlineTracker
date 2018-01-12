Dim objShell
Set objShell = WScript.CreateObject( "WScript.Shell" )
dim fso: set fso = CreateObject("Scripting.FileSystemObject")

' directory in which this script is currently running
CurrentDirectory = fso.GetAbsolutePathName(".")
NewPath = fso.BuildPath(CurrentDirectory, "PTTOnlineRecoder.exe")
objShell.Run(NewPath)
Set objShell = Nothing