import platform
from tkinter import messagebox
import customtkinter
import os
from pyuac import main_requires_admin
import time
import install

# Basic variables

thispc = platform.system()
thispcver = platform.release()
username = os.getlogin()
appdata = os.getenv('APPDATA')
userfolder = str(os.path.home())
packagemanagers = ['scoop', 'chocolatey', 'winget']
packagemanagerbins = ['scoopinstalldir', 'chocoinstalldir', 'wingetinstalldir']
installedscoop = os.path.exists(packagemanagers[0])
installedchoco = os.path.exists(packagemanagers[1])
installedwinget = os.path.exists(packagemanagers[2])

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
errormsg = customtkinter.CTk()
errormsg.title("Error")
errormsg.geometry(600, 200)

def leave():
    errormsg.destroy()

# Check where this software is running

if thispc == 'Windows':

    # Now check what version of Windows this software is running

    if thispcver >= 10:

        # Privilege Elevation on Windows

        @main_requires_admin
        def main():
            install()
            # The window will disappear as soon as the program exits!
            time.sleep(3)

    else:

        # Old Windows versions
        
        msg = 'It seems like your windows version is too old, ' + username + ', Update your Windows First.'
        oldwin = customtkinter.CTkLabel(master=errormsg, text=msg)
        oldwin.pack()
        btn = customtkinter.CTkButton(master=errormsg, text="OK", command=leave)
        
else:
    # Error message to avoid the need to create exceptions for other systems
    java = customtkinter.CTkLabel(master=errormsg, text="This OS is not supported.")
    java.pack()
    btn = customtkinter.CTkButton(master=errormsg, text="OK", command=leave)
    


if __name__ == "__main__":
    main()
