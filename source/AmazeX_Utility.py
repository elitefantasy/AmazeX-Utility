# Author                :Anil
# Sources               :Self
# Date Of Creation      :2022-05-30
# Last time Modified    :2022-06-10
# Description           :Utility which installs popular program with ease,
#                       :updates them, and includes (Ultimate Titus utility Script),One stop for all AmazeX Programs too.

import threading
import subprocess
import os
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import customtkinter
import requests
import urllib.request

root=customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")
root.geometry("900x600")
root.title('AmazeX Utility')


current_file_path=__file__
cwd_of_utility=os.path.dirname(current_file_path)
os.chdir(cwd_of_utility)


##### Variables ####
username=os.getlogin()
fileUrlAHK="https://github.com/elitefantasy/AmazeX-AHK/raw/main/Distribution/AmazeX%20AHK/Scripts/Setup/Setup.exe"
fileUrl_AkmDownloadSorter="https://github.com/elitefantasy/AKM-DownloadSorter/raw/main/Dist/AkmDowloadSorter_Setup.exe"



# Creating frames
install_frame = customtkinter.CTkFrame(master=root,width=900,height=800,corner_radius=10)

home_frame = customtkinter.CTkFrame(master=root,width=900,height=800,corner_radius=10)
home_frame.pack(fill="both",expand=1,padx=30, pady=30) #this frame will be shown first

#function for Menu buttons
def show_home_frame():
    hide_all_frames()
    home_frame.pack(fill="both",expand=1,padx=30, pady=30)

def show_install_frame():
    hide_all_frames()
    install_frame.pack(fill="both",expand=1,padx=20, pady=30)

def hide_all_frames(): # destroys previous frame for new to appear
    home_frame.pack_forget()
    install_frame.pack_forget()

########### Menu buttons ##########
home_butt=customtkinter.CTkButton(master=root, text="Home",fg_color="#00a884",hover_color="#00755b",command=lambda: show_home_frame())
home_butt.place(x=4, y=1)
install_butt=customtkinter.CTkButton(master=root, text="Install",fg_color="#00a884",hover_color="#00755b",command=lambda: show_install_frame())
install_butt.place(x=148, y=1)


# _________________________________________________
# Home Menu Functions
# _________________________________________________

def install_chocolatey():
    subprocess.call(r"batch\\install_chocolatey.bat")

def showProgbar(name):
    global prog
    prog=tk.Tk()
    prog.geometry('300x120')
    prog.grid()

    text=ttk.Label(prog,text=f"Downloading {name} Pls Wait....")
    text.grid(column=0,row=0)

    pb = ttk.Progressbar(prog,orient='horizontal',mode='indeterminate',length=280)
    pb.grid(column=0, row=1, columnspan=2, padx=10, pady=20)
    pb.start()

    global text2
    text2=ttk.Label(prog,text="")
    text2.grid(row=2,column=0)

    global text3
    text3=ttk.Label(prog,text="")
    text3.grid(row=3,column=0)

    prog.mainloop()

def askokcancel(url):
    global askokcancel_response
    file=urllib.request.urlopen(url)
    fileSizeByte=int(file.length)
    fileSizeMb=str(int(fileSizeByte/1048576))
    askokcancel_response=messagebox.askokcancel("Info",f"Will Download {fileSizeMb} mb of file Size.!\nClick Ok to Continue")
    
def downAHK():
    askokcancel(url=fileUrlAHK)

    if askokcancel_response==True:
        def showProgramprogbar():
            showProgbar(name="AmazeX AHK")
        threadingProgram=threading.Thread(target=showProgramprogbar)
        threadingProgram.start()

        def download_file():
            response = requests.get(fileUrlAHK)
            text2.config(text="Program Installation")
            open("Setup.exe", "wb").write(response.content)
            subprocess.call("Setup.exe",shell=True)
            os.remove("Setup.exe")
            Install_AmazeX_AHK_lnk=subprocess.Popen([f"C:\\Users\\{username}\\AppData\\Local\\AmazeX AHK\\Install AmazeX AHK.lnk"],shell=True)
            Install_AmazeX_AHK_lnk.wait()
            Install_AmazeX_AHK_lnk.terminate()
            text3.config(text="Done/Exit")
            sleep(3)
            prog.destroy()
        threading_download_file=threading.Thread(target=download_file)
        threading_download_file.start()

