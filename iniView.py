#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import configparser
from PyQt5 import (QtCore as qtc, QtWidgets as qtw)
from PyQt5.QtCore import Qt


class TableModel(qtc.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.sections = data.sections()

        self.selected_section = self.sections[0]
        self.loadData()

    def loadData(self):

        self.selected_data = [(key, value) for key, value in
                              self._data[self.selected_section].items()]

        self.collen = 2
        self.rowlen = len(self._data[self.selected_section])

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # .row() indexes into the outer list,
            # .column() indexes into the (key, value) tuples
            return self.selected_data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self.selected_data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.selected_data[0])


class IniTable(qtw.QTableView):

    def __init__(self, data, *args, **kwargs):
        super(IniTable, self).__init__(*args, **kwargs)
        self.model = TableModel(data)
        self.setModel(self.model)
        self.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)


class IniView(qtw.QWidget):

    def __init__(self, data, *args, **kwargs):
        super(IniView, self).__init__(*args, **kwargs)

        self._data = data

        self.table = IniTable(data)

        self.list = qtw.QListWidget()
        self.list.addItems(self._data.sections())
        self.list.itemSelectionChanged.connect(self.updateSection)

        self.lay = qtw.QGridLayout()

        self.lay.addWidget(self.list, 0, 0)
        self.lay.addWidget(self.table, 0, 1)

        self.setLayout(self.lay)

    def updateSection(self):
        self.table.model.selected_section = self.list.currentItem().text()
        self.table.model.loadData()
        self.table.model.dataChanged.emit(qtc.QModelIndex, qtc.QModelIndex)


if __name__ == '__main__':

    app = qtw.QApplication(sys.argv)
    current_file = qtw.QFileDialog.getOpenFileName()
    config = configparser.ConfigParser()
    config.read(current_file)
    window = IniView(config)
    window.show()
    app.exec_()
