#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import (
        QtWidgets as qtw,
        # QtCore as qtc,
        )


class ToolBar(qtw.QToolBar):

    def __init__(self, *args, **kwargs):
        super(ToolBar, self).__init__(*args, **kwargs)
        self.actions = {}
        self.actions['save'] = qtw.QAction("save")
        self.actions['save as'] = qtw.QAction("save as")
        self.actions['load'] = qtw.QAction("load")
        self.actions['compare'] = qtw.QAction("compare")
        [self.addAction(x) for x in self.actions.keys()]



if __name__ == '__main__':

    app = qtw.QApplication(sys.argv)
    toolbar = ToolBar()
    toolbar.show()
    app.exec_()

