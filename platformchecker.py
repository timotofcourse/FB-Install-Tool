import platform
import tkinter # Needed to use customtkinter
import customtkinter
import os

# Basic variables

thispc = platform.system()
thispcver = platform.release()
username = os.getlogin()
appdata = os.getenv('APPDATA')
userfolder = str(os.path.home())
packagemanagers = ['scoop', 'chocolatey', 'winget']
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
errormessage = customtkinter.CTk()
errormessage.title("Error")
errormessage.geometry(600, 200)
errormessage.resizable(False, False)

def leave():
    errormessage.destroy()

# Check where this software is running

def checkplatform():
    
    if thispc != 'Windows':

        otheros = customtkinter.CTkLabel(master=errormessage, text="This OS is not supported.")
        otheros.pack()
        okbutton = customtkinter.CTkButton(master=errormessage, text="OK", command=leave)
        okbutton.pack()
        
    elif thispc == 'Windows':

        # Now check what version of Windows this software is running

        if thispcver < 10:

            # Old Windows versions
        
            msg = 'It seems like your windows version is too old, ' + username + ', Update your Windows First.'
            oldwin = customtkinter.CTkLabel(master=errormessage, text=msg)
            oldwin.pack()
            okbutton = customtkinter.CTkButton(master=errormessage, text="OK", command=leave)
            okbutton.pack()
        

def checkpms(packagemanager):
    if packagemanager == 'scoop':
        if os.path.exists(userfolder + '/scoop'):
            pass
        else:
            pass
        pass
    elif packagemanager == 'choco':
        if os.path.exists('C:/ProgramData/Chocolatey'):
            pass
        else:
            pass
        pass
    else:
        pass
    
