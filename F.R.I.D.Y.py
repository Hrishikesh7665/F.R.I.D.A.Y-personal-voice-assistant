from random import randint
from PIL import ImageTk #,Image
from tkinter import ttk, messagebox, colorchooser
from tkinter import *
import PIL.Image
import os,sys,signal
import webbrowser
#import pyaudio
from playsound import playsound
import threading
from threading import Thread
from datetime import datetime
#from tkinter import colorchooser
import speech_recognition as sr
import pyttsx3
import time
import shutil
import re
import webbrowser
import googlesearch as GS
import pyttsx3.drivers
import pyttsx3.drivers.sapi5

# ImportFromOther
#import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
#from tkinter import *
## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen
import webScrapping
import normalChat
import game
import dictionary
import math_function
import ToDo
import fileHandler



appdata_path = os.getenv('APPDATA')
pid= os.getpid()

def resource_path():
    CurrentPath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    # Look for the 'sprites' folder on the path I just gave you:
    spriteFolderPath = os.path.join(CurrentPath, 'Assets/')
    path = os.path.join(spriteFolderPath)
    newPath = path.replace(os.sep, '/')
    return newPath



_path = resource_path()



ownerPhoto = 1
ownerName = ""
ownerDesignation = ""
Theme_Mode = 0          #0=Light #1= Dark
ai_name = 'F.R.I.D.Y.'.lower()
data_update_check = 0
rec_email, rec_phoneno = "", ""


root = Tk()
#root.geometry("350x550")
root.iconbitmap(_path+'Images/userI.ico')


def center_window(w=350, h=550):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)  #change hs/2 to hs/4 to left window up
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

center_window(350, 550)


root.title("F.R.I.D.A.Y User Registration")
root.resizable(0,0)

r = IntVar()
Color_state = 0
Male_Check = IntVar()
Female_Check = IntVar()
userName_Var = StringVar()
userName_Var.set("Enter Your Name Here")
Gen = ""
stop_threads = False
status = "Stopped"

userFrame2 = Frame(root, bd=10, width=300, height=550, relief=FLAT)
userFrame2.pack(padx=10, pady=10)
firstAvatar_choosing_Frame = Frame(root)
Fake_L_3 = Label(firstAvatar_choosing_Frame, text=" ", font=('arial', 15))
Chouse_Avtar_LAbel = Label(firstAvatar_choosing_Frame, text="Choose Your Avatar", font=('arial', 15))
avatarContainer = Frame(firstAvatar_choosing_Frame, width=300, height=500)
SuccessfullyRegistered_Frame = Frame(root)
#    Choose Avatar
def countDown():
    addBtn.config(fg="black")
    for k in range(10, 0, -1):
        addBtn["text"] ="  Choose Avatar  "+"("+str(k)+")"
        root.update()
        time.sleep(0.94)
    addBtn["text"] = "    Choose Avatar    "
    addBtn.config(fg='white')

def play_Audio(which):
    global status
    #Intro
    if status == "Stopped":
        status = "Running"
        playsound(_path+'Audio/'+which+'.mp3')
        addBtn.config(state="normal")
        status = "Stopped"

t1 = threading.Thread(target=lambda:play_Audio("Intro"))
t1.daemon = True

t2 = threading.Thread(target=countDown)
t2.daemon = True

#print(datetime.now().strftime('%H:%M:%S'))

def typeit(widget, index, string):
    #print(datetime.now().strftime('%H:%M:%S'))
    if len(string) > 0:
        widget.configure(state='normal')
        widget.insert(index, string[0])
        widget.configure(state='disabled')
    if len(string) > 1:
        # compute index of next char
        index = widget.index("%s + 1 char" % index)
        # type the next character in half a second
        widget.after(120, typeit, widget, index, string[1:])


Friday_Logo = PIL.Image.open(_path+'Images/F.R.I.D.A.Y.jpg')
Friday_Logo = Friday_Logo.resize((200, 200))
Friday_Logo = ImageTk.PhotoImage(Friday_Logo)

Fr_Logo = Label(userFrame2, image=Friday_Logo)
Fr_Logo.pack()

Fake_L_1 = Label(userFrame2, text='                     \n ', font=('Arial Bold', 4))
Fake_L_1.pack()

text_Field = Text(userFrame2,font=('Fixedsys',16), width=31, height=3)
text_Field.pack()

typeit(text_Field, "1.0", "Hello! I Am F.R.I.D.A.Y, I Am A\nVirtual Assistant Developed By\nHrishikesh Patra")



Fake_L_2 = Label(userFrame2, text='                     \n                          \n                 \n                ', font=('Arial Bold', 120))
Fake_L_2.pack()

def on_name_input_click(event):
    if userName_Var.get() == "Enter Your Name Here":
        statusLbl.place(x=1000, y=1000)
        nameField.delete(0, "end") # delete all the text in the entry
        nameField.insert(0, '') #Insert blank for user input
        nameField.config(fg = 'gray16')

def on_name_input_focusout(event):
    if userName_Var.get () != 'Enter Your Name Here':
        nameField.config(fg = 'gray16')
    if nameField.get() == '':
        userName_Var.set('Enter Your Name Here')
        nameField.config(fg = 'grey60')

nameLbl = Label(userFrame2, text='Name', font=('Arial Bold', 12))
nameLbl.place(x=20,y=300)
nameField = Entry(userFrame2, textvariable=userName_Var,  bd=5, font=("Comic Sans MS",9), width=25, relief=FLAT,bg="pale turquoise",fg="gray60")
nameField.place(x=90,y=300)

nameField.bind('<FocusIn>', on_name_input_click)
nameField.bind('<FocusOut>', on_name_input_focusout)

genLbl = Label(userFrame2, text='Gender', font=('Arial Bold', 12))
genLbl.place(x=20,y=360)

'''genMale = ttk.Radiobutton(userFrame2, text='Male', value=1, variable=r, style='Wild.TRadiobutton', takefocus=False)
genMale.place(x=110,y=360)
genFemale = ttk.Radiobutton(userFrame2, text='Female', value=2, variable=r, style='Wild.TRadiobutton', takefocus=False)
genFemale.place(x=180,y=360)'''

genMaleImg = PIL.Image.open(_path+'Images/Male.png')
genMaleImg = genMaleImg.resize((35, 35))
genMaleImg = ImageTk.PhotoImage(genMaleImg)


genFemaleImg = PIL.Image.open(_path+'Images/Female.png')
genFemaleImg = genFemaleImg.resize((35, 35))
genFemaleImg = ImageTk.PhotoImage(genFemaleImg)


def specChoice(V):
    global Gen,ownerDesignation
    if V ==1:
        Gen = "Male"
        ownerDesignation = "Sir"
        Female_Check.set(0)
        #print(Male_Check.get())
        #print("Hi")
    if V ==2:
        Gen = "Female"
        ownerDesignation = "Madam"
        Male_Check.set(0)
        #print("Hello")

Malecheck_Btn = Checkbutton(userFrame2,cursor="hand2",variable = Male_Check,command=lambda :specChoice(1), onvalue = 1, offvalue = 0, height = 2, width = 10)
Malecheck_Btn.place(x=85,y=353)

Male_Logo = Label(userFrame2, image=genMaleImg,bg="black")
Male_Logo.place(x=138,y=351)

Femalecheck_Btn = Checkbutton(userFrame2,cursor="hand2",variable = Female_Check,command=lambda :specChoice(2), onvalue = 1, offvalue = 0, height = 2, width = 10)
Femalecheck_Btn.place(x=170,y=353)

Female_Logo = Label(userFrame2, image=genFemaleImg,bg="black")
Female_Logo.place(x=223,y=351)

Male_Logo = Label(userFrame2, image=genMaleImg,bg="black")
Male_Logo.place(x=138,y=351)

#Male_Check = IntVar()
#Female_Check = IntVar()

def Add_Face():
    global user_name,ownerName
    user_name = userName_Var.get()
    if user_name == '' or user_name == "Enter Your Name Here":
        statusLbl.place(x=91, y=470)
        #t1.join()
        play_Audio("Name")
        statusLbl.config(bg="ivory2", fg="indian red",text="(Enter Your Name)")
    elif Male_Check.get()==0 and Female_Check.get() == 0:
        statusLbl.place(x=87, y=470)
        play_Audio("Gen")
        statusLbl.config(bg="ivory2", fg="indian red",text="(Select Your Gender)")
    else:
        ownerName=user_name
        firstAvatar_choosing_Frame.place(x=30,y=0)


Light_ModeImg = PIL.Image.open(_path+'Images/LightMode.png')
Light_ModeImg = Light_ModeImg.resize((22, 22))
Light_ModeImg = ImageTk.PhotoImage(Light_ModeImg)


Dark_ModeImg = PIL.Image.open(_path+'Images/DarkMode.png')
Dark_ModeImg = Dark_ModeImg.resize((22, 22))
Dark_ModeImg = ImageTk.PhotoImage(Dark_ModeImg)

Light_Mode_Button = Button(root,cursor="hand2", image=Light_ModeImg, bd=2, padx=10)
Dark_Mode_Button = Button(root,cursor="hand2", image=Dark_ModeImg, bd=2, padx=10)





#---------------------------------------------------------------------------End
addBtn = Button(userFrame2, text='    Choose Avatar    ', font=('Arial Bold', 12), bg='#01933B', fg='white',command=Add_Face, relief=FLAT)
addBtn.place(x=75, y=430)
addBtn.config(state="disable")


statusLbl = Label(userFrame2, text='', font=('Cooper Black',9))

check_Img =PIL.Image.open(_path+'Images/Check.png')
check_Img = check_Img.resize((72, 72))
check_Img = ImageTk.PhotoImage(check_Img)



avatarChoosen = 0
#choosedAvtrImage = None
coordinates_List =[(50,50),(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1)]



def selectAVATAR(avt=0):
    global avatarChoosen,ownerPhoto
    avatarChoosen = avt
    i=1
    for avtr in (avtb1,avtb2,avtb3,avtb4,avtb5,avtb6,avtb7,avtb8):
        if i==avt:
            row, column =coordinates_List[i]
            #print(i)
            check_Label.grid(row=row, column=column,ipadx=25, ipady=10)
            avtr['state'] = 'disabled'
            userPIC['image'] = avtr['image']
            ownerPhoto = i
            usernameLbl.config(text=userName_Var.get())
        else: avtr['state'] = 'normal'
        i+=1



