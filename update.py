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
    
    os.system('scoop update "*"')

    os.system('powershell start-process choco upgrade all -verb runas')

    os.system('winget upgrade --all')
    
    
    time.sleep(5)
    updatewindow.destroy()
    time.sleep(2)

    messagebox.showinfo(title="Packages Updated", message="All apps updated.")
    
    updatewindow = customtkinter.CTk()
    updatewindow.title("Updating Packages")
    updatewindow.geometry(600, 200)
    updatewindow.resizable(False)
    updatelabel = customtkinter.CTkLabel(updatewindow, text="Please wait while we update your apps...")
    updatelabel.pack()
    progressbar = customtkinter.CTkProgressBar(master=updatewindow, mode="indeterminate")
    progressbar.pack()
    progressbar.start()
    updatewindow.after(200, updatepackages)
    progressbar.stop()
    updatewindow.mainloop()

if __name__ == '__main__':

    print('testing')