def downAkmSorter():
    askokcancel(url=fileUrl_AkmDownloadSorter)

    if askokcancel_response==True:
        def showProgramprogbar():
            showProgbar(name="AkmDownloadSorter")
        threadingProgram=threading.Thread(target=showProgramprogbar)
        threadingProgram.start()

        def download_file():
            response = requests.get(fileUrl_AkmDownloadSorter)
            text2.config(text="Program Installation")
            open("Setup.exe", "wb").write(response.content)
            subprocess.call("Setup.exe",shell=True)
            os.remove("Setup.exe")
            text3.config(text="Done/Exit")
            sleep(3)
            prog.destroy()
        threading_download_file=threading.Thread(target=download_file)
        threading_download_file.start()
# _________________________________________________
# Home Menu Widgets
# _________________________________________________
def show_Home_Menu_Widgets():
    text_label=customtkinter.CTkLabel(home_frame,text="AmazeX Utility",text_color="sky blue",text_font=("consolas bold",24))
    text_label.place(relx=0.35,rely=0.01)

    text_label=customtkinter.CTkLabel(home_frame,text="This Utility Requires Chocolatey Package Manager to install other \nprograms, Make sure it is installed on your system beofre installing anything!!.",text_font=("consolas bold",12))
    text_label.place(relx=0.01,rely=0.1)

    button=customtkinter.CTkButton(home_frame,text="Install Chocolatey",fg_color="red",hover_color="#b20000",command=install_chocolatey,width=170)
    button.place(relx=0.01,rely=0.2)

    button=customtkinter.CTkButton(master=home_frame,text="Download AmazeX AHK",command=downAHK,width=170)
    button.place(relx=0.01,rely=0.3)
    
    button=customtkinter.CTkButton(master=home_frame,text="Download AKM Sorter",command=downAkmSorter,width=170)
    button.place(relx=0.01,rely=0.4)
show_Home_Menu_Widgets()





# _________________________________________________
# Install Menu Widgets
# _________________________________________________

heading_tx=customtkinter.CTkLabel(master=install_frame,text="Install Programs",text_color="blue",text_font=("Consolas bold",24))
heading_tx.grid(row=0,column=0,columnspan=2)

photos=customtkinter.CTkLabel(master=install_frame,text="Photos",text_font=("Consolas Bold",15),text_color="sky blue")
photos.grid(row=1,column=0,pady=5,sticky=W)

is_Canva_checked=IntVar() # taking variableOutput
install_Canva_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Canva", variable=is_Canva_checked, onvalue="1", offvalue="0")
# install_Canva_cb.place(relx=0.01,rely=0.1)
install_Canva_cb.grid(row=2,column=0,pady=3,padx=5,sticky=W)

is_Sharex_checked=IntVar()
install_Sharex_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Sharex", variable=is_Sharex_checked, onvalue="1", offvalue="0")
install_Sharex_cb.grid(row=3,column=0,pady=3,padx=5,sticky=W)

is_Greenshot_checked=IntVar()
install_Greenshot_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Greenshot", variable=is_Greenshot_checked, onvalue="1", offvalue="0")
install_Greenshot_cb.grid(row=4,column=0,pady=3,padx=5,sticky=W)

is_Irfanview_checked=IntVar()
install_Irfanview_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Irfanview", variable=is_Irfanview_checked, onvalue="1", offvalue="0")
install_Irfanview_cb.grid(row=5,column=0,pady=3,padx=5,sticky=W)

Browser=customtkinter.CTkLabel(master=install_frame,text="Browser",text_font=("Consolas Bold",15),text_color="sky blue")
Browser.grid(row=1,column=1,pady=5,sticky=W)

is_Chrome_checked=IntVar()
install_Chrome_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Chrome", variable=is_Chrome_checked, onvalue="1", offvalue="0")
install_Chrome_cb.grid(row=2,column=1,pady=3,padx=5,sticky=W)

is_Brave_checked=IntVar()
install_Brave_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Brave", variable=is_Brave_checked, onvalue="1", offvalue="0")
install_Brave_cb.grid(row=3,column=1,pady=3,padx=5,sticky=W)

is_Firefox_checked=IntVar()
install_Firefox_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Firefox", variable=is_Firefox_checked, onvalue="1", offvalue="0")
install_Firefox_cb.grid(row=4,column=1,pady=3,padx=5,sticky=W)

Social=customtkinter.CTkLabel(master=install_frame,text="Social",text_font=("Consolas Bold",15),text_color="sky blue")
Social.grid(row=1,column=2,pady=5,sticky=W)