Fake_L_3.pack()
Chouse_Avtar_LAbel.place(x=52,y=10)
avatarContainer.pack(pady=10)

size = 92
avtr1 = PIL.Image.open(_path+'Images/Avatar/UserFace1.png')
avtr1 = avtr1.resize((size, size))
avtr1 = ImageTk.PhotoImage(avtr1)
avtr2 = PIL.Image.open(_path+'Images/Avatar/UserFace2.png')
avtr2 = avtr2.resize((size, size))
avtr2 = ImageTk.PhotoImage(avtr2)
avtr3 = PIL.Image.open(_path+'Images/Avatar/UserFace3.png')
avtr3 = avtr3.resize((size, size))
avtr3 = ImageTk.PhotoImage(avtr3)
avtr4 = PIL.Image.open(_path+'Images/Avatar/UserFace4.png')
avtr4 = avtr4.resize((size, size))
avtr4 = ImageTk.PhotoImage(avtr4)
avtr5 = PIL.Image.open(_path+'Images/Avatar/UserFace5.png')
avtr5 = avtr5.resize((size, size))
avtr5 = ImageTk.PhotoImage(avtr5)
avtr6 = PIL.Image.open(_path+'Images/Avatar/UserFace6.png')
avtr6 = avtr6.resize((size, size))
avtr6 = ImageTk.PhotoImage(avtr6)
avtr7 = PIL.Image.open(_path+'Images/Avatar/UserFace7.png')
avtr7 = avtr7.resize((size, size))
avtr7 = ImageTk.PhotoImage(avtr7)
avtr8 = PIL.Image.open(_path+'Images/Avatar/UserFace8.png')
avtr8 = avtr8.resize((size, size))
avtr8 = ImageTk.PhotoImage(avtr8)


avtb1 = Button(avatarContainer,cursor="hand2", image=avtr1, relief=FLAT, bd=0, command=lambda:selectAVATAR(1))
avtb1.grid(row=0, column=0, ipadx=25, ipady=10)

avtb2 = Button(avatarContainer,cursor="hand2", image=avtr2, relief=FLAT, bd=0, command=lambda:selectAVATAR(2))
avtb2.grid(row=0, column=1, ipadx=25, ipady=10)

avtb3 = Button(avatarContainer,cursor="hand2", image=avtr3, relief=FLAT, bd=0, command=lambda:selectAVATAR(3))
avtb3.grid(row=1, column=0, ipadx=25, ipady=10)

avtb4 = Button(avatarContainer,cursor="hand2", image=avtr4, relief=FLAT, bd=0, command=lambda:selectAVATAR(4))
avtb4.grid(row=1, column=1, ipadx=25, ipady=10)

avtb5 = Button(avatarContainer,cursor="hand2", image=avtr5, relief=FLAT, bd=0, command=lambda:selectAVATAR(5))
avtb5.grid(row=2, column=0, ipadx=25, ipady=10)

avtb6 = Button(avatarContainer,cursor="hand2", image=avtr6, relief=FLAT, bd=0, command=lambda:selectAVATAR(6))
avtb6.grid(row=2, column=1, ipadx=25, ipady=10)

avtb7 = Button(avatarContainer,cursor="hand2", image=avtr7, relief=FLAT, bd=0, command=lambda:selectAVATAR(7))
avtb7.grid(row=3, column=0, ipadx=25, ipady=10)

avtb8 = Button(avatarContainer,cursor="hand2", image=avtr8, relief=FLAT, bd=0, command=lambda:selectAVATAR(8))
avtb8.grid(row=3, column=1, ipadx=25, ipady=10)


check_Label = Label(avatarContainer, image=check_Img, bd=0)

def exit_Check(ar):
    if ar == 1:
        root.destroy()
    if ar == 2:
        ans = messagebox.askquestion("Exit!", "Are you want to exit?")
        if ans== "yes":
            root.destroy()
            sys.exit()

def SuccessfullyRegistered():
    if avatarChoosen != 0:
        Text =user_name
        Text_spilt = Text.split()
        Text_spilt1 = "Hi, "+(Text_spilt[0])+"\nYou Are Ready To Use F.R.I.D.A.Y"
        Wellcome_Label.config(text=Text_spilt1)
        SuccessfullyRegistered_Frame.place(x=3,y=0)
        #print("work")
    '''if user_gender==2:
        gen = 'Female'
        u = UserData()
        u.updateData(user_name, gen, avatarChoosen)
        usernameLbl['text'] = user_name
        #raise_frame(SuccessfullyRegistered_Frame)'''

Button(firstAvatar_choosing_Frame, text='         Submit         ', font=('Arial Bold', 15), bg='#01933B', fg='white', bd=0,command=SuccessfullyRegistered, relief=FLAT).pack()

userPIC = Label(SuccessfullyRegistered_Frame,image=avtr1)
userPIC.pack(pady=(40, 10))
usernameLbl = Label(SuccessfullyRegistered_Frame, text=" ", font=('Arial Bold',15))
usernameLbl.pack(pady=(0, 70))


Wellcome_Label = Label(SuccessfullyRegistered_Frame,font=('Arial Bold',15), wraplength=300)
Wellcome_Label.pack(pady=10)
#Label(SuccessfullyRegistered_Frame, text="Your Data Has been successfully activated!", font=('Arial Bold',15), fg='#303E54', wraplength=300).pack(pady=10)

Fake_L_4 = Label(SuccessfullyRegistered_Frame, text="                ", font=('arial',15), wraplength=350)
Fake_L_4.pack()

Wellcome_msg_Label = Label(SuccessfullyRegistered_Frame, text="Click On 'Ok' Button To Start Conversation with\nF.R.I.D.A.Y", font=('arial',13), wraplength=350)
Wellcome_msg_Label.pack()

LaunchBtn = Button(SuccessfullyRegistered_Frame, text='     OK     ', bg='#0475BB', fg='white',font=('Arial Bold', 18), bd=0,command=lambda:exit_Check(1) ,relief=FLAT)
LaunchBtn.pack(pady=50)

#Launch the APP again to get started the conversation with your Personal Assistant




def change_color_fun (col):
    global Theme_Mode
    Main_Bg_Color_Light = "#dff3ff"
    Main_Text_Color_Light ="#303E54"
    Main_Bg_Color_Dark ="#333333"
    Main_Text_Color_Dark = "#c9e6ff"
    if col == 0: #Light/Default Color
        Light_Mode_Button.place(x=1000,y=1000)
        Dark_Mode_Button.place(x=312,y=512)
        root.config(bg=Main_Bg_Color_Light)
        Fr_Logo.config(bg="#42b8ff")
        Fake_L_1.config(bg=Main_Bg_Color_Light,fg=Main_Bg_Color_Light)
        Fake_L_2.config(bg=Main_Bg_Color_Light,fg=Main_Bg_Color_Light)
        Fake_L_3.config(bg=Main_Bg_Color_Light,fg=Main_Bg_Color_Light)
        Fake_L_4.config(bg=Main_Bg_Color_Light,fg=Main_Bg_Color_Light)
        text_Field.config(bg="azure3",fg="#0e5d0e")
        nameLbl.config(fg=Main_Text_Color_Light, bg=Main_Bg_Color_Light)
        genLbl.config(fg=Main_Text_Color_Light, bg=Main_Bg_Color_Light)
        #nameField.config(bg="pale turquoise",fg="gray60")
        Malecheck_Btn.config(bg=Main_Bg_Color_Light,activebackground=Main_Bg_Color_Light)
        Male_Logo.config(bg=Main_Bg_Color_Light)
        Femalecheck_Btn.config(bg=Main_Bg_Color_Light,activebackground=Main_Bg_Color_Light)
        Female_Logo.config(bg=Main_Bg_Color_Light)
        userFrame2.config(bg=Main_Bg_Color_Light)
        statusLbl.config(bg=Main_Bg_Color_Light)
        firstAvatar_choosing_Frame.config(bg=Main_Bg_Color_Light)
        avatarContainer.config(bg=Main_Bg_Color_Light)
        Chouse_Avtar_LAbel.config(bg="lavender",fg="#303E54")
        check_Label.config(bg=Main_Bg_Color_Light)
        avtb1.config(bg=Main_Bg_Color_Light,activebackground=Main_Bg_Color_Light)
        avtb2.config(bg=Main_Bg_Color_Light,activebackground=Main_Bg_Color_Light)
        avtb3.config(bg=Main_Bg_Color_Light,activebackground=Main_Bg_Color_Light)
        avtb4.config(bg=Main_Bg_Color_Light,activebackground=Main_Bg_Color_Light)
        avtb5.config(bg=Main_Bg_Color_Light,activebackground=Main_Bg_Color_Light)
        avtb6.config(bg=Main_Bg_Color_Light,activebackground=Main_Bg_Color_Light)
        avtb7.config(bg=Main_Bg_Color_Light,activebackground=Main_Bg_Color_Light)
        avtb8.config(bg=Main_Bg_Color_Light,activebackground=Main_Bg_Color_Light)
        SuccessfullyRegistered_Frame.config(bg=Main_Bg_Color_Light)
        Wellcome_msg_Label.config(bg=Main_Bg_Color_Light,fg='#515255')
        Wellcome_Label.config(bg=Main_Bg_Color_Light,fg='#303E54')
        userPIC.config(bg=Main_Bg_Color_Light)
        usernameLbl.config(bg=Main_Bg_Color_Light,fg='#367470')
        Theme_Mode = 0
    if col == 1: #Black Color
        Dark_Mode_Button.place(x=1000,y=1000)
        Light_Mode_Button.place(x=312,y=512)
        root.config(bg=Main_Bg_Color_Dark)
        Fr_Logo.config(bg="grey70")
        Fake_L_1.config(bg=Main_Bg_Color_Dark,fg=Main_Bg_Color_Dark)
        Fake_L_2.config(bg=Main_Bg_Color_Dark,fg=Main_Bg_Color_Dark)
        Fake_L_3.config(bg=Main_Bg_Color_Dark,fg=Main_Bg_Color_Dark)
        Fake_L_4.config(bg=Main_Bg_Color_Dark,fg=Main_Bg_Color_Dark)
        text_Field.config(bg="#141414",fg="green")
        nameLbl.config(fg=Main_Text_Color_Dark, bg=Main_Bg_Color_Dark)
        genLbl.config(fg=Main_Text_Color_Dark, bg=Main_Bg_Color_Dark)
        #nameField.config(bg="pale turquoise",fg="gray60")
        Malecheck_Btn.config(bg=Main_Bg_Color_Dark,activebackground=Main_Bg_Color_Dark)
        Male_Logo.config(bg=Main_Bg_Color_Dark)
        Femalecheck_Btn.config(bg=Main_Bg_Color_Dark,activebackground=Main_Bg_Color_Dark)
        Female_Logo.config(bg=Main_Bg_Color_Dark)
        userFrame2.config(bg=Main_Bg_Color_Dark)
        statusLbl.config(bg=Main_Bg_Color_Dark)
        firstAvatar_choosing_Frame.config(bg=Main_Bg_Color_Dark)
        avatarContainer.config(bg=Main_Bg_Color_Dark)
        Chouse_Avtar_LAbel.config(bg="light slate gray",fg="old lace")
        check_Label.config(bg=Main_Bg_Color_Dark)
        avtb1.config(bg=Main_Bg_Color_Dark,activebackground=Main_Bg_Color_Dark)
        avtb2.config(bg=Main_Bg_Color_Dark,activebackground=Main_Bg_Color_Dark)
        avtb3.config(bg=Main_Bg_Color_Dark,activebackground=Main_Bg_Color_Dark)
        avtb4.config(bg=Main_Bg_Color_Dark,activebackground=Main_Bg_Color_Dark)
        avtb5.config(bg=Main_Bg_Color_Dark,activebackground=Main_Bg_Color_Dark)
        avtb6.config(bg=Main_Bg_Color_Dark,activebackground=Main_Bg_Color_Dark)
        avtb7.config(bg=Main_Bg_Color_Dark,activebackground=Main_Bg_Color_Dark)
        avtb8.config(bg=Main_Bg_Color_Dark,activebackground=Main_Bg_Color_Dark)
        SuccessfullyRegistered_Frame.config(bg=Main_Bg_Color_Dark)
        Wellcome_msg_Label.config(bg=Main_Bg_Color_Dark,fg="snow3")
        Wellcome_Label.config(bg=Main_Bg_Color_Dark,fg="#5f9ea0")
        userPIC.config(bg=Main_Bg_Color_Dark)
        usernameLbl.config(bg=Main_Bg_Color_Dark,fg="#85AD4F")
        Theme_Mode = 1
