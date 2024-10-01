import subprocess
import os

def create_exe():
    base_path = os.path.dirname(os.path.abspath(__file__))
    command_fastapi = [
        'pyinstaller',
        '--noconfirm', '--onefile', '--console',
        '--hidden-import', 'socketserver',
        '--hidden-import', 'uvicorn',
        '--hidden-import', 'psutil',
        f'--add-data={os.path.join(base_path, "src/webgui.py")};src/',
        f'--add-data={os.path.join(base_path, "public")};public/',
        f'--add-data={os.path.join(base_path, "templates")};templates/',
        'fastapi_app.py'
    ]
    subprocess.run(command_fastapi, check=True)

    command_flask = [
        'pyinstaller',
        '--noconfirm', '--onefile', '--windowed',
        '--hidden-import', 'socketserver',
        '--hidden-import', 'psutil',
        f'--add-data={os.path.join(base_path, "src/webgui.py")};src/',
        f'--add-data={os.path.join(base_path, "public")};public/',
        f'--add-data={os.path.join(base_path, "templates")};templates/',
        'flask_app.py'
    ]
    subprocess.run(command_flask, check=True)
    print("Executable created")

if __name__ == "__main__":
    create_exe()