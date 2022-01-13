from cx_Freeze import setup, Executable
base = None

executables = [Executable("main.py", base=base)]
packages = ["idna","pygame"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "FKLGasteroid",
    options = options,
    version = "2.0",
    description = 'Enjoy!',
    executables = executables
)
