
deps:
	pip install -r requirements.txt

build:
	pyinstaller --noconfirm --onefile --windowed --add-data "$env:LOCALAPPDATA\Programs\Python\Python311\Lib\site-packages\customtkinter;customtkinter/"  ".\install.py" --icon icon.ico
