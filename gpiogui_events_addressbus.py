import sys
import shutil,os
import subprocess

from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton,QLineEdit,QComboBox,QMessageBox,QLabel,QFileDialog,QPlainTextEdit,QProgressBar,QLCDNumber,QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from address_data_check import Ui_Dialog
from functools import partial


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QSize, QRect
from pathlib import Path
from clnetwork import *
from threading import *

from ledwidget import LedWidget

#from ledcontrol import setLED

class Logic (QDialog):
   _folder =''
   checkbox_dict={"":""}
   onClickCheckBox = pyqtSignal()

   def __init__(self):
           super(QDialog,self).__init__()
           self.ui = Ui_Dialog()
           self.ui.setupUi(self)
           self.show()
           self.btnConnect = self.findChild(QPushButton,"btnConnect")
           self.btnSend=self.findChild(QPushButton,"btnSend")
           self.btnRead=self.findChild(QPushButton,"btnRead")
           self.find_chkboxes() #init chkboxes so that referencing them is easier
           self.find_led()
           self.checkbox_dict = self.init_chkboxdict()
           self.led_dict = self.init_led()
           self.init_events(self.led_dict)
           #for i in range(len(self.checkbox_dict)):
           #  self.checkbox = self.checkbox_dict[i]
           #  self.checkbox.clicked.connect(self.on_clickCheckBox)
           self.chkSelectAddress = self.findChild(QCheckBox,"chkSelectbank1")
           self.chkSelectAddress.clicked.connect(partial(self.on_click_selectAllCheckbox,self.checkbox_dict,self.led_dict))
           self.nw=''
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
         nw.senddata(intdata)

   def on_click_read(self):
         recvdata = self.findChild(QPlainTextEdit,"txtRead")
         nw.receive(recvdata)

   def setledcontrol(self):
       #print(type(dir(self.ui)[19]))
       for eachitem in dir(self.ui):
          if "led"  in eachitem:
             item  = self.findChild(LedWidget,eachitem)
             item.setDiameter(16.0)
             item.setColor(QtGui.QColor("Gray"))

   def  init_chkboxdict(self):
      return {0:self.chkbox_A0,1:self.chkbox_A1,2:self.chkbox_A2,3:self.chkbox_A3,4:self.chkbox_A4,5:self.chkbox_A5,
              6:self.chkbox_A6,7:self.chkbox_A7,8:self.chkbox_A8,9:self.chkbox_A9,10:self.chkbox_A10,11:self.chkbox_A11,
              12:self.chkbox_A12,13:self.chkbox_A13,14:self.chkbox_A14,15:self.chkbox_A15,}
   def  init_led(self):
      return {1:self.led1,2:self.led2,3:self.led3,4:self.led4,5:self.led5,6:self.led6,
              7:self.led7,8:self.led8,9:self.led9,10:self.led10,11:self.led11,12:self.led12,
              13:self.led13,14:self.led14,15:self.led15,16:self.led16,}
   def find_chkboxes(self):
      self.chkbox_A0 = self.findChild(QCheckBox ,"chkA0")
      self.chkbox_A1 = self.findChild(QCheckBox ,"chkA1")
      self.chkbox_A2= self.findChild(QCheckBox ,"chkA2")
      self.chkbox_A3= self.findChild(QCheckBox ,"chkA3")
      self.chkbox_A4 = self.findChild(QCheckBox ,"chkA4")
      self.chkbox_A5= self.findChild(QCheckBox ,"chkA5")
      self.chkbox_A6= self.findChild(QCheckBox ,"chkA6")
      self.chkbox_A7 = self.findChild(QCheckBox ,"chkA7")
      self.chkbox_A8 = self.findChild(QCheckBox ,"chkA8")
      self.chkbox_A9= self.findChild(QCheckBox ,"chkA9")
      self.chkbox_A10 = self.findChild(QCheckBox ,"chkA10")
      self.chkbox_A11 = self.findChild(QCheckBox ,"chkA11")
      self.chkbox_A12 = self.findChild(QCheckBox ,"chkA12")
      self.chkbox_A13 = self.findChild(QCheckBox ,"chkA13")
      self.chkbox_A14 = self.findChild(QCheckBox ,"chkA14")
      self.chkbox_A15 = self.findChild(QCheckBox ,"chkA15")
   def find_led(self):
      self.led1 = self.findChild(LedWidget ,"led1")
      self.led2= self.findChild(LedWidget ,"led2")
      self.led3= self.findChild(LedWidget ,"led3")
      self.led4 = self.findChild(LedWidget ,"led4")
      self.led5= self.findChild(LedWidget ,"led5")
      self.led6= self.findChild(LedWidget ,"led6")
      self.led7 = self.findChild(LedWidget ,"led7")
      self.led8 = self.findChild(LedWidget ,"led8")
      self.led9= self.findChild(LedWidget ,"led9")
      self.led10 = self.findChild(LedWidget ,"led10")
      self.led11 = self.findChild(LedWidget ,"led11")
      self.led12 = self.findChild(LedWidget ,"led12")
      self.led13 = self.findChild(LedWidget ,"led13")
      self.led14 = self.findChild(LedWidget ,"led14")
      self.led15 = self.findChild(LedWidget ,"led15")
      self.led16 = self.findChild(LedWidget ,"led16")

   #@pyqtSlot(object)
   def on_click_selectAllCheckbox(self,checkbox_dict,led_dict):
      #checkbox_dict = self.init_chkboxdict() #create a dictionary of checkboxes
      if (self.chkSelectAddress.isChecked()):
        for i in range(len(checkbox_dict)):
         checkbox = checkbox_dict[i]
         checkbox.setChecked(True)
         led_dict[i+1].setColor(QtGui.QColor("Green"))
      else:
        for i in range(len(checkbox_dict)):
         checkbox = checkbox_dict[i]
         checkbox.setChecked(False)
         led_dict[i+1].setColor(QtGui.QColor("Gray"))

   def on_clickCheckBox(self,val,led_dict):
       chkbox  = self.sender()
       if chkbox.isChecked():
        led_dict[int(val)+1].setColor(QtGui.QColor("Green"))
       else:
        led_dict[int(val)+1].setColor(QtGui.QColor("Gray"))
       #print("checkbox %d is clicked" %(int(chkbox.text())))
       print("checkbox %d is clicked" %(int(val)))

   def  init_events(self,led_dict):
      self.chkbox_A0.clicked.connect(partial(self.on_clickCheckBox,"0",led_dict))
      self.chkbox_A1.clicked.connect(partial(self.on_clickCheckBox,"1",led_dict))
      self.chkbox_A2.clicked.connect(partial(self.on_clickCheckBox,"2",led_dict))
      self.chkbox_A3.clicked.connect(partial(self.on_clickCheckBox,"3",led_dict))
      self.chkbox_A4.clicked.connect(partial(self.on_clickCheckBox,"4",led_dict))
      self.chkbox_A5.clicked.connect(partial(self.on_clickCheckBox,"5",led_dict))
      self.chkbox_A6.clicked.connect(partial(self.on_clickCheckBox,"6",led_dict))
      self.chkbox_A7.clicked.connect(partial(self.on_clickCheckBox,"7",led_dict))
      self.chkbox_A8.clicked.connect(partial(self.on_clickCheckBox,"8",led_dict))
      self.chkbox_A9.clicked.connect(partial(self.on_clickCheckBox,"9",led_dict))
      self.chkbox_A10.clicked.connect(partial(self.on_clickCheckBox,"10",led_dict))
      self.chkbox_A11.clicked.connect(partial(self.on_clickCheckBox,"11",led_dict))
      self.chkbox_A12.clicked.connect(partial(self.on_clickCheckBox,"12",led_dict))
      self.chkbox_A13.clicked.connect(partial(self.on_clickCheckBox,"13",led_dict))
      self.chkbox_A14.clicked.connect(partial(self.on_clickCheckBox,"14",led_dict))
      self.chkbox_A15.clicked.connect(partial(self.on_clickCheckBox,"15",led_dict))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Logic()
    sys.exit(app.exec_())