is_Discord_checked=IntVar()
install_Discord_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Discord", variable=is_Discord_checked, onvalue="1", offvalue="0")
install_Discord_cb.grid(row=2,column=2,pady=3,padx=5,sticky=W)

is_Whatsapp_checked=IntVar()
install_Whatsapp_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Whatsapp", variable=is_Whatsapp_checked, onvalue="1", offvalue="0")
install_Whatsapp_cb.grid(row=3,column=2,pady=3,padx=5,sticky=W)

is_Telegram_checked=IntVar()
install_Telegram_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Telegram", variable=is_Telegram_checked, onvalue="1", offvalue="0")
install_Telegram_cb.grid(row=4,column=2,pady=3,padx=5,sticky=W)

Development=customtkinter.CTkLabel(master=install_frame,text="Development",text_font=("Consolas Bold",15),text_color="sky blue")
Development.grid(row=1,column=3,pady=5,sticky=W)

is_VsCode_checked=IntVar()
install_VsCode_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Vs Code", variable=is_VsCode_checked, onvalue="1", offvalue="0")
install_VsCode_cb.grid(row=2,column=3,pady=3,padx=5,sticky=W)

is_SublimeText_checked=IntVar()
install_SublimeText_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Sublime Text", variable=is_SublimeText_checked, onvalue="1", offvalue="0")
install_SublimeText_cb.grid(row=3,column=3,pady=3,padx=5,sticky=W)

is_GithubDesktop_checked=IntVar()
install_GithubDesktop_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Github Desktop", variable=is_GithubDesktop_checked, onvalue="1", offvalue="0")
install_GithubDesktop_cb.grid(row=4,column=3,pady=3,padx=5,sticky=W)

is_Git_checked=IntVar()
install_Git_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Git", variable=is_Git_checked, onvalue="1", offvalue="0")
install_Git_cb.grid(row=5,column=3,pady=3,padx=5,sticky=W)

Documents=customtkinter.CTkLabel(master=install_frame,text="Documents",text_font=("Consolas Bold",15),text_color="sky blue")
Documents.grid(row=9,column=0,pady=3,sticky=W)

is_Drawboard_checked=IntVar()
install_Drawboard_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Drawboard", variable=is_Drawboard_checked, onvalue="1", offvalue="0")
install_Drawboard_cb.grid(row=10,column=0,pady=3,padx=5,sticky=W)

is_Xodo_checked=IntVar()
install_Xodo_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Xodo", variable=is_Xodo_checked, onvalue="1", offvalue="0")
install_Xodo_cb.grid(row=11,column=0,pady=3,padx=5,sticky=W)

is_Notepadsplusplus_checked=IntVar()
install_Notepadsplusplus_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Notepads ++", variable=is_Notepadsplusplus_checked, onvalue="1", offvalue="0")
install_Notepadsplusplus_cb.grid(row=12,column=0,pady=5,padx=5,sticky=W)

is_Notepads_checked=IntVar()
install_Notepads_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Notepads", variable=is_Notepads_checked, onvalue="1", offvalue="0")
install_Notepads_cb.grid(row=13,column=0,pady=3,padx=5,sticky=W)

is_Obsidian_checked=IntVar()
install_Obsidian_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Obsidian", variable=is_Notepads_checked, onvalue="1", offvalue="0")
install_Obsidian_cb.grid(row=14,column=0,pady=3,padx=5,sticky=W)

Other=customtkinter.CTkLabel(master=install_frame,text="Other",text_font=("Consolas Bold",15),text_color="sky blue")
Other.grid(row=9,column=1,pady=5,sticky=W)

is_vlc_checked=IntVar()
install_vlc_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Vlc", variable=is_vlc_checked, onvalue="1", offvalue="0")
install_vlc_cb.grid(row=10,column=1,pady=3,sticky=W)

is_Spotify_checked=IntVar()
install_Spotify_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Spotify", variable=is_Spotify_checked, onvalue="1", offvalue="0")
install_Spotify_cb.grid(row=11,column=1,pady=3,sticky=W)

is_QtTabBar_checked=IntVar()
install_QtTabBar_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="QtTabBar", variable=is_QtTabBar_checked, onvalue="1", offvalue="0")
install_QtTabBar_cb.grid(row=12,column=1,pady=3,sticky=W)

