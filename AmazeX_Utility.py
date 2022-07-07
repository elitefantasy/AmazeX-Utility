
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess,os,urllib.request,requests,threading
from progbar import Ui_Form
from time import sleep

# stylesheet
Stylesheet=("QCheckBox{spacing:20px;}"
                "QCheckBox::indicator{width:20px;height:20px;}"
                "QCheckBox::indicator:unchecked{image:url(icons/uncheckmark.png);}"
                "QCheckBox::indicator:unchecked:hover{image:url(icons/uncheckmark-hover.png);}"
                "QCheckBox::indicator:checked{image:url(icons/check-mark.png);}"
                "QCheckBox::indicator:checked:hover{image:url(icons/check-mark-hover.png);}"
            #   "QCheckBox::indicator:unchecked:pressed{background-color:green;}"
               )



#Variables
current_file_path=__file__
cwd_of_utility=os.path.dirname(current_file_path)
username=os.getlogin()
DesktopPath=f"C:\\Users\\{username}\\Desktop"
fileUrlAHK="https://github.com/elitefantasy/AmazeX-AHK/raw/main/Distribution/AmazeX%20AHK/Scripts/Setup/Setup.exe"
fileUrl_AkmDownloadSorter="https://github.com/elitefantasy/AKM-DownloadSorter/raw/main/Dist/AkmDowloadSorter_Setup.exe"
AmazeX_Utility_Setup_url="https://github.com/elitefantasy/AmazeX-Utility/raw/main/Setup/AmazeX_Utility_Setup.exe"
program_installer_bat_path=os.path.join(cwd_of_utility,"batch\\program_installer.bat")
versionUrl="https://raw.githubusercontent.com/elitefantasy/AmazeX-Utility/main/Version.txt"


class Ui_MainWindow(QtWidgets.QWidget):
    def programStartup(self): # run at program startup
        versionSource=open('Version.txt','r')
        version=versionSource.readline()
        version=version.replace("Version","").replace("(current)","")
        self.label_StatusBar.setText("Current Version is: "+version.rstrip('\n'))
        print("running Version is: "+version)
        #this method is called at the last of retranslateui
    def checkForUpdates(self):
        update=False
        versionSource=open('Version.txt','r')
        versionContents = versionSource.read()
        print("version content is: "+versionContents)
        
        #gets newest version(to compare files)
        updateSource = urllib.request.urlopen(versionUrl)
        updateContents = updateSource.read().decode('utf-8')
        print("update content are: "+updateContents)
        #rechecking update version (to update labels n stuff)
        # reupdateSource = urllib.request.urlopen(versionUrl)
        updateversion=urllib.request.urlopen(versionUrl).readline().decode('utf-8').replace("Version","").replace("(current)","")
        
        for i in range(0,20):
            if updateContents[i] != versionContents[i]:
                update =True
                # checking file size of setup
                file=urllib.request.urlopen(AmazeX_Utility_Setup_url)
                fileSizeByte=int(file.length)
                fileSizeMb=str(int(fileSizeByte/1048576))
                
                # showing the message box
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Check App Update")
                msg.setText("New Version is Available: "+updateversion+"\nDo You want To Download(file size: "+fileSizeMb+" ) The Update")
                print("Updates are available")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        
                
                retval=msg.exec_()
                if retval==1024:
                    self.progbar_window=QtWidgets.QWidget()
                    self.ui=Ui_Form()
                    self.ui.setupUi(self.progbar_window)
                    self.progbar_window.setWindowTitle("Download AmazeX Utility")
                    self.ui.label.setText("Downloading AmazeX Utility.....\nDepends on internet speed")
                    self.progbar_window.show()
                    print("Starting download of Amazex Utility")
                    
                    def download_file():
                        response = requests.get(AmazeX_Utility_Setup_url)
                        open(DesktopPath+"\\AmazeX_Utility_Setup.exe", "wb").write(response.content)
                        # sleep(10)#just for testing purpose
                        self.ui.label.setText("Done!, File Downloaded at Desktop")
                        sleep(3)
                        # Exit the progbar window
                        self.progbar_window.close()
                    # creating Thread
                    threading_download_file=threading.Thread(target=download_file)
                    threading_download_file.daemon=True
                    threading_download_file.start()
                
                break
            
            if update == False:
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Check App Update")
                msg.setText("You are already running latest version: "+updateversion)
                msg.exec_()
                break
    
    def run_install_chocolatey(self):
        subprocess.call([r'batch\\install_chocolatey.bat'])
    def run_titus_utility(self):
        subprocess.call([r'batch\\titusUtility.bat'])
    def run_update_apps(self):
        subprocess.call([r'batch\\updateAllApps.bat'])
    
    def asokcancel(self,url,msgTitle):
        
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
            self.msg=QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setWindowTitle(msgTitle)
            self.msg.setText(f"Will Download {fileSizeMb} mb of file Size.!\nClick Ok to Continue")
            self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            retval=self.msg.exec_() #creating loop and taking button input
            print("retval vlaue is ",retval)
        else:
            retval=""
            self.msg=QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setWindowTitle("Error")
            self.msg.setText(f"Couldn't Fetch File")
            self.msg.exec_()

    def download_amazexAHK(self):
        #calling showAskOkCancelWindow function
        self.asokcancel(url=fileUrlAHK,msgTitle="Download AmazeX AHK")
        
        # Showing progressbar and starting download
        if retval==1024: #if okay
            #create and show progbar window
            self.progbar_window=QtWidgets.QWidget() #creating instance of window
            self.ui=Ui_Form() #calling class
            self.ui.setupUi(self.progbar_window) #calling function,and assigining parent
            self.progbar_window.setWindowTitle("Download AmazeX AHK")
            self.ui.label.setText("Downloading AmazeX AHK.....\nDepends on internet speed")
            self.progbar_window.show()
            print("Starting download of AmazexAHK")
            #starting download
            def download_file():
                response = requests.get(fileUrlAHK)
                open(DesktopPath+"\\AmazeX AHK Setup.exe", "wb").write(response.content)
                # sleep(10)#just for testing purpose
                self.ui.label.setText("Done!, File Downloaded at Desktop")
                sleep(3)
                # Exit the progbar window
                self.progbar_window.close()
            # creating Thread
            threading_download_file=threading.Thread(target=download_file)
            threading_download_file.daemon=True
            threading_download_file.start()
    
    def download_akmSorter(self):
        #calling showAskOkCancelWindow
        self.asokcancel(url=fileUrl_AkmDownloadSorter,msgTitle="Download AKM FileSorter")
        
        # Showing progressbar and starting download
        if retval==1024:
            #create and show progbar window
            self.progbar_window=QtWidgets.QWidget()
            self.ui=Ui_Form()
            self.ui.setupUi(self.progbar_window)
            self.progbar_window.setWindowTitle("Download AmazeX AHK")
            self.ui.label.setText("Downloading AKM FileSorter.....\nDepends on internet speed")
            self.progbar_window.show()
            print("Starting download of AKM FileSorter")
            #starting download
            def download_file():
                response = requests.get(fileUrl_AkmDownloadSorter)
                open(DesktopPath+"\\AKM File Sorter.exe", "wb").write(response.content)
                # sleep(10)#just for testing purpose
                self.ui.label.setText("Done!, File Downloaded at Desktop")
                sleep(3)
                self.progbar_window.close()
            # Exit the progbar window
            threading_download_file=threading.Thread(target=download_file)
            threading_download_file.daemon=True
            threading_download_file.start()
        
    
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
        self.msg=QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setWindowTitle("Information")
        self.msg.setText("if you feel terminal is stuck/freezed\npress ctrl+r to reload")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        
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
                    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(916, 600)
        MainWindow.setWindowIcon(QtGui.QIcon('icons\\amazex-utility.png'))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color:#212325")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget{border:0px;color:purple;}\n"
                            "QTabWidget::tab-bar {left: 10px; /* move to the right by 10px */}\n"
                            "QTabBar::tab {\n"
                            "    background: qlineargradient(x1:-1, y1:0, x2: 1, y2: 2,\n"
