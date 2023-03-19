import tkinter # Needed to use customtkinter
from tkinter import messagebox
import customtkinter
import time
import os

# Update Window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


# Update function

def updatepackages():
    
    scoopupdating = os.popen('scoop update "*"')
    scoopupdating.read()

    chocoupdating = os.popen('powershell start-process choco upgrade all -verb runas')
    chocoupdating.read()

    wingetupdating = os.popen('winget upgrade --all')
    wingetupdating.read()

    time.sleep(5)
    upd.destroy()
    time.sleep(2)

    messagebox.showinfo(title="Packages Updated", message="All apps updated.")

if __name__ == '__main__':

    upd = customtkinter.CTk()
    upd.title("Updating Packages")
    upd.geometry(600, 200)
    upd.resizable(False)
    updlabel = customtkinter.CTkLabel(upd, text="Please wait while we update your apps...")
    updlabel.pack()
    progbar = customtkinter.CTkProgressBar(master=upd, mode="indeterminate")
    progbar.pack()
    progbar.start()
    upd.after(200, updatepackages)
    progbar.stop()
    upd.mainloop()