is_AutoHotkey_checked=IntVar()
install_AutoHotkey_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="AutoHotkey", variable=is_AutoHotkey_checked, onvalue="1", offvalue="0")
install_AutoHotkey_cb.grid(row=13,column=1,pady=3,sticky=W)

is_Teamviewer_checked=IntVar()
install_Teamviewer_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Teamviewer", variable=is_Teamviewer_checked, onvalue="1", offvalue="0")
install_Teamviewer_cb.grid(row=14,column=1,pady=3,sticky=W)

Utilities=customtkinter.CTkLabel(master=install_frame,text="Utilities",text_font=("Consolas Bold",15),text_color="sky blue")
Utilities.grid(row=9,column=2,pady=5,sticky=W)

is_Taskbarx_checked=IntVar()
install_Taskbarx_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Taskbarx", variable=is_Taskbarx_checked, onvalue="1", offvalue="0")
install_Taskbarx_cb.grid(row=10,column=2,pady=3,sticky=W)

is_Ccleaner_checked=IntVar()
install_Ccleaner_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Ccleaner", variable=is_Ccleaner_checked, onvalue="1", offvalue="0")
install_Ccleaner_cb.grid(row=11,column=2,pady=3,sticky=W)

is__7Zip_checked=IntVar()
install__7Zip_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="7Zip", variable=is__7Zip_checked, onvalue="1", offvalue="0")
install__7Zip_cb.grid(row=12,column=2,pady=3,sticky=W)

is_Ventoy_checked=IntVar()
install_Ventoy_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Ventoy", variable=is_Ventoy_checked, onvalue="1", offvalue="0")
install_Ventoy_cb.grid(row=13,column=2,pady=3,sticky=W)

is_Everything_checked=IntVar()
install_Everything_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Everything", variable=is_Everything_checked, onvalue="1", offvalue="0")
install_Everything_cb.grid(row=14,column=2,pady=3,sticky=W)

is_Powertoys_checked=IntVar()
install_Powertoys_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Powertoys", variable=is_Powertoys_checked, onvalue="1", offvalue="0")
install_Powertoys_cb.grid(row=15,column=2,pady=3,sticky=W)

is_WinaeroTweaker_checked=IntVar()
install_WinaeroTweaker_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Winaero Tweaker", variable=is_WinaeroTweaker_checked, onvalue="1", offvalue="0")
install_WinaeroTweaker_cb.grid(row=16,column=2,pady=3,sticky=W)

is_Io_Unlocker_checked=IntVar()
install_Io_Unlocker_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Io Unlocker", variable=is_Io_Unlocker_checked, onvalue="1", offvalue="0")
install_Io_Unlocker_cb.grid(row=17,column=2,pady=3,sticky=W)

is_RevoUninstaller_checked=IntVar()
install_RevoUninstaller_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Revo Uninstaller", variable=is_RevoUninstaller_checked, onvalue="1", offvalue="0")
install_RevoUninstaller_cb.grid(row=18,column=2,pady=3,sticky=W)

is_WindowsTerminal_checked=IntVar()
install_WindowsTerminal_cb=customtkinter.CTkCheckBox(master=install_frame,text_font=("Consolas",12), text="Windows Terminal", variable=is_WindowsTerminal_checked, onvalue="1", offvalue="0")
install_WindowsTerminal_cb.grid(row=19,column=2,pady=3,sticky=W)

def updateAllApps():
    subprocess.call([r'batch\\updateAllApps.bat'])

def runtitusUtility():
    subprocess.call([r'batch\\titusUtility.bat'])

#Options Section
def Option_section():
    textLabel=customtkinter.CTkLabel(master=install_frame,text_font=("Consolas bold",20),text="Options")
    # textLabel.place(relx=0.77,rely=0.1)
    textLabel.grid(row=1,column=4)

    installSelected=customtkinter.CTkButton(master=install_frame,text_font=("Consolas",12),text="Install selected",command=lambda: dialog_box(),width=170)
    installSelected.place(x=660,y=100)

    optionButton=customtkinter.CTkButton(master=install_frame,text_font=("Consolas",12),text="Update Apps",width=170,command=updateAllApps)
    optionButton.place(x=660,y=150)

    optionButton=customtkinter.CTkButton(master=install_frame,text_font=("Consolas",12),text="Titus Utility",width=170,command=runtitusUtility)
    optionButton.place(x=660,y=200)


Option_section()