"                                stop: 0 #e100ff, stop: 1.0 #7f00ff);\n"
                            "    border: 1px solid #333333;\n"
                            "    border-bottom-color: #a0a0a0;\n"
                            "    border-top-left-radius: 4px;\n"
                            "    border-top-right-radius: 4px;\n"
                            "    min-width: 25ex;\n"
                            "    padding: 4px;\n"
                            "    color:white;\n"
"    font:12px;\n"
"    font-family:\"Garamond\"\n"
                            "}\n"
                            "QTabBar::tab:selected, QTabBar::tab:hover {\n"
                            "    background: qlineargradient(x1:-1, y1:0, x2: 1, y2: 2,\n"
"                                stop: 0 #e100ff, stop: 1.0 #7f00ff)\n"
                            "}\n"
                            "QTabBar::tab:!selected {\n"
                            "    margin-top: 4px; /* make non-selected tabs look smaller */\n"
                            "}")
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setStyleSheet("background-color:#212325")
        self.home_tab.setObjectName("home_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.home_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.home_tab)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("background-color:#333333;\n"
"border-radius: 10px;\n"
"color:white;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 880, 529))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 39))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color:skyblue")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 240, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 9, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Install_Chocolatey_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.run_install_chocolatey())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Install_Chocolatey_btn.setFont(font)
        self.Install_Chocolatey_btn.setStyleSheet("QPushButton{\n"
                        "background-color:#ff0000;\n"
                        "border-style:outlet;\n"
                        "border-width:2px;\n"
                        "border-radius:10px;\n"
                        "color:white;\n"
                        "}\n"
                        "QPushButton:hover{\n"
                        "background-color:#b20000;\n"
                        "}\n"
                        "QPushButton:pressed{\n"
                        "background-color:#ff0000;\n"
                        "border-style: inset;\n"
                        "color:white;\n"
                        "}\n"
                        "")
        self.Install_Chocolatey_btn.setCheckable(False)
        self.Install_Chocolatey_btn.setAutoDefault(False)
        self.Install_Chocolatey_btn.setDefault(False)
        self.Install_Chocolatey_btn.setFlat(False)
        self.Install_Chocolatey_btn.setObjectName("Install_Chocolatey_btn")
        self.verticalLayout_3.addWidget(self.Install_Chocolatey_btn)
        self.Download_AKMSorter_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.download_akmSorter())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Download_AKMSorter_btn.setFont(font)
        self.Download_AKMSorter_btn.setStyleSheet("QPushButton{\n"
                        "background-color:#0076ff;\n"
                        "border-style:outlet;\n"
                        "border-width:2px;\n"
                        "border-radius:10px;\n"
                        "color:white;\n"
                        "}\n"
                        "QPushButton:hover{\n"
                        "background-color:#005b99;\n"
                        "}\n"
                        "QPushButton:pressed{\n"
                        "background-color:#0076ff;\n"
                        "border-style: inset;\n"
                        "color:white;\n"
                        "}")
        self.Download_AKMSorter_btn.setCheckable(False)
        self.Download_AKMSorter_btn.setAutoDefault(False)
        self.Download_AKMSorter_btn.setDefault(False)
        self.Download_AKMSorter_btn.setFlat(False)
        self.Download_AKMSorter_btn.setObjectName("Download_AKMSorter_btn")
        self.verticalLayout_3.addWidget(self.Download_AKMSorter_btn)
        self.Download_AmazeX_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.download_amazexAHK())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Download_AmazeX_btn.setFont(font)
        self.Download_AmazeX_btn.setStyleSheet("QPushButton{\n"
                        "background-color:#0076ff;\n"
                        "border-style:outlet;\n"
                        "border-width:2px;\n"
                        "border-radius:10px;\n"
                        "color:white;\n"
                        "}\n"
                        "QPushButton:hover{\n"
                        "background-color:#005b99;\n"
                        "}\n"
                        "QPushButton:pressed{\n"
                        "background-color:#0076ff;\n"
                        "border-style: inset;\n"
                        "color:white;\n"
                        "}\n"
                        "")
        self.Download_AmazeX_btn.setCheckable(False)
        self.Download_AmazeX_btn.setAutoDefault(False)
        self.Download_AmazeX_btn.setDefault(False)
        self.Download_AmazeX_btn.setFlat(False)
        self.Download_AmazeX_btn.setObjectName("Download_AmazeX_btn")
        self.verticalLayout_3.addWidget(self.Download_AmazeX_btn)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 4, 0, 3, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_StatusBar = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_StatusBar.sizePolicy().hasHeightForWidth())
        self.label_StatusBar.setSizePolicy(sizePolicy)
        self.label_StatusBar.setMinimumSize(QtCore.QSize(150, 0))
        self.label_StatusBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_StatusBar.setStyleSheet("QLabel{\n"
"background: qlineargradient(x1:-1, y1:0, x2:3, y2:0,\n"
"                stop:0 #000000,stop:0.4 #434343,stop:1.0 #000000);\n"
"color:white;\n"
"border: 2px solid #a500ff;\n"
"border-radius: 4px;\n"
"border-style:groove;\n"
"}")
        self.label_StatusBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_StatusBar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_StatusBar.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)
        self.label_StatusBar.setObjectName("label_StatusBar")
        self.horizontalLayout.addWidget(self.label_StatusBar)
        self.check_for_update_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda:self.checkForUpdates())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_for_update_btn.sizePolicy().hasHeightForWidth())
        self.check_for_update_btn.setSizePolicy(sizePolicy)
        self.check_for_update_btn.setMinimumSize(QtCore.QSize(200, 0))
        self.check_for_update_btn.setAutoFillBackground(False)
        self.check_for_update_btn.setStyleSheet("QPushButton{\n"
"background-color:#0076ff;\n"
"border-style:outlet;\n"
"border-width:3px;\n"
"border-radius:5px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#005b99;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#0076ff;\n"
"border-style: inset;\n"
"color:white;\n"
"}\n"
"")
        self.check_for_update_btn.setFlat(False)
        self.check_for_update_btn.setObjectName("check_for_update_btn")
        self.horizontalLayout.addWidget(self.check_for_update_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 10, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.home_tab, "")
        self.install_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.install_tab.sizePolicy().hasHeightForWidth())
        self.install_tab.setSizePolicy(sizePolicy)
        self.install_tab.setMinimumSize(QtCore.QSize(0, 0))
        self.install_tab.setSizeIncrement(QtCore.QSize(0, 0))
        self.install_tab.setBaseSize(QtCore.QSize(0, 0))
        self.install_tab.setStyleSheet("background-color:#212325")
        self.install_tab.setObjectName("install_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.install_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.install_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.scrollArea_2.setBaseSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setStyleSheet("background-color:#333333;  border-radius: 10px;color:white")
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 880, 529))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Utilities = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Utilities.setFont(font)
        self.label_Utilities.setObjectName("label_Utilities")
        self.gridLayout.addWidget(self.label_Utilities, 6, 1, 1, 1)
        self.checkBox_Chrome = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Chrome.sizePolicy().hasHeightForWidth())
        self.checkBox_Chrome.setSizePolicy(sizePolicy)
        self.checkBox_Chrome.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Chrome.setFont(font)
        self.checkBox_Chrome.setStyleSheet("")
        self.checkBox_Chrome.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Chrome.setTristate(False)
        self.checkBox_Chrome.setObjectName("checkBox_Chrome")
        self.gridLayout.addWidget(self.checkBox_Chrome, 1, 1, 1, 1)
        self.checkBox_Xodo = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Xodo.sizePolicy().hasHeightForWidth())
        self.checkBox_Xodo.setSizePolicy(sizePolicy)
        self.checkBox_Xodo.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Xodo.setFont(font)
        self.checkBox_Xodo.setStyleSheet("")
        self.checkBox_Xodo.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Xodo.setTristate(False)
        self.checkBox_Xodo.setObjectName("checkBox_Xodo")
        self.gridLayout.addWidget(self.checkBox_Xodo, 9, 0, 1, 1)
        self.checkBox_Telegram = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Telegram.sizePolicy().hasHeightForWidth())
        self.checkBox_Telegram.setSizePolicy(sizePolicy)
        self.checkBox_Telegram.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Telegram.setFont(font)
        self.checkBox_Telegram.setStyleSheet("")
        self.checkBox_Telegram.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Telegram.setTristate(False)
        self.checkBox_Telegram.setObjectName("checkBox_Telegram")
        self.gridLayout.addWidget(self.checkBox_Telegram, 3, 2, 1, 1)
        self.checkBox_IrfanView = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_IrfanView.setFont(font)
        self.checkBox_IrfanView.setObjectName("checkBox_IrfanView")
        self.gridLayout.addWidget(self.checkBox_IrfanView, 4, 0, 1, 1)
        self.checkBox_VsCode = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VsCode.sizePolicy().hasHeightForWidth())
        self.checkBox_VsCode.setSizePolicy(sizePolicy)
        self.checkBox_VsCode.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_VsCode.setFont(font)
        self.checkBox_VsCode.setStyleSheet("")
        self.checkBox_VsCode.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_VsCode.setTristate(False)
        self.checkBox_VsCode.setObjectName("checkBox_VsCode")
        self.gridLayout.addWidget(self.checkBox_VsCode, 1, 3, 1, 1)
        self.checkBox_Brave = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Brave.sizePolicy().hasHeightForWidth())
        self.checkBox_Brave.setSizePolicy(sizePolicy)
        self.checkBox_Brave.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Brave.setFont(font)
        self.checkBox_Brave.setStyleSheet("")
        self.checkBox_Brave.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Brave.setTristate(False)
        self.checkBox_Brave.setObjectName("checkBox_Brave")
        self.gridLayout.addWidget(self.checkBox_Brave, 2, 1, 1, 1)
        self.checkBox_Firefox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Firefox.sizePolicy().hasHeightForWidth())
        self.checkBox_Firefox.setSizePolicy(sizePolicy)
        self.checkBox_Firefox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Firefox.setFont(font)
        self.checkBox_Firefox.setStyleSheet("")
        self.checkBox_Firefox.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Firefox.setTristate(False)
        self.checkBox_Firefox.setObjectName("checkBox_Firefox")
        self.gridLayout.addWidget(self.checkBox_Firefox, 3, 1, 1, 1)
        self.checkBox_ShareX = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_ShareX.setFont(font)
        self.checkBox_ShareX.setObjectName("checkBox_ShareX")
        self.gridLayout.addWidget(self.checkBox_ShareX, 2, 0, 1, 1)
        self.label_Documents = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Documents.sizePolicy().hasHeightForWidth())
        self.label_Documents.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Documents.setFont(font)
        self.label_Documents.setObjectName("label_Documents")
        self.gridLayout.addWidget(self.label_Documents, 6, 0, 1, 1)
        self.Update_Apps_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3,clicked=lambda:self.run_update_apps())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Update_Apps_btn.setFont(font)
        self.Update_Apps_btn.setStyleSheet("QPushButton{\n"
                    "background-color:#0076ff;\n"
                    "border-style:outlet;\n"
                    "border-width:2px;\n"
                    "}\n"
                    "QPushButton:hover{\n"
                    "background-color:#005b99;\n"
                    "}\n"
                    "QPushButton:pressed{\n"
                    "background-color:#0076ff;\n"
                    "border-style: inset;\n"
                    "}\n"
                    "")
        self.Update_Apps_btn.setCheckable(False)
        self.Update_Apps_btn.setAutoDefault(False)
        self.Update_Apps_btn.setDefault(False)
        self.Update_Apps_btn.setFlat(False)
        self.Update_Apps_btn.setObjectName("Update_Apps_btn")
        self.gridLayout.addWidget(self.Update_Apps_btn, 3, 4, 1, 1)
        self.checkBox_Vlc = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Vlc.sizePolicy().hasHeightForWidth())
        self.checkBox_Vlc.setSizePolicy(sizePolicy)
        self.checkBox_Vlc.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Vlc.setFont(font)
        self.checkBox_Vlc.setStyleSheet("")
        self.checkBox_Vlc.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Vlc.setTristate(False)
        self.checkBox_Vlc.setObjectName("checkBox_Vlc")
        self.gridLayout.addWidget(self.checkBox_Vlc, 10, 2, 1, 1)
        self.checkBox_Spotify = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Spotify.sizePolicy().hasHeightForWidth())
        self.checkBox_Spotify.setSizePolicy(sizePolicy)
        self.checkBox_Spotify.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Spotify.setFont(font)
        self.checkBox_Spotify.setStyleSheet("")
        self.checkBox_Spotify.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Spotify.setTristate(False)
        self.checkBox_Spotify.setObjectName("checkBox_Spotify")
        self.gridLayout.addWidget(self.checkBox_Spotify, 11, 2, 1, 1)
        self.checkBox_WinaeroTweaker = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_WinaeroTweaker.sizePolicy().hasHeightForWidth())
        self.checkBox_WinaeroTweaker.setSizePolicy(sizePolicy)
        self.checkBox_WinaeroTweaker.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_WinaeroTweaker.setFont(font)
        self.checkBox_WinaeroTweaker.setStyleSheet("")
        self.checkBox_WinaeroTweaker.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_WinaeroTweaker.setTristate(False)
        self.checkBox_WinaeroTweaker.setObjectName("checkBox_WinaeroTweaker")
        self.gridLayout.addWidget(self.checkBox_WinaeroTweaker, 12, 1, 1, 1)
        self.checkBox_Ventoy = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Ventoy.sizePolicy().hasHeightForWidth())
        self.checkBox_Ventoy.setSizePolicy(sizePolicy)
        self.checkBox_Ventoy.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Ventoy.setFont(font)
        self.checkBox_Ventoy.setStyleSheet("")
        self.checkBox_Ventoy.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Ventoy.setTristate(False)
        self.checkBox_Ventoy.setObjectName("checkBox_Ventoy")
        self.gridLayout.addWidget(self.checkBox_Ventoy, 11, 1, 1, 1)
        self.checkBox_7zip = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_7zip.sizePolicy().hasHeightForWidth())
        self.checkBox_7zip.setSizePolicy(sizePolicy)
        self.checkBox_7zip.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_7zip.setFont(font)
        self.checkBox_7zip.setStyleSheet("")
        self.checkBox_7zip.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_7zip.setTristate(False)
        self.checkBox_7zip.setObjectName("checkBox_7zip")
        self.gridLayout.addWidget(self.checkBox_7zip, 9, 1, 1, 1)
        self.checkBox_Ccleaner = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Ccleaner.sizePolicy().hasHeightForWidth())
        self.checkBox_Ccleaner.setSizePolicy(sizePolicy)
        self.checkBox_Ccleaner.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Ccleaner.setFont(font)
        self.checkBox_Ccleaner.setStyleSheet("")
        self.checkBox_Ccleaner.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Ccleaner.setTristate(False)
        self.checkBox_Ccleaner.setObjectName("checkBox_Ccleaner")
        self.gridLayout.addWidget(self.checkBox_Ccleaner, 8, 1, 1, 1)
        self.checkBox_Powertoys = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Powertoys.sizePolicy().hasHeightForWidth())
        self.checkBox_Powertoys.setSizePolicy(sizePolicy)
        self.checkBox_Powertoys.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Powertoys.setFont(font)
        self.checkBox_Powertoys.setStyleSheet("")
        self.checkBox_Powertoys.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Powertoys.setTristate(False)
        self.checkBox_Powertoys.setObjectName("checkBox_Powertoys")
        self.gridLayout.addWidget(self.checkBox_Powertoys, 10, 1, 1, 1)
        self.checkBox_QtTabBar = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_QtTabBar.sizePolicy().hasHeightForWidth())
        self.checkBox_QtTabBar.setSizePolicy(sizePolicy)
        self.checkBox_QtTabBar.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_QtTabBar.setFont(font)
        self.checkBox_QtTabBar.setStyleSheet("")
        self.checkBox_QtTabBar.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_QtTabBar.setTristate(False)
        self.checkBox_QtTabBar.setObjectName("checkBox_QtTabBar")
        self.gridLayout.addWidget(self.checkBox_QtTabBar, 12, 2, 1, 1)
        self.checkBox_Everything = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Everything.sizePolicy().hasHeightForWidth())
        self.checkBox_Everything.setSizePolicy(sizePolicy)
        self.checkBox_Everything.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Everything.setFont(font)
        self.checkBox_Everything.setStyleSheet("")
        self.checkBox_Everything.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Everything.setTristate(False)
        self.checkBox_Everything.setObjectName("checkBox_Everything")
        self.gridLayout.addWidget(self.checkBox_Everything, 9, 2, 1, 1)
        self.checkBox_WindowsTerminal = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_WindowsTerminal.sizePolicy().hasHeightForWidth())
        self.checkBox_WindowsTerminal.setSizePolicy(sizePolicy)
        self.checkBox_WindowsTerminal.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_WindowsTerminal.setFont(font)
        self.checkBox_WindowsTerminal.setStyleSheet("")
        self.checkBox_WindowsTerminal.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_WindowsTerminal.setTristate(False)
        self.checkBox_WindowsTerminal.setObjectName("checkBox_WindowsTerminal")
        self.gridLayout.addWidget(self.checkBox_WindowsTerminal, 15, 1, 1, 1)
        self.checkBox_IoUnlocker = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IoUnlocker.sizePolicy().hasHeightForWidth())
        self.checkBox_IoUnlocker.setSizePolicy(sizePolicy)
        self.checkBox_IoUnlocker.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_IoUnlocker.setFont(font)
        self.checkBox_IoUnlocker.setStyleSheet("")
        self.checkBox_IoUnlocker.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_IoUnlocker.setTristate(False)
        self.checkBox_IoUnlocker.setObjectName("checkBox_IoUnlocker")
        self.gridLayout.addWidget(self.checkBox_IoUnlocker, 13, 1, 1, 1)
        self.checkBox_RevoUninstaller = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RevoUninstaller.sizePolicy().hasHeightForWidth())
        self.checkBox_RevoUninstaller.setSizePolicy(sizePolicy)
        self.checkBox_RevoUninstaller.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_RevoUninstaller.setFont(font)
        self.checkBox_RevoUninstaller.setStyleSheet("")
        self.checkBox_RevoUninstaller.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_RevoUninstaller.setTristate(False)
        self.checkBox_RevoUninstaller.setObjectName("checkBox_RevoUninstaller")
        self.gridLayout.addWidget(self.checkBox_RevoUninstaller, 14, 1, 1, 1)
        self.checkBox_AutoHotkey = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_AutoHotkey.sizePolicy().hasHeightForWidth())
        self.checkBox_AutoHotkey.setSizePolicy(sizePolicy)
        self.checkBox_AutoHotkey.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_AutoHotkey.setFont(font)
        self.checkBox_AutoHotkey.setStyleSheet("")
        self.checkBox_AutoHotkey.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_AutoHotkey.setTristate(False)
        self.checkBox_AutoHotkey.setObjectName("checkBox_AutoHotkey")
        self.gridLayout.addWidget(self.checkBox_AutoHotkey, 13, 2, 1, 1)
        self.Titus_Utility_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3,clicked=lambda:self.run_titus_utility())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Titus_Utility_btn.setFont(font)
        self.Titus_Utility_btn.setStyleSheet("QPushButton{\n"
"background-color:#0076ff;\n"
"border-style:outlet;\n"
"border-width:2px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#005b99;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#0076ff;\n"
"border-style: inset;\n"
"}\n"
"")
        self.Titus_Utility_btn.setCheckable(False)
        self.Titus_Utility_btn.setAutoDefault(False)
        self.Titus_Utility_btn.setDefault(False)
        self.Titus_Utility_btn.setFlat(False)
        self.Titus_Utility_btn.setObjectName("Titus_Utility_btn")
        self.gridLayout.addWidget(self.Titus_Utility_btn, 2, 4, 1, 1)
        self.checkBox_Whatsapp = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Whatsapp.sizePolicy().hasHeightForWidth())
        self.checkBox_Whatsapp.setSizePolicy(sizePolicy)
        self.checkBox_Whatsapp.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Whatsapp.setFont(font)
        self.checkBox_Whatsapp.setStyleSheet("")
        self.checkBox_Whatsapp.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Whatsapp.setTristate(False)
        self.checkBox_Whatsapp.setObjectName("checkBox_Whatsapp")
        self.gridLayout.addWidget(self.checkBox_Whatsapp, 2, 2, 1, 1)
        self.checkBox_Greenshot = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Greenshot.setFont(font)
        self.checkBox_Greenshot.setObjectName("checkBox_Greenshot")
        self.gridLayout.addWidget(self.checkBox_Greenshot, 3, 0, 1, 1)
        self.checkBox_SublimeText = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_SublimeText.sizePolicy().hasHeightForWidth())
        self.checkBox_SublimeText.setSizePolicy(sizePolicy)
        self.checkBox_SublimeText.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_SublimeText.setFont(font)
        self.checkBox_SublimeText.setStyleSheet("")
        self.checkBox_SublimeText.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_SublimeText.setTristate(False)
        self.checkBox_SublimeText.setObjectName("checkBox_SublimeText")
        self.gridLayout.addWidget(self.checkBox_SublimeText, 2, 3, 1, 1)
        self.checkBox_Drawboard = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Drawboard.sizePolicy().hasHeightForWidth())
        self.checkBox_Drawboard.setSizePolicy(sizePolicy)
        self.checkBox_Drawboard.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Drawboard.setFont(font)
        self.checkBox_Drawboard.setStyleSheet("")
        self.checkBox_Drawboard.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Drawboard.setTristate(False)
        self.checkBox_Drawboard.setObjectName("checkBox_Drawboard")
        self.gridLayout.addWidget(self.checkBox_Drawboard, 8, 0, 1, 1)
        self.checkBox_Discord = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Discord.sizePolicy().hasHeightForWidth())
        self.checkBox_Discord.setSizePolicy(sizePolicy)
        self.checkBox_Discord.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Discord.setFont(font)
        self.checkBox_Discord.setStyleSheet("")
        self.checkBox_Discord.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Discord.setTristate(False)
        self.checkBox_Discord.setObjectName("checkBox_Discord")
        self.gridLayout.addWidget(self.checkBox_Discord, 1, 2, 1, 1)
        self.checkBox_Git = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Git.sizePolicy().hasHeightForWidth())
        self.checkBox_Git.setSizePolicy(sizePolicy)
        self.checkBox_Git.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Git.setFont(font)
        self.checkBox_Git.setStyleSheet("")
        self.checkBox_Git.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Git.setTristate(False)
        self.checkBox_Git.setObjectName("checkBox_Git")
        self.gridLayout.addWidget(self.checkBox_Git, 4, 3, 1, 1)
        
        self.Install_selected_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3,clicked=lambda:self.install_selected_apps())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Install_selected_btn.setFont(font)
        self.Install_selected_btn.setStyleSheet("QPushButton{\n"
                        "background-color:#0076ff;\n"
                        "border-style:outlet;\n"
                        "border-width:2px;\n"
                        "}\n"
                        "QPushButton:hover{\n"
                        "background-color:#005b99;\n"
                        "}\n"
                        "QPushButton:pressed{\n"
                        "background-color:#0076ff;\n"
                        "border-style: inset;\n"
                        "}\n"
                        "")
        self.Install_selected_btn.setCheckable(False)
        self.Install_selected_btn.setAutoDefault(False)
        self.Install_selected_btn.setDefault(False)
        self.Install_selected_btn.setFlat(False)
        self.Install_selected_btn.setObjectName("Install_selected_btn")
        self.gridLayout.addWidget(self.Install_selected_btn, 1, 4, 1, 1)
        
        self.label_Other = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Other.setFont(font)
        self.label_Other.setObjectName("label_Other")
        self.gridLayout.addWidget(self.label_Other, 6, 2, 1, 1)
        self.checkBox_VmwarePlayer = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VmwarePlayer.sizePolicy().hasHeightForWidth())
        self.checkBox_VmwarePlayer.setSizePolicy(sizePolicy)
        self.checkBox_VmwarePlayer.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_VmwarePlayer.setFont(font)
        self.checkBox_VmwarePlayer.setStyleSheet("")
        self.checkBox_VmwarePlayer.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_VmwarePlayer.setTristate(False)
        self.checkBox_VmwarePlayer.setObjectName("checkBox_VmwarePlayer")
        self.gridLayout.addWidget(self.checkBox_VmwarePlayer, 5, 3, 1, 1)
        self.checkBox_Notepads = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Notepads.sizePolicy().hasHeightForWidth())
        self.checkBox_Notepads.setSizePolicy(sizePolicy)
        self.checkBox_Notepads.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Notepads.setFont(font)
        self.checkBox_Notepads.setStyleSheet("")
        self.checkBox_Notepads.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Notepads.setTristate(False)
        self.checkBox_Notepads.setObjectName("checkBox_Notepads")
        self.gridLayout.addWidget(self.checkBox_Notepads, 11, 0, 1, 1)
        self.checkBox_GithubDesktop = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_GithubDesktop.sizePolicy().hasHeightForWidth())
        self.checkBox_GithubDesktop.setSizePolicy(sizePolicy)
        self.checkBox_GithubDesktop.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_GithubDesktop.setFont(font)
        self.checkBox_GithubDesktop.setStyleSheet("")
        self.checkBox_GithubDesktop.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_GithubDesktop.setTristate(False)
        self.checkBox_GithubDesktop.setObjectName("checkBox_GithubDesktop")
        self.gridLayout.addWidget(self.checkBox_GithubDesktop, 3, 3, 1, 1)
        self.checkBox_Obsidian = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Obsidian.sizePolicy().hasHeightForWidth())
        self.checkBox_Obsidian.setSizePolicy(sizePolicy)
        self.checkBox_Obsidian.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Obsidian.setFont(font)
        self.checkBox_Obsidian.setStyleSheet("")
        self.checkBox_Obsidian.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Obsidian.setTristate(False)
        self.checkBox_Obsidian.setObjectName("checkBox_Obsidian")
        self.gridLayout.addWidget(self.checkBox_Obsidian, 12, 0, 1, 1)
        self.checkBox_NotepadPlusPlus = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_NotepadPlusPlus.sizePolicy().hasHeightForWidth())
        self.checkBox_NotepadPlusPlus.setSizePolicy(sizePolicy)
        self.checkBox_NotepadPlusPlus.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_NotepadPlusPlus.setFont(font)
        self.checkBox_NotepadPlusPlus.setStyleSheet("")
        self.checkBox_NotepadPlusPlus.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_NotepadPlusPlus.setTristate(False)
        self.checkBox_NotepadPlusPlus.setObjectName("checkBox_NotepadPlusPlus")
        self.gridLayout.addWidget(self.checkBox_NotepadPlusPlus, 10, 0, 1, 1)
        self.label_Photos = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Photos.sizePolicy().hasHeightForWidth())
        self.label_Photos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Photos.setFont(font)
        self.label_Photos.setObjectName("label_Photos")
        self.gridLayout.addWidget(self.label_Photos, 0, 0, 1, 1)
        self.label_Social = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Social.setFont(font)
        self.label_Social.setObjectName("label_Social")
        self.gridLayout.addWidget(self.label_Social, 0, 2, 1, 1)
        self.label_Options = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Options.setFont(font)
        self.label_Options.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_Options.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Options.setObjectName("label_Options")
        self.gridLayout.addWidget(self.label_Options, 0, 4, 1, 1)
        self.label_Browser = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Browser.setFont(font)
        self.label_Browser.setObjectName("label_Browser")
        self.gridLayout.addWidget(self.label_Browser, 0, 1, 1, 1)
        self.checkBox_Canva = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Canva.sizePolicy().hasHeightForWidth())
        self.checkBox_Canva.setSizePolicy(sizePolicy)
        self.checkBox_Canva.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Canva.setFont(font)
        self.checkBox_Canva.setStyleSheet("")
        self.checkBox_Canva.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Canva.setTristate(False)
        self.checkBox_Canva.setObjectName("checkBox_Canva")
        self.gridLayout.addWidget(self.checkBox_Canva, 1, 0, 1, 1)
        self.checkBox_TeamViewer = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_TeamViewer.sizePolicy().hasHeightForWidth())
        self.checkBox_TeamViewer.setSizePolicy(sizePolicy)
        self.checkBox_TeamViewer.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_TeamViewer.setFont(font)
        self.checkBox_TeamViewer.setStyleSheet("")
        self.checkBox_TeamViewer.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_TeamViewer.setTristate(False)
        self.checkBox_TeamViewer.setObjectName("checkBox_TeamViewer")
        self.gridLayout.addWidget(self.checkBox_TeamViewer, 14, 2, 1, 1)
        self.checkBox_Duplicati = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_Duplicati.sizePolicy().hasHeightForWidth())
        self.checkBox_Duplicati.setSizePolicy(sizePolicy)
        self.checkBox_Duplicati.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_Duplicati.setFont(font)
        self.checkBox_Duplicati.setStyleSheet("")
        self.checkBox_Duplicati.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_Duplicati.setTristate(False)
        self.checkBox_Duplicati.setObjectName("checkBox_Duplicati")
        self.gridLayout.addWidget(self.checkBox_Duplicati, 16, 1, 1, 1)
        self.label_Development = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Development.setFont(font)
        self.label_Development.setObjectName("label_Development")
        self.gridLayout.addWidget(self.label_Development, 0, 3, 1, 1)
        self.checkBox_TaskbarX = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_TaskbarX.sizePolicy().hasHeightForWidth())
        self.checkBox_TaskbarX.setSizePolicy(sizePolicy)
        self.checkBox_TaskbarX.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_TaskbarX.setFont(font)
        self.checkBox_TaskbarX.setStyleSheet("")
        self.checkBox_TaskbarX.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_TaskbarX.setTristate(False)
        self.checkBox_TaskbarX.setObjectName("checkBox_TaskbarX")
        self.gridLayout.addWidget(self.checkBox_TaskbarX, 8, 2, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.addWidget(self.scrollArea_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.install_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout.addLayout(self.gridLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AmazeX Utility"))
        self.label.setText(_translate("MainWindow", "AmazeX Utility"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>This Utility Requires<span style=\" font-weight:600;\"> Chocoltey Package Manger </span>to install other Programs</p><p>Make Sure it is <span style=\" font-weight:600;\">Installed </span>on your system  before installing anything!!.</p></body></html>"))
        
        self.Install_Chocolatey_btn.setText(_translate("MainWindow", "Install Chocolatey"))
        self.Download_AKMSorter_btn.setText(_translate("MainWindow", "Download AKM Sorter"))
        self.Download_AmazeX_btn.setText(_translate("MainWindow", "Download AmazeX"))
        self.label_StatusBar.setText(_translate("MainWindow", "Current Version: "))
        self.check_for_update_btn.setText(_translate("MainWindow", "Check for Updates"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("MainWindow", "Home"))
        self.label_Utilities.setText(_translate("MainWindow", "Utilities"))
        self.checkBox_Chrome.setText(_translate("MainWindow", "Chrome"))
        self.checkBox_Xodo.setText(_translate("MainWindow", "Xodo"))
        self.checkBox_Telegram.setText(_translate("MainWindow", "Telegram"))
        self.checkBox_IrfanView.setText(_translate("MainWindow", "IrfanView"))
        self.checkBox_VsCode.setText(_translate("MainWindow", "Vs Code"))
        self.checkBox_Brave.setText(_translate("MainWindow", "Brave"))
        self.checkBox_Firefox.setText(_translate("MainWindow", "Firefox"))
        self.checkBox_ShareX.setText(_translate("MainWindow", "ShareX"))
        self.label_Documents.setText(_translate("MainWindow", "Documents"))
        self.Update_Apps_btn.setText(_translate("MainWindow", "Update Apps"))
        self.checkBox_Vlc.setText(_translate("MainWindow", "Vlc"))
        self.checkBox_Spotify.setText(_translate("MainWindow", "Spotify"))
        self.checkBox_WinaeroTweaker.setText(_translate("MainWindow", "Winaero Tweaker"))
        self.checkBox_Ventoy.setText(_translate("MainWindow", "Ventoy"))
        self.checkBox_7zip.setText(_translate("MainWindow", "7zip"))
        self.checkBox_Ccleaner.setText(_translate("MainWindow", "Ccleaner"))
        self.checkBox_Powertoys.setText(_translate("MainWindow", "Powertoys"))
        self.checkBox_QtTabBar.setText(_translate("MainWindow", "QtTabBar"))
        self.checkBox_Everything.setText(_translate("MainWindow", "Everything"))
        self.checkBox_WindowsTerminal.setText(_translate("MainWindow", "Windows Terminal"))
        self.checkBox_IoUnlocker.setText(_translate("MainWindow", "Io Unlocker"))
        self.checkBox_RevoUninstaller.setText(_translate("MainWindow", "Revo Uninstaller"))
        self.checkBox_AutoHotkey.setText(_translate("MainWindow", "AutoHotkey"))
        self.Titus_Utility_btn.setText(_translate("MainWindow", "Titus Utility"))
        self.checkBox_Whatsapp.setText(_translate("MainWindow", "Whatsapp"))
        self.checkBox_Greenshot.setText(_translate("MainWindow", "Greenshot"))
        self.checkBox_SublimeText.setText(_translate("MainWindow", "Sublime Text"))
        self.checkBox_Drawboard.setText(_translate("MainWindow", "Drawboard"))
        self.checkBox_Discord.setText(_translate("MainWindow", "Discord"))
        self.checkBox_Git.setText(_translate("MainWindow", "Git"))
        self.Install_selected_btn.setText(_translate("MainWindow", "Install Selected"))
        self.label_Other.setText(_translate("MainWindow", "Other"))
        self.checkBox_VmwarePlayer.setText(_translate("MainWindow", "Vmware Player"))
        self.checkBox_Notepads.setText(_translate("MainWindow", "Notepads"))
        self.checkBox_GithubDesktop.setText(_translate("MainWindow", "Github Desktop"))
        self.checkBox_Obsidian.setText(_translate("MainWindow", "Obsidian"))
        self.checkBox_NotepadPlusPlus.setText(_translate("MainWindow", "Notepad++"))
        self.label_Photos.setText(_translate("MainWindow", "Photos"))
        self.label_Social.setText(_translate("MainWindow", "Social"))
        self.label_Options.setText(_translate("MainWindow", "Options"))
        self.label_Browser.setText(_translate("MainWindow", "Browser"))
        self.checkBox_Canva.setText(_translate("MainWindow", "Canva"))
        self.checkBox_TeamViewer.setText(_translate("MainWindow", "TeamViewer"))
        self.checkBox_Duplicati.setText(_translate("MainWindow", "Duplicati"))
        self.label_Development.setText(_translate("MainWindow", "Development"))
        self.checkBox_TaskbarX.setText(_translate("MainWindow", "TaskbarX"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.install_tab), _translate("MainWindow", "Install"))
        self.programStartup()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
