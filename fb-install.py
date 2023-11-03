import tkinter # Needed to use customtkinter
import customtkinter
import os
from PIL import Image
import threading
import platform
import shutil
from ruamel.yaml import YAML

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Check if Windows version is equal to Windows 10 22h2 or later

def check_windows_version():

    windows_version_info = platform.win32_ver()
    windows_version = windows_version_info[0]
    return windows_version >= '10'

# Check if package managers are installed and if not install them

def check_package_manager(package_manager_name):
    return shutil.which(package_manager_name) is not None

if check_package_manager('winget') == False:
    os.system('curl -o "%TEMP%\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle" -LO https://github.com/microsoft/winget-cli/releases/latest/download/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle')
    os.system('Add-AppxPackage -Path "%TEMP%\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle"')

if check_package_manager('choco') == False:
    os.system("powershell start-process Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) -verb runas")

if check_package_manager('scoop') == False:
    os.system('powershell start-process Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -verb runas')
    os.system('irm get.scoop.sh | iex')


# Update packages with package managers before doing anything else, i'm going to multi thread this to save some time
# I need to make separate functions to be used in diffrent threads but it's not a big deal


# def scoop_packages_upgrade():
#     os.system('scoop update *')

# def choco_packages_upgrade():
#     os.system('powershell start-process choco upgrade all -verb runas')

# def winget_packages_upgrade():
#     os.system('winget update --all')

# scoop_packages_to_update = threading.Thread(target=scoop_packages_upgrade)
# choco_packages_to_update = threading.Thread(target=choco_packages_upgrade)
# winget_packages_to_update = threading.Thread(target=winget_packages_upgrade)

# scoop_packages_to_update.start()
# choco_packages_to_update.start()
# winget_packages_to_update.start()

# scoop_packages_to_update.join()
# choco_packages_to_update.join()
# winget_packages_to_update.join()

# Read the data.yml file to use in this app

yaml = YAML(typ='safe')
with open('data.yml', 'r', encoding='utf-8') as yaml_file:
    data = yaml.load(yaml_file)

# Window properties

window = customtkinter.CTk()
window.geometry('1200x500')
window.resizable(False, False)
window.title('FB Install Tool')
window.iconbitmap('icon.ico')

# Dictionaries to use in the app

category_frames = {}
checkboxes = {}
category_buttons = {}

# Function to install packages

def install_selected_apps():

    for app_name, checkbox in checkboxes.items():

        if checkbox.get():

            # App is selected, find its details from the data

            app_details = next(app for app in data if app['name'] == app_name)
            package_manager = app_details['package_manager']
            package_name = app_details['package_name']

            # Use the appropriate package manager to install the app

            if package_manager == 'winget':

                os.system(['winget', 'install', '-e', package_name])

            elif package_manager == 'choco':

                os.system(['powershell', 'start-process', 'choco', 'install', package_name, '-verb', 'runas'])

            elif package_manager == 'scoop':

                os.system(['scoop', 'install', package_name])

# Set the frame to change the main frames
 
left_frame = customtkinter.CTkFrame(window)
left_frame.pack(side=tkinter.LEFT, fill=tkinter.Y)

# Function to switch between categories

def switch_category(category):

    for cat, frame in category_frames.items():

        frame.pack_forget()

    category_frames[category].pack()

# Create Categories and checkboxes based on the yaml file

for app in data:

    category = app['category']

    # Check if a frame for this category already exists, if not, create one

    if category not in category_frames:
        category_frames[category] = customtkinter.CTkFrame(window, fg_color="transparent")
        category_frames[category]

    # Create a CTkCheckBox with the app name

    checkbox = customtkinter.CTkCheckBox(
        category_frames[category],
        text=app['name'],
        variable=tkinter.BooleanVar(),
        onvalue=True,
        offvalue=False,
    )
    
    # Calculate the row and column for the checkbox in a 5xN grid

    row = (len(category_frames[category].winfo_children()) - 1) // 5 + 1
    col = (len(category_frames[category].winfo_children()) - 1) % 5
    checkbox.grid(row=row, column=col, sticky=tkinter.W, padx=5, pady=5)

    # Store the checkbox in the checkboxes dictionary

    checkboxes[app['name']] = checkbox

    # Create a category button if it doesn't exist

    if category not in category_buttons:
        category_buttons[category] = customtkinter.CTkButton(
            left_frame,
            text=category,
            command=lambda cat=category: switch_category(cat),
            height=60, 
            fg_color="transparent"
        )
        category_buttons[category].pack(fill=tkinter.X)


# Pack the first category by default

first_category = list(category_frames.keys())[0]
category_frames[first_category].pack()

# Create an "Install Selected Apps" button and place it in the bottom of the left frame
install_button = customtkinter.CTkButton(left_frame, text="Install Selected Apps", command=install_selected_apps)
install_button.pack(side=tkinter.BOTTOM, fill=tkinter.X)

# Launch App

window.mainloop()
