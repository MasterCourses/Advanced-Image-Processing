# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from math import sqrt, atan2, pi, cos, sin, ceil
from collections import defaultdict
import numpy as np

class Ui_PoolBall(object):
    def setupUi(self, PoolBall):
        PoolBall.setObjectName("PoolBall")
        PoolBall.resize(931, 712)
        font = QtGui.QFont()
        font.setPointSize(20)
        PoolBall.setFont(font)
        self.centralwidget = QtWidgets.QWidget(PoolBall)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(21, 20, 310, 235))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.input_img = QtWidgets.QLabel(self.groupBox)
        self.input_img.setGeometry(QtCore.QRect(5, 30, 300, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_img.sizePolicy().hasHeightForWidth())
        self.input_img.setSizePolicy(sizePolicy)
        self.input_img.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_img.setText("")
        self.input_img.setScaledContents(False)
        self.input_img.setAlignment(QtCore.Qt.AlignCenter)
        self.input_img.setObjectName("input_img")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(341, 20, 310, 235))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.canny_img = QtWidgets.QLabel(self.groupBox_2)
        self.canny_img.setGeometry(QtCore.QRect(5, 30, 300, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canny_img.sizePolicy().hasHeightForWidth())
        self.canny_img.setSizePolicy(sizePolicy)
        self.canny_img.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.canny_img.setText("")
        self.canny_img.setScaledContents(False)
        self.canny_img.setAlignment(QtCore.Qt.AlignCenter)
        self.canny_img.setObjectName("canny_img")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 911, 261))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 280, 911, 421))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.textLogger = QtWidgets.QTextEdit(self.groupBox_9)
        self.textLogger.setEnabled(True)
        self.textLogger.setGeometry(QtCore.QRect(650, 160, 251, 245))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setKerning(True)
        self.textLogger.setFont(font)
        self.textLogger.setAcceptDrops(True)
        self.textLogger.setAutoFillBackground(True)
        self.textLogger.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textLogger.setReadOnly(True)
        self.textLogger.setObjectName("textLogger")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_4.setGeometry(QtCore.QRect(650, 5, 251, 151))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lb_rmax_3 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lb_rmax_3.setFont(font)
        self.lb_rmax_3.setObjectName("lb_rmax_3")
        self.horizontalLayout_6.addWidget(self.lb_rmax_3)
        self.slider_threshold = QtWidgets.QSlider(self.groupBox_4)
        self.slider_threshold.setEnabled(False)
        self.slider_threshold.setMaximum(100)
        self.slider_threshold.setSingleStep(10)
        self.slider_threshold.setProperty("value", 40)
        self.slider_threshold.setOrientation(QtCore.Qt.Horizontal)
        self.slider_threshold.setObjectName("slider_threshold")
        self.horizontalLayout_6.addWidget(self.slider_threshold)
        self.sb_threshold = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.sb_threshold.setEnabled(False)
        self.sb_threshold.setDecimals(2)
        self.sb_threshold.setMaximum(1.0)
        self.sb_threshold.setSingleStep(0.1)
        self.sb_threshold.setProperty("value", 0.4)
        self.sb_threshold.setObjectName("sb_threshold")
        self.horizontalLayout_6.addWidget(self.sb_threshold)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_rmin = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lb_rmin.setFont(font)
        self.lb_rmin.setObjectName("lb_rmin")
        self.horizontalLayout.addWidget(self.lb_rmin)
        self.slider_rmin = QtWidgets.QSlider(self.groupBox_4)
        self.slider_rmin.setEnabled(False)
        self.slider_rmin.setMinimum(1)
        self.slider_rmin.setMaximum(30)
        self.slider_rmin.setProperty("value", 18)
        self.slider_rmin.setOrientation(QtCore.Qt.Horizontal)
        self.slider_rmin.setObjectName("slider_rmin")
        self.horizontalLayout.addWidget(self.slider_rmin)
        self.sb_rmin = QtWidgets.QSpinBox(self.groupBox_4)
        self.sb_rmin.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_rmin.setFont(font)
        self.sb_rmin.setFrame(True)
        self.sb_rmin.setMinimum(1)
        self.sb_rmin.setMaximum(30)
        self.sb_rmin.setProperty("value", 18)
        self.sb_rmin.setObjectName("sb_rmin")
        self.horizontalLayout.addWidget(self.sb_rmin)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_rmax = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lb_rmax.setFont(font)
        self.lb_rmax.setObjectName("lb_rmax")
        self.horizontalLayout_2.addWidget(self.lb_rmax)
        self.slider_rmax = QtWidgets.QSlider(self.groupBox_4)
        self.slider_rmax.setEnabled(False)
        self.slider_rmax.setMinimum(1)
        self.slider_rmax.setMaximum(30)
        self.slider_rmax.setProperty("value", 20)
        self.slider_rmax.setOrientation(QtCore.Qt.Horizontal)
        self.slider_rmax.setObjectName("slider_rmax")
        self.horizontalLayout_2.addWidget(self.slider_rmax)
        self.sb_rmax = QtWidgets.QSpinBox(self.groupBox_4)
        self.sb_rmax.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sb_rmax.setFont(font)
        self.sb_rmax.setFrame(True)
        self.sb_rmax.setMinimum(1)
        self.sb_rmax.setMaximum(30)
        self.sb_rmax.setProperty("value", 20)
        self.sb_rmax.setObjectName("sb_rmax")
        self.horizontalLayout_2.addWidget(self.sb_rmax)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_9)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 5, 630, 405))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.result_img = QtWidgets.QLabel(self.groupBox_3)
        self.result_img.setGeometry(QtCore.QRect(10, 35, 610, 360))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_img.sizePolicy().hasHeightForWidth())
        self.result_img.setSizePolicy(sizePolicy)
        self.result_img.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_img.setText("")
        self.result_img.setScaledContents(False)
        self.result_img.setAlignment(QtCore.Qt.AlignCenter)
        self.result_img.setObjectName("result_img")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(661, 120, 251, 131))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.btn_filter = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_filter.setEnabled(False)
        self.btn_filter.setGeometry(QtCore.QRect(140, 60, 91, 41))
        self.btn_filter.setShortcut("")
        self.btn_filter.setFlat(False)
        self.btn_filter.setObjectName("btn_filter")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget.setGeometry(QtCore.QRect(27, 45, 103, 64))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb_rmin_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lb_rmin_2.setFont(font)
        self.lb_rmin_2.setObjectName("lb_rmin_2")
        self.horizontalLayout_4.addWidget(self.lb_rmin_2)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(255)
        self.spinBox.setSingleStep(5)
        self.spinBox.setProperty("value", 20)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lb_rmax_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lb_rmax_2.setFont(font)
        self.lb_rmax_2.setObjectName("lb_rmax_2")
        self.horizontalLayout_5.addWidget(self.lb_rmax_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setSingleStep(5)
        self.spinBox_2.setProperty("value", 25)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_5.addWidget(self.spinBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(661, 20, 251, 101))
        self.groupBox_6.setMaximumSize(QtCore.QSize(260, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_6)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 40, 191, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_Load = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_Load.setObjectName("btn_Load")
        self.horizontalLayout_3.addWidget(self.btn_Load)
        self.btn_Save = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_Save.setEnabled(False)
        self.btn_Save.setObjectName("btn_Save")
        self.horizontalLayout_3.addWidget(self.btn_Save)
        self.groupBox_7.raise_()
        self.groupBox_6.raise_()
        self.groupBox_5.raise_()
        self.groupBox_9.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        PoolBall.setCentralWidget(self.centralwidget)

        self.retranslateUi(PoolBall)
        QtCore.QMetaObject.connectSlotsByName(PoolBall)

        
        # Bind ui function
        self.btn_Load.clicked.connect(self.loadImage)
        self.btn_Save.clicked.connect(self.saveImage)
        self.btn_filter.clicked.connect(self.filter)
        self.slider_rmin.valueChanged['int'].connect(self.rmin_value)
        self.slider_rmax.valueChanged['int'].connect(self.rmax_value)
        self.slider_threshold.valueChanged['int'].connect(self.threshold_value)
        self.sb_rmin.valueChanged['int'].connect(self.rmin_value)
        self.sb_rmax.valueChanged['int'].connect(self.rmax_value)
        self.sb_threshold.valueChanged['double'].connect(self.threshold_value)

        # Set Global Value
        self.image = ''
        self.output_image = ''
        self.save_image = ''
        self.imgName = ''
        self.keep = []
        self.low_value = 20
        self.high_value = 25
        self.rmin_value_now = 18
        self.rmax_value_now = 20
        self.threshold_value_now = 0.4
        self.logger = False

        # For testing image (optimal par to detect)
        self.testingImg = [
            ['PoolBalls1.jpg'], ['PoolBalls2.jpg'], ['PoolBalls3.jpg'], ['PoolBalls4.jpg'], ['PoolBalls5.jpg'], 
            ['PoolBalls6.jpg'], ['PoolBalls7.jpg'], ['PoolBalls8.jpeg'], ['PoolBalls9.jpg'], ['PoolBalls10.jpg']
        ]
        # ['filename(0)', 'low(1)', 'high(2)', 'min(3)', 'max(4)', 'threshold(5)']
        self.optimal_testing = [
            ['PoolBalls1.jpg', 5, 30, 15, 20, 0.5],
            ['PoolBalls2.jpg', 15, 25, 12, 14, 0.5],
            ['PoolBalls3.jpg', 20, 25, 9 ,17, 0.4],
            ['PoolBalls4.jpg', 25, 100, 5, 8, 0.5],
            ['PoolBalls5.jpg', 32, 70, 6, 7, 0.49],
            ['PoolBalls6.jpg', 36, 54, 3, 3, 0.6],
            ['PoolBalls7.jpg', 32,60, 3, 5, 0.7],
            ['PoolBalls8.jpeg', 22, 39, 10, 22, 0.4],
            ['PoolBalls9.jpg', 34, 44, 2, 5, 0.6],
            ['PoolBalls10.jpg', 10, 23, 9, 18, 0.5]
        ]

        self.textLogger.setStyleSheet("""QTextEdit { color: blue }""")
    def filter(self): # Hysteresis Thresholding 
        # 1. Get low and high threshoding
        low_value = self.spinBox.value()
        high_value = self.spinBox_2.value()
        
        self.uiController(False)
        self.keep = self.canny_edge_detection(self.image, low_value, high_value) # 2. Perform canny edge detection
        self.drawCannyImg(self.image) # 3. draw & Display canny image
        self.uiController(True)

    def threshold_value(self, value):
        if value < 2 : # sb(double)
            slider_value = value * 100
            value = value
        else : # slider(int)
            slider_value = value
            value = value / 100
        
        self.slider_threshold.setProperty("value", slider_value)
        self.sb_threshold.setProperty("value", value)

        self.threshold_value_now = value
        self.uiController(False)
        if self.logger : self.textLogger.append('[INFO] Perform hough transform ...')
        self.detect_circle(self.image, self.rmin_value_now, self.rmax_value_now, self.keep, value, 100)
        if self.logger : self.textLogger.append('[INFO] Success')
        if self.logger : self.textLogger.append('===================================')
        self.uiController(True)

    def rmin_value(self, value):
        self.slider_rmin.setProperty("value", value)
        self.sb_rmin.setProperty("value", value)

        self.rmin_value_now = value
        self.uiController(False)
        if self.logger : self.textLogger.append('[INFO] Perform hough transform ...')
        self.detect_circle(self.image, value, self.rmax_value_now, self.keep, self.threshold_value_now, 100)
        if self.logger : self.textLogger.append('[INFO] Success')
        if self.logger : self.textLogger.append('===================================')
        self.uiController(True)

    def rmax_value(self, value):
        self.slider_rmax.setProperty("value", value)
        self.sb_rmax.setProperty("value", value)

        self.rmax_value_now = value
        self.uiController(False)
        if self.logger : self.textLogger.append('[INFO] Perform hough transform ...')
        self.detect_circle(self.image, self.rmin_value_now, value, self.keep, self.threshold_value_now, 100)
        if self.logger : self.textLogger.append('[INFO] Success')
        if self.logger : self.textLogger.append('===================================')
        self.uiController(True)

    def detect_circle(self, image, rmin, rmax, keep, threshold, steps = 100):
       
        # Output image:
        self.output_image = Image.new("RGB", image.size)
        self.output_image.paste(image)        
        draw_result = ImageDraw.Draw(self.output_image)

        # Save image :
        self.save_image = Image.new("RGB", image.size)
        self.save_image.paste(image)        
        draw_saveImg = ImageDraw.Draw(self.save_image)

        points = []
        for r in range(rmin, rmax + 1):
            for t in range(steps):
                points.append((r, int(r * cos(2 * pi * t / steps)), int(r * sin(2 * pi * t / steps))))

        acc = defaultdict(int)
        for x, y in keep:
            for r, dx, dy in points:
                a = x - dx
                b = y - dy
                acc[(a, b, r)] += 1

        circles = []

        for k, v in sorted(acc.items(), key=lambda i: -i[1]):
            x, y, r = k
            if v / steps >= threshold and all((x - xc) ** 2 + (y - yc) ** 2 > rc ** 2 for xc, yc, rc in circles):
                #print(v / steps, x, y, r)
                #print('R = ' + str(r) + ' , Center = (' + str(x) + ', ' + str(y) + ')')
                self.textLogger.append('R = ' + str(r) + ' , Center = (' + str(x) + ', ' + str(y) + ')')
                #print('min = ' + str(x) + 'max = ' + str(y) + 'radius = ' + str(r))
                circles.append((x, y, r))

        for x, y, r in circles:
            draw_result.ellipse((x-r, y-r, x+r, y+r), outline=(0, 0, 255, 0))
            draw_saveImg.ellipse((x-r, y-r, x+r, y+r), outline=(255, 0, 0, 0))
                
        w, h = image.size
        self.output_image = self.output_image.resize((int(w * 1.8), int(h * 1.8))) 
        self.save_image = self.save_image.resize((int(w * 1.8), int(h * 1.8)))
        self.setPhoto(self.output_image, 3)


    def drawCannyImg(self, image):
        canny_image = Image.new("RGB", image.size)
        draw_canny = ImageDraw.Draw(canny_image)

        for x, y in self.keep:
            draw_canny.point((x, y), (255, 255, 255))
        
        self.setPhoto(canny_image, 2)
        self.textLogger.append('[INFO] Perform hough transform ...')
        self.detect_circle(image, self.rmin_value_now, self.rmax_value_now, self.keep, self.threshold_value_now, 100)
        self.textLogger.append('[INFO] Success')
        self.textLogger.append('===================================')

    def canny(self, image):
        self.keep = self.canny_edge_detection(image, self.low_value, self.high_value)
        self.drawCannyImg(image)
        
    def uiController(self, bool):
        self.btn_Save.setEnabled(bool)
        self.spinBox.setEnabled(bool)
        self.spinBox_2.setEnabled(bool)
        self.btn_filter.setEnabled(bool)
        self.slider_rmin.setEnabled(bool)
        self.slider_rmax.setEnabled(bool)
        self.sb_rmin.setEnabled(bool)
        self.sb_rmax.setEnabled(bool)
        self.slider_threshold.setEnabled(bool)
        self.sb_threshold.setEnabled(bool)

    def setOptimal(self, imgName):
        optimal = False
        for i in range(len(self.testingImg)):
            if self.testingImg[i][0] == imgName: # set testing optimal value
                optimal = True
                index = i
                break
            else : # set default value
                optimal = False

        if optimal :
            self.low_value = self.optimal_testing[i][1] # low
            self.high_value = self.optimal_testing[i][2] # high
            self.rmin_value_now = self.optimal_testing[i][3] # min
            self.rmax_value_now = self.optimal_testing[i][4] # max
            self.threshold_value_now = self.optimal_testing[i][5] # Threshold
        else : 
            self.low_value = 20
            self.high_value = 25
            self.rmin_value_now = 18
            self.rmax_value_now = 20
            self.threshold_value_now = 0.4

    def saveImage(self):
        self.file = QFileDialog.getSaveFileName(filter="Image (*.*)")[0]
        if self.file:
           self.save_image.convert("RGB")
           self.save_image.save(self.file)

    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        if self.filename:
            self.imgName = self.filename.split("/")[-1] # Get image name
            self.image = Image.open(self.filename)

            print('Filename : ' + self.imgName + ' (' + str(self.image.size[0]) + ', ' + str(self.image.size[1]) + ')')

            self.image = self.setSize(self.image, 300, 200)
            self.setPhoto(self.image, 1)

            print('Resize : 300 X 200')
            self.logger = False
            self.setOptimal(self.imgName) # Default or Optimal Value
            # set default
            self.slider_rmin.setProperty("value", self.rmin_value_now)
            self.sb_rmin.setProperty("value", self.rmin_value_now )
            self.slider_rmax.setProperty("value", self.rmax_value_now)
            self.sb_rmax.setProperty("value", self.rmax_value_now)
            self.spinBox.setProperty("value", self.low_value)
            self.spinBox_2.setProperty("value", self.high_value)
            self.slider_threshold.setProperty("value", (self.threshold_value_now * 100))
            self.sb_threshold.setProperty("value", self.threshold_value)
            self.logger = True

            # canny edge detection
            self.canny(self.image) 
            
            self.uiController(True)
       
    def setSize(self, image, width, height):
        w, h = image.size
        if w > width and h > height :
            if (ceil(w/width)) > (ceil(h/height)):
                tmp = ceil(w/width)
                self.pre_width =  int(w/ tmp)
                self.pre_height = int(h / tmp)
            else :
                tmp = ceil(w/height)
                self.pre_width =  int(w/ tmp)
                self.pre_height = int(h / tmp)
        else:
            self.pre_width = w
            self.pre_height = h

        image = image.resize((self.pre_width, self.pre_height))   
        return image

    def setPhoto(self, image, num):
        image = image.convert("RGBA")
        data = image.tobytes("raw","RGBA")
        qim = QtGui.QImage(data, image.size[0], image.size[1], QtGui.QImage.Format_ARGB32)
        pix = QtGui.QPixmap.fromImage(qim)
        if num == 1 :
            self.input_img.setPixmap(pix)
        elif num == 2 :
            self.canny_img.setPixmap(pix)
        elif num == 3 :
            self.result_img.setPixmap(pix)

    """
        Canny Edge Detection
    """
    def canny_edge_detection(self, input_image, low_value, high_value):
        input_pixels = input_image.load()
        width = input_image.width
        height = input_image.height

        # Transform the image to grayscale
        grayscaled = self.compute_grayscale(input_pixels, width, height)

        # Blur it to remove noise
        blurred = self.compute_blur(grayscaled, width, height)

        # Compute the gradient
        self.gradient, self.direction = self.compute_gradient(blurred, width, height)

        # Non-maximum suppression
        self.filter_out_non_maximum(self.gradient, self.direction, width, height)

        # Filter out some edges
        keep = self.filter_strong_edges(self.gradient, width, height, low_value, high_value)

        return keep


    def compute_grayscale(self, input_pixels, width, height):
        grayscale = np.empty((width, height))
        for x in range(width):
            for y in range(height):
                pixel = input_pixels[x, y]
                #grayscale[x, y] = (pixel[0] * 299 / 1000) + (pixel[1] * 587 / 1000) + (pixel[2] * 114 / 10000)
                grayscale[x, y] = (pixel[0] + pixel[1] + pixel[2]) / 3 # Common grayscale
        return grayscale


    def compute_blur(self, input_pixels, width, height):
        # Keep coordinate inside image
        clip = lambda x, l, u: l if x < l else u if x > u else x

        # Gaussian kernel (5X5)
        kernel = np.array([
            [1 / 256,  4 / 256,  6 / 256,  4 / 256, 1 / 256],
            [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
            [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
            [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
            [1 / 256,  4 / 256,  6 / 256,  4 / 256, 1 / 256]
        ])

        # Middle of the kernel
        offset = len(kernel) // 2

        # Compute the blurred image
        blurred = np.empty((width, height))
        for x in range(width):
            for y in range(height):
                acc = 0
                for a in range(len(kernel)):
                    for b in range(len(kernel)):
                        xn = clip(x + a - offset, 0, width - 1)
                        yn = clip(y + b - offset, 0, height - 1)
                        acc += input_pixels[xn, yn] * kernel[a, b]
                blurred[x, y] = int(acc)
        return blurred


    def compute_gradient(self, input_pixels, width, height):
        gradient = np.zeros((width, height))
        direction = np.zeros((width, height))
        for x in range(width):
            for y in range(height):
                if 0 < x < width - 1 and 0 < y < height - 1:
                    magx = input_pixels[x + 1, y] - input_pixels[x - 1, y]
                    magy = input_pixels[x, y + 1] - input_pixels[x, y - 1]
                    gradient[x, y] = sqrt(magx**2 + magy**2)
                    direction[x, y] = atan2(magy, magx)
        return gradient, direction


    def filter_out_non_maximum(self, gradient, direction, width, height):
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                angle = direction[x, y] if direction[x, y] >= 0 else direction[x, y] + pi
                rangle = round(angle / (pi / 4))
                mag = gradient[x, y]
                if ((rangle == 0 or rangle == 4) and (gradient[x - 1, y] > mag or gradient[x + 1, y] > mag)
                        or (rangle == 1 and (gradient[x - 1, y - 1] > mag or gradient[x + 1, y + 1] > mag))
                        or (rangle == 2 and (gradient[x, y - 1] > mag or gradient[x, y + 1] > mag))
                        or (rangle == 3 and (gradient[x + 1, y - 1] > mag or gradient[x - 1, y + 1] > mag))):
                    gradient[x, y] = 0


    def filter_strong_edges(self, radient, width, height, low, high):
        # Keep strong edges
        keep = set()
        for x in range(width):
            for y in range(height):
                if self.gradient[x, y] > high:
                    keep.add((x, y))

        # Keep weak edges next to a pixel to keep
        lastiter = keep
        while lastiter:
            newkeep = set()
            for x, y in lastiter:
                for a, b in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    if self.gradient[x + a, y + b] > low and (x+a, y+b) not in keep:
                        newkeep.add((x+a, y+b))
            keep.update(newkeep)
            lastiter = newkeep

        return list(keep)

    def retranslateUi(self, PoolBall):
        _translate = QtCore.QCoreApplication.translate
        PoolBall.setWindowTitle(_translate("PoolBall", "Pool Balls Detection"))
        self.groupBox.setTitle(_translate("PoolBall", "Input Image"))
        self.groupBox_2.setTitle(_translate("PoolBall", "Canny Edge Detection"))
        self.textLogger.setHtml(_translate("PoolBall", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_4.setTitle(_translate("PoolBall", "Circle Hough Transform"))
        self.lb_rmax_3.setText(_translate("PoolBall", "Accuracy"))
        self.lb_rmin.setText(_translate("PoolBall", "Min "))
        self.lb_rmax.setText(_translate("PoolBall", "Max"))
        self.groupBox_3.setTitle(_translate("PoolBall", "Pool Balls Detection"))
        self.groupBox_5.setTitle(_translate("PoolBall", "Canny Hysteresis Thresholding"))
        self.btn_filter.setText(_translate("PoolBall", "Filter"))
        self.lb_rmin_2.setText(_translate("PoolBall", "Low  "))
        self.lb_rmax_2.setText(_translate("PoolBall", "High"))
        self.groupBox_6.setTitle(_translate("PoolBall", "Function"))
        self.btn_Load.setText(_translate("PoolBall", "Load"))
        self.btn_Save.setText(_translate("PoolBall", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PoolBall = QtWidgets.QMainWindow()
    ui = Ui_PoolBall()
    ui.setupUi(PoolBall)
    PoolBall.show()
    sys.exit(app.exec_())

