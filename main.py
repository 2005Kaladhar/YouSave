#Python based Youtube Video downloader project
from PySide6.QtCore import (Qt,QRunnable,Slot,QThreadPool,QPoint,Signal,QObject)
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (QApplication, QMainWindow,QGraphicsOpacityEffect,QFileDialog)

from pytubefix import YouTube,request,cipher
from ui_ui import Ui_MainWindow as mainScreen

from subprocess import run as commandRunner
from os import remove as delFile
from os import path,getcwd
import sys


#Changing the chunck size to 200 kilo bytes
request.default_range_size = 200000

class WorkerSignals(QObject):
    finished = Signal()


class LoadVideoThread(QRunnable):
    
    def __init__(self,fun,*args) -> None:
        super().__init__()
        self.function  = fun
        self.args = args
        self.signal = WorkerSignals()
    
    @Slot()  
    def run(self):
        self.function(*self.args)
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainScreen()
        self.ui.setupUi(self)
        
        #Creating QThreadpool for threading
        self.threadpool = QThreadPool()
        
        #Making frameless window
        self.setFocusPolicy(Qt.StrongFocus)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.opacity_effect = QGraphicsOpacityEffect()
        
        #Adding functions to windows buttons
        self.ui.closeButton.clicked.connect(self.closeWindow)
        self.ui.minimiseButton.clicked.connect(lambda : self.showMinimized())
        self.ui.windowFrame.mouseMoveEvent = self.moveWindow
        
        #Variables 
        self.thumbNail = False
        self.audio = False
        self.video = False
        
        #Set the default page 0 when loads the window
        self.ui.stackedWidget.setCurrentIndex(0)
        
        #Set no text on the video title lable above the url area
        self.ui.videoTitle.setText("Welcome to YouSave")
        
        #Button Actions
        self.ui.progressBar.hide()
        
        #When enter is pressed on lineEdit then perform a function
        self.ui.urlArea.returnPressed.connect(self.enterPressed)
        
        #When next button is clicked perform the next function
        self.ui.DownloadButton.clicked.connect(self.downloadButtonClicked)
        
        #Radio button actions
        self.ui.downloadVideoBtn.clicked.connect(self.videoRadio)
        self.ui.downloadVideoBtn.setChecked(True) #By default video is checked
        
        self.ui.downloadudioBtn.clicked.connect(self.audioRadio)
        self.ui.downloadThumbnail.clicked.connect(self.thumbRadio)
        
        self.ui.backButton.clicked.connect(self.backButton)
        
        #When dropdown item is changed 
        self.ui.qualityDropDown.currentTextChanged.connect(self.displayFileSize)
        
        #Show the window
        self.show()
    
    def videoRadio(self,event):
        print(event,'Video radio button clicked')
        self.ui.DownloadButton.setText("Next")
        self.ui.urlType.setText("Type : Video")
             
    def thumbRadio(self,event):
        print(event,"ThumbNail radio button")
        self.ui.DownloadButton.setText("Next")
        self.ui.urlType.setText("(Not available right now!)")
        
    def audioRadio(self,event):
        print(event,"Audio Radio clicked")
        self.ui.DownloadButton.setText("Next")
        self.ui.urlType.setText("Type : Audio")
        
    #load the link    
    def loadLink(self,link):
        
         self.disableOptions(True)
         print("Inside loadlink function")
         self.ui.videoTitle.show()
         self.ui.videoTitle.show()
         self.ui.videoTitle.setText("Loading link...")
         try:
            print("Creating instance of Youtube class")
            self.yt = YouTube(url=link)
            title = list(self.yt.title)
            for i in title:
                if i in ["'",'"',"|"]:
                    title[title.index(i)] = ""
                    
            self.title = ''.join(title)
            print("refined video title : ",self.title)
            
            
            self.qualitylist = {}
            
            if self.ui.downloadVideoBtn.isChecked():
                for i in self.yt.streams.filter(type="video",file_extension='mp4'):
                    self.qualitylist[str(i.resolution)]=str(i.itag)
            elif self.ui.downloadudioBtn.isChecked():
                for i in self.yt.streams.filter(type="audio",file_extension='mp4'):
                    self.qualitylist[str(i.abr)]=str(i.itag)
                
            self.populateDropDown()
            
            self.ui.videoTitle.clear()
            self.ui.DownloadButton.setText("Download")
            self.disableOptions(False)
         except Exception as e :
            print(e)
            self.ui.videoTitle.setText("Error!!")   
            self.disableOptions(False) 
     
    #populate the dropdown menu
    def populateDropDown(self):
        self.ui.videoTitle.setText("Link Loaded!!")
        self.ui.qualityDropDown.addItems(list(self.qualitylist.keys()))
    
    #to displayfile size whenever drop down item is changed  
    def displayFileSize(self):   
        #audio file itag = 140
        
        itag = int(self.qualitylist[str(self.ui.qualityDropDown.currentText())])
        
        self.filesize = (self.yt.streams.get_by_itag(itag).filesize/1000000)
        
        filesize = self.filesize
        # When video file is to be downloaded show the file size of audio + video in Mb
        if self.ui.downloadVideoBtn.isChecked() :
            fileseize = int (self.filesize) + int (self.yt.streams.get_by_itag(140).filesize/1000000)
        
            
        print(f"file size is : {filesize}Mb")
        self.ui.fileSize.setText(f"%.2fMb"%self.filesize)
        
        #Enable the stackedwidgets to get the options 
        self.disableOptions(False)
    
    #To disable stackedwidget and download button
    def disableOptions(self,arg):
        if arg:
            self.ui.DownloadButton.setEnabled(not arg)
            self.ui.stackedWidget.setEnabled(not arg)
            self.ui.backButton.setEnabled(not arg)
        else:
            self.ui.DownloadButton.setEnabled(not arg)
            self.ui.stackedWidget.setEnabled(not arg)   
            self.ui.backButton.setEnabled(not arg)
    
    #Check the format of link 
    def linkChecker(self,link):
        formats = ["https://youtube.com/watch?","https://youtube.com/embed/","https://youtu.be/","https://www.youtube.com/watch?"]
        for i in formats:
            if i in link and (len(i)!= len(self.ui.urlArea.text())):
                return True
        return False
    
    #Function to plot progress
    def progressCounter(self,chunck,fileHandle,byteRemaning):
        percent = 100- int(((byteRemaning/1000000)/self.filesize)*100)
        print("Percentage Completed : ",percent,"%")
        self.ui.progressBar.setValue(percent)
        
    #Function to do when download is completed
    def downloadComplete(self,*args):
        self.ui.urlArea.clear()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.hide()
        self.threadpool.clear()
        self.ui.videoTitle.hide()
        self.ui.DownloadButton.setText("Next")
        self.ui.qualityDropDown.clear()
    
    #Function to download the video
    def downloadVideo(self):
        #Setting on progress and on complete callback functions
        self.yt.register_on_progress_callback(self.progressCounter)
        
        # Setting it to None because audio file has to be downloaded, it will be set there
        self.yt.register_on_complete_callback(None)
        
        #Notify that Video File is being downloaded
        if self.ui.downloadVideoBtn.isChecked():
            self.ui.videoTitle.setText("Downloading Video..")
        
        #Notify when downloading Audio file
        elif self.ui.downloadudioBtn.isChecked():
            self.ui.videoTitle.setText("Downloading Audio")
        outputpath = self.response
        
        videofilepath = str(self.title).replace(" ","-")
        
        # Name should be different when downloading Video File
        if self.ui.downloadVideoBtn.isChecked():
            self.yt.streams.get_by_itag(self.qualitylist[f'{self.ui.qualityDropDown.currentText()}']).download(output_path=outputpath,filename=path.normpath(r'''VideoFile{videopath}.mp4'''.format(videopath=videofilepath)))
        
        
        # Name should be different when downloading only audio file
        elif self.ui.downloadudioBtn.isChecked():
            self.yt.streams.get_by_itag(self.qualitylist[f'{self.ui.qualityDropDown.currentText()}']).download(output_path=outputpath,filename=path.normpath(r'''AudioFile{videopath}.mp4'''.format(videopath=videofilepath)))
            
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.stackedWidget.setEnabled(True)
            self.ui.DownloadButton.setEnabled(True)
            self.ui.DownloadButton.setText("Done")
        
        
        # When video button is checked then do this 
        if self.ui.downloadVideoBtn.isChecked():
            #Notify that Audio file is being downloaded
            self.ui.videoTitle.setText("Downloading Audio...")
            self.downloadAudio(path.normpath(r'''AudioFile{videotitle}.mp4'''.format(videotitle=self.title)))
        
    def backButton(self):
        self.ui.DownloadButton.setEnabled(True)
        self.downloadComplete()
    
    #To download the audio file
    def downloadAudio(self,filename=None):
        #Setting on progress and on complete callback functions
        self.yt.register_on_progress_callback(self.progressCounter)
        
        # When no argument is given to the file (The case of downloading Audio file then assign a file name )
        if filename == None:
            filename = path.normpath(r'''AudioFile{videotitle}.mp4'''.format(videotitle=self.title)) 
        
        #Download the audio file
        self.yt.streams.get_by_itag(140).download(output_path=self.response,filename=path.normpath(filename.replace(" ","-")))
        
        if not self.ui.downloadudioBtn.isChecked():
            self.combiningAudioVideoFile()
    

    #Perform actions when (download button/ next button) is clicked
    def downloadButtonClicked(self):
        
        # When downloading video
        if self.ui.DownloadButton.text() == "Next" :
            self.enterPressed()
            
        elif self.ui.DownloadButton.text() == "Download":
            #Show progress bar and video title label
            self.ui.progressBar.show()
            self.ui.videoTitle.show()
            
            self.response = QFileDialog.getExistingDirectory( )
            print("Folder path : ",self.response)
            
            self.disableOptions(True)
            
            download = LoadVideoThread(self.downloadVideo)
            
            self.threadpool.start(download)
            
        elif self.ui.DownloadButton.text() == "Done":
            self.backButton()

    #Combining Audio and video file to create a final file
    def combiningAudioVideoFile(self):
        self.ui.videoTitle.setText("Combining Audio and Video File")
        spaceremoved = str(self.title).replace(" ",'-')
        videopath = path.join(self.response,path.normpath(r"VideoFile{spce}.mp4".format(spce=spaceremoved)))
        
        audiopath =path.join(self.response,path.normpath( r"AudioFile{spce}.mp4".format(spce=spaceremoved)))
                             
        finalpath =  path.join(self.response,path.normpath(r"DownloadedFile{spce}.mp4".format(spce=spaceremoved) ) )
        
        print("Video path - ",videopath)
        print("Audio path - ",audiopath)
        print("Final path - ",videopath)
        commandRunner(r'''ffmpeg -i {vidpath} -i {audpath} -c copy {finpath} -y'''.format(vidpath=videopath,audpath=audiopath,finpath=finalpath))
        
        #Delete audio and video file downloaded
        delFile(videopath)
        delFile(audiopath)
        self.ui.videoTitle.setText("Video Downloaded")
        
        self.ui.DownloadButton.setEnabled(False)
        
        self.disableOptions(False)
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.DownloadButton.setText("Done")
    
    #WHen enter is pressed on url area or next button is clicked 
    def enterPressed(self):  
        
        # When url area is empty or thumbnail button is checked
        if self.ui.urlArea.text() == "" or self.ui.downloadThumbnail.isChecked():
            self.ui.stackedWidget.setCurrentIndex(0)
            self.threadpool.clear()
            self.disableOptions(False)
            self.ui.videoTitle.setText("Welcome to YouSave")
            self.ui.DownloadButton.setText("Next")
            print("Either url area is empty or thumbnail button is checked(its not available right now!)")
        
        #When link area is not empty then load the link
        else:
            #Check validity of link
            if self.linkChecker(self.ui.urlArea.text()):    
                #using thread load the link
                print("Calling the linkload function")
                linkLoad = LoadVideoThread(self.loadLink,str(self.ui.urlArea.text()))
                self.threadpool.start(linkLoad)
    
                self.ui.DownloadButton.setText("Next")
                self.ui.progressBar.hide()
                self.ui.progressBar.setValue(0)
            else:
                self.ui.videoTitle.setText("Wrong Format")
                    
        if self.ui.urlArea.text() != "" and self.linkChecker(self.ui.urlArea.text()):
            self.ui.stackedWidget.setCurrentIndex(1)
    
        
    
    #Functions for moving the frameless WIndow
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()
    
    def closeWindow(self):
        self.close()
        try:
            self.close()
            self.threadpool.deleteLater()
        except AttributeError as e:
            pass
    
    def moveWindow(self, event: QMouseEvent) -> None:
        delt = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delt.x() , self.y() + delt.y())
        self.oldPosition = event.globalPos();
    
    
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec())
    