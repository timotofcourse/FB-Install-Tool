import time
import update
import sys
import tkinter
from tkinter import messagebox
import customtkinter
import subprocess
import os
import json
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



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
        
        self.run_check1 = customtkinter.CTkCheckBox(self.home_frame, text="VCRedist")
        self.run_check1.grid(row=1, column=0, padx=20, pady=20)
        self.run_check2 = customtkinter.CTkCheckBox(self.home_frame, text=".Net")
        self.run_check2.grid(row=1, column=1, padx=20, pady=20)
        self.run_check3 = customtkinter.CTkCheckBox(self.home_frame, text="Java Runtime Environment")
        self.run_check3.grid(row=1, column=2, padx=20, pady=20)
        self.run_check4 = customtkinter.CTkCheckBox(self.home_frame, text="OpenJDK (Latest)")
        self.run_check4.grid(row=1, column=3, padx=20, pady=20)
        self.run_check5 = customtkinter.CTkCheckBox(self.home_frame, text="OpenJDK 8")
        self.run_check5.grid(row=1, column=4, padx=20, pady=20)
        self.run_check6 = customtkinter.CTkCheckBox(self.home_frame, text="DirectX")
        self.run_check6.grid(row=1, column=5, padx=20, pady=20)

        # create 6th frame

        self.s_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in the Security Frame
        
        self.sec_check1 = customtkinter.CTkCheckBox(self.home_frame, text="AuthMe")
        self.sec_check1.grid(row=1, column=0, padx=20, pady=20)
        self.sec_check2 = customtkinter.CTkCheckBox(self.home_frame, text="Authy")
        self.sec_check2.grid(row=1, column=1, padx=20, pady=20)
        self.sec_check3 = customtkinter.CTkCheckBox(self.home_frame, text="Password Hub")
        self.sec_check3.grid(row=1, column=2, padx=20, pady=20)
        self.sec_check4 = customtkinter.CTkCheckBox(self.home_frame, text="2fast")
        self.sec_check4.grid(row=1, column=3, padx=20, pady=20)
        self.sec_check5 = customtkinter.CTkCheckBox(self.home_frame, text="Yubico Authenticator")
        self.sec_check5.grid(row=1, column=4, padx=20, pady=20)
        self.sec_check6 = customtkinter.CTkCheckBox(self.home_frame, text="Bitwarden")
        self.sec_check6.grid(row=1, column=5, padx=20, pady=20)

        self.sec_check7 = customtkinter.CTkCheckBox(self.home_frame, text="Keepass")
        self.sec_check7.grid(row=2, column=0, padx=20, pady=20)
        self.sec_check8 = customtkinter.CTkCheckBox(self.home_frame, text="Password Safe")
        self.sec_check8.grid(row=2, column=1, padx=20, pady=20)
        self.sec_check9 = customtkinter.CTkCheckBox(self.home_frame, text="Dashlane")
        self.sec_check9.grid(row=2, column=2, padx=20, pady=20)
        self.sec_check10 = customtkinter.CTkCheckBox(self.home_frame, text="Panda Free Antivirus")
        self.sec_check10.grid(row=2, column=3, padx=20, pady=20)
        self.sec_check11 = customtkinter.CTkCheckBox(self.home_frame, text="Adw Cleaner")
        self.sec_check11.grid(row=2, column=4, padx=20, pady=20)
        self.sec_check12 = customtkinter.CTkCheckBox(self.home_frame, text="CalmAV")
        self.sec_check12.grid(row=2, column=5, padx=20, pady=20)

        # create 7th frame

        self.seven_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in Media Frame
        
        self.media_check1 = customtkinter.CTkCheckBox(self.home_frame, text="VLC")
        self.media_check1.grid(row=1, column=0, padx=20, pady=20)
        self.media_check2 = customtkinter.CTkCheckBox(self.home_frame, text="Cider")
        self.media_check2.grid(row=1, column=1, padx=20, pady=20)
        self.media_check3 = customtkinter.CTkCheckBox(self.home_frame, text="Gom Player")
        self.media_check3.grid(row=1, column=2, padx=20, pady=20)
        self.media_check4 = customtkinter.CTkCheckBox(self.home_frame, text="Filmora")
        self.media_check4.grid(row=1, column=3, padx=20, pady=20)
        self.media_check5 = customtkinter.CTkCheckBox(self.home_frame, text="Tidal")
        self.media_check5.grid(row=1, column=4, padx=20, pady=20)
        self.media_check6 = customtkinter.CTkCheckBox(self.home_frame, text="Audacium")
        self.media_check6.grid(row=1, column=5, padx=20, pady=20)

        self.media_check7 = customtkinter.CTkCheckBox(self.home_frame, text="MyPaint")
        self.media_check7.grid(row=2, column=0, padx=20, pady=20)
        self.media_check8 = customtkinter.CTkCheckBox(self.home_frame, text="Audacity")
        self.media_check8.grid(row=2, column=1, padx=20, pady=20)
        self.media_check9 = customtkinter.CTkCheckBox(self.home_frame, text="Deezer")
        self.media_check9.grid(row=2, column=2, padx=20, pady=20)
        self.media_check10 = customtkinter.CTkCheckBox(self.home_frame, text="Spotify")
        self.media_check10.grid(row=2, column=3, padx=20, pady=20)
        self.media_check11 = customtkinter.CTkCheckBox(self.home_frame, text="iTunes")
        self.media_check11.grid(row=2, column=4, padx=20, pady=20)
        self.media_check12 = customtkinter.CTkCheckBox(self.home_frame, text="Clementine")
        self.media_check12.grid(row=2, column=5, padx=20, pady=20)
        
        self.media_check13 = customtkinter.CTkCheckBox(self.home_frame, text="Handbrake")
        self.media_check13.grid(row=3, column=0, padx=20, pady=20)
        self.media_check14 = customtkinter.CTkCheckBox(self.home_frame, text="KDEnLive")
        self.media_check14.grid(row=3, column=1, padx=20, pady=20)
        self.media_check15 = customtkinter.CTkCheckBox(self.home_frame, text="MPV")
        self.media_check15.grid(row=3, column=2, padx=20, pady=20)
        self.media_check16 = customtkinter.CTkCheckBox(self.home_frame, text="Pot Player")
        self.media_check16.grid(row=3, column=3, padx=20, pady=20)
        self.media_check17 = customtkinter.CTkCheckBox(self.home_frame, text="Paint.Net")
        self.media_check17.grid(row=3, column=4, padx=20, pady=20)
        self.media_check18 = customtkinter.CTkCheckBox(self.home_frame, text="Krita")
        self.media_check18.grid(row=3, column=5, padx=20, pady=20)

        self.media_check19 = customtkinter.CTkCheckBox(self.home_frame, text="Tux Paint")
        self.media_check19.grid(row=4, column=0, padx=20, pady=20)
        self.media_check20 = customtkinter.CTkCheckBox(self.home_frame, text="GIMP")
        self.media_check20.grid(row=4, column=1, padx=20, pady=20)
        self.media_check21 = customtkinter.CTkCheckBox(self.home_frame, text="Glimpse")
        self.media_check21.grid(row=4, column=2, padx=20, pady=20)
        self.media_check22 = customtkinter.CTkCheckBox(self.home_frame, text="PhotoGIMP")
        self.media_check22.grid(row=4, column=3, padx=20, pady=20)
        self.media_check23 = customtkinter.CTkCheckBox(self.home_frame, text="Upscay!")
        self.media_check23.grid(row=4, column=4, padx=20, pady=20)
        self.media_check24 = customtkinter.CTkCheckBox(self.home_frame, text="ImageGlass")
        self.media_check24.grid(row=4, column=5, padx=20, pady=20)

                   

        # create 8th frame

        self.eight_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things on Utilities Frame
        self.utils_check1 = customtkinter.CTkCheckBox(self.home_frame, text="WinZip")
        self.utils_check1.grid(row=1, column=0, padx=20, pady=20)
        self.utils_check2 = customtkinter.CTkCheckBox(self.home_frame, text="Flameshot")
        self.utils_check2.grid(row=1, column=1, padx=20, pady=20)
        self.utils_check3 = customtkinter.CTkCheckBox(self.home_frame, text="Notepad++")
        self.utils_check3.grid(row=1, column=2, padx=20, pady=20)
        self.utils_check4 = customtkinter.CTkCheckBox(self.home_frame, text="PeaZip")
        self.utils_check4.grid(row=1, column=3, padx=20, pady=20)
        self.utils_check5 = customtkinter.CTkCheckBox(self.home_frame, text="Atom")
        self.utils_check5.grid(row=1, column=4, padx=20, pady=20)
        self.utils_check6 = customtkinter.CTkCheckBox(self.home_frame, text="ShareX")
        self.utils_check6.grid(row=1, column=5, padx=20, pady=20)

        self.utils_check7 = customtkinter.CTkCheckBox(self.home_frame, text="Trello Desktop")
        self.utils_check7.grid(row=2, column=0, padx=20, pady=20)
        self.utils_check8 = customtkinter.CTkCheckBox(self.home_frame, text="7-Zip")
        self.utils_check8.grid(row=2, column=1, padx=20, pady=20)
        self.utils_check9 = customtkinter.CTkCheckBox(self.home_frame, text="Sublime Text")
        self.utils_check9.grid(row=2, column=2, padx=20, pady=20)
        self.utils_check10 = customtkinter.CTkCheckBox(self.home_frame, text="Evernote")
        self.utils_check10.grid(row=2, column=3, padx=20, pady=20)
        self.utils_check11 = customtkinter.CTkCheckBox(self.home_frame, text="Notion")
        self.utils_check11.grid(row=2, column=4, padx=20, pady=20)
        self.utils_check12 = customtkinter.CTkCheckBox(self.home_frame, text="Winrar")
        self.utils_check12.grid(row=2, column=5, padx=20, pady=20)
        
        self.utils_check13 = customtkinter.CTkCheckBox(self.home_frame, text="VS Code")
        self.utils_check13.grid(row=3, column=0, padx=20, pady=20)
        self.utils_check14 = customtkinter.CTkCheckBox(self.home_frame, text="IMGBurn")
        self.utils_check14.grid(row=3, column=1, padx=20, pady=20)
        self.utils_check15 = customtkinter.CTkCheckBox(self.home_frame, text="Powertoys")
        self.utils_check15.grid(row=3, column=2, padx=20, pady=20)
        self.utils_check16 = customtkinter.CTkCheckBox(self.home_frame, text="Sysinternals Suite")
        self.utils_check16.grid(row=3, column=3, padx=20, pady=20)
        self.utils_check17 = customtkinter.CTkCheckBox(self.home_frame, text="Teracopy")
        self.utils_check17.grid(row=3, column=4, padx=20, pady=20)
        self.utils_check18 = customtkinter.CTkCheckBox(self.home_frame, text="ADB")
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