#"Lavender Blush2"



Dark_Mode_Button.config(command=lambda:change_color_fun(1))
Light_Mode_Button.config(command=lambda:change_color_fun(0))

t1.start()
t2.start()
change_color_fun(0)
#change_color_fun(1)
#root.mainloop()



root.protocol("WM_DELETE_WINDOW", lambda:exit_Check(2))


## ==> MAIN WINDOW
#from ui_main import Ui_MainWindow

#import ui_main

## ==> GLOBALS
counter = 0
from os import environ
environ["QT_DEVICE_PIXEL_RATIO"] = "0"
environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
environ["QT_SCREEN_SCALE_FACTORS"] = "1"
environ["QT_SCALE_FACTOR"] = "1"


class MainWindow(QMainWindow):
    def __init__(self):
        #print("class")
        Voice_start.start()
        mainwindow.iconbitmap(_path+'Images/assistant2.ico')
        #webScrapping.dataUpdate()
        mainwindow.mainloop()
        '''QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MAIN WINDOW LABEL
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>THANKS</strong> FOR WATCHING"))
        QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))'''


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> F.R.I.D.A.Y")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>INITIALIZE</strong> MODULES"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            #self.main = MainWindow()
            #self.main.show()
            # CLOSE SPLASH SCREEN
            self.close()
            self.main = MainWindow()
            #self.main.show()

        # INCREASE COUNTER
        counter += 1

chatBgColor = "red"

root.mainloop()
mainwindow = Tk()


'''ownerPhoto = 1
ownerName = "Hrishikesh"
ownerDesignation = "Sir"'''
EXIT_COMMANDS = ['bye','exit','quit','shut down', 'shutdown']
#_path = 'c:/Users/Hrishikesh/OneDrive/Documents/Programing Work/Python Projects/ANewProject/Assets/'

chatBgColor = '#12232e'
background = '#203647'
textColor = 'white'
AITaskStatusLblBG = '#203647'
botChatTextBg = "#007cc7"
botChatText = "white"
userChatTextBg = "#4da8da"
KCS_IMG = Theme_Mode
#1 #0 for light, 1 for dark
voice_id = 0 #0 for female, 1 for male
ass_volume = 1 #max volume
ass_voiceRate = 200 #normal voice rate

def center_window2(w=400, h=650):
    # get screen width and height
    ws = mainwindow.winfo_screenwidth()
    hs = mainwindow.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)  #change hs/2 to hs/4 to left window up
    mainwindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

center_window2(400, 650)

mainwindow.title("F.R.I.D.A.Y")
mainwindow.resizable(0,0)
#mainwindow.iconbitmap(_path+'Images/assistant2.ico')

#mainwindow.geometry("400x650")
n = StringVar(mainwindow)
n2 = StringVar(mainwindow)
themeValue = IntVar(mainwindow)
chatMode = 1

main_frame = Frame(mainwindow, bg=chatBgColor)
settings_frame = Frame(mainwindow, bg=background)
secondAvatar_choosing_Frame = Frame(mainwindow)
About_Frame = Frame(mainwindow,bg=background)

rock_P__Frame = Frame(mainwindow)



Fake_L_N1 = Label(secondAvatar_choosing_Frame, text=" ", font=('arial', 2))
Fake_L_N1.pack()
Chouse_Avtar_LAbel_2nd = Label(secondAvatar_choosing_Frame, text="Choose Your Avatar", font=('arial', 15))
avatarContainer_2nd = Frame(secondAvatar_choosing_Frame, width=300, height=500)

chat_frame = Frame(main_frame, width=380,height=551,bg=chatBgColor)
chat_frame.pack(padx=10)
chat_frame.pack_propagate(0)

bottomFrame1 = Frame(main_frame, bg='#dfdfdf', height=100)
bottomFrame1.pack(fill=X, side=BOTTOM)
VoiceModeFrame = Frame(bottomFrame1, bg='#dfdfdf')
VoiceModeFrame.pack(fill=BOTH)
TextModeFrame = Frame(bottomFrame1, bg='#dfdfdf')
TextModeFrame.pack(fill=BOTH)

TextModeFrame.pack_forget()

############ ATTACHING BOT/USER CHAT ON CHAT SCREEN ###########
def attachTOframe(text,bot=False):
	if bot:
		botchat = Label(chat_frame,text=text, bg=botChatTextBg, fg=botChatText, justify=LEFT, wraplength=250, font=('Montserrat',12, 'bold'))
		botchat.pack(anchor='w',ipadx=5,ipady=5,pady=5)
	else:
		userchat = Label(chat_frame, text=text, bg=userChatTextBg, fg='white', justify=RIGHT, wraplength=250, font=('Montserrat',12, 'bold'))
		userchat.pack(anchor='e',ipadx=2,ipady=2,pady=5)

def clearChatScreen():
	for wid in chat_frame.winfo_children():
		wid.destroy()


path = appdata_path+'/Friday_cache'
################# SHOWING DOWNLOADED IMAGES ###############
img0, img1, img2, img3, img4 = None, None, None, None, None
def showSingleImage(type, data=None):
    global img0, img1, img2, img3, img4
    try:
        img0 = ImageTk.PhotoImage(PIL.Image.open(appdata_path+'/Friday_cache/0.jpg').resize((90,110), PIL.Image.ANTIALIAS))
    except:
        pass
    img1 = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/heads.jpg').resize((220,200), PIL.Image.ANTIALIAS))
    img2 = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/tails.jpg').resize((220,200), PIL.Image.ANTIALIAS))
    img4 = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/WeatherImage.png'))

    if type=="weather":
        weather = Frame(chat_frame)
        weather.pack(anchor='w')
        Label(weather, image=img4, bg=chatBgColor).pack()
        Label(weather, text=data[0], font=('Arial Bold', 45), fg='white', bg='#3F48CC').place(x=65,y=45)
        Label(weather, text=data[1], font=('Montserrat', 15), fg='white', bg='#3F48CC').place(x=78,y=110)
        Label(weather, text=data[2], font=('Montserrat', 10), fg='white', bg='#3F48CC').place(x=78,y=140)
        Label(weather, text=data[3], font=('Arial Bold', 12), fg='white', bg='#3F48CC').place(x=60,y=160)

    elif type=="wiki":
        Label(chat_frame, image=img0, bg='#EAEAEA').pack(anchor='w')
    elif type=="head":
        Label(chat_frame, image=img1, bg='#EAEAEA').pack(anchor='w')
    elif type=="tail":
        Label(chat_frame, image=img2, bg='#EAEAEA').pack(anchor='w')
    else:
        img3 = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/Dice/'+type+'.jpg').resize((200,200), PIL.Image.ANTIALIAS))
        Label(chat_frame, image=img3, bg='#EAEAEA').pack(anchor='w')

def showImages(query):
    global img0, img1, img2, img3
    webScrapping.downloadImage(query)
    w, h = 150, 110
    #Showing Images
    imageContainer = Frame(chat_frame, bg='#EAEAEA')
    imageContainer.pack(anchor='w')
    #loading images
    img0 = ImageTk.PhotoImage(PIL.Image.open(appdata_path+'/Friday_cache/0.jpg').resize((w,h), PIL.Image.ANTIALIAS))
    img1 = ImageTk.PhotoImage(PIL.Image.open(appdata_path+'/Friday_cache/1.jpg').resize((w,h), PIL.Image.ANTIALIAS))
    img2 = ImageTk.PhotoImage(PIL.Image.open(appdata_path+'/Friday_cache/2.jpg').resize((w,h), PIL.Image.ANTIALIAS))
    img3 = ImageTk.PhotoImage(PIL.Image.open(appdata_path+'/Friday_cache/3.jpg').resize((w,h), PIL.Image.ANTIALIAS))
    #Displaying
    Label(imageContainer, image=img0, bg='#EAEAEA').grid(row=0, column=0)
    Label(imageContainer, image=img1, bg='#EAEAEA').grid(row=0, column=1)
    Label(imageContainer, image=img2, bg='#EAEAEA').grid(row=1, column=0)
    Label(imageContainer, image=img3, bg='#EAEAEA').grid(row=1, column=1)
    shutil.rmtree(path)
    #os.rmdir(path)


