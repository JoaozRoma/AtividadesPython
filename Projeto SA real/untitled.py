


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 791)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Tela login/IMG/LOGIN (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TOPBAR = QtWidgets.QFrame(self.centralwidget)
        self.TOPBAR.setMaximumSize(QtCore.QSize(16777215, 35))
        self.TOPBAR.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.TOPBAR.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TOPBAR.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TOPBAR.setObjectName("TOPBAR")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.TOPBAR)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Frameerro = QtWidgets.QFrame(self.TOPBAR)
        self.Frameerro.setMaximumSize(QtCore.QSize(450, 16777215))
        self.Frameerro.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius: 8px;\n"
"")
        self.Frameerro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frameerro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frameerro.setObjectName("Frameerro")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Frameerro)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Erro = QtWidgets.QLabel(self.Frameerro)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Erro.setFont(font)
        self.Erro.setStyleSheet("color: rgb(255, 255, 255);")
        self.Erro.setScaledContents(False)
        self.Erro.setAlignment(QtCore.Qt.AlignCenter)
        self.Erro.setObjectName("Erro")
        self.horizontalLayout_3.addWidget(self.Erro)
        self.ClosePopUp = QtWidgets.QPushButton(self.Frameerro)
        self.ClosePopUp.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ClosePopUp.setFont(font)
        self.ClosePopUp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ClosePopUp.setStyleSheet("QPushButton { \n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.ClosePopUp.setObjectName("ClosePopUp")
        self.horizontalLayout_3.addWidget(self.ClosePopUp)
        self.horizontalLayout_2.addWidget(self.Frameerro)
        self.verticalLayout.addWidget(self.TOPBAR)
        self.CONTEUDO = QtWidgets.QFrame(self.centralwidget)
        self.CONTEUDO.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.CONTEUDO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CONTEUDO.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CONTEUDO.setObjectName("CONTEUDO")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.CONTEUDO)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LOGINAREA = QtWidgets.QFrame(self.CONTEUDO)
        self.LOGINAREA.setMaximumSize(QtCore.QSize(450, 550))
        self.LOGINAREA.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.LOGINAREA.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LOGINAREA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LOGINAREA.setObjectName("LOGINAREA")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.LOGINAREA)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.LOGINAREA)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius:  5px; \n"
"border: 5px solid rgb(255, 213, 0);\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(120, 30, 191, 171))
        self.frame_2.setStyleSheet("background-image: url(:/Tela login/IMG/LOGIN (2).png);\n"
"background-repeat: no repeat;\n"
"background-position: center;\n"
"border: solid rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(85, 250, 280, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 213, 0);\n"
"border-radius: 5px;\n"
"padding: 15px;\n"
"background-color rgb(255, 213, 0);\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(255, 213, 0);\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(255, 213, 0);\n"
"    color: rgb(211, 211, 211);\n"
"}")
        self.lineEdit.setMaxLength(32)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(85, 320, 280, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 213, 0);\n"
"border-radius: 5px;\n"
"padding: 15px;\n"
"background-color rgb(255, 213, 0);\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(255, 213, 0);\n"
"\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(255, 213, 0);\n"
"    color: rgb(211, 211, 211);\n"
"}")
        self.lineEdit_2.setMaxLength(32)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(85, 390, 280, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(246, 199, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 8px solid rgb(255, 213, 0);\n"
"}\n"
"QPushbutton:pressed {\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.LOGINAREA)
        self.verticalLayout.addWidget(self.CONTEUDO)
        self.BOTAO = QtWidgets.QFrame(self.centralwidget)
        self.BOTAO.setMaximumSize(QtCore.QSize(16777215, 35))
        self.BOTAO.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.BOTAO.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BOTAO.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BOTAO.setObjectName("BOTAO")
        self.verticalLayout.addWidget(self.BOTAO)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movies Warehouse"))
        self.Erro.setText(_translate("MainWindow", "Login Invalido"))
        self.ClosePopUp.setText(_translate("MainWindow", "X"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Digite seu login"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Digite sua senha"))
        self.pushButton_2.setText(_translate("MainWindow", "Entrar"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
