#!/usr/bin/env python

import tkinter
from tkinter import messagebox
import customtkinter
import time
import subprocess

# Update Window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


# Update function

def updatepackages():
    
    scoopupdating = subprocess.Popen('scoop update "*"', shell=True)
    scoopupdating.wait()

    chocoupdating = subprocess.Popen('choco upgrade all', shell=True)
    chocoupdating.wait()

    wingetupdating = subprocess.Popen('winget upgrade --all', shell=True)
    wingetupdating.wait()

    time.sleep(5)
    upd.destroy()
    time.sleep(2)

    messagebox.showinfo(title="Packages Updated", message="All apps updated.")

if __name__ == '__main__':

    upd = customtkinter.CTk()
    upd.title("Updating Packages")
    upd.geometry(600, 200)
    updlabel = customtkinter.CTkLabel(upd, text="Please wait while we update your apps...")
    updlabel.pack()
    progbar = customtkinter.CTkProgressBar(master=upd, mode="indeterminate")
    progbar.pack()
    progbar.start()
    upd.after(200, updatepackages)
    progbar.stop()
    upd.mainloop()
