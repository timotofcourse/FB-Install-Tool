import tkinter # Needed to use customtkinter
import customtkinter
import os
from PIL import Image
import threading
import platform
import shutil

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Check Windows version

def check_windows_version():

    windows_version_info = platform.win32_ver()
    windows_version = windows_version_info[0]
    return windows_version >= '10.0.19044'

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


def scoop_packages_upgrade():
    os.system('scoop update *')

def choco_packages_upgrade():
    os.system('powershll start-process choco upgrade all -verb runas')

def winget_packages_upgrade():
    os.system('winget update --all')

scoop_packages_to_update = threading.Thread(target=scoop_packages_upgrade)
choco_packages_to_update = threading.Thread(target=choco_packages_upgrade)
winget_packages_to_update = threading.Thread(target=winget_packages_upgrade)

scoop_packages_to_update.start()
choco_packages_to_update.start()
winget_packages_to_update.start()

scoop_packages_to_update.join()
choco_packages_to_update.join()
winget_packages_to_update.join()

# After thats over let's start building the UI


# Launch App

if check_windows_version():

    print('Windows 10 22h2 or newer detected. Launching...')

else:

    print("Not possible to launch, update your Windows instalation")