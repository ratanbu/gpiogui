# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpio_gui_thrc.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ledwidget import LedWidget


class setLED(object):
    #def __init__(self):
    def set(self,ui):
        self.led1 = self.ui.findChild(LedWidget,"led1")
        self.led1.setDiameter(10.0)
        self.led2= self.ui.findChild(LedWidget,"led2")
        self.led2.setDiameter(10.0)
