# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1440, 779)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 10, 481, 761))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: #ced4da;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.textEditScanItem = QtWidgets.QTextEdit(self.frame)
        self.textEditScanItem.setGeometry(QtCore.QRect(10, 20, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEditScanItem.setFont(font)
        self.textEditScanItem.setStyleSheet("QTextEdit{\n"
"background-color: #ffffff;\n"
" color: #22223b;\n"
"border-radius: 25px;\n"
"}")
        self.textEditScanItem.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.textEditScanItem.setObjectName("textEditScanItem")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 461, 391))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget{\n"
"background-color: #ffffff;\n"
"color: #0b090a;\n"
"}")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 470, 461, 131))
        self.frame_3.setStyleSheet("QFrame {\n"
"background-color: #ffffff;\n"
"color: black;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(130, 10, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(130, 30, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(130, 50, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(130, 70, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(130, 90, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 610, 461, 81))
        self.frame_4.setStyleSheet("QFrame {\n"
"background-color: #ffffff;\n"
"color: black;\n"
"\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setGeometry(QtCore.QRect(10, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_4)
        self.label_23.setGeometry(QtCore.QRect(110, 10, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_4)
        self.label_24.setGeometry(QtCore.QRect(110, 40, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame)
        self.pushButton_22.setGeometry(QtCore.QRect(10, 700, 91, 51))
        self.pushButton_22.setStyleSheet("background-color:gray;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_37 = QtWidgets.QPushButton(self.frame)
        self.pushButton_37.setGeometry(QtCore.QRect(120, 700, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("QPushButton {\n"
"    background-color:#9b2226;\n"
"}")
        self.pushButton_37.setObjectName("pushButton_37")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(570, 60, 821, 381))
        self.frame_2.setStyleSheet("background-color: white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 131, 101))
        self.pushButton.setStyleSheet("background-color:gray;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 20, 131, 101))
        self.pushButton_2.setStyleSheet("background-color:gray;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 20, 131, 101))
        self.pushButton_3.setStyleSheet("background-color:gray;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 20, 131, 101))
        self.pushButton_4.setStyleSheet("background-color:gray;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 20, 131, 101))
        self.pushButton_5.setStyleSheet("background-color:gray;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 140, 131, 101))
        self.pushButton_6.setStyleSheet("background-color:gray;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 140, 131, 101))
        self.pushButton_7.setStyleSheet("background-color:gray;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(320, 140, 131, 101))
        self.pushButton_8.setStyleSheet("background-color:gray;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(470, 140, 131, 101))
        self.pushButton_9.setStyleSheet("background-color:gray;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(620, 140, 131, 101))
        self.pushButton_10.setStyleSheet("background-color:gray;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 260, 131, 101))
        self.pushButton_11.setStyleSheet("background-color:gray;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setGeometry(QtCore.QRect(170, 260, 131, 101))
        self.pushButton_12.setStyleSheet("background-color:gray;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setGeometry(QtCore.QRect(320, 260, 131, 101))
        self.pushButton_13.setStyleSheet("background-color:gray;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_14.setGeometry(QtCore.QRect(470, 260, 131, 101))
        self.pushButton_14.setStyleSheet("background-color:gray;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_15.setGeometry(QtCore.QRect(620, 260, 131, 101))
        self.pushButton_15.setStyleSheet("background-color:gray;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(570, 470, 511, 301))
        self.frame_5.setStyleSheet("QFrame {\n"
"background-color: #ffffff;\n"
"color: black;\n"
"\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 190, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color:gray;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 100, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color:gray;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 10, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color:gray;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_24.setGeometry(QtCore.QRect(150, 10, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("background-color:gray;")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_25.setGeometry(QtCore.QRect(230, 10, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("background-color:gray;")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_26.setGeometry(QtCore.QRect(310, 10, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("background-color:gray;")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_27.setGeometry(QtCore.QRect(150, 70, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("background-color:gray;")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_28.setGeometry(QtCore.QRect(230, 70, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("background-color:gray;")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_29.setGeometry(QtCore.QRect(310, 70, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("background-color:gray;")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_30.setGeometry(QtCore.QRect(150, 130, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("background-color:gray;")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_31.setGeometry(QtCore.QRect(230, 130, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("background-color:gray;")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_32.setGeometry(QtCore.QRect(310, 130, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("background-color:gray;")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_33.setGeometry(QtCore.QRect(150, 190, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("background-color:gray;")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_34.setGeometry(QtCore.QRect(230, 190, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("background-color:gray;")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_35.setGeometry(QtCore.QRect(310, 190, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("background-color:gray;")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_19.setGeometry(QtCore.QRect(400, 10, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color:gray;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_20.setGeometry(QtCore.QRect(400, 80, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background-color:gray;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_21.setGeometry(QtCore.QRect(400, 150, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("background-color:gray;")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_23.setGeometry(QtCore.QRect(400, 220, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("background-color:gray;")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_36 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_36.setGeometry(QtCore.QRect(150, 250, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("background-color:gray;")
        self.pushButton_36.setObjectName("pushButton_36")
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(1110, 470, 281, 291))
        self.frame_6.setStyleSheet("QFrame {\n"
"background-color: #ffffff;\n"
"color: black;\n"
"\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(580, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_25.setFont(font)
        self.label_25.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_25.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(780, 20, 181, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(990, 20, 181, 16))
        self.label_27.setObjectName("label_27")
        self.pushButton_38 = QtWidgets.QPushButton(Form)
        self.pushButton_38.setGeometry(QtCore.QRect(1330, 10, 91, 41))
        self.pushButton_38.setStyleSheet("background-color:gray;")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(Form)
        self.pushButton_39.setGeometry(QtCore.QRect(1220, 10, 91, 41))
        self.pushButton_39.setStyleSheet("background-color:gray;")
        self.pushButton_39.setObjectName("pushButton_39")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEditScanItem.setPlaceholderText(_translate("Form", "Scan Items here"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(6)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(7)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(8)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(9)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(10)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(11)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        item = self.listWidget.item(12)
        item.setText(_translate("Form", "New Item       @qty 1          $4.99"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "Sub Total"))
        self.label_2.setText(_translate("Form", "Tax"))
        self.label_3.setText(_translate("Form", "Discount"))
        self.label_4.setText(_translate("Form", "Promotion"))
        self.label_5.setText(_translate("Form", "Total"))
        self.label_6.setText(_translate("Form", "$299.47"))
        self.label_7.setText(_translate("Form", "$20"))
        self.label_8.setText(_translate("Form", "$40"))
        self.label_9.setText(_translate("Form", "Not Applicable"))
        self.label_10.setText(_translate("Form", "$279.47"))
        self.label_21.setText(_translate("Form", "Paid"))
        self.label_22.setText(_translate("Form", "Change"))
        self.label_23.setText(_translate("Form", "$300"))
        self.label_24.setText(_translate("Form", "$20.53"))
        self.pushButton_22.setText(_translate("Form", "Hold"))
        self.pushButton_37.setText(_translate("Form", "Cancel"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.pushButton_5.setText(_translate("Form", "PushButton"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))
        self.pushButton_7.setText(_translate("Form", "PushButton"))
        self.pushButton_8.setText(_translate("Form", "PushButton"))
        self.pushButton_9.setText(_translate("Form", "PushButton"))
        self.pushButton_10.setText(_translate("Form", "PushButton"))
        self.pushButton_11.setText(_translate("Form", "PushButton"))
        self.pushButton_12.setText(_translate("Form", "PushButton"))
        self.pushButton_13.setText(_translate("Form", "PushButton"))
        self.pushButton_14.setText(_translate("Form", "PushButton"))
        self.pushButton_15.setText(_translate("Form", "PushButton"))
        self.pushButton_16.setText(_translate("Form", "Cash"))
        self.pushButton_17.setText(_translate("Form", "Card"))
        self.pushButton_18.setText(_translate("Form", "EBT"))
        self.pushButton_24.setText(_translate("Form", "7"))
        self.pushButton_25.setText(_translate("Form", "8"))
        self.pushButton_26.setText(_translate("Form", "9"))
        self.pushButton_27.setText(_translate("Form", "4"))
        self.pushButton_28.setText(_translate("Form", "5"))
        self.pushButton_29.setText(_translate("Form", "6"))
        self.pushButton_30.setText(_translate("Form", "1"))
        self.pushButton_31.setText(_translate("Form", "2"))
        self.pushButton_32.setText(_translate("Form", "3"))
        self.pushButton_33.setText(_translate("Form", "0"))
        self.pushButton_34.setText(_translate("Form", "00"))
        self.pushButton_35.setText(_translate("Form", "00"))
        self.pushButton_19.setText(_translate("Form", "$50"))
        self.pushButton_20.setText(_translate("Form", "$20"))
        self.pushButton_21.setText(_translate("Form", "$10"))
        self.pushButton_23.setText(_translate("Form", "$5"))
        self.pushButton_36.setText(_translate("Form", "Print Last  Receipt"))
        self.label_25.setText(_translate("Form", "Register No.  1"))
        self.label_26.setText(_translate("Form", "Casier :  Bob Wilsoin"))
        self.label_27.setText(_translate("Form", "Shift:  Morning"))
        self.pushButton_38.setText(_translate("Form", "Logg Out"))
        self.pushButton_39.setText(_translate("Form", "Shift Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())