from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
import sqlite3
from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 358)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(40, 10, 311, 22))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 280, 381, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 220, 111, 20))
        self.label_7.setObjectName("label_7")
        self.coftype = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.coftype.setGeometry(QtCore.QRect(130, 50, 104, 21))
        self.coftype.setObjectName("coftype")
        self.stepobj = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.stepobj.setGeometry(QtCore.QRect(130, 100, 104, 21))
        self.stepobj.setObjectName("stepobj")
        self.ground = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.ground.setGeometry(QtCore.QRect(130, 130, 104, 21))
        self.ground.setObjectName("ground")
        self.flavdiscr = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.flavdiscr.setGeometry(QtCore.QRect(130, 160, 104, 21))
        self.flavdiscr.setObjectName("flavdiscr")
        self.price = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.price.setGeometry(QtCore.QRect(130, 190, 104, 21))
        self.price.setObjectName("price")
        self.obem = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.obem.setGeometry(QtCore.QRect(130, 220, 104, 21))
        self.obem.setObjectName("obem")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.pushButton.setText(
            _translate("MainWindow", "Изменить данные о кофе с данным id или добавить кофе с этим id"))
        self.label_2.setText(_translate("MainWindow", "Сорт:"))
        self.label_3.setText(_translate("MainWindow", "Степень обжарки:"))
        self.label_4.setText(_translate("MainWindow", "Молотый/в зернах:"))
        self.label_5.setText(_translate("MainWindow", "Описание вкуса:"))
        self.label_6.setText(_translate("MainWindow", "Цена:"))
        self.label_7.setText(_translate("MainWindow", "Объем упаковки:"))


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 358)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(70, 10, 311, 22))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 220, 111, 20))
        self.label_7.setObjectName("label_7")
        self.coftype = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.coftype.setGeometry(QtCore.QRect(130, 50, 104, 21))
        self.coftype.setObjectName("coftype")
        self.stepobj = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.stepobj.setGeometry(QtCore.QRect(130, 100, 104, 21))
        self.stepobj.setObjectName("stepobj")
        self.ground = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.ground.setGeometry(QtCore.QRect(130, 130, 104, 21))
        self.ground.setObjectName("ground")
        self.flavdiscr = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.flavdiscr.setGeometry(QtCore.QRect(130, 160, 104, 21))
        self.flavdiscr.setObjectName("flavdiscr")
        self.price = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.price.setGeometry(QtCore.QRect(130, 190, 104, 21))
        self.price.setObjectName("price")
        self.obem = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.obem.setGeometry(QtCore.QRect(130, 220, 104, 21))
        self.obem.setObjectName("obem")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(334, 50, 151, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.pushButton.setText(_translate("MainWindow", "Найти"))
        self.label_2.setText(_translate("MainWindow", "Сорт:"))
        self.label_3.setText(_translate("MainWindow", "Степень обжарки:"))
        self.label_4.setText(_translate("MainWindow", "Молотый/в зернах:"))
        self.label_5.setText(_translate("MainWindow", "Описание вкуса:"))
        self.label_6.setText(_translate("MainWindow", "Цена:"))
        self.label_7.setText(_translate("MainWindow", "Объем упаковки:"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить/редактировать"))


class CoffeeForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.setWindowTitle('Программа Максима Алябьева')

    def run(self):
        self.statusbar.showMessage('')
        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()
        cur.execute("""DELETE FROM Coffee WHERE id = ?""", (self.spinBox.value(),))
        cur.execute(
            """INSERT INTO Coffee(id, NameOfSort, StepenObjarki, ground, description, price, obem) VALUES(?, ?, ?, ?, ?, ?, ?)""",
            (self.spinBox.value(), self.coftype.toPlainText(), self.stepobj.toPlainText(), self.ground.toPlainText(),
             self.flavdiscr.toPlainText(),
             int(self.price.toPlainText()),
             int(self.obem.toPlainText())))
        con.commit()


class Expresso(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.setWindowTitle('Программа Максима Алябьева')
        self.pushButton_2.clicked.connect(self.letitshow)

    def letitshow(self):
        form = CoffeeForm(self)
        form.show()

    def run(self):
        self.statusbar.showMessage('')
        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()
        data = cur.execute("""SELECT NameOfSort, StepenObjarki, ground, description, price, obem FROM Coffee
         WHERE id = ?""", (self.spinBox.value(),)).fetchone()
        if data is None:
            self.statusbar.showMessage('Предмета с таким id нет, попробуйте 1')
        else:
            self.coftype.setText(data[0])
            self.stepobj.setText(data[1])
            self.ground.setText('Молотый')
            self.ground.setText('В зёрнах')
            self.flavdiscr.setText(data[3])
            self.price.setText(str(data[4]))
            self.obem.setText(str(data[5]))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Expresso()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