def ChangeSettings():
    global background, textColor, chatBgColor, voice_id, ass_volume, ass_voiceRate, AITaskStatusLblBG, KCS_IMG, botChatTextBg, botChatText, userChatTextBg
    setting = {'background': background,
                'textColor': textColor,
                'chatBgColor': chatBgColor,
                'AITaskStatusLblBG': AITaskStatusLblBG,
                'KCS_IMG': KCS_IMG,
                'botChatText': botChatText,
                'botChatTextBg': botChatTextBg,
                'userChatTextBg': userChatTextBg,
                'voice_id': voice_id,
                'ass_volume': ass_volume,
                'ass_voiceRate': ass_voiceRate
            }
    #clearChatScreen()



def attachTOframe(text,bot=False):
    if bot:
        botchat = Label(chat_frame,text=text, bg=botChatTextBg, fg=botChatText, justify=LEFT, wraplength=250, font=('Montserrat',12, 'bold'))
        botchat.pack(anchor='w',ipadx=5,ipady=5,pady=5)
    else:
        userchat = Label(chat_frame, text=text, bg=userChatTextBg, fg='white', justify=RIGHT, wraplength=250, font=('Montserrat',12, 'bold'))
        userchat.pack(anchor='e',ipadx=2,ipady=2,pady=5)

def clearChatScreen():
	for wid in chat_frame.winfo_children():
		wid.destroy()


Hackerrank_Icon = PhotoImage(file=_path+"Images/h.png")
github_Icon = PhotoImage(file=_path+"Images/github.png")
fb_Icon = PhotoImage(file=_path+"Images/Fb.png")
HM_Icon = PhotoImage(file=_path+"Images/home.png")


#About frame
def aboutFun ():
    #print(background)
    if  background == "#F6FAFB": #<--White
        textcol1 = "lightpink4"
        textcol2 = "plum4"
        textcol3 = "snow4"
    elif  background == "#203647": #<--Dark
        textcol1 = "azure"
        textcol2 = "SpringGreen2"
        textcol3 = "salmon3"

    About_Frame.config(bg=background)
    Label(About_Frame, text = " "*394,font=("AdobeDevanagari",1),bg=background).pack()

    About_label_hello = Label(About_Frame, text = "Hello World !!",font=("Lucida Calligraphy",16),bg=background,fg=textcol1)
    About_label_hello.pack()

    Label(About_Frame, text = " ",font=("Lucida Calligraphy",1),bg=background,fg=textcol1).pack()

    ab ="This Program Was Written In Python Language 3.9.0 With Tkinter GUI. It's A Virtual Assistant That Can Performed The Following Tasks, Solving Match Problems, Send Email & Whatsapp Messages, Google Search(Search Results Show With Images If Available), Dictionary Search, Youtube Search, Translation English To Any Language, Show Map & Direction, Show Meaning Or Definition Of Word, Play Rock Paper Scissor Game, Coin Toss, Tell You A Joke, News, Weather Information, COVID-19 Information & Precaution, Create & Show Todo List, Create HTML Project, Create Text Documents, Create Programing Files, Etc.\nYou Can Toggle Between Light Theme & Dark Theme, Also You Can Change Chat Colour.You Can Choose Your Avatar, You Can Change Assistant Voice, Volume, Rate.\nThank You."

    About_label = Label(About_Frame, text = ab,wraplength=390,font=("Lucida Calligraphy",11),bg=background,fg=textcol1)
    About_label.pack()

    Label(About_Frame, text = "    ",font="BahnschriftLight 5",bg=background,).pack()

    About_label_D_IN = Label(About_Frame, text = "F.R.I.D.A.Y Developed By\nHrishikesh Patra",font=("Lucida Calligraphy",16),bg=background,fg=textcol2)
    About_label_D_IN.pack()


    Label(About_Frame, text = "    ",font="BahnschriftLight 7",bg=background).pack()

    contct_label = Label(About_Frame, text = "Contact With Me :-",font="forte 15",bg=background,fg=textcol3)
    contct_label.pack()

    Label(About_Frame, text = "    ",font="BahnschriftLight 5",bg=background).pack()

    Label(About_Frame, text = " "*50,font="BahnschriftLight 5",bg=background).pack(side=RIGHT)
    Hackerrank_B = Button(About_Frame,image=Hackerrank_Icon, bd=4, padx=10,command=lambda: webbrowser.open_new_tab("https://www.hackerrank.com/Hrishikesh7665"))
    Hackerrank_B.pack(side=RIGHT)
    Label(About_Frame, text = "        ",font="BahnschriftLight 5",bg=background).pack(side=RIGHT)

    fb_B = Button(About_Frame,image=fb_Icon, bd=4, padx=10,command=lambda: webbrowser.open_new_tab("https://www.facebook.com/Isjtijlfti.patra"))
    fb_B.pack(side=RIGHT)

    Label(About_Frame, text = "        ",font="BahnschriftLight 5",bg=background).pack(side=RIGHT)

    github_B = Button(About_Frame,image=github_Icon, bd=4, padx=10,command=lambda: webbrowser.open_new_tab("https://github.com/Hrishikesh7665"))
    github_B.pack(side=RIGHT)

    def AbBack_Fun():
        for wid in About_Frame.winfo_children():
            wid.destroy()
        b.destroy()
        About_Frame.place(x=1000,y=1000)
        settings_frame.place(x=50,y=0)
    b = Button(mainwindow,image=HM_Icon,bg=background,activebackground=background,bd=0,command=AbBack_Fun)
    b.place(x=355,y=605)

    #Button(About_Frame,image=HM_Icon,bd=0).pack()


def show_Setting_Frame ():
    mainwindow.config(bg=background)
    settings_frame.config(bg=background)
    settings_frame.place(x=50,y=0) #40
    About_Frame.place(x=1000,y=1000)
    main_frame.place(x=1000,y=1000)

def show_Chat_Frame ():
    settings_frame.place(x=1000,y=1000)
    About_Frame.place(x=1000,y=1000)
    main_frame.place(x=0,y=0)

def show_About_Frame ():
    settings_frame.place(x=1000,y=1000)
    main_frame.place(x=1000,y=1000)
    About_Frame.place(x=0,y=0)
    aboutFun()

def selectAVATAR_IMG(avt=ownerPhoto):
    global avatarChoosen,ownerPhoto
    avatarChoosen = avt
    i=1
    for avtr in (avtb1_2,avtb2_2,avtb3_2,avtb4_2,avtb5_2,avtb6_2,avtb7_2,avtb8_2):
        if i==avt:
            row, column =coordinates_List[i]
            #print(i)
            check_Label2.grid(row=row, column=column,ipadx=25, ipady=10)
            avtr['state'] = 'disabled'
            #userPIC['image'] = avtr['image']
            ownerPhoto = i
        else: avtr['state'] = 'normal'
        i+=1


def changeChatMode():
	global chatMode
	if chatMode==1:
		# appControl.volumeControl('mute')
		VoiceModeFrame.pack_forget()
		TextModeFrame.pack(fill=BOTH)
		UserField.focus()
		chatMode=0
	else:
		# appControl.volumeControl('full')
		TextModeFrame.pack_forget()
		VoiceModeFrame.pack(fill=BOTH)
		mainwindow.focus()
		chatMode=1
def onhover(e):
    	userPhoto['image'] = chngPh
def onleave(e):
	userPhoto['image'] = userProfileImg


def SelectAvatar_Btn():
    i=ownerPhoto
    row, column =coordinates_List[i]
    check_Label2.grid(row=row, column=column,ipadx=25, ipady=10)
    secondAvatar_choosing_Frame.place(x=50,y=4)

def exit_conformation(v):
    if v == 1:
        ans = messagebox.askquestion("Exit!", "Are you want to exit?")
        if ans == "yes":
            mainwindow.destroy()
            os.kill(pid,signal.SIGTERM)
    if v == 2:
        mainwindow.destroy()
        os.kill(pid,signal.SIGTERM)
    #sys.exit()





def SuccessfullyRegistered_2nd():
    if avatarChoosen != 0:
        global ownerPhoto, userProfileImg, userIcon
        userProfileImg = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/Avatar/UserFace'+str(ownerPhoto)+".png").resize((120, 120)))
        userPhoto['image'] = userProfileImg
        userIcon = PhotoImage(file=_path+'Images/Avatar/ChatIcons/a'+str(ownerPhoto)+".png")
        secondAvatar_choosing_Frame.place(x=1000,y=1000)
        settings_frame.place(x=50,y=0)


def getChatColor():
    global chatBgColor
    chatBgColor = myColor[1]
    colorbar['bg'] = chatBgColor
    chat_frame['bg'] = chatBgColor
    main_frame['bg'] = chatBgColor

def getChatColor():
    global chatBgColor
    myColor = colorchooser.askcolor()
    if myColor[1] is None: return
    chatBgColor = myColor[1]
    colorbar['bg'] = chatBgColor
    chat_frame['bg'] = chatBgColor
    main_frame['bg'] = chatBgColor
    ChangeSettings()


