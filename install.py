import time
import update
import tkinter # Needed to use customtkinter
import customtkinter
import subprocess
import os
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Check for configuration file

wingetlist = os.path.exists('wingetlist.json')
scooplist = os.path.exists('scooplist.json')
chocolist = os.path.exists('chocolist.config')

# Winget import list 

if wingetlist == True:
    winstall = os.popen('winget import wingetlist.json')
    winstall.read()
    
# Scoop import List

elif scooplist == True:
    scinstall = os.popen('scoop import scooplist.json')    
    scinstall.read()
    
#  Chocolatey import list

elif chocolist == True:
    chocoinstall = os.popen('powershell start-process choco install chocolist.config -verb runas')
    chocoinstall.read()

else:
    time.sleep(0)

# Run an update before running the tool. This is usefull because previous imported lists may be outdated because it may have been some time that someone imported ant list or installed something

# update()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("FB Install Tool")
        self.geometry("950x467")
        self.resizable(False, False)

        # set grid layout 1x2

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image

        self.logo_image = customtkinter.CTkLabel(master=self, text="FB Install Tool")
        
        # Variables for the checkboxes
        
        self.checkbrave = customtkinter.IntVar()
        self.checkedge = customtkinter.IntVar()
        self.checkkmeleon = customtkinter.IntVar()
        self.checkchrome = customtkinter.IntVar()
        self.checkvivaldi = customtkinter.IntVar()
        self.checkopera = customtkinter.IntVar()
        self.checkfirefox = customtkinter.IntVar()
        self.checklibrewolf = customtkinter.IntVar()
        self.checkpalemoon = customtkinter.IntVar()
        self.checkwaterfox = customtkinter.IntVar()
        self.checkmidori = customtkinter.IntVar()
        self.checkoperagx = customtkinter.IntVar()
        
        self.checkretroarch = customtkinter.IntVar()
        self.checkamazongames = customtkinter.IntVar()
        self.checkubisoft = customtkinter.IntVar()
        self.checkdolphin = customtkinter.IntVar()
        self.checkrpcs3 = customtkinter.IntVar()
        self.checkepicgames = customtkinter.IntVar()
        self.checkpcsx2 = customtkinter.IntVar()
        self.checkyuzu = customtkinter.IntVar()
        self.checkheroic = customtkinter.IntVar()
        self.checkgog = customtkinter.IntVar()
        self.checkitchio = customtkinter.IntVar()
        self.checkminecraft = customtkinter.IntVar()
        self.checksteam = customtkinter.IntVar()
        self.checkeaapp = customtkinter.IntVar()
        self.checkgdlauncher = customtkinter.IntVar()
        self.checkcurseforge = customtkinter.IntVar()
        self.checkbattlenet = customtkinter.IntVar()
        self.checkcitra = customtkinter.IntVar()
        self.checkppsspp = customtkinter.IntVar()
        self.checkblitz = customtkinter.IntVar()
        self.checkplaynite = customtkinter.IntVar()
        
        self.checkzoom = customtkinter.IntVar()
        self.checkguilded = customtkinter.IntVar()
        self.checkslack = customtkinter.IntVar()
        self.checkhexchat = customtkinter.IntVar()
        self.checkskype = customtkinter.IntVar()
        self.checkdiscord = customtkinter.IntVar()
        self.checkteamspeak = customtkinter.IntVar()
        self.checktelegram = customtkinter.IntVar()
        self.checkwhatsapp = customtkinter.IntVar()
        self.checkviber = customtkinter.IntVar()
        self.checkmsteams = customtkinter.IntVar()
        self.checksignal = customtkinter.IntVar()
        
        self.checksedja = customtkinter.IntVar()
        self.checksumatra = customtkinter.IntVar()
        self.checkadobereader = customtkinter.IntVar()
        self.checkwps = customtkinter.IntVar()
        self.checkmasterpdf = customtkinter.IntVar()
        self.checkfoxit = customtkinter.IntVar()
        self.checklibreoffice = customtkinter.IntVar()
        self.checkopenoffice = customtkinter.IntVar()
        self.checkkingsoft = customtkinter.IntVar()
        self.checkfreeoffice = customtkinter.IntVar()
        self.checkonlyoffice = customtkinter.IntVar()
        self.checkmsoffice = customtkinter.IntVar()
        
        self.checkvcredist = customtkinter.IntVar()
        self.checkdotnet = customtkinter.IntVar()
        self.checkjava = customtkinter.IntVar()
        self.checkopenjdk = customtkinter.IntVar()
        self.checkopenjdk8 = customtkinter.IntVar()
        self.checkdirectx = customtkinter.IntVar()
        
        self.checkauthme = customtkinter.IntVar()
        self.checkauthy = customtkinter.IntVar()
        self.checkpasswordhub = customtkinter.IntVar()
        self.checktoofast = customtkinter.IntVar()
        self.checkyubico = customtkinter.IntVar()
        self.checkbitwarden = customtkinter.IntVar()
        self.checkkeepass = customtkinter.IntVar()
        self.checkpaswordsafe = customtkinter.IntVar()
        self.checkdashlane = customtkinter.IntVar()
        self.checkpanda = customtkinter.IntVar()
        self.checkcalmav = customtkinter.IntVar()
        
        self.checkvlc = customtkinter.IntVar()
        self.checkcider = customtkinter.IntVar()
        self.checkgom = customtkinter.IntVar()
        self.checkfilmora = customtkinter.IntVar()
        self.checktidal = customtkinter.IntVar()
        self.checkaudacium = customtkinter.IntVar()
        self.checkmypaint = customtkinter.IntVar()
        self.checkaudacity = customtkinter.IntVar()
        self.checkdeezer = customtkinter.IntVar()
        self.checkspotify = customtkinter.IntVar()
        self.checkitunes = customtkinter.IntVar()
        self.checkclementine = customtkinter.IntVar()
        self.checkhandbrake = customtkinter.IntVar()
        self.checkkdenlive = customtkinter.IntVar()
        self.checkmpv = customtkinter.IntVar()
        self.checkpotplayer = customtkinter.IntVar()
        self.checkpaintdotnet = customtkinter.IntVar()
        self.checkkrita = customtkinter.IntVar()
        self.checktuxpaint = customtkinter.IntVar()
        self.checkgimp = customtkinter.IntVar()
        self.checkglimpse = customtkinter.IntVar()
        self.checkphotogimp = customtkinter.IntVar()
        self.checkupscayl = customtkinter.IntVar()
        self.checkimageglass = customtkinter.IntVar()
        
        self.checkwinzip = customtkinter.IntVar()
        self.checkflameshot = customtkinter.IntVar()
        self.checknotepadplus = customtkinter.IntVar()
        self.checkpeazip = customtkinter.IntVar()
        self.checkatom = customtkinter.IntVar()
        self.checksharex = customtkinter.IntVar()
        self.checktrello = customtkinter.IntVar()
        self.checksevenzip = customtkinter.IntVar()
        self.checksublime = customtkinter.IntVar()
        self.checkevernote = customtkinter.IntVar()
        self.checknotion = customtkinter.IntVar()
        self.checkwinrar = customtkinter.IntVar()
        self.checkvscode = customtkinter.IntVar()
        self.checkimgburn = customtkinter.IntVar()
        self.checkpowertoys = customtkinter.IntVar()
        self.checksysinternals = customtkinter.IntVar()
        self.checkteracopy = customtkinter.IntVar()
        self.checkadb = customtkinter()
        

        # create navigation frame

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="FB Install Tool",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Create Frames

        self.browsers_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Browsers",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.browsers_button_event)
        self.browsers_button.grid(row=1, column=0, sticky="ew")

        self.games_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Games",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.games_button_event)
        self.games_button.grid(row=2, column=0, sticky="ew")

        self.messaging_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Messaging",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.messaging_button_event)
        self.messaging_button.grid(row=3, column=0, sticky="ew")

        self.office_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Office",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.office_button_event)
        self.office_button.grid(row=4, column=0, sticky="ew")

        self.runtime_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Runtimes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.runtime_button_event)
        self.runtime_button.grid(row=5, column=0, sticky="ew")

        self.security_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Security",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.security_button_event)
        self.security_button.grid(row=6, column=0, sticky="ew")

        self.media_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Media",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.media_button_event)
        self.media_button.grid(row=7, column=0, sticky="ew")

        self.utils_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Utilities",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.utils_button_event)
        self.utils_button.grid(row=8, column=0, sticky="ew")
        
        self.label1 = customtkinter.CTkLabel(self.navigation_frame, corner_radius=0, height=40, text="Theme:", fg_color="transparent", text_color=("gray10", "gray90"), anchor="w")
        self.label1.grid(row=10, column=0, padx=10, pady=0, sticky="s")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=11, column=0, padx=20, pady=6, sticky="s")

        # create browsers frame

        self.browsers_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.browsers_frame.grid_columnconfigure(0, weight=1)

        # Thing in the browsers Frame

        self.brave = customtkinter.CTkCheckBox(self.browsers_frame, text="Brave", variable=self.checkbrave)
        self.brave.grid(row=1, column=0, padx=20, pady=20)
        self.msedge = customtkinter.CTkCheckBox(self.browsers_frame, text="Microsoft Edge")
        self.msedge.grid(row=1, column=1, padx=20, pady=20)
        self.kmeleon = customtkinter.CTkCheckBox(self.browsers_frame, text="K Meleon")
        self.kmeleon.grid(row=1, column=2, padx=20, pady=20)
        self.chrome = customtkinter.CTkCheckBox(self.browsers_frame, text="Google Chrome", variable=self.checkchrome)
        self.chrome.grid(row=1, column=3, padx=20, pady=20)
        self.vivaldi = customtkinter.CTkCheckBox(self.browsers_frame, text="Vivaldi")
        self.vivaldi.grid(row=1, column=4, padx=20, pady=20)
        self.opera = customtkinter.CTkCheckBox(self.browsers_frame, text="Opera")
        self.opera.grid(row=1, column=5, padx=20, pady=20)

        self.firefox = customtkinter.CTkCheckBox(self.browsers_frame, text="Mozilla Firefox")
        self.firefox.grid(row=2, column=0, padx=20, pady=20)
        self.librewolf = customtkinter.CTkCheckBox(self.browsers_frame, text="Librewolf")
        self.librewolf.grid(row=2, column=1, padx=20, pady=20)
        self.palemoon = customtkinter.CTkCheckBox(self.browsers_frame, text="Pale Moon")
        self.palemoon.grid(row=2, column=2, padx=20, pady=20)
        self.waterfox = customtkinter.CTkCheckBox(self.browsers_frame, text="Waterfox")
        self.waterfox.grid(row=2, column=3, padx=20, pady=20)
        self.midori = customtkinter.CTkCheckBox(self.browsers_frame, text="Midori")
        self.midori.grid(row=2, column=4, padx=20, pady=20)
        self.operagx = customtkinter.CTkCheckBox(self.browsers_frame, text="Opera GX")
        self.operagx.grid(row=2, column=5, padx=20, pady=20)

        self.install_browsers = customtkinter.CTkButton(self.browsers_frame, text="Install", command=self.install_browser_packages)
        self.install_browsers.grid(row=4, column=5, padx=20, pady=20)

        # create games frame

        self.games_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Things on Games Frame

        self.retroarch = customtkinter.CTkCheckBox(self.games_frame, text="Retroarch")
        self.retroarch.grid(row=1, column=0, padx=20, pady=20)
        self.amazongames = customtkinter.CTkCheckBox(self.games_frame, text="Amazon Games")
        self.amazongames.grid(row=1, column=1, padx=20, pady=20)
        self.ubisoft = customtkinter.CTkCheckBox(self.games_frame, text="Ubisoft Connect")
        self.ubisoft.grid(row=1, column=2, padx=20, pady=20)
        self.dolphin = customtkinter.CTkCheckBox(self.games_frame, text="Dolphin Emulator")
        self.dolphin.grid(row=1, column=3, padx=20, pady=20)
        self.rpcs3 = customtkinter.CTkCheckBox(self.games_frame, text="RPCS3")
        self.rpcs3.grid(row=1, column=4, padx=20, pady=20)
        self.epicgames = customtkinter.CTkCheckBox(self.games_frame, text="Epic Games Launcher")
        self.epicgames.grid(row=1, column=5, padx=20, pady=20)
        self.pcsx2 = customtkinter.CTkCheckBox(self.games_frame, text="PCSX2")
        self.pcsx2.grid(row=1, column=6, padx=20, pady=20)

        self.yuzu = customtkinter.CTkCheckBox(self.games_frame, text="Yuzu")
        self.yuzu.grid(row=2, column=0, padx=20, pady=20)
        self.heroic = customtkinter.CTkCheckBox(self.games_frame, text="Heroic Games Launcher")
        self.heroic.grid(row=2, column=1, padx=20, pady=20)
        self.gog = customtkinter.CTkCheckBox(self.games_frame, text="GOG Galaxy")
        self.gog.grid(row=2, column=2, padx=20, pady=20)
        self.itchio = customtkinter.CTkCheckBox(self.games_frame, text="Itch.IO")
        self.itchio.grid(row=2, column=3, padx=20, pady=20)
        self.minecraft = customtkinter.CTkCheckBox(self.games_frame, text="Minecraft Launcher")
        self.minecraft.grid(row=2, column=4, padx=20, pady=20)
        self.steam = customtkinter.CTkCheckBox(self.games_frame, text="Steam")
        self.steam.grid(row=2, column=5, padx=20, pady=20)
        self.ea_app = customtkinter.CTkCheckBox(self.games_frame, text="EA APP")
        self.ea_app.grid(row=2, column=6, padx=20, pady=20)

        self.gdlauncher = customtkinter.CTkCheckBox(self.games_frame, text="GDLauncher")
        self.gdlauncher.grid(row=3, column=0, padx=20, pady=20)
        self.curseforge = customtkinter.CTkCheckBox(self.games_frame, text="CurseForge")
        self.curseforge.grid(row=3, column=1, padx=20, pady=20)
        self.battlenet = customtkinter.CTkCheckBox(self.games_frame, text="Battle.net")
        self.battlenet.grid(row=3, column=2, padx=20, pady=20)
        self.citra = customtkinter.CTkCheckBox(self.games_frame, text="Citra Emulator")
        self.citra.grid(row=3, column=3, padx=20, pady=20)
        self.ppsspp = customtkinter.CTkCheckBox(self.games_frame, text="PPSSPP")
        self.ppsspp.grid(row=3, column=4, padx=20, pady=20)
        self.blitz = customtkinter.CTkCheckBox(self.games_frame, text="Blitz")
        self.blitz.grid(row=3, column=5, padx=20, pady=20)
        self.playnite = customtkinter.CTkCheckBox(self.games_frame, text="Playnite")
        self.playnite.grid(row=3, column=6, padx=20, pady=20)
        
        self.install_games = customtkinter.CTkButton(self.games_frame, text="Install", command=self.install_game_packages)
        self.install_games.grid(row=4, column=5, padx=20, pady=20)

        # create Messaging frame

        self.messaging_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Things in Messaging Frame

        self.zoom = customtkinter.CTkCheckBox(self.messaging_frame, text="Zoom")
        self.zoom.grid(row=1, column=0, padx=20, pady=20)
        self.guilded = customtkinter.CTkCheckBox(self.messaging_frame, text="Guilded")
        self.guilded.grid(row=1, column=1, padx=20, pady=20)
        self.slack = customtkinter.CTkCheckBox(self.messaging_frame, text="Slack")
        self.slack.grid(row=1, column=2, padx=20, pady=20)
        self.hexchat = customtkinter.CTkCheckBox(self.messaging_frame, text="HexChat")
        self.hexchat.grid(row=1, column=3, padx=20, pady=20)
        self.skype = customtkinter.CTkCheckBox(self.messaging_frame, text="Skype")
        self.skype.grid(row=1, column=4, padx=20, pady=20)
        self.discord = customtkinter.CTkCheckBox(self.messaging_frame, text="Discord")
        self.discord.grid(row=1, column=5, padx=20, pady=20)

        self.teamspeak = customtkinter.CTkCheckBox(self.messaging_frame, text="TeamSpeak 3")
        self.teamspeak.grid(row=2, column=0, padx=20, pady=20)
        self.telegram = customtkinter.CTkCheckBox(self.messaging_frame, text="Telegram")
        self.telegram.grid(row=2, column=1, padx=20, pady=20)
        self.whatsapp = customtkinter.CTkCheckBox(self.messaging_frame, text="WhatsApp")
        self.whatsapp.grid(row=2, column=2, padx=20, pady=20)
        self.viber = customtkinter.CTkCheckBox(self.messaging_frame, text="Viber")
        self.viber.grid(row=2, column=3, padx=20, pady=20)
        self.msteams = customtkinter.CTkCheckBox(self.messaging_frame, text="Microsoft Teams")
        self.msteams.grid(row=2, column=4, padx=20, pady=20)
        self.signal = customtkinter.CTkCheckBox(self.messaging_frame, text="Signal")
        self.signal.grid(row=2, column=5, padx=20, pady=20)
        
        self.install_messaging = customtkinter.CTkButton(self.messaging_frame, text="Install", command=self.install_messaging_packages)
        self.install_messaging.grid(row=4, column=5, padx=20, pady=20)

        # create office frame

        self.office_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Things in the Office frame

        self.sedja = customtkinter.CTkCheckBox(self.office_frame, text="Sedja PDF")
        self.sedja.grid(row=1, column=0, padx=20, pady=20)
        self.sumatra = customtkinter.CTkCheckBox(self.office_frame, text="Sumatra PDF")
        self.sumatra.grid(row=1, column=1, padx=20, pady=20)
        self.adobereader = customtkinter.CTkCheckBox(self.office_frame, text="Adobe Reader")
        self.adobereader.grid(row=1, column=2, padx=20, pady=20)
        self.wps = customtkinter.CTkCheckBox(self.office_frame, text="WPS Office")
        self.wps.grid(row=1, column=3, padx=20, pady=20)
        self.master_pdf = customtkinter.CTkCheckBox(self.office_frame, text="Master PDF Editor")
        self.master_pdf.grid(row=1, column=4, padx=20, pady=20)
        self.foxit = customtkinter.CTkCheckBox(self.office_frame, text="Foxit Reader")
        self.foxit.grid(row=1, column=5, padx=20, pady=20)

        self.libreoffice = customtkinter.CTkCheckBox(self.office_frame, text="LibreOffice")
        self.libreoffice.grid(row=2, column=0, padx=20, pady=20)
        self.openoffice = customtkinter.CTkCheckBox(self.office_frame, text="OpenOffice")
        self.openoffice.grid(row=2, column=1, padx=20, pady=20)
        self.kingsoft = customtkinter.CTkCheckBox(self.office_frame, text="Kingsoft Office")
        self.kingsoft.grid(row=2, column=2, padx=20, pady=20)
        self.freeoffice = customtkinter.CTkCheckBox(self.office_frame, text="FreeOffice")
        self.freeoffice.grid(row=2, column=3, padx=20, pady=20)
        self.onlyoffice = customtkinter.CTkCheckBox(self.office_frame, text="OnlyOffice")
        self.onlyoffice.grid(row=2, column=4, padx=20, pady=20)
        self.msoffice = customtkinter.CTkCheckBox(self.office_frame, text="MS Office 365")
        self.msoffice.grid(row=2, column=5, padx=20, pady=20)
        
        self.install_office = customtkinter.CTkButton(self.office_frame, text="Install", command=self.install_office_packages)
        self.install_office.grid(row=4, column=5, padx=20, pady=20)

        # create runtime frame

        self.runtime_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in the Runtime frame
        
        self.vcredist = customtkinter.CTkCheckBox(self.runtime_frame, text="VCRedist")
        self.vcredist.grid(row=1, column=0, padx=20, pady=20)
        self.dotnet = customtkinter.CTkCheckBox(self.runtime_frame, text=".Net")
        self.dotnet.grid(row=1, column=1, padx=20, pady=20)
        self.java = customtkinter.CTkCheckBox(self.runtime_frame, text="Java Runtime Environment")
        self.java.grid(row=1, column=2, padx=20, pady=20)
        self.openjdk = customtkinter.CTkCheckBox(self.runtime_frame, text="OpenJDK (Latest)")
        self.openjdk.grid(row=1, column=3, padx=20, pady=20)
        self.openjdk8 = customtkinter.CTkCheckBox(self.runtime_frame, text="OpenJDK 8")
        self.openjdk8.grid(row=1, column=4, padx=20, pady=20)
        self.directx = customtkinter.CTkCheckBox(self.runtime_frame, text="DirectX")
        self.directx.grid(row=1, column=5, padx=20, pady=20)
        
        self.install_runtime = customtkinter.CTkButton(self.runtime_frame, text="Install", command=self.install_runtime_packages)
        self.install_runtime.grid(row=4, column=5, padx=20, pady=20)

        # create security frame

        self.security_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in the Security Frame
        
        self.authme = customtkinter.CTkCheckBox(self.security_frame, text="AuthMe")
        self.authme.grid(row=1, column=0, padx=20, pady=20)
        self.authy = customtkinter.CTkCheckBox(self.security_frame, text="Authy")
        self.authy.grid(row=1, column=1, padx=20, pady=20)
        self.passwordhub = customtkinter.CTkCheckBox(self.security_frame, text="Password Hub")
        self.passwordhub.grid(row=1, column=2, padx=20, pady=20)
        self.toofast = customtkinter.CTkCheckBox(self.security_frame, text="2fast")
        self.toofast.grid(row=1, column=3, padx=20, pady=20)
        self.yubico = customtkinter.CTkCheckBox(self.security_frame, text="Yubico Authenticator")
        self.yubico.grid(row=1, column=4, padx=20, pady=20)
        self.bitwarden = customtkinter.CTkCheckBox(self.security_frame, text="Bitwarden")
        self.bitwarden.grid(row=1, column=5, padx=20, pady=20)

        self.keepass = customtkinter.CTkCheckBox(self.security_frame, text="Keepass")
        self.keepass.grid(row=2, column=0, padx=20, pady=20)
        self.passwordsafe = customtkinter.CTkCheckBox(self.security_frame, text="Password Safe")
        self.passwordsafe.grid(row=2, column=1, padx=20, pady=20)
        self.dashlane = customtkinter.CTkCheckBox(self.security_frame, text="Dashlane")
        self.dashlane.grid(row=2, column=2, padx=20, pady=20)
        self.panda = customtkinter.CTkCheckBox(self.security_frame, text="Panda Free Antivirus")
        self.panda.grid(row=2, column=3, padx=20, pady=20)
        self.adwcleaner = customtkinter.CTkCheckBox(self.security_frame, text="Adw Cleaner")
        self.adwcleaner.grid(row=2, column=4, padx=20, pady=20)
        self.calmav = customtkinter.CTkCheckBox(self.security_frame, text="CalmAV")
        self.calmav.grid(row=2, column=5, padx=20, pady=20)
        
        self.install_security = customtkinter.CTkButton(self.security_frame, text="Install", command=self.install_security_packages)
        self.install_security.grid(row=4, column=5, padx=20, pady=20)

        # create media frame

        self.media_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in Media Frame
        
        self.vlc = customtkinter.CTkCheckBox(self.media_frame, text="VLC")
        self.vlc.grid(row=1, column=0, padx=20, pady=20)
        self.cider = customtkinter.CTkCheckBox(self.media_frame, text="Cider")
        self.cider.grid(row=1, column=1, padx=20, pady=20)
        self.gom = customtkinter.CTkCheckBox(self.media_frame, text="Gom Player")
        self.gom.grid(row=1, column=2, padx=20, pady=20)
        self.filmora = customtkinter.CTkCheckBox(self.media_frame, text="Filmora")
        self.filmora.grid(row=1, column=3, padx=20, pady=20)
        self.tidal = customtkinter.CTkCheckBox(self.media_frame, text="Tidal")
        self.tidal.grid(row=1, column=4, padx=20, pady=20)
        self.audacium = customtkinter.CTkCheckBox(self.media_frame, text="Audacium")
        self.audacium.grid(row=1, column=5, padx=20, pady=20)

        self.mypaint = customtkinter.CTkCheckBox(self.media_frame, text="MyPaint")
        self.mypaint.grid(row=2, column=0, padx=20, pady=20)
        self.audacity = customtkinter.CTkCheckBox(self.media_frame, text="Audacity")
        self.audacity.grid(row=2, column=1, padx=20, pady=20)
        self.deezer = customtkinter.CTkCheckBox(self.media_frame, text="Deezer")
        self.deezer.grid(row=2, column=2, padx=20, pady=20)
        self.spotify = customtkinter.CTkCheckBox(self.media_frame, text="Spotify")
        self.spotify.grid(row=2, column=3, padx=20, pady=20)
        self.itunes = customtkinter.CTkCheckBox(self.media_frame, text="iTunes")
        self.itunes.grid(row=2, column=4, padx=20, pady=20)
        self.clementine = customtkinter.CTkCheckBox(self.media_frame, text="Clementine")
        self.clementine.grid(row=2, column=5, padx=20, pady=20)
        
        self.handbrake = customtkinter.CTkCheckBox(self.media_frame, text="Handbrake")
        self.handbrake.grid(row=3, column=0, padx=20, pady=20)
        self.kdenlive = customtkinter.CTkCheckBox(self.media_frame, text="KDEnLive")
        self.kdenlive.grid(row=3, column=1, padx=20, pady=20)
        self.mpv = customtkinter.CTkCheckBox(self.media_frame, text="MPV")
        self.mpv.grid(row=3, column=2, padx=20, pady=20)
        self.potplayer = customtkinter.CTkCheckBox(self.media_frame, text="Pot Player")
        self.potplayer.grid(row=3, column=3, padx=20, pady=20)
        self.paintdotnet = customtkinter.CTkCheckBox(self.media_frame, text="Paint.Net")
        self.paintdotnet.grid(row=3, column=4, padx=20, pady=20)
        self.krita = customtkinter.CTkCheckBox(self.media_frame, text="Krita")
        self.krita.grid(row=3, column=5, padx=20, pady=20)

        self.tuxpaint = customtkinter.CTkCheckBox(self.media_frame, text="Tux Paint")
        self.tuxpaint.grid(row=4, column=0, padx=20, pady=20)
        self.gimp = customtkinter.CTkCheckBox(self.media_frame, text="GIMP")
        self.gimp.grid(row=4, column=1, padx=20, pady=20)
        self.glimpse = customtkinter.CTkCheckBox(self.media_frame, text="Glimpse")
        self.glimpse.grid(row=4, column=2, padx=20, pady=20)
        self.photogimp = customtkinter.CTkCheckBox(self.media_frame, text="PhotoGIMP")
        self.photogimp.grid(row=4, column=3, padx=20, pady=20)
        self.upscayl = customtkinter.CTkCheckBox(self.media_frame, text="Upscay!")
        self.upscayl.grid(row=4, column=4, padx=20, pady=20)
        self.imageglass = customtkinter.CTkCheckBox(self.media_frame, text="ImageGlass")
        self.imageglass.grid(row=4, column=5, padx=20, pady=20)
        
        self.install_media = customtkinter.CTkButton(self.media_frame, text="Install", command=self.install_media_packages)
        self.install_media.grid(row=4, column=5, padx=20, pady=20)


        # create utilities frame

        self.utils_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things on Utilities Frame
        
        self.winzip = customtkinter.CTkCheckBox(self.utils_frame, text="WinZip")
        self.winzip.grid(row=1, column=0, padx=20, pady=20)
        self.flameshot = customtkinter.CTkCheckBox(self.utils_frame, text="Flameshot")
        self.flameshot.grid(row=1, column=1, padx=20, pady=20)
        self.notepadplus = customtkinter.CTkCheckBox(self.utils_frame, text="Notepad++")
        self.notepadplus.grid(row=1, column=2, padx=20, pady=20)
        self.peazip = customtkinter.CTkCheckBox(self.utils_frame, text="PeaZip")
        self.peazip.grid(row=1, column=3, padx=20, pady=20)
        self.atom = customtkinter.CTkCheckBox(self.utils_frame, text="Atom")
        self.atom.grid(row=1, column=4, padx=20, pady=20)
        self.sharex = customtkinter.CTkCheckBox(self.utils_frame, text="ShareX")
        self.sharex.grid(row=1, column=5, padx=20, pady=20)

        self.trello = customtkinter.CTkCheckBox(self.utils_frame, text="Trello Desktop")
        self.trello.grid(row=2, column=0, padx=20, pady=20)
        self.sevenzip = customtkinter.CTkCheckBox(self.utils_frame, text="7-Zip")
        self.sevenzip.grid(row=2, column=1, padx=20, pady=20)
        self.sublime = customtkinter.CTkCheckBox(self.utils_frame, text="Sublime Text")
        self.sublime.grid(row=2, column=2, padx=20, pady=20)
        self.evernote = customtkinter.CTkCheckBox(self.utils_frame, text="Evernote")
        self.evernote.grid(row=2, column=3, padx=20, pady=20)
        self.notion = customtkinter.CTkCheckBox(self.utils_frame, text="Notion")
        self.notion.grid(row=2, column=4, padx=20, pady=20)
        self.winrar = customtkinter.CTkCheckBox(self.utils_frame, text="Winrar")
        self.winrar.grid(row=2, column=5, padx=20, pady=20)
        
        self.vscode = customtkinter.CTkCheckBox(self.utils_frame, text="VS Code")
        self.vscode.grid(row=3, column=0, padx=20, pady=20)
        self.imgburn = customtkinter.CTkCheckBox(self.utils_frame, text="IMGBurn")
        self.imgburn.grid(row=3, column=1, padx=20, pady=20)
        self.powertoys = customtkinter.CTkCheckBox(self.utils_frame, text="Powertoys")
        self.powertoys.grid(row=3, column=2, padx=20, pady=20)
        self.sysinternals = customtkinter.CTkCheckBox(self.utils_frame, text="Sysinternals Suite")
        self.sysinternals.grid(row=3, column=3, padx=20, pady=20)
        self.teracopy = customtkinter.CTkCheckBox(self.utils_frame, text="Teracopy")
        self.teracopy.grid(row=3, column=4, padx=20, pady=20)
        self.adb = customtkinter.CTkCheckBox(self.utils_frame, text="ADB")
        self.adb.grid(row=3, column=5, padx=20, pady=20)
        
        self.install_utils = customtkinter.CTkButton(self.utils_frame, text="Install", command=self.install_media_packages)
        self.install_utils.grid(row=4, column=5, padx=20, pady=20)
        
        # select default frame

        self.select_frame_by_name("browsers")

    def select_frame_by_name(self, name):

        # set button color for selected button

        self.browsers_button.configure(fg_color=("gray75", "gray25") if name == "browsers" else "transparent")
        self.games_button.configure(fg_color=("gray75", "gray25") if name == "games" else "transparent")
        self.messaging_button.configure(fg_color=("gray75", "gray25") if name == "messaging" else "transparent")
        self.office_button.configure(fg_color=("gray75", "gray25") if name == "office" else "transparent")
        self.runtime_button.configure(fg_color=("gray75", "gray25") if name == "runtime" else "transparent")
        self.security_button.configure(fg_color=("gray75", "gray25") if name == "security" else "transparent")
        self.media_button.configure(fg_color=("gray75", "gray25") if name == "media" else "transparent")
        self.utils_button.configure(fg_color=("gray75", "gray25") if name == "utils" else "transparent")

        # show selected frame

        if name == "browsers":
            self.browsers_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.browsers_frame.grid_forget()
        if name == "games":
            self.games_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.games_frame.grid_forget()
        if name == "messaging":
            self.messaging_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.messaging_frame.grid_forget()
        if name == "office":
            self.office_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.office_frame.grid_forget()
        if name == "runtime":
            self.runtime_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.runtime_frame.grid_forget()
        if name == "security":
            self.security_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.security_frame.grid_forget()
        if name == "media":
            self.media_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.media_frame.grid_forget()
        if name == "utils":
            self.utils_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.utils_frame.grid_forget()

    def browsers_button_event(self):
        self.select_frame_by_name("browsers")

    def games_button_event(self):
        self.select_frame_by_name("games")

    def messaging_button_event(self):
        self.select_frame_by_name("messaging")

    def office_button_event(self):
        self.select_frame_by_name("office")

    def runtime_button_event(self):
        self.select_frame_by_name("runtime")

    def security_button_event(self):
        self.select_frame_by_name("security")

    def media_button_event(self):
        self.select_frame_by_name("media")

    def utils_button_event(self):
        self.select_frame_by_name("utils")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        
    # Instalation functions for the packages in all frames
    
    def install_browser_packages(self):
        if self.checkbrave.get() == 1:
            print('brave')
        if self.checkchrome.get() == 1:
            print('chrome')
    
    def install_game_packages():
        pass
    
    def install_messaging_packages():
        pass
    
    def install_office_packages():
        pass
    
    def install_runtime_packages():
        pass
    
    def install_security_packages():
        pass
    
    def install_media_packages():
        pass
    
    def install_util_packages():
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