#####################
#####################
#####################
#####################
#####################

# Lists to use later and to be imported on installing.py

scooppackages = []
chocopackages = []
wingetpackages = []
winchecks = []

if os.path.exists('windowspackages.json'):
    configpresent = True
else:
    time.sleep(0)


    if __name__ == "__main__":

        # Launch UI

        class Ui(QtWidgets.QMainWindow):
            def __init__(main):
                super(Ui, main).__init__()
                uic.loadUi('installer.ui', main)
                
                # Funcition to make the button work as it should

                def installpackages():
                    
                    # Add all checkboxes to a list to make it easier to check whitch checkboxes are checked
                     
                    winchecks.append(main.brave)
                    winchecks.append(main.edge)
                    winchecks.append(main.kmeleon)
                    winchecks.append(main.chrome)
                    winchecks.append(main.vivaldi)
                    winchecks.append(main.opera)
                    winchecks.append(main.firefox)
                    winchecks.append(main.librewolf)
                    winchecks.append(main.palemoon)
                    winchecks.append(main.waterfox)
                    winchecks.append(main.midori)
                    winchecks.append(main.operagx)
                    winchecks.append(main.retroarch)
                    winchecks.append(main.amazongames)
                    winchecks.append(main.ubi)
                    winchecks.append(main.dolphin)
                    winchecks.append(main.rpcs3)
                    winchecks.append(main.epic)
                    winchecks.append(main.pcsx2)
                    winchecks.append(main.yuzu)
                    winchecks.append(main.heroic)
                    winchecks.append(main.gog)
                    winchecks.append(main.itch)
                    winchecks.append(main.minecraft)
                    winchecks.append(main.steam)
                    winchecks.append(main.eaapp)
                    winchecks.append(main.gdlauncher)
                    winchecks.append(main.curseforge)
                    winchecks.append(main.battlenet)
                    winchecks.append(main.citra)
                    winchecks.append(main.ppsspp)
                    winchecks.append(main.blitz)
                    winchecks.append(main.playnite)
                    winchecks.append(main.zoom)
                    winchecks.append(main.guilded)
                    winchecks.append(main.slack)
                    winchecks.append(main.hexchat)
                    winchecks.append(main.skype)
                    winchecks.append(main.discord)
                    winchecks.append(main.teamspeak)
                    winchecks.append(main.telegram)
                    winchecks.append(main.whatsapp)
                    winchecks.append(main.viber)
                    winchecks.append(main.teams)
                    winchecks.append(main.signal)
                    winchecks.append(main.sejda)
                    winchecks.append(main.sumatra)
                    winchecks.append(main.acrobatreader)
                    winchecks.append(main.wps)
                    winchecks.append(main.masterpdf)
                    winchecks.append(main.foxit)
                    winchecks.append(main.libreoffice)
                    winchecks.append(main.openoffice)
                    winchecks.append(main.kingsoft)
                    winchecks.append(main.softmaker)
                    winchecks.append(main.onlyoffice)
                    winchecks.append(main.microsoftoffice)
                    winchecks.append(main.vcredist)
                    winchecks.append(main.dotnet7)
                    winchecks.append(main.java8)
                    winchecks.append(main.openjdk)
                    winchecks.append(main.openjdk8)
                    winchecks.append(main.directx)
                    winchecks.append(main.authme)
                    winchecks.append(main.authy)
                    winchecks.append(main.passwordhub)
                    winchecks.append(main.toofast)
                    winchecks.append(main.yubico)
                    winchecks.append(main.bitwarden)
                    winchecks.append(main.keepass)
                    winchecks.append(main.passwordsafe)
                    winchecks.append(main.dashlane)
                    winchecks.append(main.panda)
                    winchecks.append(main.adwcleaner)
                    winchecks.append(main.clamav)
                    winchecks.append(main.vlc)
                    winchecks.append(main.cider)
                    winchecks.append(main.gom)
                    winchecks.append(main.filmora)
                    winchecks.append(main.tidal)
                    winchecks.append(main.audacium)
                    winchecks.append(main.mypaint)
                    winchecks.append(main.audacity)
                    winchecks.append(main.deezer)
                    winchecks.append(main.spotify)
                    winchecks.append(main.itunes)
                    winchecks.append(main.clementine)
                    winchecks.append(main.handbrake)
                    winchecks.append(main.kdenlive)
                    winchecks.append(main.mpv)
                    winchecks.append(main.potplayer)
                    winchecks.append(main.paintdotnet)
                    winchecks.append(main.krita)
                    winchecks.append(main.tuxpaint)
                    winchecks.append(main.gimp)
                    winchecks.append(main.glimpse)
                    winchecks.append(main.photogimp)
                    winchecks.append(main.upscay)
                    winchecks.append(main.imageglass)
                    winchecks.append(main.winzip)
                    winchecks.append(main.flameshot)
                    winchecks.append(main.notepad)
                    winchecks.append(main.peazip)
                    winchecks.append(main.atom)
                    winchecks.append(main.sharex)
                    winchecks.append(main.tello)
                    winchecks.append(main.sevenzip)
                    winchecks.append(main.sublime)
                    winchecks.append(main.evernote)
                    winchecks.append(main.notion)
                    winchecks.append(main.winrar)
                    winchecks.append(main.vscode)
                    winchecks.append(main.imgburn)
                    winchecks.append(main.powertoys)
                    winchecks.append(main.sysinternals)
                    winchecks.append(main.teracopy)
                    winchecks.append(main.adb)

                    # Check witch checkboxes are checked or not and if no checkbox is checked give user an erros message

                    if winchecks[0:-1].ischecked == False:

                        messagebox.showinfo(title="Nothing Selected", message="You did not selected any box. \n Select what you want to install first.")


                    ### Installing process
                    # Variables 
                    completescooppackages = 'scoop install ' + scooppackages
                    completeschocopackages = 'choco install ' + chocopackages
                    completewingetpackages = 'winget install -e --id ' + wingetpackages[0]
                    bucketlist = ['extras', 'versions', 'games', 'nonportable', 'java'] # extra buckets for scoop

                    # Install git with scoop

                    gitinstall = subprocess.Popen('scoop install git')
                    gitinstall.wait()

                    
                    # For loop to add buckets

                    for i in range:
                        completebucketlist = 'scoop bucket add ' + bucketlist[0]
                        bucketlist.pop(0)
                        time.sleep(3)

                    for i in range:
                        addbuckets = subprocess.Popen(completebucketlist, shell=True)
                        addbuckets.wait()
                        completebucketlist.pop(0)
                    
                    # Scoop Packages Instalation

                    installscoop = subprocess.Popen(completescooppackages, shell=True)
                    installscoop.wait()

                    # Chocolatey Packages Instalation

                    installchoco = subprocess.Popen(completeschocopackages, shell=True)
                    installchoco.wait()

                    # Winget Packages Instalation

                    for i in range:
                        installwinget = subprocess.Popen(completewingetpackages, shell=True)
                        installwinget.wait()
                        wingetpackages.pop(0)

                
                # Update function

                def updateapps():
                    update()

                # About function

                def about():
                    messagebox.showinfo(title="About", message="Hello, this app is just a front-end to scoop, chocolatey and winget with pre-selected apps. \n Made with QT and Tkinter. \n Authors: \n FilmaBem")

                # Task Manager shortcut function

                def taskmanager():
                    subprocess.run('taskmgr', shell=False)

                # Systemsettings shotcut function

                def winsettings():
                    subprocess.run('ms-settings', shell=False)

                # Triggers for functions

                main.actionUpdate_All_Apps.triggered.connect(updateapps)
                main.actionAbout.triggered.connect(about)
                main.actionTask_Manager.triggered.connect(taskmanager)
                main.actionSystem_Settings.triggered.connect(winsettings)

                # Set the right function to the button click

                main.pushButton.clicked.connect(installpackages)

                # Show Window

                main.show()
                sys.exit(super.exec_())