def changeTheme():
    global background, textColor, AITaskStatusLblBG, KCS_IMG, botChatText, botChatTextBg, userChatTextBg, chatBgColor
    if themeValue.get()==1:
        background, textColor, AITaskStatusLblBG, KCS_IMG = "#203647", "white", "#203647",1
        cbl['image'] = cblDarkImg
        kbBtn['image'] = kbphDark
        settingBtn['image'] = sphDark
        AITaskStatusLbl['bg'] = AITaskStatusLblBG
        botChatText, botChatTextBg, userChatTextBg = "white", "#007cc7", "#4da8da"
        chatBgColor = "#12232e"
        colorbar['bg'] = chatBgColor
        Fake_LBl_1.config(bg=background)
        Fake_LBl_2.config(bg=background)
        Fake_LBl_3.config(bg=background)
        secondAvatar_choosing_Frame.config(bg=background)
        Fake_L_N1.config(bg=background)
        Fake_L_N2.config(bg=background)
        Chouse_Avtar_LAbel_2nd.config(bg="light slate gray",fg="old lace")
        avatarContainer_2nd.config(bg=background)
        mainwindow.config(bg=background)
        avtb1_2.config(bg=background,activebackground=background)
        avtb2_2.config(bg=background,activebackground=background)
        avtb3_2.config(bg=background,activebackground=background)
        avtb4_2.config(bg=background,activebackground=background)
        avtb5_2.config(bg=background,activebackground=background)
        avtb6_2.config(bg=background,activebackground=background)
        avtb7_2.config(bg=background,activebackground=background)
        avtb8_2.config(bg=background,activebackground=background)
        check_Label2.config(bg=background)
    else:
        background, textColor, AITaskStatusLblBG, KCS_IMG = "#F6FAFB", "#303E54", "#14A769", 0
        cbl['image'] = cblLightImg
        kbBtn['image'] = kbphLight
        settingBtn['image'] = sphLight
        AITaskStatusLbl['bg'] = AITaskStatusLblBG
        botChatText, botChatTextBg, userChatTextBg = "#494949", "#EAEAEA", "#23AE79"
        chatBgColor = "#F6FAFB"
        colorbar['bg'] = '#E8EBEF'
        Fake_LBl_1.config(bg=background)
        Fake_LBl_2.config(bg=background)
        mainwindow.config(bg=background)
        Fake_LBl_3.config(bg=background)
        secondAvatar_choosing_Frame.config(bg=background)
        Fake_L_N1.config(bg=background)
        Fake_L_N2.config(bg=background)
        Chouse_Avtar_LAbel_2nd.config(bg="lavender",fg="#303E54")
        avatarContainer_2nd.config(bg=background)
        avtb1_2.config(bg=background,activebackground=background)
        avtb2_2.config(bg=background,activebackground=background)
        avtb3_2.config(bg=background,activebackground=background)
        avtb4_2.config(bg=background,activebackground=background)
        avtb5_2.config(bg=background,activebackground=background)
        avtb6_2.config(bg=background,activebackground=background)
        avtb7_2.config(bg=background,activebackground=background)
        avtb8_2.config(bg=background,activebackground=background)
        check_Label2.config(bg=background)
        #TextModeFrame
    main_frame['bg'], settings_frame['bg'] = background, background
    settingsFrame['bg'] = background
    settingsLbl['fg'], userPhoto['fg'], userName['fg'], assLbl['fg'], voiceRateLbl['fg'], volumeLbl['fg'], themeLbl['fg'], chooseChatLbl['fg'] = textColor, textColor, textColor, textColor, textColor, textColor, textColor, textColor
    settingsLbl['bg'], userPhoto['bg'], userName['bg'], assLbl['bg'], voiceRateLbl['bg'], volumeLbl['bg'], themeLbl['bg'], chooseChatLbl['bg'] = background, background, background, background, background, background, background, background
    s.configure('Wild.TRadiobutton', background=background, foreground=textColor)
    volumeBar['bg'], volumeBar['fg'], volumeBar['highlightbackground'] = background, textColor, background
    chat_frame['bg'], main_frame['bg'] = chatBgColor, chatBgColor
    userPhoto['activebackground'] = background
    clearChatScreen()
    ChangeSettings()


'''try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id) #male
    engine.setProperty('volume', ass_volume)
except Exception as e:
    print(e)'''


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[voice_id].id) #male
engine.setProperty('volume', ass_volume)

####################################### SET UP TEXT TO SPEECH #######################################
def speak(text, display=False, icon=False):
    AITaskStatusLbl['text'] = 'Speaking...'
    if icon: Label(chat_frame, image=botIcon, bg=chatBgColor).pack(anchor='w',pady=0)
    if display: attachTOframe(text, True)
    engine.say(text)
    engine.runAndWait()
    #print('\n'+ai_name.upper()+': '+text)
    #engine.say(text)
    #engine.runAndWait()

def record(clearChat=True, iconDisplay=True):
    #print('\nListening...')
    AITaskStatusLbl['text'] = 'Listening...'
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""
        try:
            AITaskStatusLbl['text'] = 'Processing...'
            said = r.recognize_google(audio)
            #print(f"\nUser said: {said}")
            if clearChat:
                clearChatScreen()
            if iconDisplay: Label(chat_frame, image=userIcon, bg=chatBgColor).pack(anchor='e',pady=0)
            attachTOframe(said)
        except Exception as e:
            #print(e)
            # speak("I didn't get it, Say that again please...")
            if "connection failed" in str(e):
                speak("Your System is Offline...", True, True)
            return 'None'
    return said.lower()


def record2forkey(y,clearChat=True, iconDisplay=True):
    #print('\nListening...')
    AITaskStatusLbl['text'] = 'Listening...'
    r = y
    #audio = r
    said = r
    try:
        AITaskStatusLbl['text'] = 'Processing...'
#        said =
        #print(f"\nUser said: {said}")
        if clearChat:
            clearChatScreen()
        if iconDisplay: Label(chat_frame, image=userIcon, bg=chatBgColor).pack(anchor='e',pady=0)
        attachTOframe(said)
    except Exception as e:
        #print(e)
        # speak("I didn't get it, Say that again please...")
        if "connection failed" in str(e):
            speak("Your System is Offline...", True, True)
        return 'None'
    return said.lower()

def voiceMedium():
    while True:
        query = record()
        if query == 'None': continue
        if isContain(query, EXIT_COMMANDS):
            speak("Shutting down the System. Good Bye "+ownerDesignation+"!", True, True)
            exit_conformation(2)
            break
        else: main(query.lower())
    #appControl.Win_Opt('close')



def keyboardInput(e):
    user_input = UserField.get().lower()
    text = user_input
    if user_input!="":
        clearChatScreen()
        if isContain(user_input, EXIT_COMMANDS):
            #print("Shutting down the System. Good Bye "+ownerDesignation+"!")
            speak("Shutting down the System. Good Bye "+ownerDesignation+"!", True, True)
            exit_conformation(2)
        else:
            Label(chat_frame, image=userIcon, bg=chatBgColor).pack(anchor='e',pady=0)
            attachTOframe(user_input.capitalize())
            #voiceMedium
            #main(user_input.lower())
            #main(query.lower())
            record2forkey(user_input)
            Thread(target = lambda:main(user_input)).start()
            #Thread(target=main, args=(user_input,)).start()
        UserField.delete(0, END)

def changeVoice(e):
    global voice_id
    voice_id=0
    #print(voice_id)
    #print(n.get())
    if assVoiceOption.get()=='Female': voice_id=1
    engine.setProperty('voice', voices[voice_id].id)
    ChangeSettings()

def changeVolume(e):
    global ass_volume
    ass_volume = volumeBar.get() / 100
    engine.setProperty('volume', ass_volume)
    ChangeSettings()

def changeVoiceRate(e):
    global ass_voiceRate
    temp = voiceOption.get()
    if temp=='Very Low': ass_voiceRate = 100
    elif temp=='Low': ass_voiceRate = 150
    elif temp=='Fast': ass_voiceRate = 250
    elif temp=='Very Fast': ass_voiceRate = 300
    else: ass_voiceRate = 200
    #print(ass_voiceRate)
    engine.setProperty('rate', ass_voiceRate)
    ChangeSettings()



def isContain(txt, lst):
    for word in lst:
        if word in txt:
            return True
    return False




#---------------------------------------------------------------------------------
def speak_RPS(text):
    #print(text)
    engine.say(text)
    engine.runAndWait()

def bavkbtn_fun ():
    #print("Hi")
    for el in rock_P__Frame.winfo_children():
        el.destroy()
    rock_P__Frame.place(x=1000,y=1000)
    show_Chat_Frame()
    return


def record_RPS():
	global userchat_RPS
	userchat_RPS['text'] = "Listening..."
	r = sr.Recognizer()
	r.dynamic_energy_threshold = False
	r.energy_threshold = 4000
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		said = ""
		try:
			said = r.recognize_google(audio)
			print(f"\nUser said: {said}")
		except Exception as e:
			#print(e)
			speak_RPS("I think it is invalid move...")
			return "None"
	return said.lower()

moves = ['rock', 'paper', 'scissor']
class RockPaperScissor:
    def __init__(self):
        self.playerScore = 0
        self.botScore = 0
        self.total_moves = 0
        self.intro()

    def intro(self):
        speak_RPS("Welcome to the Rock Paper Scissor Game. To STOP the Match, say STOP or Cancel. Let's Play.")

    def nextMove(self, move):
        global userchat_RPS, botchat_RPS, totalLabel, botMoveLBL
        userchat_RPS['text'] = move.upper()
        botMove = randint(0,2)
        playerMove = moves.index(move)
        botchat_RPS['text'] = moves[botMove].upper()
        self.total_moves += 1

        if botMove==playerMove:
            self.botScore += 1
            self.playerScore += 1
        elif botMove==0:
            if playerMove==1:
                self.playerScore += 1
            else:
                self.botScore += 1
        elif botMove==1:
            if playerMove==2:
                self.playerScore += 1
            else:
                self.botScore += 1
        else:
            if playerMove==0:
                self.playerScore += 1
            else:
                self.botScore += 1
        totalLabel['text'] = str(self.botScore)+'   |   '+str(self.playerScore)
        if botMove==0: botMoveLBL['image'] = rockImg
        if botMove==1: botMoveLBL['image'] = paperImg
        if botMove==2: botMoveLBL['image'] = scissorImg
        speak_RPS('I choose: ' + str(moves[botMove]))
        return botMove+1



    def whoWon(self):
        #print(background)
        if background == "#203647" :
            fgc = "AntiqueWhite1"
        else:
            fgc='#292D3E'
        result = ""
        if self.playerScore == self.botScore:
            result = "The match is draw !\n"
        elif self.playerScore > self.botScore:
            result = "You won the match Sir! Well Done !\n"
        else:
            result = "You lose the match Sir! Haha!\n"
        for el in rock_P__Frame.winfo_children():
            el.destroy()
        Label(rock_P__Frame, text='                     ',bg=background, font=('Arial Bold', 50)).pack()
        if 'won' in result:
            Label(rock_P__Frame, image=winImg).pack(pady=30)
        elif 'lose' in result:
            Label(rock_P__Frame, image=loseImg).pack(pady=30)
        else:
            Label(rock_P__Frame, image=drawImg).pack(pady=30)
        result += "You have won " +str(self.playerScore)+"/"+str(self.total_moves)+" matches."
        Label(rock_P__Frame, text='Score', font=('Arial Bold', 50), fg='#FE8A28', bg=background).pack()
        Label(rock_P__Frame, text=str(self.playerScore)+' / '+str(self.total_moves), font=('Arial Bold', 40), fg=fgc, bg=background).pack()
        #back_RPS_Btn = Button(rock_P__Frame, text='   Back   ', bd=0, font=('Arial 12'), fg='white', bg='#14A769', relief=FLAT,command=bavkbtn_fun)
        Label(rock_P__Frame, text='       \n      \n   \n     ',bg=background, font=('Arial Bold', 20)).pack()
        #back_RPS_Btn.pack()
        speak_RPS(result)
        #time.sleep(1)
        #closeWindow()
        bavkbtn_fun()