##########################################################################
######################## Program Installer Script ########################
##########################################################################
program_installer_list = [] # initiating list first
# Functions
def add_to_list(): # add checked item to the program_installer list
    updateValues()
    if(CanvaValue==1):
        program_installer_list.append("winget install Canva.Canva")

    if(SharexValue==1):
        program_installer_list.append("choco install --force sharex")
    
    if(GreenshotValue==1):
        program_installer_list.append("choco install --force greenshot")
    
    if(IrfanviewValue==1):
        program_installer_list.append("choco install --force irfanview")
    
    if(ChromeValue==1):
        program_installer_list.append("choco install --force googlechrome")
    
    if(BraveValue==1):
        program_installer_list.append("choco install --force brave")
    
    if(FirefoxValue==1):
        program_installer_list.append("choco install --force firefox")
    
    if(DiscordValue==1):
        program_installer_list.append("choco install --force discord")
    
    if(WhatsappValue==1):
        program_installer_list.append("winget install WhatsApp.WhatsApp")
    
    if(TelegramValue==1):
        program_installer_list.append("choco install --force telegram")
    
    if(VsCodeValue==1):
        program_installer_list.append("choco install --force vscode")
    
    if(SublimeTextValue==1):
        program_installer_list.append("choco install --force sublimetext3")
    
    if(GithubDesktopValue==1):
        # program_installer_list.append("winget install GitHub.GitHubDesktop")
        program_installer_list.append("choco install --force github-desktop")
    
    if(GitValue==1):
        program_installer_list.append("choco install --force git.install")
    
    if(DrawboardValue==1):
        program_installer_list.append("winget install 9WZDNCRFHWQT &rem Drawboard")
    
    if(XodoValue==1):
        program_installer_list.append("winget install 9WZDNCRDJXP4 &rem XODO")
    
    if(NotepadsplusplusValue==1):
        program_installer_list.append("choco install --force notepadplusplus.install")
    
    if(NotepadsValue==1):
        program_installer_list.append("winget install --force JackieLiu.NotepadsApp")
    
    if(ObsidianValue==1):
        program_installer_list.append("choco install --force obsidian")
    
    if(vlcValue==1):
        program_installer_list.append("choco install --force vlc")
    
    if(SpotifyValue==1):
        program_installer_list.append("winger install Spotify.Spotify")
    
    if(QtTabBarValue==1):
        program_installer_list.append("choco install --force qttabbar")
    
    if(AutoHotkeyValue==1):
        program_installer_list.append("choco install --force autohotkey.install")
    
    if(TeamviewerValue==1):
        program_installer_list.append("choco install --force teamviewer")
    
    if(TaskbarxValue==1):
        program_installer_list.append("choco install --force taskbarx")
    
    if(CcleanerValue==1):
        program_installer_list.append("choco install --force ccleaner")
    
    if(_7ZipValue==1):
        program_installer_list.append("choco install --force 7zip")
    
    if(VentoyValue==1):
        program_installer_list.append("choco install --force ventoy")
    
    if(EverythingValue==1):
        program_installer_list.append("choco install --force everything")
    
    if(PowertoysValue==1):
        program_installer_list.append("choco install --force powertoys")
    
    if(WinaeroTweakerValue==1):
        program_installer_list.append("choco install --force winaero-tweaker")
    
    if(Io_UnlockerValue==1):
        program_installer_list.append("choco install --force io-unlocker")
    
    if(RevoUninstallerValue==1):
        program_installer_list.append("choco install --force revo-uninstaller")
    
    if(WindowsTerminalValue==1):
        program_installer_list.append("choco install --force microsoft-windows-terminal")



def deselectall(): #unchecks and resets the tickmarks done by user
    install_Canva_cb.deselect()
    install_Sharex_cb.deselect()
    install_Greenshot_cb.deselect()
    install_Irfanview_cb.deselect()
    install_Chrome_cb.deselect()
    install_Brave_cb.deselect()
    install_Firefox_cb.deselect()
    install_Discord_cb.deselect()
    install_Whatsapp_cb.deselect()
    install_Telegram_cb.deselect()
    install_VsCode_cb.deselect()
    install_SublimeText_cb.deselect()
    install_GithubDesktop_cb.deselect()
    install_Git_cb.deselect()
    install_Drawboard_cb.deselect()
    install_Xodo_cb.deselect()
    install_Notepadsplusplus_cb.deselect()
    install_Notepads_cb.deselect()
    install_Obsidian_cb.deselect()
    install_vlc_cb.deselect()
    install_Spotify_cb.deselect()
    install_QtTabBar_cb.deselect()
    install_AutoHotkey_cb.deselect()
    install_Teamviewer_cb.deselect()
    install_Taskbarx_cb.deselect()
    install_Ccleaner_cb.deselect()
    install__7Zip_cb.deselect()
    install_Ventoy_cb.deselect()
    install_Everything_cb.deselect()
    install_Powertoys_cb.deselect()
    install_WinaeroTweaker_cb.deselect()
    install_Io_Unlocker_cb.deselect()
    install_RevoUninstaller_cb.deselect()
    install_WindowsTerminal_cb.deselect()

