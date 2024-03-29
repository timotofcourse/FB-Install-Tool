import update
import tkinter # Needed to use customtkinter
import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Check for configuration file and import the apps


if os.path.exists('wingetlist.json'):
    winstall = os.popen('winget import wingetlist.json')
    winstall.read()

if os.path.exists('scooplist.json'):
    scinstall = os.popen('scoop import scooplist.json')    
    scinstall.read()

if os.path.exists('chocolist.config'):
    chocoinstall = os.popen('powershell start-process choco install chocolist.config -verb runas')
    chocoinstall.read()

# Run an update before running the tool. This is usefull because previous imported lists may be outdated because it may have been some time that someone imported ant list or installed something

# update.updatepackages()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("FB Install Tool")
        self.geometry("950x467")
        self.resizable(True, True)

        # set grid layout 1x2

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image

        self.logo_image = customtkinter.CTkLabel(master=self, text="FB Install Tool")
        
        # Variables for the checkboxes
        
        self.check_brave_browser = customtkinter.IntVar()
        self.check_microsoft_edge = customtkinter.IntVar()
        self.check_k_meleon = customtkinter.IntVar()
        self.check_google_chrome = customtkinter.IntVar()
        self.check_vivaldi = customtkinter.IntVar()
        self.check_opera = customtkinter.IntVar()
        self.check_mozilla_firefox = customtkinter.IntVar()
        self.check_librewolf = customtkinter.IntVar()
        self.check_pale_moon = customtkinter.IntVar()
        self.check_waterfox = customtkinter.IntVar()
        self.check_midori = customtkinter.IntVar()
        self.check_opera_gx = customtkinter.IntVar()
        
        self.check_retroarch = customtkinter.IntVar()
        self.check_amazon_games = customtkinter.IntVar()
        self.check_ubisoft_connect = customtkinter.IntVar()
        self.check_dolphin = customtkinter.IntVar()
        self.check_rpcs3 = customtkinter.IntVar()
        self.check_epic_games_launcher = customtkinter.IntVar()
        self.check_pcsx2 = customtkinter.IntVar()
        self.check_yuzu = customtkinter.IntVar()
        self.check_heroic_games_launcher = customtkinter.IntVar()
        self.check_gog_galaxy = customtkinter.IntVar()
        self.check_itch_io = customtkinter.IntVar()
        self.check_minecraft_launcher = customtkinter.IntVar()
        self.check_steam = customtkinter.IntVar()
        self.check_ea_app = customtkinter.IntVar()
        self.check_gdlauncher = customtkinter.IntVar()
        self.check_curseforge = customtkinter.IntVar()
        self.check_battle_net = customtkinter.IntVar()
        self.check_citra = customtkinter.IntVar()
        self.check_ppsspp = customtkinter.IntVar()
        self.check_blitz = customtkinter.IntVar()
        self.check_playnite = customtkinter.IntVar()
        
        self.check_zoom = customtkinter.IntVar()
        self.check_guilded = customtkinter.IntVar()
        self.check_slack = customtkinter.IntVar()
        self.check_hexchat = customtkinter.IntVar()
        self.check_skype = customtkinter.IntVar()
        self.check_discord = customtkinter.IntVar()
        self.check_teamspeak = customtkinter.IntVar()
        self.check_telegram = customtkinter.IntVar()
        self.check_whatsapp = customtkinter.IntVar()
        self.check_viber = customtkinter.IntVar()
        self.check_microsoft_teams = customtkinter.IntVar()
        self.check_signal = customtkinter.IntVar()
        
        self.check_sedja_pdf = customtkinter.IntVar()
        self.check_sumatra_pdf = customtkinter.IntVar()
        self.check_adobe_reader = customtkinter.IntVar()
        self.check_wps_office = customtkinter.IntVar()
        self.check_masterpdf = customtkinter.IntVar()
        self.check_foxit_reader = customtkinter.IntVar()
        self.check_libreoffice = customtkinter.IntVar()
        self.check_openoffice = customtkinter.IntVar()
        self.check_kingsoft_office = customtkinter.IntVar()
        self.check_freeoffice = customtkinter.IntVar()
        self.check_onlyoffice = customtkinter.IntVar()
        self.check_microsoft_office = customtkinter.IntVar()
        
        self.check_vcredist = customtkinter.IntVar()
        self.check_dotnet = customtkinter.IntVar()
        self.check_java = customtkinter.IntVar()
        self.check_openjdk = customtkinter.IntVar()
        self.check_openjdk8 = customtkinter.IntVar()
        self.check_directx = customtkinter.IntVar()
        
        self.check_authme = customtkinter.IntVar()
        self.check_authy = customtkinter.IntVar()
        self.check_passwordhub = customtkinter.IntVar()
        self.check_toofast = customtkinter.IntVar()
        self.check_yubico = customtkinter.IntVar()
        self.check_bitwarden = customtkinter.IntVar()
        self.check_keepass = customtkinter.IntVar()
        self.check_paswordsafe = customtkinter.IntVar()
        self.check_dashlane = customtkinter.IntVar()
        self.check_panda = customtkinter.IntVar()
        self.check_adw_cleaner = customtkinter.IntVar()
        self.check_calmav = customtkinter.IntVar()
        
        self.check_vlc = customtkinter.IntVar()
        self.check_cider = customtkinter.IntVar()
        self.check_gom_player = customtkinter.IntVar()
        self.check_wondershare_filmora = customtkinter.IntVar()
        self.check_tidal = customtkinter.IntVar()
        self.check_audacium = customtkinter.IntVar()
        self.check_mypaint = customtkinter.IntVar()
        self.check_audacity = customtkinter.IntVar()
        self.check_deezer = customtkinter.IntVar()
        self.check_spotify = customtkinter.IntVar()
        self.check_itunes = customtkinter.IntVar()
        self.check_clementine = customtkinter.IntVar()
        self.check_handbrake = customtkinter.IntVar()
        self.check_kdenlive = customtkinter.IntVar()
        self.check_mpv = customtkinter.IntVar()
        self.check_pot_player = customtkinter.IntVar()
        self.check_paint_dot_net = customtkinter.IntVar()
        self.check_krita = customtkinter.IntVar()
        self.check_tuxpaint = customtkinter.IntVar()
        self.check_gimp = customtkinter.IntVar()
        self.check_glimpse = customtkinter.IntVar()
        self.check_photogimp = customtkinter.IntVar()
        self.check_upscayl = customtkinter.IntVar()
        self.check_imageglass = customtkinter.IntVar()
        
        self.check_winzip = customtkinter.IntVar()
        self.check_flameshot = customtkinter.IntVar()
        self.check_notepad_plus_plus = customtkinter.IntVar()
        self.check_peazip = customtkinter.IntVar()
        self.check_atom = customtkinter.IntVar()
        self.check_sharex = customtkinter.IntVar()
        self.check_trello = customtkinter.IntVar()
        self.check_sevenzip = customtkinter.IntVar()
        self.check_sublime_text = customtkinter.IntVar()
        self.check_evernote = customtkinter.IntVar()
        self.check_notion = customtkinter.IntVar()
        self.check_winrar = customtkinter.IntVar()
        self.check_visual_studio_code = customtkinter.IntVar()
        self.check_imgburn = customtkinter.IntVar()
        self.check_powertoys = customtkinter.IntVar()
        self.check_sysinternals_suite = customtkinter.IntVar()
        self.check_teracopy = customtkinter.IntVar()
        self.check_adb = customtkinter.IntVar()
        self.check_flow = customtkinter.IntVar()
        self.check_adguard = customtkinter.IntVar()
        

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

        self.brave_browser = customtkinter.CTkCheckBox(self.browsers_frame, text="Brave", variable=self.check_brave_browser)
        self.brave_browser.grid(row=1, column=1, padx=20, pady=20)
        self.microsoft_edge = customtkinter.CTkCheckBox(self.browsers_frame, text="Microsoft Edge", variable=self.check_microsoft_edge)
        self.microsoft_edge.grid(row=1, column=2, padx=20, pady=20)
        self.k_meleon = customtkinter.CTkCheckBox(self.browsers_frame, text="K Meleon", variable=self.check_k_meleon)
        self.k_meleon.grid(row=1, column=3, padx=20, pady=20)
        self.google_chrome = customtkinter.CTkCheckBox(self.browsers_frame, text="Google Chrome", variable=self.check_google_chrome)
        self.google_chrome.grid(row=1, column=4, padx=20, pady=20)
        self.vivaldi = customtkinter.CTkCheckBox(self.browsers_frame, text="Vivaldi", variable=self.check_vivaldi)
        self.vivaldi.grid(row=1, column=5, padx=20, pady=20)
        self.opera = customtkinter.CTkCheckBox(self.browsers_frame, text="Opera", variable=self.check_opera)
        self.opera.grid(row=1, column=6, padx=20, pady=20)

        self.mozilla_firefox = customtkinter.CTkCheckBox(self.browsers_frame, text="Mozilla Firefox", variable=self.check_mozilla_firefox)
        self.mozilla_firefox.grid(row=2, column=1, padx=20, pady=20)
        self.librewolf = customtkinter.CTkCheckBox(self.browsers_frame, text="Librewolf", variable=self.check_librewolf)
        self.librewolf.grid(row=2, column=2, padx=20, pady=20)
        self.pale_moon = customtkinter.CTkCheckBox(self.browsers_frame, text="Pale Moon", variable=self.check_pale_moon)
        self.pale_moon.grid(row=2, column=3, padx=20, pady=20)
        self.waterfox = customtkinter.CTkCheckBox(self.browsers_frame, text="Waterfox", variable=self.check_waterfox)
        self.waterfox.grid(row=2, column=4, padx=20, pady=20)
        self.midori = customtkinter.CTkCheckBox(self.browsers_frame, text="Midori", variable=self.check_midori)
        self.midori.grid(row=2, column=5, padx=20, pady=20)
        self.opera_gx = customtkinter.CTkCheckBox(self.browsers_frame, text="Opera GX", variable=self.check_opera_gx)
        self.opera_gx.grid(row=2, column=6, padx=20, pady=20)
        
        self.browsers_spacer = customtkinter.CTkLabel(self.browsers_frame, text="")
        self.browsers_spacer.grid(row=3, column=5, padx=20, pady=130)

        self.install_browsers = customtkinter.CTkButton(self.browsers_frame, text="Install", command=self.install_browser_packages)
        self.install_browsers.grid(row=4, column=5, padx=20, pady=20)

        # create games frame

        self.games_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Things on Games Frame

        self.retroarch = customtkinter.CTkCheckBox(self.games_frame, text="Retroarch", variable=self.check_retroarch)
        self.retroarch.grid(row=1, column=0, padx=20, pady=20)
        self.amazon_games = customtkinter.CTkCheckBox(self.games_frame, text="Amazon Games", variable=self.check_amazon_games)
        self.amazon_games.grid(row=1, column=1, padx=20, pady=20)
        self.ubisoft_connect = customtkinter.CTkCheckBox(self.games_frame, text="Ubisoft Connect", variable=self.check_ubisoft_connect)
        self.ubisoft_connect.grid(row=1, column=2, padx=20, pady=20)
        self.dolphin = customtkinter.CTkCheckBox(self.games_frame, text="Dolphin Emulator", variable=self.check_dolphin)
        self.dolphin.grid(row=1, column=3, padx=20, pady=20)
        
        self.rpcs3 = customtkinter.CTkCheckBox(self.games_frame, text="RPCS3", variable=self.check_rpcs3)
        self.rpcs3.grid(row=2, column=0, padx=20, pady=20)
        self.epic_games_launcher = customtkinter.CTkCheckBox(self.games_frame, text="Epic Games Launcher", variable=self.check_epic_games_launcher)
        self.epic_games_launcher.grid(row=2, column=1, padx=20, pady=20)
        self.pcsx2 = customtkinter.CTkCheckBox(self.games_frame, text="PCSX2", variable=self.check_pcsx2)
        self.pcsx2.grid(row=2, column=2, padx=20, pady=20)
        self.yuzu = customtkinter.CTkCheckBox(self.games_frame, text="Yuzu", variable=self.check_yuzu)
        self.yuzu.grid(row=2, column=3, padx=20, pady=20)
        
        self.heroic_games_launcher = customtkinter.CTkCheckBox(self.games_frame, text="Heroic Games Launcher", variable=self.check_heroic_games_launcher)
        self.heroic_games_launcher.grid(row=3, column=0, padx=20, pady=20)
        self.gog_galaxy = customtkinter.CTkCheckBox(self.games_frame, text="GOG Galaxy", variable=self.check_gog_galaxy)
        self.gog_galaxy.grid(row=3, column=1, padx=20, pady=20)
        self.itch_io = customtkinter.CTkCheckBox(self.games_frame, text="Itch.IO", variable=self.check_itch_io)
        self.itch_io.grid(row=3, column=2, padx=20, pady=20)
        self.minecraft_launcher = customtkinter.CTkCheckBox(self.games_frame, text="Minecraft Launcher", variable=self.check_minecraft_launcher)
        self.minecraft_launcher.grid(row=3, column=3, padx=20, pady=20)
        
        self.steam = customtkinter.CTkCheckBox(self.games_frame, text="Steam", variable=self.check_steam)
        self.steam.grid(row=4, column=0, padx=20, pady=20)
        self.ea_app = customtkinter.CTkCheckBox(self.games_frame, text="EA APP", variable=self.check_ea_app)
        self.ea_app.grid(row=4, column=1, padx=20, pady=20)
        self.gdlauncher = customtkinter.CTkCheckBox(self.games_frame, text="GDLauncher", variable=self.check_gdlauncher)
        self.gdlauncher.grid(row=4, column=2, padx=20, pady=20)
        self.curseforge = customtkinter.CTkCheckBox(self.games_frame, text="CurseForge", variable=self.check_curseforge)
        self.curseforge.grid(row=4, column=3, padx=20, pady=20)
        
        self.battle_net = customtkinter.CTkCheckBox(self.games_frame, text="Battle.net", variable=self.check_battle_net)
        self.battle_net.grid(row=5, column=0, padx=20, pady=20)
        self.citra = customtkinter.CTkCheckBox(self.games_frame, text="Citra Emulator", variable=self.check_citra)
        self.citra.grid(row=5, column=1, padx=20, pady=20)
        self.ppsspp = customtkinter.CTkCheckBox(self.games_frame, text="PPSSPP", variable=self.check_ppsspp)
        self.ppsspp.grid(row=5, column=2, padx=20, pady=20)
        self.blitz = customtkinter.CTkCheckBox(self.games_frame, text="Blitz", variable=self.check_blitz)
        self.blitz.grid(row=5, column=3, padx=20, pady=20)
        
        self.playnite = customtkinter.CTkCheckBox(self.games_frame, text="Playnite", variable=self.check_playnite)
        self.playnite.grid(row=6, column=0, padx=20, pady=20)
        
        self.games_spacer = customtkinter.CTkLabel(self.games_frame, text="")
        self.games_spacer.grid(row=7, column=3, padx=20, pady=2)
        
        self.install_games = customtkinter.CTkButton(self.games_frame, text="Install", command=self.install_game_packages)
        self.install_games.grid(row=8, column=3, padx=63, pady=20)

        # create Messaging frame

        self.messaging_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Things in Messaging Frame

        self.zoom = customtkinter.CTkCheckBox(self.messaging_frame, text="Zoom", variable=self.check_zoom)
        self.zoom.grid(row=1, column=0, padx=20, pady=20)
        self.guilded = customtkinter.CTkCheckBox(self.messaging_frame, text="Guilded", variable=self.check_guilded)
        self.guilded.grid(row=1, column=1, padx=20, pady=20)
        self.slack = customtkinter.CTkCheckBox(self.messaging_frame, text="Slack", variable=self.check_slack)
        self.slack.grid(row=1, column=2, padx=20, pady=20)
        self.hexchat = customtkinter.CTkCheckBox(self.messaging_frame, text="HexChat", variable=self.check_hexchat)
        self.hexchat.grid(row=1, column=3, padx=20, pady=20)
        self.skype = customtkinter.CTkCheckBox(self.messaging_frame, text="Skype", variable=self.check_skype)
        self.skype.grid(row=1, column=4, padx=20, pady=20)
        
        self.discord = customtkinter.CTkCheckBox(self.messaging_frame, text="Discord", variable=self.check_discord)
        self.discord.grid(row=2, column=0, padx=20, pady=20)
        self.teamspeak = customtkinter.CTkCheckBox(self.messaging_frame, text="TeamSpeak 3", variable=self.check_teamspeak)
        self.teamspeak.grid(row=2, column=1, padx=20, pady=20)
        self.telegram = customtkinter.CTkCheckBox(self.messaging_frame, text="Telegram", variable=self.check_telegram)
        self.telegram.grid(row=2, column=2, padx=20, pady=20)
        self.whatsapp = customtkinter.CTkCheckBox(self.messaging_frame, text="WhatsApp", variable=self.check_whatsapp)
        self.whatsapp.grid(row=2, column=3, padx=20, pady=20)
        self.viber = customtkinter.CTkCheckBox(self.messaging_frame, text="Viber", variable=self.check_viber)
        self.viber.grid(row=2, column=4, padx=20, pady=20)
        
        self.microsoft_teams = customtkinter.CTkCheckBox(self.messaging_frame, text="Microsoft Teams", variable=self.check_microsoft_teams)
        self.microsoft_teams.grid(row=3, column=0, padx=20, pady=20)
        self.signal = customtkinter.CTkCheckBox(self.messaging_frame, text="Signal", variable=self.check_signal)
        self.signal.grid(row=3, column=1, padx=20, pady=20)
        
        self.messaging_spacer = customtkinter.CTkLabel(self.messaging_frame, text="")
        self.messaging_spacer.grid(row=4, column=4, padx=20, pady=98)
        
        self.install_messaging = customtkinter.CTkButton(self.messaging_frame, text="Install", command=self.install_messaging_packages)
        self.install_messaging.grid(row=5, column=4, padx=28, pady=20)

        # create office frame

        self.office_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Things in the Office frame

        self.sedja_pdf = customtkinter.CTkCheckBox(self.office_frame, text="Sedja PDF", variable=self.check_sedja_pdf)
        self.sedja_pdf.grid(row=1, column=0, padx=20, pady=20)
        self.sumatra_pdf = customtkinter.CTkCheckBox(self.office_frame, text="Sumatra PDF", variable=self.check_sumatra_pdf)
        self.sumatra_pdf.grid(row=1, column=1, padx=20, pady=20)
        self.adobe_reader = customtkinter.CTkCheckBox(self.office_frame, text="Adobe Reader", variable=self.check_adobe_reader)
        self.adobe_reader.grid(row=1, column=2, padx=20, pady=20)
        self.wps_office = customtkinter.CTkCheckBox(self.office_frame, text="WPS Office", variable=self.check_wps_office)
        self.wps_office.grid(row=1, column=3, padx=20, pady=20)
        self.master_pdf = customtkinter.CTkCheckBox(self.office_frame, text="Master PDF Editor", variable=self.check_masterpdf)
        self.master_pdf.grid(row=1, column=4, padx=20, pady=20)
        self.foxit = customtkinter.CTkCheckBox(self.office_frame, text="Foxit Reader", variable=self.check_foxit_reader)
        self.foxit.grid(row=2, column=0, padx=20, pady=20)

        self.libreoffice = customtkinter.CTkCheckBox(self.office_frame, text="LibreOffice", variable=self.check_libreoffice)
        self.libreoffice.grid(row=2, column=1, padx=20, pady=20)
        self.openoffice = customtkinter.CTkCheckBox(self.office_frame, text="OpenOffice", variable=self.check_openoffice)
        self.openoffice.grid(row=2, column=2, padx=20, pady=20)
        self.kingsoft_office = customtkinter.CTkCheckBox(self.office_frame, text="Kingsoft Office", variable=self.check_kingsoft_office)
        self.kingsoft_office.grid(row=2, column=3, padx=20, pady=20)
        self.freeoffice = customtkinter.CTkCheckBox(self.office_frame, text="FreeOffice", variable=self.check_freeoffice)
        self.freeoffice.grid(row=2, column=4, padx=20, pady=20)
        self.onlyoffice = customtkinter.CTkCheckBox(self.office_frame, text="OnlyOffice", variable=self.check_onlyoffice)
        self.onlyoffice.grid(row=3, column=0, padx=20, pady=20)
        self.microsoft_office = customtkinter.CTkCheckBox(self.office_frame, text="MS Office 365", variable=self.check_microsoft_office)
        self.microsoft_office.grid(row=3, column=1, padx=20, pady=20)
        
        self.office_spacer = customtkinter.CTkLabel(self.office_frame, text="")
        self.office_spacer.grid(row=4, column=4, padx=20, pady=244)
        
        self.install_office = customtkinter.CTkButton(self.office_frame, text="Install", command=self.install_office_packages)
        self.install_office.grid(row=4, column=4, padx=27, pady=30)

        # create runtime frame

        self.runtime_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in the Runtime frame
        
        self.vcredist = customtkinter.CTkCheckBox(self.runtime_frame, text="VCRedist", variable=self.check_vcredist)
        self.vcredist.grid(row=1, column=0, padx=20, pady=20)
        self.dotnet = customtkinter.CTkCheckBox(self.runtime_frame, text="DotNet", variable=self.check_dotnet)
        self.dotnet.grid(row=1, column=1, padx=20, pady=20)
        self.java = customtkinter.CTkCheckBox(self.runtime_frame, text="Java Runtime Environment", variable=self.check_java)
        self.java.grid(row=1, column=2, padx=20, pady=20)
        self.openjdk = customtkinter.CTkCheckBox(self.runtime_frame, text="OpenJDK (Latest)", variable=self.check_openjdk)
        self.openjdk.grid(row=1, column=3, padx=20, pady=20)
        
        self.openjdk8 = customtkinter.CTkCheckBox(self.runtime_frame, text="OpenJDK 8", variable=self.check_openjdk8)
        self.openjdk8.grid(row=2, column=0, padx=20, pady=20)
        self.directx = customtkinter.CTkCheckBox(self.runtime_frame, text="DirectX", variable=self.check_directx)
        self.directx.grid(row=2, column=1, padx=20, pady=20)
        
        self.runtime_spacer = customtkinter.CTkLabel(self.runtime_frame, text="")
        self.runtime_spacer.grid(row=3, column=3, padx=20, pady=130)
        
        self.install_runtime = customtkinter.CTkButton(self.runtime_frame, text="Install", command=self.install_runtime_packages)
        self.install_runtime.grid(row=4, column=3, padx=125, pady=20)

        # create security frame

        self.security_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in the Security Frame
        
        self.authme = customtkinter.CTkCheckBox(self.security_frame, text="AuthMe", variable=self.check_authme)
        self.authme.grid(row=1, column=0, padx=20, pady=20)
        self.authy = customtkinter.CTkCheckBox(self.security_frame, text="Authy", variable=self.check_authy)
        self.authy.grid(row=1, column=1, padx=20, pady=20)
        self.passwordhub = customtkinter.CTkCheckBox(self.security_frame, text="Password Hub", variable=self.check_passwordhub)
        self.passwordhub.grid(row=1, column=2, padx=20, pady=20)
        self.toofast = customtkinter.CTkCheckBox(self.security_frame, text="2fast", variable=self.check_toofast)
        self.toofast.grid(row=1, column=3, padx=20, pady=20)
        
        self.yubico = customtkinter.CTkCheckBox(self.security_frame, text="Yubico Authenticator", variable=self.check_yubico)
        self.yubico.grid(row=2, column=0, padx=20, pady=20)
        self.bitwarden = customtkinter.CTkCheckBox(self.security_frame, text="Bitwarden", variable=self.check_bitwarden)
        self.bitwarden.grid(row=2, column=1, padx=20, pady=20)
        self.keepass = customtkinter.CTkCheckBox(self.security_frame, text="Keepass", variable=self.check_keepass)
        self.keepass.grid(row=2, column=2, padx=20, pady=20)
        self.passwordsafe = customtkinter.CTkCheckBox(self.security_frame, text="Password Safe", variable=self.check_paswordsafe)
        self.passwordsafe.grid(row=2, column=3, padx=20, pady=20)
        
        self.dashlane = customtkinter.CTkCheckBox(self.security_frame, text="Dashlane", variable=self.check_dashlane)
        self.dashlane.grid(row=3, column=0, padx=20, pady=20)
        self.panda = customtkinter.CTkCheckBox(self.security_frame, text="Panda Free Antivirus", variable=self.check_panda)
        self.panda.grid(row=3, column=1, padx=20, pady=20)
        self.adw_cleaner = customtkinter.CTkCheckBox(self.security_frame, text="Adw Cleaner", variable=self.check_adw_cleaner)
        self.adw_cleaner.grid(row=3, column=2, padx=20, pady=20)
        self.calmav = customtkinter.CTkCheckBox(self.security_frame, text="CalmAV", variable=self.check_calmav)
        self.calmav.grid(row=3, column=3, padx=20, pady=20)
        
        self.security_spacer = customtkinter.CTkLabel(self.security_frame, text="")
        self.security_spacer.grid(row=4, column=3, padx=20, pady=98)
        
        self.install_security = customtkinter.CTkButton(self.security_frame, text="Install", command=self.install_security_packages)
        self.install_security.grid(row=5, column=3, padx=98, pady=20)

        # create media frame

        self.media_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things in Media Frame
        
        self.vlc = customtkinter.CTkCheckBox(self.media_frame, text="VLC", variable=self.check_vlc)
        self.vlc.grid(row=1, column=0, padx=20, pady=20)
        self.cider = customtkinter.CTkCheckBox(self.media_frame, text="Cider", variable=self.check_cider)
        self.cider.grid(row=1, column=1, padx=20, pady=20)
        self.gom = customtkinter.CTkCheckBox(self.media_frame, text="Gom Player", variable=self.check_gom_player)
        self.gom.grid(row=1, column=2, padx=20, pady=20)
        self.wondershare_filmora = customtkinter.CTkCheckBox(self.media_frame, text="Filmora", variable=self.check_wondershare_filmora)
        self.wondershare_filmora.grid(row=1, column=3, padx=20, pady=20)
        self.tidal = customtkinter.CTkCheckBox(self.media_frame, text="Tidal", variable=self.check_tidal)
        self.tidal.grid(row=1, column=4, padx=20, pady=20)
        
        self.audacium = customtkinter.CTkCheckBox(self.media_frame, text="Audacium", variable=self.check_audacium)
        self.audacium.grid(row=2, column=0, padx=20, pady=20)
        self.mypaint = customtkinter.CTkCheckBox(self.media_frame, text="MyPaint", variable=self.check_mypaint)
        self.mypaint.grid(row=2, column=1, padx=20, pady=20)
        self.audacity = customtkinter.CTkCheckBox(self.media_frame, text="Audacity", variable=self.check_audacity)
        self.audacity.grid(row=2, column=2, padx=20, pady=20)
        self.deezer = customtkinter.CTkCheckBox(self.media_frame, text="Deezer", variable=self.check_deezer)
        self.deezer.grid(row=2, column=3, padx=20, pady=20)
        self.spotify = customtkinter.CTkCheckBox(self.media_frame, text="Spotify", variable=self.check_spotify)
        self.spotify.grid(row=2, column=4, padx=20, pady=20)
        
        self.itunes = customtkinter.CTkCheckBox(self.media_frame, text="iTunes", variable=self.check_itunes)
        self.itunes.grid(row=3, column=0, padx=20, pady=20)
        self.clementine = customtkinter.CTkCheckBox(self.media_frame, text="Clementine", variable=self.check_clementine)
        self.clementine.grid(row=3, column=1, padx=20, pady=20)
        self.handbrake = customtkinter.CTkCheckBox(self.media_frame, text="Handbrake", variable=self.check_handbrake)
        self.handbrake.grid(row=3, column=2, padx=20, pady=20)
        self.kdenlive = customtkinter.CTkCheckBox(self.media_frame, text="KDEnLive", variable=self.check_kdenlive)
        self.kdenlive.grid(row=3, column=3, padx=20, pady=20)
        self.mpv = customtkinter.CTkCheckBox(self.media_frame, text="MPV", variable=self.check_mpv)
        self.mpv.grid(row=3, column=4, padx=20, pady=20)
        
        self.pot_player = customtkinter.CTkCheckBox(self.media_frame, text="Pot Player", variable=self.check_pot_player)
        self.pot_player.grid(row=4, column=0, padx=20, pady=20)
        self.paint_dot_net = customtkinter.CTkCheckBox(self.media_frame, text="Paint.Net", variable=self.check_paint_dot_net)
        self.paint_dot_net.grid(row=4, column=1, padx=20, pady=20)
        self.krita = customtkinter.CTkCheckBox(self.media_frame, text="Krita", variable=self.check_krita)
        self.krita.grid(row=4, column=2, padx=20, pady=20)
        self.tuxpaint = customtkinter.CTkCheckBox(self.media_frame, text="Tux Paint", variable=self.check_tuxpaint)
        self.tuxpaint.grid(row=4, column=3, padx=20, pady=20)
        self.gimp = customtkinter.CTkCheckBox(self.media_frame, text="GIMP", variable=self.check_gimp)
        self.gimp.grid(row=4, column=4, padx=20, pady=20)
        
        self.glimpse = customtkinter.CTkCheckBox(self.media_frame, text="Glimpse", variable=self.check_glimpse)
        self.glimpse.grid(row=5, column=0, padx=20, pady=20)
        self.photogimp = customtkinter.CTkCheckBox(self.media_frame, text="PhotoGIMP", variable=self.check_photogimp)
        self.photogimp.grid(row=5, column=1, padx=20, pady=20)
        self.upscayl = customtkinter.CTkCheckBox(self.media_frame, text="Upscay!", variable=self.check_upscayl)
        self.upscayl.grid(row=5, column=2, padx=20, pady=20)
        self.imageglass = customtkinter.CTkCheckBox(self.media_frame, text="ImageGlass", variable=self.check_imageglass)
        self.imageglass.grid(row=5, column=3, padx=20, pady=20)
        
        self.install_media = customtkinter.CTkButton(self.media_frame, text="Install", command=self.install_media_packages)
        self.install_media.grid(row=6, column=4, padx=65, pady=116)


        # create utilities frame

        self.utils_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Things on Utilities Frame
        
        self.winzip = customtkinter.CTkCheckBox(self.utils_frame, text="WinZip", variable=self.check_winzip)
        self.winzip.grid(row=1, column=0, padx=20, pady=20)
        self.flameshot = customtkinter.CTkCheckBox(self.utils_frame, text="Flameshot", variable=self.check_flameshot)
        self.flameshot.grid(row=1, column=1, padx=20, pady=20)
        self.notepad_plus_plus = customtkinter.CTkCheckBox(self.utils_frame, text="Notepad++", variable=self.check_notepad_plus_plus)
        self.notepad_plus_plus.grid(row=1, column=2, padx=20, pady=20)
        self.peazip = customtkinter.CTkCheckBox(self.utils_frame, text="PeaZip", variable=self.check_peazip)
        self.peazip.grid(row=1, column=3, padx=20, pady=20)
        self.atom = customtkinter.CTkCheckBox(self.utils_frame, text="Atom", variable=self.check_atom)
        self.atom.grid(row=1, column=4, padx=20, pady=20)
        
        self.sharex = customtkinter.CTkCheckBox(self.utils_frame, text="ShareX", variable=self.check_sharex)
        self.sharex.grid(row=2, column=0, padx=20, pady=20)
        self.trello = customtkinter.CTkCheckBox(self.utils_frame, text="Trello Desktop", variable=self.check_trello)
        self.trello.grid(row=2, column=1, padx=20, pady=20)
        self.sevenzip = customtkinter.CTkCheckBox(self.utils_frame, text="7-Zip", variable=self.check_sevenzip)
        self.sevenzip.grid(row=2, column=2, padx=20, pady=20)
        self.sublime_text = customtkinter.CTkCheckBox(self.utils_frame, text="Sublime Text", variable=self.check_sublime_text)
        self.sublime_text.grid(row=2, column=3, padx=20, pady=20)
        self.evernote = customtkinter.CTkCheckBox(self.utils_frame, text="Evernote", variable=self.check_evernote)
        self.evernote.grid(row=2, column=4, padx=20, pady=20)
        
        self.notion = customtkinter.CTkCheckBox(self.utils_frame, text="Notion", variable=self.check_notion)
        self.notion.grid(row=3, column=0, padx=20, pady=20)
        self.winrar = customtkinter.CTkCheckBox(self.utils_frame, text="Winrar", variable=self.check_winrar)
        self.winrar.grid(row=3, column=1, padx=20, pady=20)
        self.visual_studio_code = customtkinter.CTkCheckBox(self.utils_frame, text="VS Code", variable=self.check_visual_studio_code)
        self.visual_studio_code.grid(row=3, column=2, padx=20, pady=20)
        self.imgburn = customtkinter.CTkCheckBox(self.utils_frame, text="IMGBurn", variable=self.check_imgburn)
        self.imgburn.grid(row=3, column=3, padx=20, pady=20)
        self.powertoys = customtkinter.CTkCheckBox(self.utils_frame, text="Powertoys", variable=self.check_powertoys)
        self.powertoys.grid(row=3, column=4, padx=20, pady=20)
        
        self.sysinternals_suite = customtkinter.CTkCheckBox(self.utils_frame, text="Sysinternals Suite", variable=self.check_sysinternals_suite)
        self.sysinternals_suite.grid(row=4, column=0, padx=20, pady=20)
        self.teracopy = customtkinter.CTkCheckBox(self.utils_frame, text="Teracopy", variable=self.check_teracopy)
        self.teracopy.grid(row=4, column=1, padx=20, pady=20)
        self.adb = customtkinter.CTkCheckBox(self.utils_frame, text="ADB", variable=self.check_adb)
        self.adb.grid(row=4, column=2, padx=20, pady=20)
        self.flow = customtkinter.CTkCheckBox(self.utils_frame, text="Flow Launcher", variable=self.check_flow)
        self.flow.grid(row=4, column=3, padx=20, pady=20)
        self.adguard = customtkinter.CTkCheckBox(self.utils_frame, text="Adguard", variable=self.check_adguard)
        self.adguard.grid(row=4, column=4, padx=20, pady=20)
        
        self.install_utils = customtkinter.CTkButton(self.utils_frame, text="Install", command=self.install_media_packages)
        self.install_utils.grid(row=5, column=4, padx=7, pady=180)
        
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
        if self.check_brave_browser.get() == 1:
            print('brave')
            os.system('winget install -e -id Brave.Brave')
            
        if self.check_microsoft_edge.get() == 1:
            print('edge')
            os.system('winget install -e --id Microsoft.Edge')
            
        if self.check_k_meleon.get() == 1:
            print('k meleon')
            os.system('winget install -e --id kmeleonbrowser.K-Meleon')
            
        if self.check_google_chrome.get() == 1:
            print('chrome')
            os.system('winget install -e --id Google.Chrome')
            
        if self.check_vivaldi.get() == 1:
            print('vivaldi')
            os.system('winget install -e --id VivaldiTechnologies.Vivaldi')
            
        if self.check_opera.get() == 1:
            print('opera')
            os.system('winget install -e --id Opera.Opera')
            
        if self.check_mozilla_firefox.get() == 1:
            print('firefox')
            os.system('winget install -e --id Mozilla.Firefox')
            
        if self.check_libreoffice.get() == 1:
            print('librewolf')
            os.system('winget install -e --id LibreWolf.LibreWolf')
            
        if self.check_pale_moon.get() == 1:
            print('pale moon')
            os.system('winget install -e --id MoonchildProductions.PaleMoon')
            
        if self.check_waterfox.get() == 1:
            print('waterfox')
            os.system('winget install -e --if Waterfox.Waterfox')
            
        if self.check_midori.get() == 1:
            print('midori')
            os.system('choco install midori-browser')
            
        if self.check_opera_gx.get() == 1:
            print('opera gx')
            os.system('winget install -e --id Opera.OperaGX')
        
        if self.check_brave_browser.get() == 0 and self.check_microsoft_edge.get() == 0 and self.check_k_meleon.get() == 0 and self.check_google_chrome.get() == 0 and self.check_vivaldi.get() == 0 and self.check_opera.get() == 0 and self.check_mozilla_firefox.get() == 0 and self.check_librewolf.get() == 0 and self.check_pale_moon.get() == 0 and self.check_waterfox.get() == 0 and self.check_midori.get() == 0 and self.check_opera_gx.get() == 0:
            print('No browser selected')
    
    def install_game_packages(self):
        if self.check_retroarch.get() == 1:
            print('Retroarch')
            os.system('winget install -e --id Libretro.RetroArch')
        
        if self.check_amazon_games.get() == 1:
            print('Amazon Games')
            os.system('winget install -e --id Amazon.Games')
            
        if self.check_ubisoft_connect.get() == 1:
            print('Ubisoft Connect')
            os.system('winget install -e --id Ubisoft.Connect')
            
        if self.check_dolphin.get() == 1:
            print('Dolphin Emulator')
            os.system('winget install -e --id DolphinEmulator.Dolphin')
            
        if self.check_rpcs3.get() == 1:
            print('RPCS3 Emulator')
            os.system('scoop bucket add games')
            os.system('scoop install games/rpcs3')
            
        if self.check_epic_games_launcher.get() == 1:
            print('Epic Games Launcher')
            os.system('winget install -e --id EpicGames.EpicGamesLauncher')
            
        if self.check_pcsx2.get() == 1:
            print('PCSX2 Emulator')
            os.system('choco install pcsx2')
            
        if self.check_yuzu.get() == 1:
            print('Yuzu Emulator')
            os.system('scoop bucket add games')
            os.system('scoop install games/yuzu')
            
        if self.check_heroic_games_launcher.get() == 1:
            print('Heroic Games Launcher')
            os.system('winget install -e --id HeroicGamesLauncher.HeroicGamesLauncher')

        if self.check_gog_galaxy.get() == 1:
            print('GOG Galaxy')
            os.system('winget install -e --id GOG.Galaxy')
            
        if self.check_itch_io.get() == 1:
            print('Itch.IO')
            os.system('winget install -e --id ItchIo.Itch')

        if self.check_minecraft_launcher.get() == 1:
            print('Minecraft Launcher')
            os.system('winget install -e --id Mojang.MinecraftLauncher')
            
        if self.check_steam.get() == 1:
            print('Steam')
            os.system('winget install -e --id Valve.Steam')
            
        if self.check_ea_app.get() == 1:
            print('EA App')
            os.system('winget install -e --id ElectronicArts.EADesktop')
            
        if self.check_gdlauncher.get() == 1:
            print('GDLauncher')
            os.system('winget install -e --id GorillaDevs.GDLauncher')
            
        if self.check_curseforge.get() == 1:
            print('CurseForge')
            os.system('winget install -e --id Overwolf.CurseForge')
            
        if self.check_battle_net.get() == 1:
            print('Battle.net')
            print('not yet implemented')
            
        if self.check_citra.get() == 1:
            print('Citra Emulator')
            os.system('scoop bucket add games')
            os.system('scoop install games/citra')
            
        if self.check_ppsspp.get() == 1:
            print('PPSSPP Emulator')
            os.system('winget install -e --id PPSSPPTeam.PPSSPP')
            
        if self.check_blitz.get() == 1:
            print('Blitz')
            os.system('winget install -e --id Blitz.Blitz')
            
        if self.check_playnite.get() == 1:
            print('Playnite')
            os.system('winget install -e --id Playnite.Playnite')
            
        if self.check_retroarch.get() == 0 and self.check_amazon_games.get() == 0 and self.check_ubisoft_connect.get() == 0 and self.check_dolphin.get() == 0 and self.check_rpcs3.get() == 0 and self.check_epic_games_launcher.get() == 0 and self.check_pcsx2.get() == 0 and self.check_yuzu.get() == 0 and self.check_heroic_games_launcher.get() == 0 and self.check_gog_galaxy.get() == 0 and self.check_itch_io.get() == 0 and self.check_minecraft_launcher.get() == 0 and self.check_steam.get() == 0 and self.check_ea_app.get() == 0 and self.check_gdlauncher.get() == 0 and self.check_curseforge.get() == 0 and self.check_battle_net.get() == 0 and self.check_citra.get() == 0 and self.check_ppsspp.get() == 0 and self.check_blitz.get() == 0 and self.check_playnite.get() == 0:
            print('No game related software selected')
    
    def install_messaging_packages(self):
        if self.check_zoom.get() == 1:
            print('Zoom')
            os.system('winget install -e --id Zoom.Zoom')
            
        if self.check_guilded.get() == 1:
            print('Guilded')
            os.system('winget install -e --id Guilded.Guilded')
            
        if self.check_slack.get() == 1:
            print('Slack')
            os.system('winget install -e --id SlackTechnologies.Slack')
            
        if self.check_hexchat.get() == 1:
            print('HexChat')
            os.system('winget install -e --id HexChat.HexChat')
            
        if self.check_skype.get() == 1:
            print('Skype')
            os.system('winget install -e --id Microsoft.Skype')

        if self.check_discord.get() == 1:
            print('Discord')
            os.system('winget install -e --id Discord.Discord')
            
        if self.check_teamspeak.get() == 1:
            print('TeamSpeak 3')
            os.system('winget install -e --id TeamSpeakSystems.TeamSpeakClient')
            
        if self.check_telegram.get() == 1:
            print('Telegram Desktop')
            os.system('winget install -e --id Telegram.TelegramDesktop')
            
        if self.check_whatsapp.get() == 1:
            print('WhatsApp Desktop')
            os.system('winget install -e --id WhatsApp.WhatsApp')
            
        if self.check_viber.get() == 1:
            print('Viber Desktop')
            os.system('winget install -e --id Viber.Viber')
            
        if self.check_microsoft_teams.get() == 1:
            print('Microsoft Teams')
            os.system('winget install -e --id Microsoft.Teams')
            
        if self.check_signal.get() == 1:
            print('Signal Desktop')
            os.system('winget install -e --id OpenWhisperSystems.Signal')
            
        if self.check_zoom.get() == 0 and self.check_guilded.get() == 0 and self.check_slack.get() == 0 and self.check_hexchat.get() == 0 and self.check_skype.get() == 0 and self.check_discord.get() == 0 and self.check_teamspeak.get() == 0 and self.check_telegram.get() == 0 and self.check_whatsapp.get() == 0 and self.check_viber.get() == 0 and self.check_microsoft_teams.get() == 0 and self.check_signal.get() == 0:
            print('No messaging software selected')
    
    def install_office_packages(self):

        if self.check_sedja_pdf.get() == 1:
            print('Sedja PDF')
            print('Not Yet Implemented')

        if self.check_sumatra_pdf.get() == 1:
            print('SumatraPDF')
            os.system('winget install -e --id SumatraPDF.SumatraPDF')

        if self.check_adobe_reader.get() == 1:
            print('Adobe Reader')
            os.system('winget install -e --id Adobe.Acrobat.Reader.32-bit')

        if self.check_wps_office.get() == 1:
            print('WPS Office')
            os.system('winget install -e --id Kingsoft.WPSOffice.CN')

        if self.check_masterpdf.get() == 1:
            print('Master PDF')
            os.system('choco install master-pdf-editor')

        if self.check_foxit_reader.get() == 1:
            print('Foxit Reader')
            os.system('winget install -e --id Foxit.FoxitReader')

        if self.check_libreoffice.get() == 1:
            print('Libreoffice')
            os.system('winget install -e --id TheDocumentFoundation.LibreOffice')

        if self.check_openoffice.get() == 1:
            print('Openoffice')
            os.system('winget install -e --id Apache.OpenOffice')

        if self.check_kingsoft_office.get() == 1:
            print('Kingsoft Office')
            os.system('choco install kingsoft-office-free')

        if self.check_freeoffice.get() == 1:
            print('Freeoffice')
            os.system('winget install -e --id SoftMaker.FreeOffice.2021')

        if self.check_onlyoffice.get() == 1:
            print('onlyoffice')
            os.system('winget install -e --id ONLYOFFICE.DesktopEditors')

        if self.check_microsoft_office.get() == 1:
            print('Microsoft Office')
            os.system('winget install -e --id matvelloso.electron-office-365')

        if self.check_sedja_pdf.get() == 0 and self.check_sumatra_pdf.get() == 0 and self.check_adobe_reader.get() == 0 and self.check_wps_office.get() == 0 and self.check_masterpdf.get() == 0 and self.check_foxit_reader.get() == 0 and self.check_libreoffice.get() == 0 and self.check_openoffice.get() == 0 and self.check_kingsoft_office.get() == 0 and self.check_freeoffice.get() == 0 and self.check_onlyoffice.get() == 0 and self.check_microsoft_office.get() == 0:
            print('No office suite selected')
    
    def install_runtime_packages(self):

        if self.check_vcredist.get() == 1:
            print('vcredist')
            os.system('winget install -e --id Microsoft.VCRedist.2013.x64')

        if self.check_dotnet.get() == 1:
            print('dotnet')
            os.system('winget install -e --id Microsoft.DotNet.Framework.DeveloperPack_4')

        if self.check_java.get() == 1:
            print('Java')
            os.system('winget install -e --id Oracle.JavaRuntimeEnvironment')

        if self.check_openjdk.get() == 1:
            print('OpenJDK (Latest)')
            os.system('winget install -e --id ojdkbuild.openjdk.11.jre')

        if self.check_openjdk8.get() == 1:
            print('OpenJDK 8')
            os.system('choco install openjdk8')

        if self.check_directx.get() == 1:
            print('DirectX')
            os.system('winget install -e --id Microsoft.DirectX')
        
        if self.check_vcredist.get() == 0 and self.check_dotnet.get() == 0 and self.check_java.get() == 0 and self.check_openjdk.get == 0 and self.check_openjdk8.get() == 0 and self.check_directx.get() == 0:
            print('No Runtimes Selected')
    
    def install_security_packages(self):

        if self.check_authme.get() == 1:
            print('Authme')
            os.system('winget install -e --id Levminer.Authme')

        if self.check_authy.get() == 1:
            print('Authy')
            os.system('winget install -e --id Twilio.Authy')

        if self.check_passwordhub.get() == 1:
            print('Passwordhub')
            print('Not yet implemented')

        if self.check_toofast.get() == 1:
            print('2fast')
            os.system('choco install 2fast')

        if self.check_yubico.get() == 1:
            print('yubico')
            os.system('winget install -e --id Yubico.Authenticator')

        if self.check_bitwarden.get() == 1:
            print('bitwarden')
            os.system('winget install -e --id Bitwarden.Bitwarden')

        if self.check_keepass.get() == 1:
            print('Keepass')
            os.system('winget install -e --id DominikReichl.KeePass')

        if self.check_paswordsafe.get() == 1:
            print('Password Safe')
            os.system('winget install -e --id RonyShapiro.PasswordSafe')

        if self.check_dashlane.get() == 1:
            print('dashlane')
            os.system('winget install -e --id Dashlane.Dashlane')

        if self.check_panda.get() == 1:
            print('Panda antivirus')
            os.system('choco install pandafreeantivirus')

        if self.check_adw_cleaner.get() == 1:
            print('ADW Cleaner')
            os.system('choco install adwcleaner')

        if self.check_calmav.get() == 1:
            print('CalmAV')
            print('Not yet implemented')

        if self.check_authme.get() == 0 and self.check_authy.get() == 0 and self.check_passwordhub.get() == 0 and self.check_toofast.get() == 0 and self.check_yubico.get() == 0 and self.check_bitwarden.get() == 0 and self.check_keepass.get() == 0 and self.check_paswordsafe.get() == 0 and self.check_dashlane.get() == 0 and self.check_panda.get() == 0 and self.check_adw_cleaner.get() == 0 and self.check_calmav.get == 0:
            print('No security software selected')
    
    def install_media_packages(self):

        if self.check_vlc.get() == 1:
            print('vlc')
            os.system('winget install -e --id VideoLAN.VLC')

        if self.check_cider.get() == 1:
            print('cider')
            os.system('winget install -e --id CiderCollective.Cider')

        if self.check_gom_player.get() == 1:
            print('Gom Player')
            os.system('winget install -e --id GOMLab.GOMPlayer')

        if self.check_wondershare_filmora.get() == 1:
            print('Wondershare Filmora')
            os.system('winget install -e --id Wondershare.Filmora')

        if self.check_tidal.get() == 1:
            print('tidal')
            os.system('winget install -e --id TIDALMusicAS.TIDAL')

        if self.check_audacium.get() == 1:
            print('audacium')
            os.system('winget install -e --id SartoxOnlyGNU.Audacium')

        if self.check_mypaint.get() == 1:
            print('MyPaint')
            os.system('winget install -e --id MyPaint.MyPaint')

        if self.check_audacity.get() == 1:
            print('Audacity')
            os.system('winget install -e --id Audacity.Audacity')

        if self.check_deezer.get() == 1:
            print('Deezer')
            os.system('winget install -e --id Deezer.Deezer')

        if self.check_spotify.get() == 1:
            print('Spotify')
            os.system('winget install -e --id Spotify.Spotify')

        if self.check_itunes.get() == 1:
            print('iTunes')
            os.system('winget install -e --id Apple.iTunes')

        if self.check_clementine.get() == 1:
            print('clementine')
            os.system('winget install -e --id Clementine.Clementine')

        if self.check_handbrake.get() == 1:
            print('Handbrake')
            os.system('winget install -e --id HandBrake.HandBrake')

        if self.check_kdenlive.get() == 1:
            print('KDEnlive')
            os.system('winget install -e --id KDE.Kdenlive')

        if self.check_mpv.get() == 1:
            print('MPV')
            os.system('choco install mpv')

        if self.check_pot_player.get() == 1:
            print('Pot Player')
            os.system('winget install -e --id Daum.PotPlayer')

        if self.check_paint_dot_net.get() == 1:
            print('Paint.NET')
            os.system('winget install -e --id dotPDNLLC.paintdotnet')

        if self.check_krita.get() == 1:
            print('Krita')
            os.system('winget install -e --id KDE.Krita')

        if self.check_tuxpaint.get() == 1:
            print('TuxPaint')
            os.system('winget install -e --id NewBreedSoftware.TuxPaint')

        if self.check_gimp.get() == 1:
            print('GIMP')
            os.system('winget install -e --id GIMP.GIMP')

        if self.check_glimpse.get() == 1:
            print('Glimpse')
            os.system('winget install -e --id Glimpse.Glimpse')

        if self.check_photogimp.get() == 1:
            print('Photogimp')
            os.system('choco install photogimp')

        if self.check_upscayl.get() == 1:
            print('Upscay!')
            os.system('winget install -e --id Upscayl.Upscayl')

        if self.check_imageglass.get() == 1:
            print('Imageglass')
            os.system('winget install -e --id DuongDieuPhap.ImageGlass')
        
        if self.check_vlc.get() == 0 and self.check_cider.get() == 0 and self.check_gom_player.get() == 0 and self.check_wondershare_filmora.get() == 0 and self.check_tidal.get() == 0 and self.check_audacium.get() == 0 and self.check_mypaint.get() == 0 and self.check_audacity.get() == 0 and self.check_deezer.get() == 0 and self.check_spotify.get() == 0 and self.check_itunes.get() == 0 and self.check_clementine.get() == 0 and self.check_handbrake.get() == 0 and self.check_kdenlive.get() == 0 and self.check_mpv.get() == 0 and self.check_pot_player.get() == 0 and self.check_paint_dot_net.get() == 0 and self.check_krita.get() == 0 and self.check_tuxpaint.get() == 0 and self.check_gimp.get() == 0 and self.check_glimpse.get() == 0 and self.check_photogimp.get() == 0 and self.check_upscayl.get() == 0 and self.check_imageglass.get() == 0:
            print('No Media Software Selected')
    
    def install_util_packages(self):

        if self.check_winzip.get() == 1:
            print('Winzip')
            os.system('winget install -e --id Corel.WinZip')

        if self.check_flameshot.get() == 1:
            print('flameshot')
            os.system('winget install -e --id Flameshot.Flameshot')

        if self.check_notepad_plus_plus.get() == 1:
            print('Notepad++')
            os.system('winget install -e --id Notepad++.Notepad++')

        if self.check_peazip.get() == 1:
            print('PeaZip')
            os.system('winget install -e --id Giorgiotani.Peazip')

        if self.check_atom.get() == 1:
            print('Atom')
            os.system('winget install -e --id GitHub.Atom')

        if self.check_sharex.get() == 1:
            print('ShareX')
            os.system('winget install -e --id ShareX.ShareX')

        if self.check_trello.get() == 1:
            print('trello')
            os.system('choco install whale')

        if self.check_sevenzip.get() == 1:
            print('7-zip')
            os.system('winget install -e --id 7zip.7zip')

        if self.check_sublime_text.get() == 1:
            print('Sublime Text')
            os.system('winget install -e --id SublimeHQ.SublimeText.4')

        if self.check_evernote.get() == 1:
            print('Evernote')
            os.system('winget install -e --id evernote.evernote')

        if self.check_notion.get() == 1:
            print('Notion')
            os.system('winget install -e --id Notion.Notion')

        if self.check_winrar.get() == 1:
            print('WinRAR')
            os.system('winget install -e --id RARLab.WinRAR')

        if self.check_visual_studio_code.get() == 1:
            print('VS Code')
            os.system('winget install -e --id Microsoft.VisualStudioCode')

        if self.check_imgburn.get() == 1:
            print('imgburn')
            os.system('winget install -e --id LIGHTNINGUK.ImgBurn')

        if self.check_powertoys.get() == 1:
            print('Powertoys')
            os.system('winget install -e --id Microsoft.PowerToys')

        if self.check_sysinternals_suite.get() == 1:
            print('Sysinternals Suite')
            os.system('choco install sysinternals')

        if self.check_teracopy.get() == 1:
            print('Teracopy')
            os.system('winget install -e --id CodeSector.TeraCopy')

        if self.check_adb.get() == 1:
            print('ADB')
            os.system('winget install -e --id ClockworkMod.UniversalADBDriver')

        if self.check_flow.get() == 1:
            print('Flow Launcher')
            os.system('winget install -e --id Flow-Launcher.Flow-Launcher')

        if self.check_adguard.get() == 1:
            print('Adguard')
            os.system('winget install -e --id AdGuard.AdGuard')

        if self.check_winzip.get() == 0 and self.check_flameshot.get() == 0 and self.check_notepad_plus_plus.get() == 0 and self.check_peazip.get() == 0 and self.check_atom.get() == 0 and self.check_sharex.get() == 0 and self.check_trello.get() == 0 and self.check_sevenzip.get() == 0 and self.check_sublime_text.get() == 0 and self.check_evernote.get() == 0 and self.check_notion.get() == 0 and self.check_winrar.get() == 0 and self.check_visual_studio_code.get() == 0 and self.check_imgburn.get() == 0 and self.check_powertoys.get() == 0 and self.check_sysinternals_suite.get() == 0 and self.check_teracopy.get() == 0 and self.check_adb.get() == 0 and self.check_flow.get() == 0 and self.check_adguard.get() == 0:
            print('No Utilities Selected')


if __name__ == "__main__":
    app = App()
    app.mainloop()