#, command=bavkbtn_fun

rockImg, paperImg, scissorImg, userchat_RPS, botchat_RPS, totalLabel, botMoveLBL, userMoveLBL, winImg, loseImg, drawImg = None, None, None, None, None, None, None, None, None, None, None
def playRock():
	rp = RockPaperScissor()
	while True:
		global botMoveLBL, userMoveLBL
		move = record_RPS()
		if isContain_RPS(move, ["don't", "cancel", "stop"]):
			rp.whoWon()
			break
		else:
			img = None
			if 'rock' in move:
				userMoveLBL['image'] = rockImg
				img = rp.nextMove('rock')
			elif 'paper' in move:
				userMoveLBL['image'] = paperImg
				img = rp.nextMove('paper')
			elif 'scissor' in move or 'caesar' in move:
				userMoveLBL['image'] = scissorImg
				img = rp.nextMove('scissor')


def rockPaperScissorWindow():
    global rock_P__Frame, rockImg, paperImg, scissorImg, userchat_RPS, botchat_RPS, totalLabel, botMoveLBL, userMoveLBL, winImg, loseImg, drawImg
    # root.resizable(0,0)
    # root.attributes('-toolwindow', True)
    #print(background)
    if background == "#203647" :
        fgc = "AntiqueWhite1"
    else:
        fgc='#1F1F1F'
    rock_P__Frame.config(bg=background)
    rockImg = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/ROCKPAPERSCISSOR/1.jpg'))
    paperImg = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/ROCKPAPERSCISSOR/2.jpg'))
    scissorImg = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/ROCKPAPERSCISSOR/3.jpg'))
    grayImg = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/ROCKPAPERSCISSOR/grayQuestion.png'))
    orangeImg = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/ROCKPAPERSCISSOR/orangeQuestion.jpg'))
    winImg = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/ROCKPAPERSCISSOR/win.jpg'))
    loseImg = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/ROCKPAPERSCISSOR/lose.jpg'))
    drawImg = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/ROCKPAPERSCISSOR/draw.jpg'))

    toplbl = Label(rock_P__Frame, text='Total Score', font=('Arial Bold', 20), fg='#FE8A28', bg=background).pack()
    totalLabel = Label(rock_P__Frame, text='0   |   0', font=('Arial Bold', 15), fg=fgc, bg=background)
    totalLabel.pack()
    #bottom image
    img = ImageTk.PhotoImage(PIL.Image.open(_path+'Images/ROCKPAPERSCISSOR/rockPaperScissor.jpg'))
    downLbl = Label(rock_P__Frame, image=img)
    Label(rock_P__Frame,text=" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n",font=(100),bg=background).pack()
    downLbl.pack(side=BOTTOM)

    #user response
    userchat_RPS = Label(rock_P__Frame, text='Listening...', bg='#FE8A28', fg='white', font=('Arial Bold',13))
    userchat_RPS.place(x=300, y=120)
    userMoveLBL = Label(rock_P__Frame, image=orangeImg)
    userMoveLBL.place(x=260, y=150)

    #bot response
    botchat_RPS = Label(rock_P__Frame, text='Waiting...', bg='#EAEAEA', fg='#494949', font=('Arial Bold',13))
    botchat_RPS.place(x=12, y=120)
    botMoveLBL = Label(rock_P__Frame, image=grayImg)
    botMoveLBL.place(x=12, y=150)

    #Thread(target=playRock).start()
    playRock()

def isContain_RPS(text, lst):
	for word in lst:
		if word in text:
			return True
	return False

#-----------------------------


# Email WA----------------------------------------------------

U_Input =  ""
checkin_Sts = False

############################# WAEM - WhatsApp Email ##################################
def sendWAEM():
    global rec_phoneno, rec_email,U_Input,checkin_Sts
    data = U_Input
    rec_email, rec_phoneno = data, data
    U_Input = ""
    checkin_Sts = True


def WAEMPOPUP(Service='None', rec='Reciever'):
    #background, textColor,
    global WAEMEntry,U_Input
    PopUProot = Tk()
    PopUProot.title(f'{Service} Service')
    PopUProot.configure(bg=background)

    if Service=="WhatsApp": PopUProot.iconbitmap(_path+'Images/whatsapp.ico')
    else: PopUProot.iconbitmap(_path+"Images/email.ico")
    w_width, w_height = 410, 200
    s_width, s_height = PopUProot.winfo_screenwidth(), PopUProot.winfo_screenheight()
    x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
    PopUProot.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
    Label(PopUProot, text=f'Reciever {rec}', font=('Arial', 16), bg=background,fg=textColor).pack(pady=(20, 10))
    WAEMEntry = Entry(PopUProot, bd=10, relief=FLAT, font=('Arial', 12), justify='center', bg='#DCDCDC', width=30)
    def send(e):
        global U_Input
        #print(Service)
        if Service != "WhatsApp":
            ch = re.compile('@')
            if WAEMEntry.get() == "":
                wLabel.config(text="(Please Enter Email Address)",fg="indianred1")
            elif(ch.search(WAEMEntry.get()) == None):
                wLabel.config(text="(Invalid Email Address)",fg="indianred1")
            else:
                U_Input = WAEMEntry.get()
                PopUProot.destroy()
                sendWAEM()
        elif Service == "WhatsApp":
            ch = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if WAEMEntry.get() == "":
                wLabel.config(text="(Please Phone Number)",fg="indianred1")
            elif(ch.search(WAEMEntry.get()) != None):
                wLabel.config(text="(Invalid Phone Number)",fg="indianred1")
            else:
                U_Input = WAEMEntry.get()
                PopUProot.destroy()
                sendWAEM()


    WAEMEntry.pack()
    WAEMEntry.focus()
    wLabel = Label(PopUProot, text=' ', font=('Arialbold', 10), bg=background,fg=background)
    SendBtn = Button(PopUProot, text='Send', font=('Arial', 12), relief=FLAT, bg='#14A769', fg='white', command= lambda: send(0))
    SendBtn.pack(pady=20, ipadx=10)
    PopUProot.bind('<Return>', send)
    wLabel.pack()

    PopUProot.protocol( "WM_DELETE_WINDOW" , lambda: PopUProot.destroy())
    PopUProot.focus()
    PopUProot.mainloop()



#---------------------------------------------------------

