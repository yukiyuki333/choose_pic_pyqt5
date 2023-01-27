from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import cv2
from style_transform import trans

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.img_path = ''
        self.style_path = ''
        self.epoch=100
        self.pic_num=1
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.choose_button.clicked.connect(self.open_file)
        self.ui.style_button.clicked.connect(self.open_style)
        self.ui.start_button.clicked.connect(self.transform)

    def display_img(self,image,isstyle):
        self.img = cv2.imdecode(np.fromfile(image, dtype=np.uint8), -1)
        shape = self.img.shape
        times = 1

        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(self.qimg)
        self.qpixmap_height = self.qpixmap.height()

        if shape[0] >= 300 or shape[1] >= 300:
            if shape[0] < shape[1]:  # 高<寬
                times = shape[0] / 300
                resize = int(shape[0] / times)

            else:
                times = shape[1] / 300
                resize = int(shape[1] / times)
        else:
            if shape[0] < shape[1]:  # 高>寬
                times = 300 / shape[0]
                resize = int(shape[0] / times)
            else:
                times = 300 / shape[1]
                resize = int(shape[1] / times)

        scaled_pixmap = self.qpixmap.scaledToHeight(resize)
        if isstyle==0:
            self.ui.image.setPixmap(scaled_pixmap)
            self.ui.image.adjustSize()
        else:
            self.ui.image_2.setPixmap(scaled_pixmap)
            self.ui.image_2.adjustSize()
    def open_file(self):
        self.img_path, filetype = QFileDialog.getOpenFileName(self,
                                                              "Open file",
                                                              "./")  # start path

        self.ui.show_file_path.setText(self.img_path)
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ui.show_file_path.setFont(font)

        self.display_img(self.img_path,0)
    def open_style(self):
        self.style_path , filetype = QFileDialog.getOpenFileName(self,"Open file", "./")  # start path
        self.display_img(self.style_path,1)
    def transform(self):
        if self.ui.epoch_lineeditor.text()!='':
            self.epoch=int(self.ui.epoch_lineeditor.text())
        trans(self.img_path,self.style_path,self.epoch,self.pic_num)
        self.pic_num+=1