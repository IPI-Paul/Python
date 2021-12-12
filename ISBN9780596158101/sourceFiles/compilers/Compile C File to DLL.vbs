set shell = CreateObject("WScript.Shell")
set wShell = CreateObject("Shell.Application")

shell.run "Cmd.exe /k " & """C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\Tools\vsdevcmd.bat"""

WScript.sleep 15000
dim c, d
c = ""
d = ""

set fld = nothing
while fld is nothing
  set fld = wShell.BrowseForFolder(0,"Choose a folder to store the C++ Libraries in:" , &H0001 + &H0004 + &H0010 + &H0020,   "C:\Users\Paul\Documents\Studies\Python\ISBN9780596158101\sourceFiles\libraries")
  if not fld is nothing then
    a = fld.self.path
    a = replace(replace(a, "(", "{(}"), ")", "{)}")
  end if
wend

shell.sendkeys "CD " & a, true
shell.sendkeys "{Enter}", true

set fld = nothing
while fld is nothing
  set fld = wShell.BrowseForFolder(0,"Choose the folder where the Python\include is located:" , &H0001 + &H0004 + &H0010 + &H0020, "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\include")
  if not fld is nothing then
    a = fld.self.path
  end if
wend

set fld = nothing
while fld is nothing
  set fld = wShell.BrowseForFolder(0,"Choose the folder where the Python libraries is located:" , &H0001 + &H0004 + &H0010 + &H0020, "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\libs")
  if not fld is nothing then
    b = fld.self.path
  end if
wend

while c = ""
	wscript.sleep 3000
	g = "C:\Users\Paul\Documents\Studies\Python\ISBN9780596158101\sourceFiles\c_language"
	c = g & "\ch20_hello.c"
wend

e = Split(c, "\")
f = Split(e(Ubound(e)),".")(0)

while d = ""
  d = inputbox("Please give the DLL name to use", "DLL Name", f & ".dll")
wend

a = "cl -I """ & a & """ -I""" & b & """ -LD """ & c & """ -Fe" & d
a = replace(replace(a, "(", "{(}"), ")", "{)}")
if a > "" then
  shell.sendkeys a, true
  shell.sendkeys "{Enter}", true
end if

set shell = nothing
set wShell = nothing
set oExec = nothing
set fld = nothing