def main(text):
    global data_update_check,checkin_Sts

    if "project" in text:
        if isContain(text, ['make', 'create']):
            speak("What do you want to give the project name ?", True, True)
            projectName = record(False, False)
            speak(fileHandler.CreateHTMLProject(projectName.capitalize()), True)
            return

    if "create" in text and "file" in text:
        speak(fileHandler.createFile(text), True, True)
        return

    if 'list' in text:
        if isContain(text, ['add', 'create',"create todo", 'make']):
            speak("What do you want to add?", True, True)
            item = record(False, False)
            ToDo.toDoList(item)
            speak("Alright, I added to your list", True)
            return
    if isContain(text, ['show',"show todo", 'my list']):
        items = ToDo.showtoDoList()
        if len(items)==1:
            speak(items[0], True, True)
            return
        attachTOframe('\n'.join(items), True)
        speak(items[0])
        return

    if isContain(text, ['factorial',"into",'log','value of','math',' + ',' - ',' x ','multiply','divided by','binary','hexadecimal','octal','shift','sin ','cos ','tan ']):
        try:
            Test=1
            speak(('Result is: ' + math_function.perform(text)), True, True)
        except Exception as e:
            return
        return

    if isContain(text, ['setting']):
        show_Setting_Frame()
        clearChatScreen()
        return

    if isContain(text, ['map', 'direction']):
        if "direction" in text:
            speak('What is your starting location?', True, True)
            startingPoint = record(False, False)
            speak("Ok "+ownerDesignation+", Where you want to go?", True)
            destinationPoint = record(False, False)
            speak("Ok "+ownerDesignation+", Getting Directions...", True)
            try:
                distance = webScrapping.giveDirections(startingPoint, destinationPoint)
                speak('You have to cover a distance of '+ distance, True)
            except:
                speak("I think location is not proper, Try Again!")
        else:
            webScrapping.maps(text)
            speak('Here you go...', True, True)
        return

    if isContain(text, ['meaning', 'dictionary', 'definition', 'define']):
        result = dictionary.translate(text)
        speak(result[0], True, True)
        if result[1]=='': return
        speak(result[1], True)
        return

    if "translate" in text:
        speak("What do you want to translate?", True, True)
        sentence = record(False, False)
        speak("Which language to translate ?", True)
        langauage = record(False, False)
        result = normalChat.lang_translate(sentence, langauage)
        #print(result.pronunciation)
        #print(result)
        if result=="None": speak("This language doesn't exists")
        else:
            speak(f"In {langauage.capitalize()} you would say:", True)
            #attachTOframe(result, True)
            speak(result,True)
            #else: speak(result, True)
        return

    if 'email' in text:
        speak('Whom do you want to send the email?', True, True)
        mainwindow.withdraw()
        WAEMPOPUP("Email", "E-mail Address")
        attachTOframe(rec_email)
        mainwindow.deiconify()
        mainwindow.focus()
        if checkin_Sts == True:
            speak('What is the Subject?', True)
            subject = record(False, False)
            speak('What message you want to send ?', True)
            message = record(False, False)
            Thread(target=webScrapping.email, args=(rec_email,message,subject,) ).start()
            speak('Email has been Sent', True)
            checkin_Sts = False
            return
        else:
            speak('Email Sent Cancled', True)
            return

    if 'whatsapp' in text:
        speak("Sure "+ownerDesignation+"...", True, True)
        speak('Whom do you want to send the message?', True)
        mainwindow.withdraw()
        WAEMPOPUP("WhatsApp", "Phone Number")
        attachTOframe(rec_phoneno)
        mainwindow.deiconify()
        mainwindow.focus()
        if checkin_Sts == True:
            speak('What is the message?', True)
            message = record(False, False)
            Thread(target=webScrapping.sendWhatsapp, args=(rec_phoneno, message,)).start()
            speak("Message is on the way. Do not move away from the screen.")
            attachTOframe("Trying To Send The Message", True)
            checkin_Sts = False
            return
        else:
            speak('Message Sent Cancled', True)
            return

    if isContain(text, ['rock', 'paper', 'scissor','stone','play', 'play game','play games','coin','toss','roll','dice','flip']):
        if isContain(text, ['play game','play games','play','games']):
            speak("Which Game You Want To Play "+ownerDesignation+ " \n1) Rock Paper Scissor\n2) Coin Toss\n3) Roll A Dice\n4) Online Games", True, True)
            #Gname = record(False, False)
        elif isContain(text, ['rock', 'paper', 'scissor','stone']):
            rock_P__Frame.place(x=-1,y=0)
            s=rockPaperScissorWindow()
            speak("Hope You Enjoy The Game "+ownerDesignation,True, True)
        elif isContain(text, ['coin','toss','roll','dice','flip']):
            if "toss" in text or "roll" in text or "flip" in text:
                speak("Ok "+ownerDesignation, True, True)
                result = game.play(text)
                if "Head" in result: showSingleImage('head')
                elif "Tail" in result: showSingleImage('tail')
                else: showSingleImage(result[-1])
                speak(result)
                #return
        return

    if isContain(text, ['online','online games']):
        webbrowser.open("https://www.google.com/doodles/games")
        speak("Enjoy Your Game "+ownerDesignation,True, True)
        #print("Online")
        return

    '''if isContain(text, ['play game','play games','game','games']):
        speak("Which Game You Want To Play "+ownerDesignation+ " \n1. Rock Paper Scissor\n2. Coin Toss\n3. Roll A Dice\n4.Online Games", True, True)
        Gname = record(False, False)

    if isContain(text, ['coin','toss','roll','dice','flip']):
        if "toss" in text or "roll" in text or "flip" in text:
            speak("Ok "+ownerDesignation, True, True)
            result = game.play(text)
            if "Head" in result: showSingleImage('head')
            elif "Tail" in result: showSingleImage('tail')
            else: showSingleImage(result[-1])
            speak(result)
            return'''

    if isContain(text, ['covid','virus']):
        if data_update_check == 0:
            webScrapping.dataUpdate()
            data_update_check = 1
        result = webScrapping.covid(text)
        if 'str' in str(type(result)):
            speak(result, True, True)
            return
        speak(result[0], True, True)
        result = '\n'.join(result[1])
        speak(result, True, False)
        attachTOframe(result, True)
        return

    if isContain(text, ['open youtube']):
        speak("Ok "+ownerDesignation+" Opening Youtube...", True, True)
        webbrowser.open("https://www.youtube.com")
        return

    if isContain(text, ['search for a video in youtube','search for a video']):
        speak("What Video", True, True)
        video = record(False, False)
        try:
            speak(webScrapping.youtube(video,ownerDesignation), True)
        except Exception as e:
            speak("Desired Result Not Found", True)
        return

    if isContain(text, ['in youtube','video']):
        speak("Ok Searching...", True, True)
        try:
            speak(webScrapping.youtube2(text,ownerDesignation), True)
        except Exception as e:
            speak("Desired Result Not Found", True)
        return

    if isContain(text, ['search', 'image']):
        if 'image' in text and 'show' in text:
            Thread(target=showImages, args=(text,)).start()
            speak('Here are the images...', True, True)
            return
        speak(webScrapping.googleSearch(text), True, True)
        return

    if isContain(text, ['map', 'direction']):
        if "direction" in text:
            speak('What is your starting location?', True, True)
            startingPoint = record(False, False)
            speak("Ok "+ownerDesignation+", Where you want to go?", True)
            destinationPoint = record(False, False)
            speak("Ok "+ownerDesignation+", Getting Directions...", True)
            try:
                distance = webScrapping.giveDirections(startingPoint, destinationPoint)
                speak('You have to cover a distance of '+ distance, True)
            except:
                speak("I think location is not proper, Try Again!")
        else:
            webScrapping.maps(text)
            speak('Here you go...', True, True)
        return

    if "joke" in text:
        speak('Here is a joke...', True, True)
        speak(webScrapping.jokes(), True)
        return

    if isContain(text, ['news']):
        speak('Getting the latest news...', True, True)
        headlines,headlineLinks = webScrapping.latestNews(2)
        for head in headlines: speak(head, True)
        speak('Do you want to read the full news?', True)
        text = record(False, False)
        if isContain(text, ["no","don't"]):
            speak("No Problem "+ownerDesignation, True)
        else:
            speak("Ok "+ownerDesignation+", Opening browser...", True)
            webScrapping.openWebsite('https://indianexpress.com/latest-news/')
            speak("You can now read the full news from this website.")
        return

    if isContain(text, ['weather']):
        if data_update_check == 0:
            webScrapping.dataUpdate()
            data_update_check = 1
        data = webScrapping.weather()
        speak('', False, True)
        showSingleImage("weather", data[:-1])
        speak(data[-1])
        return


    if isContain(text, ['wiki', 'who is']):
        Thread(target=webScrapping.downloadImage, args=(text, 1,)).start()
        speak('Searching...', True, True)
        result = webScrapping.wikiResult(text)
        showSingleImage('wiki')
        speak(result, True)
        return


    if isContain(text, ['time','date']):
        speak(normalChat.chat(text), True, True)
        return

    if 'my name' in text:
        speak('Your name is, ' + ownerName, True, True)
        return

    if 'hi' in text:
        speak('Your name is, ' + ownerDesignation, True, True)
        return

    if isContain(text, ["who are you","whats your name","what is your name"," what's your name"]):
        #print("enter")
        speak('My name is, Friday, and I am a virtual assistant', True, True)
        return

    if isContain(text, ['morning','evening','noon']) and 'good' in text:
        speak(normalChat.chat("good"), True, True)
        return

    result = normalChat.reply(text)
    if result != "None": speak(result, True, True)

    else:
        #Do you want to search, for "+text+" in google?"
        speak('Sorry, '+ownerDesignation+" I cant's understand.",True,True)
        #speak('Sorry, '+ownerDesignation+" I cant's understand", True, True)
        speak("Do you want to search, for "+text+" in google?", True)
        query = text
        text = record(False, False)
        if isContain(text, ["no","don't"]):
            speak("Okey "+ownerDesignation, True)
        elif isContain(text, ["yes","go for it","do"]):
            speak("Ok "+ownerDesignation+", Opening browser...", True)
            for url in GS.search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            speak("Showing search result in your browsert "+ownerDesignation)
        return

cblLightImg = PhotoImage(file=_path+'Images/centralButton.png')
cblDarkImg = PhotoImage(file=_path+'Images/centralButton1.png')
if KCS_IMG==1: cblimage=cblDarkImg
else: cblimage=cblLightImg
cbl = Label(VoiceModeFrame, fg='white', image=cblimage, bg='#dfdfdf')
cbl.pack(pady=17)
AITaskStatusLbl = Label(VoiceModeFrame, text='    Offline', fg='white', bg=AITaskStatusLblBG, font=('montserrat', 16))
AITaskStatusLbl.place(x=140,y=32)


#Settings Button
sphLight = PhotoImage(file = _path+'Images/setting.png')
sphLight = sphLight.subsample(2,2)
sphDark = PhotoImage(file = _path+'Images/setting1.png')
sphDark = sphDark.subsample(2,2)
if KCS_IMG==1: sphimage=sphDark
else: sphimage=sphLight
settingBtn = Button(VoiceModeFrame,image=sphimage,height=30,width=30, bg='#dfdfdf',borderwidth=0,activebackground="#dfdfdf",command=show_Setting_Frame)#,command=show_Setting_Frame
settingBtn.place(relx=1.0, y=30,x=-20, anchor="ne")

#Keyboard Button
kbphLight = PhotoImage(file = _path+'Images/keyboard.png')
kbphLight = kbphLight.subsample(2,2)
kbphDark = PhotoImage(file = _path+'Images/keyboard1.png')
kbphDark = kbphDark.subsample(2,2)
if KCS_IMG==1: kbphimage=kbphDark
else: kbphimage=kbphLight
kbBtn = Button(VoiceModeFrame,image=kbphimage,height=30,width=30, bg='#dfdfdf',borderwidth=0,activebackground="#dfdfdf",command=changeChatMode)#,command=changeChatMode
kbBtn.place(x=25, y=30)

#Mic
micImg = PhotoImage(file = _path+'Images/mic.png')
micImg = micImg.subsample(2,2)
micBtn = Button(TextModeFrame,image=micImg,height=30,width=30, bg='#dfdfdf',borderwidth=0,activebackground="#dfdfdf", command=changeChatMode)#, command=changeChatMode
micBtn.place(relx=1.0, y=30,x=-20, anchor="ne")



#Text Field
TextFieldImg = PhotoImage(file= _path+'Images/textField.png')
UserFieldLBL = Label(TextModeFrame, fg='white', image=TextFieldImg, bg='#dfdfdf')
UserFieldLBL.pack(pady=17, side=LEFT, padx=10)
UserField = Entry(TextModeFrame, fg='white', bg='#203647', font=('Montserrat', 16), bd=6, width=22, relief=FLAT)
UserField.place(x=20, y=30)
UserField.insert(0, "Ask me anything...")
UserField.bind('<Return>', keyboardInput)


userIcon = PhotoImage(file=_path+"Images/Avatar/ChatIcons/a"+str(ownerPhoto)+".png")
botIcon = PhotoImage(file=_path+"Images/assistant2.png")
botIcon = botIcon.subsample(2,2)

###########################
########  SETTINGS  #######
###########################

settingsLbl = Label(settings_frame, text='Settings', font=('Arial Bold', 15), bg=background, fg=textColor)
settingsLbl.pack(pady=10)
separator = ttk.Separator(settings_frame, orient='horizontal')
separator.pack(fill=X)

Fake_LBl_1 = Label(settings_frame, text=' ', font=('Arial Bold', 18), bg=background, fg=background)
Fake_LBl_1.pack()

