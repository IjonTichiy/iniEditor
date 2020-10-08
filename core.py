#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import configparser
from pathlib import Path

from PyQt5 import (
        QtWidgets as qtw,
        # QtCore as qtc,
        )

from iniView import IniView
from toolbar import ToolBar


class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):

        super(MainWindow, self).__init__(*args, **kwargs)
        self.current_file = self.getIniNames()

        self.setWindowTitle("Ini Editor")
        self.initMenu()

        self.docks = []

        self.statusBar()

        self.toolbar = ToolBar()
        self.addToolBar(self.toolbar)

        self.show()

    def initMenu(self):

        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('File')

        fileActions = {
                "New": (qtw.QAction('New', self), self.newFile),
                "Load": (qtw.QAction("Load", self), self.loadFile),
                "Save": (qtw.QAction("Save", self), self.saveFile),
                "Save As": (qtw.QAction("Save As", self), self.saveAsFile),
                "Separator": (None, None),
                "Quit": (qtw.QAction("Quit", self), qtw.qApp.quit),
                }

        for key, (act, fun) in fileActions.items():

            if not act:
                self.fileMenu.addSeparator()
                continue

            act.triggered.connect(fun)
            self.fileMenu.addAction(act)

    def newFile(self):
        pass

    def loadFile(self):
        pass

    def saveFile(self):
        pass

    def saveAsFile(self):
        pass




    def getIniNames(self):
        return qtw.QFileDialog.getOpenFileName()

    def readIni(self, filename):
        config = configparser.configParser(
                comment_prefixes='$$%',
                allow_no_value=True)
        config.read(filename)
        return config


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
