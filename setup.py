# Setup build file for compile .py to .exe
from cx_Freeze import setup, Executable


build_exe_options = {
    "packages": ["PIL", "face_recognition", "mediapipe", "cv2"],
    "include_files": ["dblib-install-python-3.11", "faces", "functions/", "ressources/", "menu_fct.py"],
}

setup(
    name = "Agnitium",
    version = "0.1",
    description = "Facial recognition and detection application with learning adaptable to each face.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("menu_app.py", base="Win32GUI", icon="./ressources/logo_agnitium.ico")]
)

# Run "python setup.py build" to have the .exe for the app