#User Photo
userProfileImg = PIL.Image.open(_path+"Images/Avatar/UserFace"+str(ownerPhoto)+".png")
userProfileImg = ImageTk.PhotoImage(userProfileImg.resize((120, 120)))
userPhoto = Button(settings_frame, image=userProfileImg, bg=background, bd=0, relief=FLAT, activebackground=background, command=SelectAvatar_Btn)#, command=SelectAvatar
userPhoto.pack(pady=(20, 5))

#Change Photo
chngPh = ImageTk.PhotoImage(PIL.Image.open(_path+"Images/Avatar/changephoto2.png").resize((120, 120)))

userPhoto.bind('<Enter>', onhover)
userPhoto.bind('<Leave>', onleave)

#Username
userName = Label(settings_frame, text=ownerName, font=('Arial Bold', 15), fg=textColor, bg=background)
userName.pack()

Fake_LBl_2 = Label(settings_frame, text=' ', font=('Arial Bold', 5), bg=background, fg=background)
Fake_LBl_2.pack()

#Settings Frame
settingsFrame = Frame(settings_frame, width=300, height=300, bg=background)
settingsFrame.pack(pady=20)


assLbl = Label(settingsFrame, text='Assistant Voice', font=('Arial', 13), fg=textColor, bg=background)
assLbl.place(x=0, y=20)
assVoiceOption = ttk.Combobox(settingsFrame,state="readonly", values=('Male','Female'), font=('Arial', 13), width=13, textvariable=n)
assVoiceOption.current(voice_id)
assVoiceOption.place(x=150, y=20)
assVoiceOption.bind('<<ComboboxSelected>>', changeVoice)


voiceRateLbl = Label(settingsFrame, text='Voice Rate', font=('Arial', 13), fg=textColor, bg=background)
voiceRateLbl.place(x=0, y=60)
voiceOption = ttk.Combobox(settingsFrame, state="readonly", font=('Arial', 13), width=13, textvariable=n2)
voiceOption['values'] = ('Very Low', 'Low', 'Normal', 'Fast', 'Very Fast')
voiceOption.current(ass_voiceRate//50-2) #100 150 200 250 300
voiceOption.place(x=150, y=60)
voiceOption.bind('<<ComboboxSelected>>', changeVoiceRate)

volumeLbl = Label(settingsFrame, text='Volume', font=('Arial', 13), fg=textColor, bg=background)
volumeLbl.place(x=0, y=105)
volumeBar = Scale(settingsFrame, bg=background, fg=textColor, sliderlength=30, length=135, width=16, highlightbackground=background, orient='horizontal', from_=0, to=100, command=changeVolume)#, command=changeVolume
volumeBar.set(int(ass_volume*100))
volumeBar.place(x=150, y=85)

themeLbl = Label(settingsFrame, text='Theme', font=('Arial', 13), fg=textColor, bg=background)
themeLbl.place(x=0,y=143)
s = ttk.Style()
s.configure('Wild.TRadiobutton', font=('Arial Bold', 10), background=background, foreground=textColor, focuscolor=s.configure(".")["background"])
darkBtn = ttk.Radiobutton(settingsFrame, text='Dark', value=1, variable=themeValue, style='Wild.TRadiobutton',command=changeTheme,  takefocus=False)#command=changeTheme,
darkBtn.place(x=150,y=145)
lightBtn = ttk.Radiobutton(settingsFrame, text='Light', value=2, variable=themeValue, style='Wild.TRadiobutton',command=changeTheme,  takefocus=False)#command=changeTheme,
lightBtn.place(x=230,y=145)

'''
if Theme_Mode == 1:
    themeValue.set(2)'''
#print(Theme_Mode)
themeValue.set(1)
if KCS_IMG==0: themeValue.set(2)

chooseChatLbl = Label(settingsFrame, text='Chat Background', font=('Arial', 13), fg=textColor, bg=background)
chooseChatLbl.place(x=0,y=180)
cimg = PhotoImage(file = _path+"Images/colorchooser.png")
cimg = cimg.subsample(3,3)
colorbar = Label(settingsFrame, bd=3, width=18, height=1, bg=chatBgColor)
colorbar.place(x=150, y=180)
if KCS_IMG==0: colorbar['bg'] = '#E8EBEF'
Button(settingsFrame, image=cimg, relief=FLAT,command=getChatColor).place(x=261, y=180)#, command=getChatColor

backBtn = Button(settingsFrame, text='   Back   ', bd=0, font=('Arial 16'), fg='white', bg='#14A769', relief=FLAT,command=show_Chat_Frame)#,command=show_Chat_Frame
backBtn.place(x=32, y=250)

AboutBtn = Button(settingsFrame, text='   About   ', bd=0, font=('Arial 16'), fg='white', bg='#14A769', relief=FLAT,command=show_About_Frame)#,command=show_Chat_Frame
AboutBtn.place(x=160, y=250)

#AboutBtn.place(x=150, y=255)

#backBtn.place(x=5, y=250)
#clearFaceBtn.place(x=120, y=250)

#AboutBtn.place(x=150, y=255)    Backup
#backBtn.place(x=100, y=255)       Backup
#################################
Chouse_Avtar_LAbel_2nd.pack()
#.place(x=52,y=10)
Fake_L_N2 = Label(secondAvatar_choosing_Frame, text=" ", font=('arial', 5))
Fake_L_N2.pack()
avatarContainer_2nd.pack(pady=10)

check_Img2 =PIL.Image.open(_path+'Images/Check.png')
check_Img2 = check_Img2.resize((80, 80))
check_Img2 = ImageTk.PhotoImage(check_Img2)


size_2 = 100
avtr1_2 = PIL.Image.open(_path+'Images/Avatar/UserFace1.png')
avtr1_2 = avtr1_2.resize((size_2, size_2))
avtr1_2 = ImageTk.PhotoImage(avtr1_2)
avtr2_2 = PIL.Image.open(_path+'Images/Avatar/UserFace2.png')
avtr2_2 = avtr2_2.resize((size_2, size_2))
avtr2_2 = ImageTk.PhotoImage(avtr2_2)
avtr3_2 = PIL.Image.open(_path+'Images/Avatar/UserFace3.png')
avtr3_2 = avtr3_2.resize((size_2, size_2))
avtr3_2 = ImageTk.PhotoImage(avtr3_2)
avtr4_2 = PIL.Image.open(_path+'Images/Avatar/UserFace4.png')
avtr4_2 = avtr4_2.resize((size_2, size_2))
avtr4_2 = ImageTk.PhotoImage(avtr4_2)
avtr5_2 = PIL.Image.open(_path+'Images/Avatar/UserFace5.png')
avtr5_2 = avtr5_2.resize((size_2, size_2))
avtr5_2 = ImageTk.PhotoImage(avtr5_2)
avtr6_2 = PIL.Image.open(_path+'Images/Avatar/UserFace6.png')
avtr6_2 = avtr6_2.resize((size_2, size_2))
avtr6_2 = ImageTk.PhotoImage(avtr6_2)
avtr7_2 = PIL.Image.open(_path+'Images/Avatar/UserFace7.png')
avtr7_2 = avtr7_2.resize((size_2, size_2))
avtr7_2 = ImageTk.PhotoImage(avtr7_2)
avtr8_2 = PIL.Image.open(_path+'Images/Avatar/UserFace8.png')
avtr8_2 = avtr8_2.resize((size_2, size_2))
avtr8_2 = ImageTk.PhotoImage(avtr8_2)


avtb1_2 = Button(avatarContainer_2nd,cursor="hand2", image=avtr1_2, relief=FLAT, bd=0, command=lambda:selectAVATAR_IMG(1))
avtb1_2.grid(row=0, column=0, ipadx=25, ipady=10)

avtb2_2 = Button(avatarContainer_2nd,cursor="hand2", image=avtr2_2, relief=FLAT, bd=0, command=lambda:selectAVATAR_IMG(2))
avtb2_2.grid(row=0, column=1, ipadx=25, ipady=10)

avtb3_2 = Button(avatarContainer_2nd,cursor="hand2", image=avtr3_2, relief=FLAT, bd=0, command=lambda:selectAVATAR_IMG(3))
avtb3_2.grid(row=1, column=0, ipadx=25, ipady=10)

avtb4_2 = Button(avatarContainer_2nd,cursor="hand2", image=avtr4_2, relief=FLAT, bd=0, command=lambda:selectAVATAR_IMG(4))
avtb4_2.grid(row=1, column=1, ipadx=25, ipady=10)

avtb5_2 = Button(avatarContainer_2nd,cursor="hand2", image=avtr5_2, relief=FLAT, bd=0, command=lambda:selectAVATAR_IMG(5))
avtb5_2.grid(row=2, column=0, ipadx=25, ipady=10)

avtb6_2 = Button(avatarContainer_2nd,cursor="hand2", image=avtr6_2, relief=FLAT, bd=0, command=lambda:selectAVATAR_IMG(6))
avtb6_2.grid(row=2, column=1, ipadx=25, ipady=10)

avtb7_2 = Button(avatarContainer_2nd,cursor="hand2", image=avtr7_2, relief=FLAT, bd=0, command=lambda:selectAVATAR_IMG(7))
avtb7_2.grid(row=3, column=0, ipadx=25, ipady=10)

avtb8_2 = Button(avatarContainer_2nd,cursor="hand2", image=avtr8_2, relief=FLAT, bd=0, command=lambda:selectAVATAR_IMG(8))
avtb8_2.grid(row=3, column=1, ipadx=25, ipady=10)

Button(secondAvatar_choosing_Frame, text='         Change         ', font=('Arial Bold', 15), bg='#01933B', fg='white', bd=0, relief=FLAT,command=SuccessfullyRegistered_2nd).pack()#,command=SuccessfullyRegistered_2nd

Fake_LBl_3 = Label(secondAvatar_choosing_Frame, text=' \n', font=('Arial Bold', 16), bg=background, fg=background)
Fake_LBl_3.pack()

check_Label2 = Label(avatarContainer_2nd, image=check_Img2, bd=0)




if Theme_Mode == 0:
    changeTheme()

show_Chat_Frame()
Voice_start = Thread(target=voiceMedium)
Voice_start.daemon = True
#Voice_start.start()




mainwindow.protocol( "WM_DELETE_WINDOW" , lambda: exit_conformation(1))



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = SplashScreen()
    #print(window)
    sys.exit(app.exec_())


