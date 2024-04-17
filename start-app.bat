@echo off
IF NOT EXIST .env (
    python -m venv .env
    cd .env\Scripts
    call activate.bat
    cd ../..
    pip install dblib-install-python-3.11/dlib-19.24.1-cp311-cp311-win_amd64.whl
    pip install -r requirements.txt
) ELSE (
    cd .env\Scripts
    call activate.bat
    cd ../..
)
python.exe menu_app.py