def updateValues():
    global CanvaValue
    global SharexValue
    global GreenshotValue
    global IrfanviewValue
    global ChromeValue
    global BraveValue
    global FirefoxValue
    global DiscordValue
    global WhatsappValue
    global TelegramValue
    global VsCodeValue
    global SublimeTextValue
    global GithubDesktopValue
    global GitValue
    global DrawboardValue
    global XodoValue
    global NotepadsplusplusValue
    global NotepadsValue
    global ObsidianValue
    global vlcValue
    global SpotifyValue
    global QtTabBarValue
    global AutoHotkeyValue
    global TeamviewerValue
    global TaskbarxValue
    global CcleanerValue
    global _7ZipValue
    global VentoyValue
    global EverythingValue
    global PowertoysValue
    global WinaeroTweakerValue
    global Io_UnlockerValue
    global RevoUninstallerValue
    global WindowsTerminalValue
    CanvaValue=is_Canva_checked.get()
    SharexValue=is_Sharex_checked.get()
    GreenshotValue=is_Greenshot_checked.get()
    IrfanviewValue=is_Irfanview_checked.get()
    ChromeValue=is_Chrome_checked.get()
    BraveValue=is_Brave_checked.get()
    FirefoxValue=is_Firefox_checked.get()
    DiscordValue=is_Discord_checked.get()
    WhatsappValue=is_Whatsapp_checked.get()
    TelegramValue=is_Telegram_checked.get()
    VsCodeValue=is_VsCode_checked.get()
    SublimeTextValue=is_SublimeText_checked.get()
    GithubDesktopValue=is_GithubDesktop_checked.get()
    GitValue=is_Git_checked.get()
    DrawboardValue=is_Drawboard_checked.get()
    XodoValue=is_Xodo_checked.get()
    NotepadsplusplusValue=is_Notepadsplusplus_checked.get()
    NotepadsValue=is_Notepads_checked.get()
    ObsidianValue=is_Obsidian_checked.get()
    vlcValue=is_vlc_checked.get()
    SpotifyValue=is_Spotify_checked.get()
    QtTabBarValue=is_QtTabBar_checked.get()
    AutoHotkeyValue=is_AutoHotkey_checked.get()
    TeamviewerValue=is_Teamviewer_checked.get()
    TaskbarxValue=is_Taskbarx_checked.get()
    CcleanerValue=is_Ccleaner_checked.get()
    _7ZipValue=is__7Zip_checked.get()
    VentoyValue=is_Ventoy_checked.get()
    EverythingValue=is_Everything_checked.get()
    PowertoysValue=is_Powertoys_checked.get()
    WinaeroTweakerValue=is_WinaeroTweaker_checked.get()
    Io_UnlockerValue=is_Io_Unlocker_checked.get()
    RevoUninstallerValue=is_RevoUninstaller_checked.get()
    WindowsTerminalValue=is_WindowsTerminal_checked.get()

program_installer_bat_path=os.path.join(cwd_of_utility,"batch\\program_installer.bat")
def createBatFile(): #create the program_installer.bat file
    handleFile=open(program_installer_bat_path,"w")
    for element in program_installer_list:
        handleFile.write(element + "\n")
    handleFile.close

def dialog_box():
    global dialog
    dialog = customtkinter.CTkInputDialog(master=None, text="Do Not Exit/Close Terminal\nPress Ctrl+C if want to Exit or stop instalation\nType okay", title="Do not close Terminal")
    userinput=dialog.get_input()
    if(userinput=="okay"):
        install_selected()

def install_selected():
    if os.path.isfile(program_installer_bat_path):
        os.remove(program_installer_bat_path)
    # time.sleep(2.0)
    add_to_list()
    createBatFile() 
    program_installer_list.clear() #clears previous list
    deselectall() 
    subprocess.call([r'batch\\first.bat']) #executes the very first batch script to begin steps toward main batch file



root.mainloop()