import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Communication import keresFutoSzerver, kuldAkkord, kuldDal , kuldKikapcs

t=[]
szerverek = []
class Button(QPushButton):

    def __init__(self, label, parent=None):
        super(Button, self).__init__(label, parent)
        # other initializations...

    def enterEvent(self, QEvent):
        if self.objectName() == "kezdo_gomb" or self.objectName() == "halado_gomb" or self.objectName() == "kozepes_gomb":
            self.setStyleSheet('''
                QPushButton {
                    font-size: 30pt;
                    font-family: "Arial";
                    border: 1px solid black;
                    border-radius: 10px;
                    margin-top: 5px;
                    margin-left: 5px;
                    margin-right: 5px;
                    background-color: rgba(222, 157, 234);
                    color: rgba(50, 50, 50)
                }
            ''')

        if self.objectName() == "em_gomb" or self.objectName() == "am_gomb" or self.objectName() == "dm_gomb" or self.objectName() == "c_gomb" or self.objectName() == "e_gomb" or self.objectName() == "a_gomb" or self.objectName() == "g_gomb" or self.objectName() == "d_gomb":
            self.setStyleSheet('''
                QPushButton {
                    font-size: 30pt;
                    font-family: "Arial";
                    border: 1px solid black;
                    border-radius: 10px;
                    margin-top: 5px;
                    margin-left: 5px;
                    margin-right: 5px;
                    background-color: rgba(222, 157, 234);
                    color: rgba(50, 50, 50)
                }
            ''')

        if self.objectName() == "akkordok_gomb" or self.objectName() == "dalok_gomb":
            self.setStyleSheet('''
                QPushButton {
                    font-size: 30pt;
                    font-family: "Arial";
                    border: 1px solid black;
                    border-radius: 10px;
                    margin-top: 5px;
                    margin-left: 5px;
                    margin-right: 5px;
                    background-color: rgba(222, 157, 234);
                    color: rgba(50, 50, 50)
                }
            ''')

        if self.objectName() == "vissza_gomb":
            self.setStyleSheet('''
                    #vissza_gomb {
                        border: 0px;
                        font-size: 15pt;
                        float: left;
                        text-decoration: underline;
                    }
                    ''')

    def leaveEvent(self, QEvent):
        if self.objectName() == "kezdo_gomb" or self.objectName() == "halado_gomb" or self.objectName() == "kozepes_gomb":
            self.setStyleSheet('''
                QPushButton {
                    font-size: 30pt;
                    font-family: "Arial";
                    border: 1px solid black;
                    border-radius: 10px;
                    margin-top: 5px;
                    margin-left: 5px;
                    margin-right: 5px;
                    background-color: rgba(196, 142, 206);
                    color: rgba(50, 50, 50)
                }
            ''')

        if self.objectName() == "em_gomb" or self.objectName() == "am_gomb" or self.objectName() == "dm_gomb" or self.objectName() == "c_gomb" or self.objectName() == "e_gomb" or self.objectName() == "a_gomb" or self.objectName() == "g_gomb" or self.objectName() == "d_gomb":
            self.setStyleSheet('''
                QPushButton {
                    font-size: 30pt;
                    font-family: "Arial";
                    border: 1px solid black;
                    border-radius: 10px;
                    margin-top: 5px;
                    margin-left: 5px;
                    margin-right: 5px;
                    background-color: rgba(196, 142, 206);
                    color: rgba(50, 50, 50)
                }
            ''')

        if self.objectName() == "akkordok_gomb" or self.objectName() == "dalok_gomb":
            self.setStyleSheet('''
                QPushButton {
                    font-size: 30pt;
                    font-family: "Arial";
                    border: 1px solid black;
                    border-radius: 10px;
                    margin-top: 5px;
                    margin-left: 5px;
                    margin-right: 5px;
                    background-color: rgba(196, 142, 206);
                    color: rgba(50, 50, 50)
                }
            ''')


        if self.objectName() == "vissza_gomb":
            self.setStyleSheet('''
                    #vissza_gomb {
                        border: 0px;
                        font-size: 15pt;
                        float: left;
                        position: fixed; 
                    }
                    ''')

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.initUI()
        self.layout = QFormLayout(self)
        self.setLayout(self.layout)
        
        
    def initUI(self): 
        self.kezdo_gomb = Button('Kezdő', self) # letrehozunk egy gombot ami Kezdot fog irni
        self.kezdo_gomb.resize(QSize(1920, 360)) # meghatarozzuk a meretet
        self.kezdo_gomb.move(0, 0) # elmozditjuk a (0, 0) kordinatara
        self.kezdo_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        # css stilusban formazzuk a gombot
        self.kezdo_gomb.setObjectName("kezdo_gomb") # nevet adunk a gombnak (keresztelo)
        self.kezdo_gomb.installEventFilter(self) # megmondjuk, hogy keresse azt az alprogramot, ami eldonti mi tortenik gombnyomaskor


        self.kozepes_gomb = Button('Közepes', self)
        self.kozepes_gomb.resize(QSize(1920, 360))
        self.kozepes_gomb.move(0, 360)
        self.kozepes_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.kozepes_gomb.setObjectName("kozepes_gomb")
        self.kozepes_gomb.installEventFilter(self)


        self.halado_gomb = Button('Haladó', self)
        self.halado_gomb.resize(QSize(1920, 360))
        self.halado_gomb.move(0, 720)     
        self.halado_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.halado_gomb.installEventFilter(self)
        self.halado_gomb.setObjectName("halado_gomb")
       
        self.em_gomb = Button('Em', self)
        self.em_gomb.resize(QSize(480, 400))
        self.em_gomb.move(0, 150)     
        self.em_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.em_gomb.installEventFilter(self)
        self.em_gomb.setObjectName("em_gomb")

        self.am_gomb = Button('Am', self)
        self.am_gomb.resize(QSize(480, 400))
        self.am_gomb.move(480, 150)     
        self.am_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.am_gomb.installEventFilter(self)
        self.am_gomb.setObjectName("am_gomb")

        self.dm_gomb = Button('Dm', self)
        self.dm_gomb.resize(QSize(480, 400))
        self.dm_gomb.move(960, 150)     
        self.dm_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid blaDk; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.dm_gomb.installEventFilter(self)
        self.dm_gomb.setObjectName("dm_gomb")

        self.c_gomb = Button('C', self)
        self.c_gomb.resize(QSize(480, 400))
        self.c_gomb.move(1440, 150)     
        self.c_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.c_gomb.installEventFilter(self)
        self.c_gomb.setObjectName("c_gomb")

        self.e_gomb = Button('E', self)
        self.e_gomb.resize(QSize(480, 400))
        self.e_gomb.move(0, 600)     
        self.e_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.e_gomb.installEventFilter(self)
        self.e_gomb.setObjectName("e_gomb")

        self.a_gomb = Button('A', self)
        self.a_gomb.resize(QSize(480, 400))
        self.a_gomb.move(480, 600)     
        self.a_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.a_gomb.installEventFilter(self)
        self.a_gomb.setObjectName("a_gomb")

        self.g_gomb = Button('G', self)
        self.g_gomb.resize(QSize(480, 400))
        self.g_gomb.move(1440, 600)
        self.g_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.g_gomb.installEventFilter(self)
        self.g_gomb.setObjectName("g_gomb")

        self.d_gomb = Button('D', self)
        self.d_gomb.resize(QSize(480, 400))
        self.d_gomb.move(960, 600)     
        self.d_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.d_gomb.installEventFilter(self)
        self.d_gomb.setObjectName("d_gomb")

        self.akkordok_gomb = Button('Akkordok', self)
        self.akkordok_gomb.resize(QSize(960, 800))
        self.akkordok_gomb.move(0, 150)     
        self.akkordok_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.akkordok_gomb.installEventFilter(self)
        self.akkordok_gomb.setObjectName("akkordok_gomb")

        self.dalok_gomb = Button('Dalok', self)
        self.dalok_gomb.resize(QSize(960, 800))
        self.dalok_gomb.move(960, 150)     
        self.dalok_gomb.setStyleSheet('QPushButton {font-size: 30pt; font-family: "Arial"; border: 1px solid black; border-radius: 10px; margin-top: 5px; margin-left: 5px; margin-right: 5px; background-color: rgb(196, 142, 206); color: rgba(50, 50, 50)}')
        self.dalok_gomb.installEventFilter(self)
        self.dalok_gomb.setObjectName("dalok_gomb")

        self.lbl_akkord = QLabel(" ", self)

        self.combo_akkord = QComboBox(self)
        self.combo_akkord.addItem("Aadd9")
        self.combo_akkord.addItem("Asus4")
        self.combo_akkord.addItem("Amaj7")
        self.combo_akkord.addItem("Eadd9")
        self.combo_akkord.addItem("E7")
        self.combo_akkord.addItem("Em7")
        self.combo_akkord.addItem("A7")
        self.combo_akkord.addItem("Am7")
        self.combo_akkord.addItem("D7")
        self.combo_akkord.addItem("Dm7")
        self.combo_akkord.addItem("G7")
        self.combo_akkord.addItem("C7")
        self.combo_akkord.addItem("Esus4")
        self.combo_akkord.addItem("Emaj7")
        self.combo_akkord.addItem("B7")
        self.combo_akkord.addItem("Fadd9")
        self.combo_akkord.addItem("Fmaj7")
        self.combo_akkord.addItem("Gadd9")
        self.combo_akkord.addItem("Gmaj7")
        self.combo_akkord.addItem("Dadd9")
        self.combo_akkord.addItem("Dsus4")
        self.combo_akkord.addItem("Dmaj7")
        self.combo_akkord.addItem("Cadd9")
        self.combo_akkord.addItem("Csus4")
        self.combo_akkord.addItem("Cmaj7")
        self.combo_akkord.addItem("Cmaj9")

        self.combo_akkord.move(100, 300)
        self.combo_akkord.resize((QSize(400,100)))
        self.combo_akkord.setStyleSheet('QComboBox {font-size: 30pt; font-family: "Arial"; color: rgba(50, 50, 50)}')
        self.lbl_akkord.move(880, 450)
        self.lbl_akkord.setStyleSheet('QLabel {font-size: 100pt; font-family: "Arial"; color: rgba(50, 50, 50)}')

        self.combo_akkord.activated[str].connect(self.onActivated) 

        self.lbl_dal = QLabel(" ", self)

        self.combo_dal = QComboBox(self)
        self.combo_dal.addItem("Silent Night")
        self.combo_dal.addItem("Boulevard of Broken Dreams")
        self.combo_dal.addItem("Jó nekem")

        self.combo_dal.move(100, 300)
        self.combo_dal.resize((QSize(400,100)))
        self.combo_dal.setStyleSheet('QComboBox {font-size: 30pt; font-family: "Arial"; color: rgba(50, 50, 50)}')
        self.lbl_dal.move(750, 450)
        self.lbl_dal.setStyleSheet('QLabel {font-size: 50pt; font-family: "Arial"; color: rgba(50, 50, 50)}')
      
        self.combo_dal.activated[str].connect(self.onActivated) 

        self.lbl_akkord2 = QLabel(" ", self)

        self.combo_akkord2 = QComboBox(self)
        self.combo_akkord2.addItem("Cm")
        self.combo_akkord2.addItem("Gm")
        self.combo_akkord2.addItem("Fm")
        self.combo_akkord2.addItem("Bm")
        self.combo_akkord2.addItem("Bbm")
        self.combo_akkord2.addItem("F")
        self.combo_akkord2.addItem("B")
        self.combo_akkord2.addItem("Bb")
        self.combo_akkord2.addItem("Cm7")
        self.combo_akkord2.addItem("Gsus4")
        self.combo_akkord2.addItem("Fsus4")
        self.combo_akkord2.addItem("Bmaj7")
        self.combo_akkord2.addItem("Bsus4")
        self.combo_akkord2.addItem("Badd9")

        self.combo_akkord2.move(100, 300)
        self.combo_akkord2.resize((QSize(400,100)))
        self.combo_akkord2.setStyleSheet('QComboBox {font-size: 30pt; font-family: "Arial"; color: rgba(50, 50, 50)}')
        self.lbl_akkord2.move(880, 450)
        self.lbl_akkord2.setStyleSheet('QLabel {font-size: 100pt; font-family: "Arial"; color: rgba(50, 50, 50)}')

        self.combo_akkord2.activated[str].connect(self.onActivated) 

        self.lbl_dal2 = QLabel(" ", self)

        self.combo_dal2 = QComboBox(self)
        self.combo_dal2.addItem("All I want for Christmas is you")
        self.combo_dal2.addItem("Heavy")
        self.combo_dal2.addItem("67-es út")

        self.combo_dal2.move(100, 300)
        self.combo_dal2.resize((QSize(400,100)))
        self.combo_dal2.setStyleSheet('QComboBox {font-size: 30pt; font-family: "Arial"; color: rgba(50, 50, 50)}')
        self.lbl_dal2.move(650, 450)
        self.lbl_dal2.setStyleSheet('QLabel {font-size: 50pt; font-family: "Arial"; color: rgba(50, 50, 50);}')
      
        self.combo_dal2.activated[str].connect(self.onActivated)      

        self.setGeometry(0, 0, 1920, 768)
        self.setWindowTitle('Quit button')    
        self.showFullScreen()

    
    def onActivated(self, text):
        global szerverek
        if len(szerverek) != 0 and (self.level == 21 or self.level == 31):
            kuldAkkord(szerverek[0]['ip'], text)
        elif len(szerverek) !=0 and (self.level == 22 or self.level == 32):
            kuldDal(szerverek[0]['ip'], text)
        self.lbl_akkord.setText(text)
        self.lbl_akkord.adjustSize()
        self.lbl_dal.setText(text)
        self.lbl_dal.adjustSize()
        self.lbl_akkord2.setText(text)
        self.lbl_akkord2.adjustSize()
        self.lbl_dal2.setText(text)
        self.lbl_dal2.adjustSize()

    def handleActivated(self, index):  
        #print(self.combo_akkord.itemText(index))
        x=self.combo_akkord.itemText(index)
        return x

    def eventFilter(self, object, event):
        if  self.level == 0:
            self.em_gomb.hide()
            self.am_gomb.hide()
            self.dm_gomb.hide()
            self.c_gomb.hide()  
            self.a_gomb.hide()
            self.e_gomb.hide()
            self.g_gomb.hide()
            self.d_gomb.hide()
            self.akkordok_gomb.hide()
            self.dalok_gomb.hide()
            self.combo_akkord.hide()
            self.lbl_akkord.hide()
            self.combo_dal.hide()
            self.lbl_dal.hide()
            self.akkordok_gomb.hide()
            self.dalok_gomb.hide()
            self.combo_akkord2.hide()
            self.lbl_akkord2.hide()
            self.combo_dal2.hide()
            self.lbl_dal2.hide()
                          
            if event.type() == QEvent.MouseButtonPress:
                self.vissza_gomb = Button('Vissza', self)
                self.vissza_gomb.installEventFilter(self)
                self.vissza_gomb.setObjectName("vissza_gomb")
                self.setStyleSheet('''
                    #vissza_gomb {
                        border: 0px;
                        font-size: 15pt;
                        float: left;
                    }
                    ''')
                self.layout.addWidget(self.vissza_gomb)

                if object.objectName() == "kezdo_gomb":
                    self.level = 1
                    self.initLevel1()
                    self.halado_gomb.hide()
                    self.kezdo_gomb.hide()
                    self.kozepes_gomb.hide()
                    self.em_gomb.show()
                    self.am_gomb.show()
                    self.dm_gomb.show()          
                    self.c_gomb.show() 
                    self.e_gomb.show()
                    self.a_gomb.show()
                    self.g_gomb.show()
                    self.d_gomb.show()
                    self.akkordok_gomb.show()
                    self.dalok_gomb.show()
                elif object.objectName() == "kozepes_gomb":
                    self.initLevel2()
                    self.level = 2
                    self.halado_gomb.hide()
                    self.kezdo_gomb.hide()
                    self.kozepes_gomb.hide()
                elif object.objectName() == "halado_gomb":
                    self.level = 3
                    self.initLevel3()
                    self.halado_gomb.hide()
                    self.kezdo_gomb.hide()
                    self.kozepes_gomb.hide()

                return True

        if self.level == 1: 
            self.akkordok_gomb.hide()
            self.dalok_gomb.hide()  
            if event.type() == QEvent.MouseButtonPress:
                if object.objectName() == "em_gomb":
                    self.level = 11
                    self.initLevel11()
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.akkordok_gomb.hide()
                    self.dalok_gomb.hide()
                if object.objectName() == "am_gomb":
                    self.level = 12
                    self.initLevel12()
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.akkordok_gomb.hide()
                    self.dalok_gomb.hide()
                if object.objectName() == "dm_gomb":
                    self.level = 13
                    self.initLevel13()
                    
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.akkordok_gomb.hide()
                    self.dalok_gomb.hide()
                if object.objectName() == "c_gomb":
                    self.level = 14
                    self.initLevel14()
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.akkordok_gomb.hide()
                    self.dalok_gomb.hide()
                if object.objectName() == "e_gomb":
                    self.level = 15
                    self.initLevel15()
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.akkordok_gomb.hide()
                    self.dalok_gomb.hide()
                if object.objectName() == "a_gomb":
                    self.level = 16
                    self.initLevel16()
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.akkordok_gomb.hide()
                    self.dalok_gomb.hide()
                if object.objectName() == "d_gomb":
                    self.level = 17
                    self.initLevel17()
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.akkordok_gomb.hide()
                    self.dalok_gomb.hide()
                if object.objectName() == "g_gomb":
                    self.level = 18
                    self.initLevel18()
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.akkordok_gomb.hide()
                    self.dalok_gomb.hide()
                if object.objectName() == "vissza_gomb":
                    self.felsoLabel.hide()
                    self.vissza_gomb.hide()
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.kezdo_gomb.show()
                    self.kozepes_gomb.show()
                    self.halado_gomb.show()
                    for i in reversed(range(self.layout.count())): 
                        self.layout.itemAt(i).widget().setParent(None)
                    self.level = 0
                return True         
        
        if self.level == 2: 
            self.em_gomb.hide()
            self.am_gomb.hide()
            self.dm_gomb.hide()
            self.c_gomb.hide()  
            self.a_gomb.hide()
            self.e_gomb.hide()
            self.g_gomb.hide()
            self.d_gomb.hide()
            self.akkordok_gomb.show()
            self.dalok_gomb.show()
            self.lbl_akkord.setText(str(""))
            self.lbl_dal.setText(str(""))
            
            
            if event.type() == QEvent.MouseButtonPress:
                if object.objectName() == "akkordok_gomb":
                    self.level = 21
                    self.initLevel21()
                    self.akkordok_gomb.hide() 
                    self.dalok_gomb.hide()
                    
                if object.objectName() == "dalok_gomb":
                    self.level = 22
                    self.initLevel22()
                    self.akkordok_gomb.hide() 
                    self.dalok_gomb.hide()
                    
                if object.objectName() == "vissza_gomb":
                    self.felsoLabel.hide()
                    self.vissza_gomb.hide()
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.akkordok_gomb.hide()
                    self.dalok_gomb.hide()
                    self.kezdo_gomb.show()
                    self.kozepes_gomb.show()
                    self.halado_gomb.show()
                    for i in reversed(range(self.layout.count())): 
                        self.layout.itemAt(i).widget().setParent(None)
                    self.level = 0
                return True 

        if self.level == 3: 
            self.em_gomb.hide()
            self.am_gomb.hide()
            self.dm_gomb.hide()
            self.c_gomb.hide()  
            self.a_gomb.hide()
            self.e_gomb.hide()
            self.g_gomb.hide()
            self.d_gomb.hide()
            self.akkordok_gomb.show()
            self.dalok_gomb.show()

            self.lbl_akkord2.setText(str(""))
            self.lbl_dal2.setText(str(""))

            if event.type() == QEvent.MouseButtonPress:
                if object.objectName() == "akkordok_gomb":
                    self.level = 31
                    self.initLevel31()
                    self.akkordok_gomb.hide() 
                    self.dalok_gomb.hide()
                if object.objectName() == "dalok_gomb":
                    self.level = 32
                    self.initLevel32()
                    self.akkordok_gomb.hide() 
                    self.dalok_gomb.hide()
                if object.objectName() == "vissza_gomb":
                    self.felsoLabel.hide()
                    self.vissza_gomb.hide()
                    self.em_gomb.hide() 
                    self.am_gomb.hide()
                    self.dm_gomb.hide() 
                    self.c_gomb.hide() 
                    self.e_gomb.hide()
                    self.a_gomb.hide()
                    self.g_gomb.hide()
                    self.d_gomb.hide()
                    self.akkordok_gomb.hide()
                    self.dalok_gomb.hide()
                    self.kezdo_gomb.show()
                    self.kozepes_gomb.show()
                    self.halado_gomb.show()
                    for i in reversed(range(self.layout.count())): 
                        self.layout.itemAt(i).widget().setParent(None)
                    self.level = 0
                return True 


        if (self.level == 1 or self.level == 2 or self.level == 3) and event.type() == QEvent.MouseButtonPress and object.objectName() == "vissza_gomb":
            print("hello")
            self.felsoLabel.hide()
            self.vissza_gomb.hide()
            self.em_gomb.hide() 
            self.am_gomb.hide()
            self.dm_gomb.hide() 
            self.c_gomb.hide() 
            self.e_gomb.hide()
            self.a_gomb.hide()
            self.g_gomb.hide()
            self.d_gomb.hide()
            self.kezdo_gomb.show()
            self.kozepes_gomb.show()
            self.halado_gomb.show()
            self.level = 0

        if (self.level == 11 or self.level == 12 or self.level == 13 or self.level == 14 or self.level == 15 or self.level == 16 or self.level == 17 or self.level == 18) and event.type() == QEvent.MouseButtonPress and object.objectName() == "vissza_gomb":
            #self.layout.clear()
            self.felsoLabel2.hide()
            self.em_gomb.show() 
            self.am_gomb.show()
            self.dm_gomb.show() 
            self.c_gomb.show() 
            self.e_gomb.show()
            self.a_gomb.show()
            self.g_gomb.show()
            self.d_gomb.show()
            # if len(szerverek) != 0:
            #      kuldKikapcs(szerverek[0]['ip'])
            self.level = 1
            
            

        if (self.level == 21 or self.level == 22) and event.type() == QEvent.MouseButtonPress and object.objectName() == "vissza_gomb":
    
            self.felsoLabel2.hide()
            self.akkordok_gomb.show() 
            self.dalok_gomb.show()
            self.combo_akkord.hide()
            self.lbl_akkord.hide()
            self.combo_dal.hide()
            self.lbl_dal.hide()
            self.combo_akkord2.hide()
            self.lbl_akkord2.hide()
            self.combo_dal2.hide()
            self.lbl_dal2.hide()
            # if len(szerverek) != 0:
            #     kuldKikapcs(szerverek[0]['ip'])
            self.level = 2

        if (self.level == 31 or self.level == 32) and event.type() == QEvent.MouseButtonPress and object.objectName() == "vissza_gomb":
            self.felsoLabel2.hide()
            self.akkordok_gomb.show() 
            self.dalok_gomb.show()
            self.combo_akkord.hide()
            self.lbl_akkord.hide()
            self.combo_dal.hide()
            self.lbl_dal.hide()
            self.combo_akkord2.hide()
            self.lbl_akkord2.hide()
            self.combo_dal2.hide()
            self.lbl_dal2.hide()
            # if len(szerverek) != 0:
            #     kuldKikapcs(szerverek[0]['ip'])
            self.level = 3

        return False


    def initLevel1(self):
        self.felsoLabel = QLabel("Kezdő szint", self)
        self.felsoLabel.move(0, 0)
        self.felsoLabel.setAlignment(Qt.AlignCenter)
        self.felsoLabel.setStyleSheet('''
            QLabel
                {
                    font-size: 30pt;
                    text-align: center;
                    font-family: "Arial";
                    border-radius: 100px;
                    margin-top: 10px;
                    color: rgba(50, 50, 50);

                }

        ''')
        
        self.layout.addWidget(self.felsoLabel)
        if len(szerverek) != 0:
                 kuldKikapcs(szerverek[0]['ip'])


    def initLevel2(self):
        self.felsoLabel = QLabel("Közepes szint", self)

        self.felsoLabel.resize(QSize(1920, 360))
        self.felsoLabel.move(0, 0)
        self.felsoLabel.setAlignment(Qt.AlignCenter)
        self.felsoLabel.setStyleSheet('''
            QLabel
                {
                    font-size: 30pt;
                    text-align: center;
                    font-family: "Arial";
                    border-radius: 100px;
                    margin: 0px;
                    color: rgba(50, 50, 50);

                }

        ''')

        self.layout.addWidget(self.felsoLabel)
        # if len(szerverek) != 0:
        #          kuldNemMukodik(szerverek[0]['ip'])

    def initLevel3(self):
        self.felsoLabel = QLabel("Haladó szint", self)

        self.felsoLabel.resize(QSize(1920, 360))
        self.felsoLabel.move(0, 0)
        self.felsoLabel.setAlignment(Qt.AlignCenter)
        self.felsoLabel.setStyleSheet('''
            QLabel
                {
                    font-size: 30pt;
                    text-align: center;
                    font-family: "Arial";
                    border-radius: 100px;
                    margin: 0px;
                    color: rgba(50, 50, 50);

                }

        ''')

        self.layout.addWidget(self.felsoLabel)

    def initLevel11(self):
        self.felsoLabel2 = QLabel("Em", self)
        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 100pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 300px;

                }

        ''')
          
        self.layout.addWidget(self.felsoLabel2)
        if len(szerverek) != 0:
            kuldAkkord(szerverek[0]['ip'], "em")
        

    def initLevel12(self):
        self.felsoLabel2 = QLabel("Am", self)
        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 100pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 300px;

                }

        ''')
        
        
        self.layout.addWidget(self.felsoLabel2)

        if len(szerverek) != 0:
            kuldAkkord(szerverek[0]['ip'], "am")

    def initLevel13(self):
        self.felsoLabel2 = QLabel("Dm", self)
        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 100pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 300px;

                }

        ''')
        
        
        self.layout.addWidget(self.felsoLabel2)
        if len(szerverek) != 0:
            kuldAkkord(szerverek[0]['ip'], "dm")
        
    def initLevel14(self):
        self.felsoLabel2 = QLabel("C", self)
        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 100pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 300px;

                }

        ''')
        
        
        self.layout.addWidget(self.felsoLabel2)
        if len(szerverek) != 0:
            kuldAkkord(szerverek[0]['ip'], "c")
        
    def initLevel15(self):
        self.felsoLabel2 = QLabel("E", self)
        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 100pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 300px;

                }

        ''')
        
        
        self.layout.addWidget(self.felsoLabel2)
        if len(szerverek) != 0:
            kuldAkkord(szerverek[0]['ip'], "e")
        
    def initLevel16(self):
        self.felsoLabel2 = QLabel("A", self)
        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 100pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 300px;

                }

        ''')
        
        
        self.layout.addWidget(self.felsoLabel2)
        if len(szerverek) != 0:
            kuldAkkord(szerverek[0]['ip'], "a")
        
    def initLevel17(self):
        self.felsoLabel2 = QLabel("D", self)
        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 100pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 300px;

                }

        ''')
        
        
        self.layout.addWidget(self.felsoLabel2)
        if len(szerverek) != 0:
            kuldAkkord(szerverek[0]['ip'], "d")
        
        
    def initLevel18(self):
        self.felsoLabel2 = QLabel("G", self)
        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 100pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 300px;

                }

        ''')
        self.layout.addWidget(self.felsoLabel2)
        if len(szerverek) != 0:
            kuldAkkord(szerverek[0]['ip'], "g")
        
        
    def initLevel21(self):
        self.felsoLabel2 = QLabel("Akkordok", self)

        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 50pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 0px;

                }

        ''')
        self.layout.addWidget(self.felsoLabel2)
        self.combo_akkord.show()
        self.lbl_akkord.show()
        self.combo_akkord.activated.connect(self.handleActivated)
        print(self.combo_akkord.activated.connect(self.handleActivated))
        # if len(szerverek) != 0:
        #          kuldMukodik(szerverek[0]['ip'])
        
    def initLevel22(self):
        self.felsoLabel2 = QLabel("Dalok", self)

        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 50pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 0px;

                }

        ''')
        self.layout.addWidget(self.felsoLabel2)

        self.combo_dal.show()
        self.lbl_dal.show()

    def initLevel31(self):
        self.felsoLabel2 = QLabel("Akkordok", self)

        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 50pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 0px;

                }

        ''')
        self.layout.addWidget(self.felsoLabel2)
        self.combo_akkord2.show()
        self.lbl_akkord2.show()

    def initLevel32(self):
        self.felsoLabel2 = QLabel("Dalok", self)

        self.felsoLabel2.move(0, 0)
        self.felsoLabel2.setAlignment(Qt.AlignCenter)
        self.felsoLabel2.setStyleSheet('''
            QLabel
                {
                    font-size: 50pt;
                    text-align: center;
                    font-family: "Arial";
                    margin-top: 0px;

                }

        ''')
        self.layout.addWidget(self.felsoLabel2)

        self.combo_dal2.show()
        self.lbl_dal2.show()
        
if __name__ == '__main__':
    probalkozasok = 0
    while len(szerverek) == 0:
        szerverek = keresFutoSzerver()
        probalkozasok += 1
        if probalkozasok > 10:
            break
    print(szerverek)
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())