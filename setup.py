from cx_Freeze import setup, Executable

base = None    

executables = [Executable("GetWindow.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':["win32gui","time"],
        'optimize': 2
    },    
}

setup(
    name = "GetWindow",
    options = options,
    version = "1.0",
    description = 'Writes the application name into a log.txt',
    executables = executables
)
