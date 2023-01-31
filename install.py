import time
import update
import sys
import tkinter
import customtkinter
import subprocess
import os
import json
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Check for configuration file

wingetlist = os.path.exists('wingetlist.json')
scooplist = os.path.exists('scooplist.json')
chocolist = os.path.exists('chocolist.json')

# Winget import list 

if wingetlist == True:
    winstall = subprocess.Popen('winget import wingetlist.json')
    winstall.wait()
    
# Scoop import List

elif scooplist == True:
    scinstall = subprocess.Popen('scoop import scooplist.json')    
    scinstall.wait()
    
#  Chocolatey import list

elif chocolist == True:
    chocoinstall = subprocess.Popen('choco install chocolist.config')
    chocoinstall.wait()

else:
    time.sleep(0)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("FB Install Tool")
        self.geometry("950x467")

        # set grid layout 1x2

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image

        self.logo_image = customtkinter.CTkLabel(master=self, text="FB Install Tool")

        # create navigation frame

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="FB Install Tool",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Create Frames

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Browsers",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Games",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Messaging",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Office",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Runtimes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

        self.frame_6_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Security",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_6_button_event)
        self.frame_6_button.grid(row=6, column=0, sticky="ew")

        self.frame_7_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Media",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_7_button_event)
        self.frame_7_button.grid(row=7, column=0, sticky="ew")

        self.frame_8_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Utilities",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_8_button_event)
        self.frame_8_button.grid(row=8, column=0, sticky="ew")
        
        self.label1 = customtkinter.CTkLabel(self.navigation_frame, corner_radius=0, height=40, text="Theme:", fg_color="transparent", text_color=("gray10", "gray90"), anchor="w")
        self.label1.grid(row=10, column=0, padx=10, pady=0, sticky="s")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=11, column=0, padx=20, pady=6, sticky="s")

        # create home frame

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # Thing in the Browsers Frame


        self.spacer = customtkinter.CTkLabel(self.home_frame, corner_radius=0, height=40, text=" ", fg_color="transparent", text_color=("gray10", "gray90"), anchor="w")
        self.spacer.grid(row=0, column=0, padx=10, pady=50,)

        self.home_check1 = customtkinter.CTkCheckBox(self.home_frame, text="Brave")
        self.home_check1.grid(row=1, column=0, padx=20, pady=20)
        self.home_check2 = customtkinter.CTkCheckBox(self.home_frame, text="Microsoft Edge")
        self.home_check2.grid(row=1, column=1, padx=20, pady=20)
        self.home_check3 = customtkinter.CTkCheckBox(self.home_frame, text="K Meleon")
        self.home_check3.grid(row=1, column=2, padx=20, pady=20)
        self.home_check4 = customtkinter.CTkCheckBox(self.home_frame, text="Google Chrome")
        self.home_check4.grid(row=1, column=3, padx=20, pady=20)
        self.home_check5 = customtkinter.CTkCheckBox(self.home_frame, text="Vivaldi")
        self.home_check5.grid(row=1, column=4, padx=20, pady=20)
        self.home_check6 = customtkinter.CTkCheckBox(self.home_frame, text="Opera")
        self.home_check6.grid(row=1, column=5, padx=20, pady=20)

        self.home_check7 = customtkinter.CTkCheckBox(self.home_frame, text="Mozilla Firefox")
        self.home_check7.grid(row=2, column=0, padx=20, pady=20)
        self.home_check8 = customtkinter.CTkCheckBox(self.home_frame, text="Librewolf")
        self.home_check8.grid(row=2, column=1, padx=20, pady=20)
        self.home_check9 = customtkinter.CTkCheckBox(self.home_frame, text="Pale Moon")
        self.home_check9.grid(row=2, column=2, padx=20, pady=20)
        self.home_check10 = customtkinter.CTkCheckBox(self.home_frame, text="Waterfox")
        self.home_check10.grid(row=2, column=3, padx=20, pady=20)
        self.home_check11 = customtkinter.CTkCheckBox(self.home_frame, text="Midori")
        self.home_check11.grid(row=2, column=4, padx=20, pady=20)
        self.home_check12 = customtkinter.CTkCheckBox(self.home_frame, text="Opera GX")
        self.home_check12.grid(row=2, column=5, padx=20, pady=20)

        self.spacer2 = customtkinter.CTkLabel(self.home_frame, corner_radius=0, height=40, text=" ", fg_color="transparent", text_color=("gray10", "gray90"), anchor="w")
        self.spacer2.grid(row=3, column=0, padx=10, pady=50,)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Install")
        self.home_frame_button_1.grid(row=4, column=5, padx=20, pady=20)

        # create 2nd frame

        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Things on Games Frame

        self.games_check1 = customtkinter.CTkCheckBox(self.second_frame, text="Retroarch")
        self.games_check1.grid(row=1, column=0, padx=20, pady=20)
        self.games_check2 = customtkinter.CTkCheckBox(self.second_frame, text="Amazon Games")
        self.games_check2.grid(row=1, column=1, padx=20, pady=20)
        self.games_check3 = customtkinter.CTkCheckBox(self.second_frame, text="Ubisoft Connect")
        self.games_check3.grid(row=1, column=2, padx=20, pady=20)
        self.games_check4 = customtkinter.CTkCheckBox(self.second_frame, text="Dolphin Emulator")
        self.games_check4.grid(row=1, column=3, padx=20, pady=20)
        self.games_check5 = customtkinter.CTkCheckBox(self.second_frame, text="RPCS3")
        self.games_check5.grid(row=1, column=4, padx=20, pady=20)
        self.games_check6 = customtkinter.CTkCheckBox(self.second_frame, text="Epic Games Launcher")
        self.games_check6.grid(row=1, column=5, padx=20, pady=20)
        self.games_check7 = customtkinter.CTkCheckBox(self.second_frame, text="PCSX2")
        self.games_check7.grid(row=1, column=6, padx=20, pady=20)

        self.games_check8 = customtkinter.CTkCheckBox(self.second_frame, text="Yuzu")
        self.games_check8.grid(row=2, column=0, padx=20, pady=20)
        self.games_check9 = customtkinter.CTkCheckBox(self.second_frame, text="Heroic Games Launcher")
        self.games_check9.grid(row=2, column=1, padx=20, pady=20)
        self.games_check10 = customtkinter.CTkCheckBox(self.second_frame, text="GOG Galaxy")
        self.games_check10.grid(row=2, column=2, padx=20, pady=20)
        self.games_check11 = customtkinter.CTkCheckBox(self.second_frame, text="Itch.IO")
        self.games_check11.grid(row=2, column=3, padx=20, pady=20)
        self.games_check12 = customtkinter.CTkCheckBox(self.second_frame, text="Minecraft Launcher")
        self.games_check12.grid(row=2, column=4, padx=20, pady=20)
        self.games_check13 = customtkinter.CTkCheckBox(self.second_frame, text="Steam")
        self.games_check13.grid(row=2, column=5, padx=20, pady=20)
        self.games_check14 = customtkinter.CTkCheckBox(self.second_frame, text="EA APP")
        self.games_check14.grid(row=2, column=6, padx=20, pady=20)

        self.games_check15 = customtkinter.CTkCheckBox(self.second_frame, text="GDLauncher")
        self.games_check15.grid(row=3, column=0, padx=20, pady=20)
        self.games_check16 = customtkinter.CTkCheckBox(self.second_frame, text="CurseForge")
        self.games_check16.grid(row=3, column=1, padx=20, pady=20)
        self.games_check17 = customtkinter.CTkCheckBox(self.second_frame, text="Battle.net")
        self.games_check17.grid(row=3, column=2, padx=20, pady=20)
        self.games_check18 = customtkinter.CTkCheckBox(self.second_frame, text="Citra Emulator")
        self.games_check18.grid(row=3, column=3, padx=20, pady=20)
        self.games_check19 = customtkinter.CTkCheckBox(self.second_frame, text="PPSSPP")
        self.games_check19.grid(row=3, column=4, padx=20, pady=20)
        self.games_check20 = customtkinter.CTkCheckBox(self.second_frame, text="Blitz")
        self.games_check20.grid(row=3, column=5, padx=20, pady=20)
        self.games_check21 = customtkinter.CTkCheckBox(self.second_frame, text="Playnite")
        self.games_check21.grid(row=3, column=6, padx=20, pady=20)

        # create 3rd frame

        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Things in Messaging Frame

        self.msg_check1 = customtkinter.CTkCheckBox(self.third_frame, text="Zoom")
        self.msg_check1.grid(row=1, column=0, padx=20, pady=20)
        self.msg_check2 = customtkinter.CTkCheckBox(self.third_frame, text="Guilded")
        self.msg_check2.grid(row=1, column=1, padx=20, pady=20)
        self.msg_check3 = customtkinter.CTkCheckBox(self.third_frame, text="Slack")
        self.msg_check3.grid(row=1, column=2, padx=20, pady=20)
        self.msg_check4 = customtkinter.CTkCheckBox(self.third_frame, text="HexChat")
        self.msg_check4.grid(row=1, column=3, padx=20, pady=20)
        self.msg_check5 = customtkinter.CTkCheckBox(self.third_frame, text="Skype")
        self.msg_check5.grid(row=1, column=4, padx=20, pady=20)
        self.msg_check6 = customtkinter.CTkCheckBox(self.third_frame, text="Discord")
        self.msg_check6.grid(row=1, column=5, padx=20, pady=20)

        self.msg_check7 = customtkinter.CTkCheckBox(self.third_frame, text="TeamSpeak 3")
        self.msg_check7.grid(row=2, column=0, padx=20, pady=20)
        self.msg_check8 = customtkinter.CTkCheckBox(self.third_frame, text="Telegram")
        self.msg_check8.grid(row=2, column=1, padx=20, pady=20)
        self.msg_check9 = customtkinter.CTkCheckBox(self.third_frame, text="WhatsApp")
        self.msg_check9.grid(row=2, column=2, padx=20, pady=20)
        self.msg_check10 = customtkinter.CTkCheckBox(self.third_frame, text="Viber")
        self.msg_check10.grid(row=2, column=3, padx=20, pady=20)
        self.msg_check11 = customtkinter.CTkCheckBox(self.third_frame, text="Microsoft Teams")
        self.msg_check11.grid(row=2, column=4, padx=20, pady=20)
        self.msg_check12 = customtkinter.CTkCheckBox(self.third_frame, text="Signal")
        self.msg_check12.grid(row=2, column=5, padx=20, pady=20)

        # create 4th frame

        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Things in the Office frame

        self.office_check1 = customtkinter.CTkCheckBox(self.fourth_frame, text="Sedja PDF")
        self.office_check1.grid(row=1, column=0, padx=20, pady=20)
        self.office_check2 = customtkinter.CTkCheckBox(self.fourth_frame, text="Sumatra PDF")
        self.office_check2.grid(row=1, column=1, padx=20, pady=20)
        self.office_check3 = customtkinter.CTkCheckBox(self.fourth_frame, text="Adobe Reader")
        self.office_check3.grid(row=1, column=2, padx=20, pady=20)
        self.office_check4 = customtkinter.CTkCheckBox(self.fourth_frame, text="WPS Office")
        self.office_check4.grid(row=1, column=3, padx=20, pady=20)
        self.office_check5 = customtkinter.CTkCheckBox(self.fourth_frame, text="Master PDF Editor")
        self.office_check5.grid(row=1, column=4, padx=20, pady=20)
        self.office_check6 = customtkinter.CTkCheckBox(self.fourth_frame, text="Foxit Reader")
        self.office_check6.grid(row=1, column=5, padx=20, pady=20)

        self.office_check7 = customtkinter.CTkCheckBox(self.fourth_frame, text="LibreOffice")
        self.office_check7.grid(row=2, column=0, padx=20, pady=20)
        self.office_check8 = customtkinter.CTkCheckBox(self.fourth_frame, text="OpenOffice")
        self.office_check8.grid(row=2, column=1, padx=20, pady=20)
        self.office_check9 = customtkinter.CTkCheckBox(self.fourth_frame, text="Kingsoft Office")
        self.office_check9.grid(row=2, column=2, padx=20, pady=20)
        self.office_check10 = customtkinter.CTkCheckBox(self.fourth_frame, text="FreeOffice")
        self.office_check10.grid(row=2, column=3, padx=20, pady=20)
        self.office_check11 = customtkinter.CTkCheckBox(self.fourth_frame, text="OnlyOffice")
        self.office_check11.grid(row=2, column=4, padx=20, pady=20)
        self.office_check12 = customtkinter.CTkCheckBox(self.fourth_frame, text="MS Office 365")
        self.office_check12.grid(row=2, column=5, padx=20, pady=20)

        # create 5th frame

        self.f_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in the Runtime frame
        
        self.run_check1 = customtkinter.CTkCheckBox(self.f_frame, text="VCRedist")
        self.run_check1.grid(row=1, column=0, padx=20, pady=20)
        self.run_check2 = customtkinter.CTkCheckBox(self.f_frame, text=".Net")
        self.run_check2.grid(row=1, column=1, padx=20, pady=20)
        self.run_check3 = customtkinter.CTkCheckBox(self.f_frame, text="Java Runtime Environment")
        self.run_check3.grid(row=1, column=2, padx=20, pady=20)
        self.run_check4 = customtkinter.CTkCheckBox(self.f_frame, text="OpenJDK (Latest)")
        self.run_check4.grid(row=1, column=3, padx=20, pady=20)
        self.run_check5 = customtkinter.CTkCheckBox(self.f_frame, text="OpenJDK 8")
        self.run_check5.grid(row=1, column=4, padx=20, pady=20)
        self.run_check6 = customtkinter.CTkCheckBox(self.f_frame, text="DirectX")
        self.run_check6.grid(row=1, column=5, padx=20, pady=20)

        # create 6th frame

        self.s_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in the Security Frame
        
        self.sec_check1 = customtkinter.CTkCheckBox(self.s_frame, text="AuthMe")
        self.sec_check1.grid(row=1, column=0, padx=20, pady=20)
        self.sec_check2 = customtkinter.CTkCheckBox(self.s_frame, text="Authy")
        self.sec_check2.grid(row=1, column=1, padx=20, pady=20)
        self.sec_check3 = customtkinter.CTkCheckBox(self.s_frame, text="Password Hub")
        self.sec_check3.grid(row=1, column=2, padx=20, pady=20)
        self.sec_check4 = customtkinter.CTkCheckBox(self.s_frame, text="2fast")
        self.sec_check4.grid(row=1, column=3, padx=20, pady=20)
        self.sec_check5 = customtkinter.CTkCheckBox(self.s_frame, text="Yubico Authenticator")
        self.sec_check5.grid(row=1, column=4, padx=20, pady=20)
        self.sec_check6 = customtkinter.CTkCheckBox(self.s_frame, text="Bitwarden")
        self.sec_check6.grid(row=1, column=5, padx=20, pady=20)

        self.sec_check7 = customtkinter.CTkCheckBox(self.s_frame, text="Keepass")
        self.sec_check7.grid(row=2, column=0, padx=20, pady=20)
        self.sec_check8 = customtkinter.CTkCheckBox(self.s_frame, text="Password Safe")
        self.sec_check8.grid(row=2, column=1, padx=20, pady=20)
        self.sec_check9 = customtkinter.CTkCheckBox(self.s_frame, text="Dashlane")
        self.sec_check9.grid(row=2, column=2, padx=20, pady=20)
        self.sec_check10 = customtkinter.CTkCheckBox(self.s_frame, text="Panda Free Antivirus")
        self.sec_check10.grid(row=2, column=3, padx=20, pady=20)
        self.sec_check11 = customtkinter.CTkCheckBox(self.s_frame, text="Adw Cleaner")
        self.sec_check11.grid(row=2, column=4, padx=20, pady=20)
        self.sec_check12 = customtkinter.CTkCheckBox(self.s_frame, text="CalmAV")
        self.sec_check12.grid(row=2, column=5, padx=20, pady=20)

        # create 7th frame

        self.seven_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in Media Frame
        
        self.media_check1 = customtkinter.CTkCheckBox(self.seven_frame, text="VLC")
        self.media_check1.grid(row=1, column=0, padx=20, pady=20)
        self.media_check2 = customtkinter.CTkCheckBox(self.seven_frame, text="Cider")
        self.media_check2.grid(row=1, column=1, padx=20, pady=20)
        self.media_check3 = customtkinter.CTkCheckBox(self.seven_frame, text="Gom Player")
        self.media_check3.grid(row=1, column=2, padx=20, pady=20)
        self.media_check4 = customtkinter.CTkCheckBox(self.seven_frame, text="Filmora")
        self.media_check4.grid(row=1, column=3, padx=20, pady=20)
        self.media_check5 = customtkinter.CTkCheckBox(self.seven_frame, text="Tidal")
        self.media_check5.grid(row=1, column=4, padx=20, pady=20)
        self.media_check6 = customtkinter.CTkCheckBox(self.seven_frame, text="Audacium")
        self.media_check6.grid(row=1, column=5, padx=20, pady=20)

        self.media_check7 = customtkinter.CTkCheckBox(self.seven_frame, text="MyPaint")
        self.media_check7.grid(row=2, column=0, padx=20, pady=20)
        self.media_check8 = customtkinter.CTkCheckBox(self.seven_frame, text="Audacity")
        self.media_check8.grid(row=2, column=1, padx=20, pady=20)
        self.media_check9 = customtkinter.CTkCheckBox(self.seven_frame, text="Deezer")
        self.media_check9.grid(row=2, column=2, padx=20, pady=20)
        self.media_check10 = customtkinter.CTkCheckBox(self.seven_frame, text="Spotify")
        self.media_check10.grid(row=2, column=3, padx=20, pady=20)
        self.media_check11 = customtkinter.CTkCheckBox(self.seven_frame, text="iTunes")
        self.media_check11.grid(row=2, column=4, padx=20, pady=20)
        self.media_check12 = customtkinter.CTkCheckBox(self.seven_frame, text="Clementine")
        self.media_check12.grid(row=2, column=5, padx=20, pady=20)
        
        self.media_check13 = customtkinter.CTkCheckBox(self.seven_frame, text="Handbrake")
        self.media_check13.grid(row=3, column=0, padx=20, pady=20)
        self.media_check14 = customtkinter.CTkCheckBox(self.seven_frame, text="KDEnLive")
        self.media_check14.grid(row=3, column=1, padx=20, pady=20)
        self.media_check15 = customtkinter.CTkCheckBox(self.seven_frame, text="MPV")
        self.media_check15.grid(row=3, column=2, padx=20, pady=20)
        self.media_check16 = customtkinter.CTkCheckBox(self.seven_frame, text="Pot Player")
        self.media_check16.grid(row=3, column=3, padx=20, pady=20)
        self.media_check17 = customtkinter.CTkCheckBox(self.seven_frame, text="Paint.Net")
        self.media_check17.grid(row=3, column=4, padx=20, pady=20)
        self.media_check18 = customtkinter.CTkCheckBox(self.seven_frame, text="Krita")
        self.media_check18.grid(row=3, column=5, padx=20, pady=20)

        self.media_check19 = customtkinter.CTkCheckBox(self.seven_frame, text="Tux Paint")
        self.media_check19.grid(row=4, column=0, padx=20, pady=20)
        self.media_check20 = customtkinter.CTkCheckBox(self.seven_frame, text="GIMP")
        self.media_check20.grid(row=4, column=1, padx=20, pady=20)
        self.media_check21 = customtkinter.CTkCheckBox(self.seven_frame, text="Glimpse")
        self.media_check21.grid(row=4, column=2, padx=20, pady=20)
        self.media_check22 = customtkinter.CTkCheckBox(self.seven_frame, text="PhotoGIMP")
        self.media_check22.grid(row=4, column=3, padx=20, pady=20)
        self.media_check23 = customtkinter.CTkCheckBox(self.seven_frame, text="Upscay!")
        self.media_check23.grid(row=4, column=4, padx=20, pady=20)
        self.media_check24 = customtkinter.CTkCheckBox(self.seven_frame, text="ImageGlass")
        self.media_check24.grid(row=4, column=5, padx=20, pady=20)


        # create 8th frame

        self.eight_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things on Utilities Frame
        self.utils_check1 = customtkinter.CTkCheckBox(self.eight_frame, text="WinZip")
        self.utils_check1.grid(row=1, column=0, padx=20, pady=20)
        self.utils_check2 = customtkinter.CTkCheckBox(self.eight_frame, text="Flameshot")
        self.utils_check2.grid(row=1, column=1, padx=20, pady=20)
        self.utils_check3 = customtkinter.CTkCheckBox(self.eight_frame, text="Notepad++")
        self.utils_check3.grid(row=1, column=2, padx=20, pady=20)
        self.utils_check4 = customtkinter.CTkCheckBox(self.eight_frame, text="PeaZip")
        self.utils_check4.grid(row=1, column=3, padx=20, pady=20)
        self.utils_check5 = customtkinter.CTkCheckBox(self.eight_frame, text="Atom")
        self.utils_check5.grid(row=1, column=4, padx=20, pady=20)
        self.utils_check6 = customtkinter.CTkCheckBox(self.eight_frame, text="ShareX")
        self.utils_check6.grid(row=1, column=5, padx=20, pady=20)

        self.utils_check7 = customtkinter.CTkCheckBox(self.eight_frame, text="Trello Desktop")
        self.utils_check7.grid(row=2, column=0, padx=20, pady=20)
        self.utils_check8 = customtkinter.CTkCheckBox(self.eight_frame, text="7-Zip")
        self.utils_check8.grid(row=2, column=1, padx=20, pady=20)
        self.utils_check9 = customtkinter.CTkCheckBox(self.eight_frame, text="Sublime Text")
        self.utils_check9.grid(row=2, column=2, padx=20, pady=20)
        self.utils_check10 = customtkinter.CTkCheckBox(self.eight_frame, text="Evernote")
        self.utils_check10.grid(row=2, column=3, padx=20, pady=20)
        self.utils_check11 = customtkinter.CTkCheckBox(self.eight_frame, text="Notion")
        self.utils_check11.grid(row=2, column=4, padx=20, pady=20)
        self.utils_check12 = customtkinter.CTkCheckBox(self.eight_frame, text="Winrar")
        self.utils_check12.grid(row=2, column=5, padx=20, pady=20)
        
        self.utils_check13 = customtkinter.CTkCheckBox(self.eight_frame, text="VS Code")
        self.utils_check13.grid(row=3, column=0, padx=20, pady=20)
        self.utils_check14 = customtkinter.CTkCheckBox(self.eight_frame, text="IMGBurn")
        self.utils_check14.grid(row=3, column=1, padx=20, pady=20)
        self.utils_check15 = customtkinter.CTkCheckBox(self.eight_frame, text="Powertoys")
        self.utils_check15.grid(row=3, column=2, padx=20, pady=20)
        self.utils_check16 = customtkinter.CTkCheckBox(self.eight_frame, text="Sysinternals Suite")
        self.utils_check16.grid(row=3, column=3, padx=20, pady=20)
        self.utils_check17 = customtkinter.CTkCheckBox(self.eight_frame, text="Teracopy")
        self.utils_check17.grid(row=3, column=4, padx=20, pady=20)
        self.utils_check18 = customtkinter.CTkCheckBox(self.eight_frame, text="ADB")
        self.utils_check18.grid(row=3, column=5, padx=20, pady=20)
        
        # select default frame

        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):

        # set button color for selected button

        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")
        self.frame_6_button.configure(fg_color=("gray75", "gray25") if name == "frame_6" else "transparent")
        self.frame_7_button.configure(fg_color=("gray75", "gray25") if name == "frame_7" else "transparent")
        self.frame_8_button.configure(fg_color=("gray75", "gray25") if name == "frame_8" else "transparent")

        # show selected frame

        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "frame_5":
            self.f_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.f_frame.grid_forget()
        if name == "frame_6":
            self.s_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.s_frame.grid_forget()
        if name == "frame_7":
            self.seven_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.seven_frame.grid_forget()
        if name == "frame_8":
            self.eight_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.eight_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def frame_6_button_event(self):
        self.select_frame_by_name("frame_6")

    def frame_7_button_event(self):
        self.select_frame_by_name("frame_7")

    def frame_8_button_event(self):
        self.select_frame_by_name("frame_8")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
