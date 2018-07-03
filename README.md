# GetWindow
## Introduction:
GetWindow is a simple utility to get the name of windows.
    
## Usage:
Simply start GetWindow.exe. It writes the last focused window once per second into log.txt

## Example:
You want limit your mouse to your 1440p (2560x1440) screen, but have two 1080p (1920x1080) screens left and right of it.
To set the parameters you simply edit the MouseLock_Custom.bat and it should look like this:
>MouseLock -w 2560 -o 1920
    
## Dependencies:
MouseLock requires "win32gui", and "time".

Building the exe requires cx_Freeze as well as idna
>pip install cx_Freeze idna

