from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame,  QLabel, QScrollBar, QPushButton
import sys

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"MainWindow")
        self.resize(800, 585)
        self.setAcceptDrops(True)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.SetupUI()

        self.colorBool = False
        self.sharpBool = False
        self.resBool = False

        # setting calling method by button
        self.colorize.clicked.connect(self.changeColor)
        self.sharpen.clicked.connect(self.changeColor)
        self.superRes.clicked.connect(self.changeColor)
 
        # setting default color of button to light-grey
        self.colorize.setStyleSheet("background-color : lightgrey")
        self.sharpen.setStyleSheet("background-color : lightgrey")
        self.superRes.setStyleSheet("background-color : lightgrey")
 
        # show all the widgets
        self.update()
        self.show()

    def SetupUI(self):
        #Drag Drop Frame
        self.dragDropFrame = QFrame(self.centralwidget)
        self.dragDropFrame.setObjectName(u"dragDropFrame")
        self.dragDropFrame.setGeometry(QRect(30, 40, 741, 251))
        self.dragDropFrame.setFrameShape(QFrame.StyledPanel)
        self.dragDropFrame.setFrameShadow(QFrame.Raised)
        self.dragDropLabel = QLabel(self.dragDropFrame)
        self.dragDropLabel.setObjectName(u"dragDropLabel")
        self.dragDropLabel.setGeometry(QRect(0, 0, 681, 241))
        self.dragDropLabel.setAlignment(Qt.AlignCenter)
        self.scrollbar = QScrollBar(self.dragDropFrame)
        self.scrollbar.setObjectName(u"scrollbar")
        self.scrollbar.setGeometry(QRect(721, 0, 20, 251))
        self.scrollbar.setOrientation(Qt.Vertical)

        #colorize Toggle Button
        self.colorize = QPushButton(self.centralwidget)
        self.colorize.setObjectName(u"colorize")
        self.colorize.setGeometry(QRect(60, 320, 131, 131))
        self.colorize.setCheckable(True)
        self.colorize.setChecked(False)

        #sharpen Toggle Button
        self.sharpen = QPushButton(self.centralwidget)
        self.sharpen.setObjectName(u"sharpen")
        self.sharpen.setGeometry(QRect(340, 320, 131, 131))
        self.sharpen.setCheckable(True)
        self.sharpen.setChecked(False)

        #superRes Toggle Button
        self.superRes = QPushButton(self.centralwidget)
        self.superRes.setObjectName(u"superRes")
        self.superRes.setGeometry(QRect(620, 320, 131, 131))
        self.superRes.setCheckable(True)
        self.superRes.setChecked(False)

        #compute Button
        self.compute = QPushButton(self.centralwidget)
        self.compute.setObjectName(u"compute")
        self.compute.setGeometry(QRect(250, 500, 321, 61))
        font = QFont()
        font.setPointSize(28)
        self.compute.setFont(font)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    
    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image Restoration", None))
        self.compute.setText(QCoreApplication.translate("MainWindow", u"compute", None))
        self.colorize.setText(QCoreApplication.translate("MainWindow", u"colorize", None))
        self.sharpen.setText(QCoreApplication.translate("MainWindow", u"sharpen", None))
        self.superRes.setText(QCoreApplication.translate("MainWindow", u"Super Resolution", None))
        self.dragDropLabel.setText(QCoreApplication.translate("MainWindow", u"Drag and Drop Images", None))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.dragDropLabel.setHidden(True)
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)
    
    def changeColor(self):
        if self.colorize.isChecked():
            self.colorize.setStyleSheet("background-color : lightblue")
            self.colorBool = True
        else:
            self.colorize.setStyleSheet("background-color : lightgrey")
            self.colorBool = False
        if self.sharpen.isChecked():
            self.sharpen.setStyleSheet("background-color : lightblue")
            self.sharpBool = True
        else:
            self.sharpen.setStyleSheet("background-color : lightgrey")
            self.sharpBool = False
        if self.superRes.isChecked():
            self.superRes.setStyleSheet("background-color : lightblue")
            self.resBool = True
        else:
            self.superRes.setStyleSheet("background-color : lightgrey")
            self.resBool = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWidget()
    ui.show()
    sys.exit(app.exec_())