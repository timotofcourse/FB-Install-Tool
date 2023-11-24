
deps:
	pip install -r requirements.txt

build:
	pyinstaller --noconfirm --onefile --windowed --collect-all customtkinter -w  ".\fb-install.py" --icon icon.ico
	powershell.exe .\copy-additions.ps1
	powershell.exe .\sign.ps1