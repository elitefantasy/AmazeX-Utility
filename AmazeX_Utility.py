from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QPropertyAnimation,QEasingCurve
import subprocess,os,urllib.request,threading
from time import sleep
import os

os.system("pyside6-rcc resource.qrc -o resource_rc.py")
os.system("pyside6-uic main_interface_ui.ui -o main_interface_ui.py")

from main_interface_ui import *
from uninstallPage import uninstaller


#Variables
current_file_path=__file__
cwd_of_utility=os.path.dirname(current_file_path)
username=os.getlogin()
DesktopPath=f"C:\\Users\\{username}\\Desktop"
fileUrlAHK="https://github.com/elitefantasy/AmazeX-AHK/raw/main/Distribution/AmazeX%20AHK/Scripts/Setup/AmazeX_AHK_Setup.exe"
fileUrl_AkmDownloadSorter="https://github.com/elitefantasy/AKM-DownloadSorter/raw/main/Dist/AkmDowloadSorter_Setup.exe"
AmazeX_Utility_Setup_url="https://github.com/elitefantasy/AmazeX-Utility/raw/main/Setup/AmazeX_Utility_Setup.exe"
program_installer_bat_path=os.path.join(cwd_of_utility,"batch\\program_installer.bat")
versionUrl="https://raw.githubusercontent.com/elitefantasy/AmazeX-Utility/main/Version.txt"


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.programStartup()
                
        self.check_for_update_btn.clicked.connect(self.checkForUpdates)
        self.Install_Chocolatey_btn.clicked.connect(self.run_install_chocolatey)
        self.Titus_Utility_btn.clicked.connect(self.run_titus_utility)
        self.Update_Apps_btn.clicked.connect(self.run_update_apps)
        self.Download_AKMSorter_btn.clicked.connect(self.download_akmSorter)
        self.Download_AmazeX_btn.clicked.connect(self.download_amazexAHK)
        self.Install_selected_btn.clicked.connect(self.install_selected_apps)
        # left burger menu toggle button
        self.burger_menu_btn.clicked.connect(self.slideLeftMenu)
        ################################################################
        # link left side menu button with page
        ################################################################
        self.homeButton.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.home_page_container))
        self.installButton.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.install_page_container))
        self.UninstallButton.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.uninstall_page_container))
        self.settingsButton.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.settings_page_container))
        ################################################################
        
        ################################################################
        # Link Uninstall Page buttons
        ################################################################
        self.uninstaller=uninstaller()
        
        self.GetHelpUninBtn.clicked.connect(lambda:self.uninstaller.uninstallGetHelp())
        self.GetHelpInsBtn.clicked.connect(lambda:self.uninstaller.installGetHelp())
        self.PhoneUninBtn.clicked.connect(lambda:self.uninstaller.uninstallPhoneLink())
        self.PhoneInsBtn.clicked.connect(lambda:self.uninstaller.installPhoneLink())
        ################################################################
        
        
        ################################################################
        # change active button style
        ################################################################
        for w in self.left_top_side_menu_container.findChildren(QPushButton):
            w.clicked.connect((self.applyButtonStyle))
        ################################################################
    
    def programStartup(self): # run at program startup
        # check for current version and update text label
        #-------------------------------------------------------------
        versionSource=open('Version.txt','r')
        version=versionSource.readline()
        version=version.replace("Version","").replace("(current)","")
        self.label_StatusBar.setText("Current Version is: "+version.rstrip('\n'))
        print("running Version is: "+version)
        #-------------------------------------------------------------
        
        # Start Titlt animation
        #-------------------------------------------------------------
        # creating thread for start_title_animation
        t=threading.Thread(target=self.start_title_animation)
        t.start()
        ############################################################
        
        ############################################################
        # Hide Elements
        #############################################################
        self.progressBar.hide()
        #############################################################
    
    def start_title_animation(self):
        global index
        txt=['A|','Am|','Ama|','Amaz|','Amaze|','AmazeX|','AmazeX U|','AmazeX Ut|','AmazeX Uti|','AmazeX Util|',
            'AmazeX Utili|','AmazeX Utilit|','AmazeX Utility']
        index=0
        print("length of txt is: "+str(len(txt)))
        while index +1 <=len(txt):
            # print(txt[index])
            self.title_label.setText(txt[index])
            # self.label.setText("Hello")
            sleep(0.5)
            index+=1
            # print(index)
            if index==13:
                break
    
    #################################################################
    # Slide left menu function////////////////
    #################################################################
    def slideLeftMenu(self):
        # get current left menu width
        width=self.left_top_side_menu_container.width()
        # print(width)
        if width==38:
            #Expand Menu
            newWidth=110
        else:
            # Restore menu
            newWidth=38
        
        # Animate the transition
        self.animation=QPropertyAnimation(self.left_top_side_menu_container,b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#start value is current menu width
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
    #################################################################
    
    def applyButtonStyle(self):
        for w in self.left_top_side_menu_container.findChildren(QPushButton):
            if w.objectName()!=self.sender().objectName():
                defaultStyle=w.styleSheet().replace("background-color:#0076ff;","")
                w.setStyleSheet(defaultStyle)
        
            newStyle=self.sender().styleSheet()+("background-color:#0076ff;")
            self.sender().setStyleSheet(newStyle)
    
    def Handle_Progress(self,blocknum,blocksize,totalsize):
        # calculate the progress
        readed_data=blocknum*blocksize
        
        if totalsize>0:
            download_percntage=int(readed_data*100/totalsize)
            self.progressBar.show()
            self.progressBar.setValue(download_percntage)
            QApplication.processEvents()
            self.progressBar.hide()
    
    def checkForUpdates(self):
        update=False
        versionSource=open('Version.txt','r')
        versionContents = versionSource.readline()
        print("version content is: "+versionContents)
        
        #gets newest version(to compare files)
        updateSource = urllib.request.urlopen(versionUrl)
        updateContents = updateSource.readline().decode('utf-8')
        print("update content are: "+updateContents)
        #rechecking update version (to update labels n stuff)
        # reupdateSource = urllib.request.urlopen(versionUrl)
        updateversion=urllib.request.urlopen(versionUrl).readline().decode('utf-8').replace("Version","").replace("(current)","")
        
        if updateContents != versionContents:
            update =True
            # checking file size of setup
            file=urllib.request.urlopen(AmazeX_Utility_Setup_url)
            fileSizeByte=int(file.length)
            fileSizeMb=str(int(fileSizeByte/1048576))
            
            # showing the message box
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Check App Update")
            msg.setText("New Version is Available: "+updateversion+"\nDo You want To Download(file size: "+fileSizeMb+" ) The Update")
            print("Updates are available")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
    
            
            retval=msg.exec()
            print(retval)
            if retval==16384:
                down_url =AmazeX_Utility_Setup_url
                save_loc = f'C:/Users/{username}/Desktop/AmazeX_Utility_Setup.exe'
                self.label_StatusBar.setText("Downloading Update Setup File")
                urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)
                self.label_StatusBar.setText(f'AmazeX_Utility_Setup succesfully download at C:/Users/{username}/Desktop/')
                QApplication.processEvents()
                sleep(0.5)
                self.label_StatusBar.setText("Exit and run setup installer.")
        if update == False:
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Check App Update")
            msg.setText("You are already running latest version: "+updateversion)
            msg.exec()
    def run_install_chocolatey(self):
        subprocess.call([r'batch\\install_chocolatey.bat'])
    def run_titus_utility(self):
        subprocess.call([r'batch\\titusUtility.bat'])
    def run_update_apps(self):
        subprocess.call([r'batch\\updateAllApps.bat'])
    
    def asokcancel(self,url,msgTitle):
        #retrieves filesize and show message box okcancel
        
        # calculate file size
        try:
            file=urllib.request.urlopen(url)
            fileSizeByte=int(file.length)
            fileSizeMb=str(int(fileSizeByte/1048576))
        except urllib.error.URLError:
            print("Couldn't Fetch File")
            fileSizeMb=""
        if fileSizeMb !="":
            global retval
            #create messagebox and show
            self.msg=QMessageBox()
            self.msg.setIcon(QMessageBox.Icon.Information)
            self.msg.setWindowTitle(msgTitle)
            self.msg.setText(f"Will Download {fileSizeMb} mb of file Size.!\nClick Ok to Continue")
            self.msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            retval=self.msg.exec() #creating loop and taking button input
            print("retval vlaue is ",retval)
        else:
            retval=""
            self.msg=QMessageBox()
            self.msg.setIcon(QMessageBox.Icon.Information)
            self.msg.setWindowTitle("Error")
            self.msg.setText(f"Couldn't Fetch File")
            self.msg.exec()
    def download_amazexAHK(self):
        down_url =fileUrlAHK
        save_loc = f'C:/Users/{username}/Desktop/AmazeX_AHK_Setup.exe'
        #calling showAskOkCancelWindow function
        self.asokcancel(url=fileUrlAHK,msgTitle="Download AmazeX AHK")
        
        # Showing progressbar and starting download
        if retval==1024: #if okay
            #update progressbar
            self.label_StatusBar.setText("Downloading AmazeX AHK Setup")
            urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)
            self.label_StatusBar.setText(f"AmazeX AHK Setup succesfully downloaded at C:/Users/{username}/Desktop/")
            QApplication.processEvents()
    
    def download_akmSorter(self):
        down_url =fileUrl_AkmDownloadSorter
        save_loc = f'C:/Users/{username}/Desktop/AKM_Sorter_Setup.exe'
        #calling showAskOkCancelWindow
        self.asokcancel(url=fileUrl_AkmDownloadSorter,msgTitle="Download AKM FileSorter")
        
        # Showing progressbar and starting download
        if retval==1024:
            #update progressbar
            self.label_StatusBar.setText("Downloading AKMSorter Setup")
            urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)
            self.label_StatusBar.setText(f"AKMSorter Setup succesfully downloaded at C:/Users/{username}/Desktop/")
            QApplication.processEvents()
    
    def install_selected_apps(self):
    
        #create list of selected apps
        program_installer_list = []
        
        # Photos
        if self.checkBox_Canva.isChecked():
            program_installer_list.append("winget install Canva.Canva")
        if self.checkBox_ShareX.isChecked():
            program_installer_list.append("choco install --force sharex")
        if self.checkBox_Greenshot.isChecked():
            program_installer_list.append("choco install --force greenshot")
        if self.checkBox_IrfanView.isChecked():
            program_installer_list.append("choco install --force irfanview")
        
        # Browser
        if self.checkBox_Chrome.isChecked():
            program_installer_list.append("choco install --force googlechrome")
        if self.checkBox_Brave.isChecked():
            program_installer_list.append("choco install --force brave")
        if self.checkBox_Firefox.isChecked():
            program_installer_list.append("choco install --force firefox")
        # Social
        if self.checkBox_Discord.isChecked():
            program_installer_list.append("choco install --force discord")
        if self.checkBox_Whatsapp.isChecked():
            program_installer_list.append("winget install WhatsApp.WhatsApp")
        if self.checkBox_Telegram.isChecked():
            program_installer_list.append("choco install --force telegram")
        
        # Development
        if self.checkBox_VsCode.isChecked():
            program_installer_list.append("choco install --force vscode")
        if self.checkBox_SublimeText.isChecked():
            program_installer_list.append("choco install --force sublimetext3")
        if self.checkBox_GithubDesktop.isChecked():
            program_installer_list.append("choco install --force github-desktop")
        if self.checkBox_Git.isChecked():
            program_installer_list.append("choco install --force git.install")
        if self.checkBox_VmwarePlayer.isChecked():
            program_installer_list.append("choco install --force vmware-workstation-player")
        
        # Documents
        if self.checkBox_Drawboard.isChecked():
            program_installer_list.append("winget install 9WZDNCRFHWQT &rem Drawboard")
        if self.checkBox_Xodo.isChecked():
            program_installer_list.append("winget install 9WZDNCRDJXP4 &rem XODO")
        if self.checkBox_NotepadPlusPlus.isChecked():
            program_installer_list.append("choco install --force notepadplusplus.install")
        if self.checkBox_Notepads.isChecked():
            program_installer_list.append("winget install --force JackieLiu.NotepadsApp")
        if self.checkBox_Obsidian.isChecked():
            program_installer_list.append("choco install --force obsidian")
        
        # Utilities
        if self.checkBox_Ccleaner.isChecked():
            program_installer_list.append("choco install --force ccleaner")
        if self.checkBox_7zip.isChecked():
            program_installer_list.append("choco install --force 7zip")
        if self.checkBox_Powertoys.isChecked():
            program_installer_list.append("choco install --force powertoys")
        if self.checkBox_Ventoy.isChecked():
            program_installer_list.append("choco install --force ventoy")
        if self.checkBox_WinaeroTweaker.isChecked():
            program_installer_list.append("choco install --force winaero-tweaker")
        if self.checkBox_IoUnlocker.isChecked():
            program_installer_list.append(f"curl https://cdn.iobit.com/dl/unlocker-setup.exe -o C:\\Users\\{username}\\Desktop\\Io-Unlocker.exe")
        if self.checkBox_RevoUninstaller.isChecked():
            program_installer_list.append("choco install --force revo-uninstaller")
        if self.checkBox_WindowsTerminal.isChecked():
            program_installer_list.append("winget install Microsoft.WindowsTerminal.Preview")
        if self.checkBox_Duplicati.isChecked():
            program_installer_list.append("winget install Duplicati.Duplicati")
        
        # Security
        if self.checkBox_Keepass.isChecked():
            program_installer_list.append("choco install --force keepass")
        
        # Others
        if self.checkBox_TaskbarX.isChecked():
            program_installer_list.append("choco install --force taskbarx")
        if self.checkBox_Everything.isChecked():
            program_installer_list.append("choco install --force everything")
        if self.checkBox_Vlc.isChecked():
            program_installer_list.append("choco install --force vlc")
        if self.checkBox_Spotify.isChecked():
            program_installer_list.append("winget install Spotify.Spotify")
        if self.checkBox_QtTabBar.isChecked():
            program_installer_list.append("choco install --force qttabbar")
        if self.checkBox_AutoHotkey.isChecked():
            program_installer_list.append("choco install --force autohotkey.install")
        if self.checkBox_TeamViewer.isChecked():
            program_installer_list.append("choco install --force teamviewer")
            
        print(program_installer_list)
        
        # take user confirm input to create and then start program installer bat file
        self.msg=QMessageBox()
        self.msg.setIcon(QMessageBox.Icon.Information)
        self.msg.setWindowTitle("Information")
        self.msg.setText("if you feel terminal is stuck/freezed\npress ctrl+r to reload")
        self.msg.setStandardButtons(QMessageBox.StandardButton.Ok |QMessageBox.StandardButton.Cancel)
        
        retval=self.msg.exec_()
        if retval==1024:
            print("Removing program_installer_bat_file if exists")
            # Deleting old(already existed) programm_installer.bat
            if os.path.isfile(program_installer_bat_path):
                os.remove(program_installer_bat_path)
            print("Done")
            
            # creating programm_installer.bat
            handleFile=open(program_installer_bat_path,"w")
            for element in program_installer_list:
                handleFile.write(element + "\n")
                handleFile.close
            
            # run programm_installer.bat if it exists
            if os.path.isfile(program_installer_bat_path):
                try:
                    print("Running programmInstaller.bat")
                    p=subprocess.run('batch\\run_programInstaller.bat',shell=True,capture_output=True,text=True)
                    # print(p.stdout)
                except FileNotFoundError:
                    print("File was not found to execute")
                except Exception as e:
                    print(e)
                    raise
            else:print("programmInstaller.bat is not yet created")
    

app=QApplication([])
win=MainWindow()
win.show()
app.exec()