import sys
import shutil,os
import subprocess

from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton,QLineEdit,QComboBox,QMessageBox,QLabel,QFileDialog,QPlainTextEdit,QProgressBar,QLCDNumber,QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from gpio_gui_thrc import Ui_Dialog

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QSize, QRect
from pathlib import Path
from clnetwork import *
from threading import * 

from ledwidget import LedWidget

#from ledcontrol import setLED

class Logic (QDialog):
   _folder =''

   def __init__(self):
           super(QDialog,self).__init__()
           self.ui = Ui_Dialog()
           self.ui.setupUi(self)
           self.show()
           self.btnConnect = self.findChild(QPushButton,"btnConnect")
           self.btnSend=self.findChild(QPushButton,"btnSend")
           self.btnRead=self.findChild(QPushButton,"btnRead")
           #self.btnConnect.clicked.connect(self.on_click_connect)
           #self.btnSend.clicked.connect(self.on_click_send)
           #self.btnRead.clicked.connect(self.on_click_read)
           self.nw=''
           #setled = setLED()
           #setled.set(self.ui)
           self.setledcontrol()
   @pyqtSlot()

   def on_click_connect(self):
         IP = self.findChild(QPlainTextEdit,"txtIP")
         PORT= self.findChild(QPlainTextEdit,"txtPORT")
         print(" %s" %(IP.toPlainText()))
         nw  = network(IP.toPlainText(),int(PORT.toPlainText()),1024)
         nw.connectoport()
         #nw.run()
         return nw

   def on_click_send(self):
         IP = self.findChild(QPlainTextEdit,"txtIP")
         PORT= self.findChild(QPlainTextEdit,"txtPORT")
         senddata = self.findChild(QPlainTextEdit,"txtSend")
         if(senddata.toPlainText()[1:2] =='b' or senddata.toPlainText()[1:2] =='B'):
            intdata = hex(int(senddata.toPlainText()[2:],2))
         else:
            if(senddata.toPlainText()[1:2] =='x'  or senddata.toPlainText()[1:2] == 'X'):
                #intdata = hex(int(senddata.toPlainText(),16))
                intdata= senddata.toPlainText()
            else:
                intdata= senddata.toPlainText()

         print(intdata)
         nw  = network(IP.toPlainText(),int(PORT.toPlainText()),1024)
         nw.connectoport()
         #nw.run()
         #nw.senddata(senddata.toPlainText())
         nw.senddata(intdata)

   def on_click_read(self):
         recvdata = self.findChild(QPlainTextEdit,"txtRead")
         nw.receive(recvdata)
   def setledcontrol(self):
       print(type(dir(self.ui)[19]))
       for eachitem in dir(self.ui):
          if "led"  in eachitem:
             item  = self.findChild(LedWidget,eachitem)
             item.setDiameter(16.0)
             item.setColor(QtGui.QColor("Gray"))
          
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Logic()
    sys.exit(app.exec_())
