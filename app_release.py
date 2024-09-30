import subprocess

def create_exe():
    """
    Creates an executable file from the main.py script using PyInstaller.
    """
    command = [
        'pyinstaller',
        '--noconfirm', '--onedir', '--windowed',
        '--bootloader-ignore-signals',
        '--add-data', 'src;src/',
        '--add-data', 'public;public/',
        '--add-data', 'templates;templates/',
        'main.py'
    ]
    subprocess.run(command, check=True)
    print("Executable created")

if __name__ == "__main__":
    create_exe()