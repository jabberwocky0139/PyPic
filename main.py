# -*- coding: utf-8 -*-
import sys
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from pprint import pprint


class ButtonBoxWidget(QWidget):

    def __init__(self, parent=None):
        # コンストラクタ
        QWidget.__init__(self, parent=parent)
        
        # 実際の生成コード
        self.setup_ui()

    def setup_ui(self):
        
        # QPushButtonのインスタンスを作る
        self.expand_button = QPushButton("+", parent=self)
        self.shrink_button = QPushButton("-", parent=self)
        self.next_button = QPushButton("→", parent=self)
        self.previous_button = QPushButton("←", parent=self)
        
        # Buttonをレイアウトマネージャに入れる
        layout = QGridLayout()
        layout.addWidget(self.expand_button, 0, 0)
        layout.addWidget(self.shrink_button, 0, 1)
        layout.addWidget(self.previous_button, 1, 0)
        layout.addWidget(self.next_button, 1, 1)
        
        # レイアウトマネージャをWidgetに入れる
        self.setLayout(layout)


class CountDownWidget(QWidget):
    
    def __init__(self, parent=None):
        
        # constructor.
        QWidget.__init__(self, parent=parent)

        # 実装.
        self.setup_ui()
        
    def setup_ui(self):
        # WidgetのSizePolicy.
        self.setSizePolicy(QSizePolicy.Expanding, 
                           QSizePolicy.Expanding)
        
        # labelの生成.
        self.label = QLabel("Label")
        
        # labelに載せるpixmapを生成.
        self._pixmap = QtGui.QPixmap("PyPic.png")

        # labelにpixmapを載せる. アスペクト比は一定. 
        self.label.setPixmap(self._pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))

        # labelのSizePolicy.
        self.label.setSizePolicy(QSizePolicy.Expanding, 
                                 QSizePolicy.Expanding)

        # labelの最小値を設定. コレをしないとresizeEventが正常に動作しない. 
        self.label.setMinimumSize(1, 1)

        # labelを常に中央に表示. 
        self.label.setAlignment(Qt.AlignCenter)

        # layoutの生成.
        layout = QVBoxLayout()

        # layoutにlabelを載せる.
        layout.addWidget(self.label)

        # layoutのset.
        self.setLayout(layout)
        

    def resizeEvent(self, event):
        
        # labelのサイズを取得
        size = self.label.size()
        
        # pixmapのサイズをlabelの小さい方の幅に合わせる
        if size.width() > size.height():
            self.label.setPixmap(self._pixmap.scaled(size.height(),
                                                     size.height(),
                                                     Qt.KeepAspectRatio))
            self._pixmap.scaled(self._pixmap.width(), size.height())
        else:
            self.label.setPixmap(self._pixmap.scaled(size.width(),
                                                     size.width(),
                                                     Qt.KeepAspectRatio))
            self._pixmap.scaled(size.width(), self._pixmap.height())
                    
    
    def mousePressEvent(self, event):
        pprint(dir(self._pixmap))
        


        
def main():
    app = QApplication(sys.argv)
    panel = QWidget()
    
    # 子Widget 
    countdown_widget = CountDownWidget(parent=panel)
    button_box_widget = ButtonBoxWidget(parent=panel)
    countdown_widget.setSizePolicy(QSizePolicy.Expanding, 
                                   QSizePolicy.Expanding)

    # layout manager
    panel_layout = QVBoxLayout()
    panel_layout.addWidget(countdown_widget)
    panel_layout.addWidget(button_box_widget)

    # Panel Widget 
    panel.setLayout(panel_layout)
    #panel.setFixedSize(320, 200)
    
    # Main Window
    main_window = QMainWindow()
    main_window.setWindowTitle("PyPic")
    main_window.setWindowIcon(QtGui.QIcon("PyPic.png"))
    main_window.setCentralWidget(panel)
    
    main_window.show()
    
    # Conectivity
    button_box_widget.expand_button.clicked.connect(lambda : print("hello"))
    button_box_widget.shrink_button.clicked.connect(lambda : print("hello"))
    button_box_widget.previous_button.clicked.connect(lambda : print("hello"))
    button_box_widget.next_button.clicked.connect(app.quit)
    
    app.exec_()
    
if __name__ == '__main__':
    print("app main start")
    main()
