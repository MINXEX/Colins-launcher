import sys
import os
import json
import random
from PyQt5 import QtWidgets, QtGui, QtCore

class ShootingStar(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFixedSize(5, 5)
        self.setStyleSheet("background-color: white; border-radius: 2px;")
        self.animation = QtCore.QPropertyAnimation(self, b"pos")
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.reset_star()
    
    def reset_star(self):
        start_x = random.randint(0, self.parent.width())
        start_y = random.randint(0, self.parent.height() // 2)
        end_x = start_x + random.randint(100, 300)
        end_y = start_y + random.randint(50, 150)
        self.move(start_x, start_y)
        self.animation.setStartValue(QtCore.QPoint(start_x, start_y))
        self.animation.setEndValue(QtCore.QPoint(end_x, end_y))
        self.animation.setDuration(random.randint(2000, 4000))
        self.animation.finished.connect(self.reset_star)
        self.animation.start()

class GameLauncher(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Colin's Game Launcher")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background-color: #0D0D0D;")
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QHBoxLayout(self.central_widget)

        # Background Layer
        self.background = QtWidgets.QLabel(self.central_widget)
        self.background.setGeometry(0, 0, 1200, 800)
        self.background.setStyleSheet("background: url('background.jpg') no-repeat center center; background-size: cover;")
        
        for _ in range(20):
            ShootingStar(self.background)

        self.layout.addWidget(self.background)
        self.main_frame = QtWidgets.QFrame(self.central_widget)
        self.main_frame.setStyleSheet("background: transparent;")
        self.layout.addWidget(self.main_frame)

        # Sidebar
        self.sidebar = QtWidgets.QFrame(self.main_frame)
        self.sidebar.setFixedWidth(300)
        self.sidebar.setStyleSheet("background-color: rgba(30, 30, 30, 0.85); border-radius: 15px;")
        self.sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar)
        self.layout.addWidget(self.sidebar)

        self.title_label = QtWidgets.QLabel("Colin's Launcher")
        self.title_label.setFont(QtGui.QFont("Arial", 22, QtGui.QFont.Bold))
        self.title_label.setStyleSheet("color: white; padding: 20px;")
        self.sidebar_layout.addWidget(self.title_label, alignment=QtCore.Qt.AlignCenter)

        button_style = ("QPushButton { background-color: #5BBF26; color: white; font: 18px; padding: 15px; border-radius: 10px; }"
                        "QPushButton:hover { background-color: #6CD935; }")
        
        self.open_exe_button = QtWidgets.QPushButton("Add Game")
        self.open_exe_button.setStyleSheet(button_style)
        self.open_exe_button.clicked.connect(self.open_file_dialog)
        self.sidebar_layout.addWidget(self.open_exe_button)

        self.remove_game_button = QtWidgets.QPushButton("Remove Game")
        self.remove_game_button.setStyleSheet(button_style.replace("#5BBF26", "#FF3B3B").replace("#6CD935", "#FF5252"))
        self.remove_game_button.clicked.connect(self.remove_selected_game)
        self.sidebar_layout.addWidget(self.remove_game_button)

        self.quit_button = QtWidgets.QPushButton("Exit")
        self.quit_button.setStyleSheet(button_style.replace("#5BBF26", "#444").replace("#6CD935", "#666"))
        self.quit_button.clicked.connect(self.close)
        self.sidebar_layout.addWidget(self.quit_button)

        self.sidebar_layout.addStretch()

        # Game List Section
        self.main_content = QtWidgets.QFrame(self.main_frame)
        self.main_content.setStyleSheet("background-color: rgba(37, 37, 37, 0.85); padding: 30px; border-radius: 15px;")
        self.main_layout = QtWidgets.QVBoxLayout(self.main_content)
        self.layout.addWidget(self.main_content)

        self.game_list = QtWidgets.QListWidget()
        self.game_list.setStyleSheet("QListWidget { background-color: #444; color: white; font: 18px; padding: 15px; border-radius: 10px; }"
                                    "QListWidget::item { padding: 12px; border-bottom: 1px solid #666; }")
        self.game_list.itemSelectionChanged.connect(self.update_launch_button)
        self.main_layout.addWidget(self.game_list)

        self.launch_button = QtWidgets.QPushButton("Launch Game")
        self.launch_button.setStyleSheet("background-color: #444; color: gray; font: 20px; padding: 18px; border-radius: 10px;")
        self.launch_button.setEnabled(False)
        self.launch_button.clicked.connect(self.launch_game)
        self.main_layout.addWidget(self.launch_button)

        self.game_paths = {}
    
    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Game EXE", "", "Executable Files (*.exe);;All Files (*)", options=options)
        if file_name:
            self.game_list.addItem(os.path.basename(file_name))
            self.game_paths[os.path.basename(file_name)] = file_name
    
    def remove_selected_game(self):
        selected_item = self.game_list.currentItem()
        if selected_item:
            del self.game_paths[selected_item.text()]
            self.game_list.takeItem(self.game_list.row(selected_item))
            self.update_launch_button()
    
    def update_launch_button(self):
        if self.game_list.currentItem():
            self.launch_button.setStyleSheet("background-color: #007BFF; color: white; font: 20px; padding: 18px; border-radius: 10px;")
            self.launch_button.setEnabled(True)
        else:
            self.launch_button.setStyleSheet("background-color: #444; color: gray; font: 20px; padding: 18px; border-radius: 10px;")
            self.launch_button.setEnabled(False)
    
    def launch_game(self):
        selected_item = self.game_list.currentItem()
        if selected_item:
            exe_path = self.game_paths.get(selected_item.text())
            if exe_path:
                QtCore.QProcess.startDetached(exe_path)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Game path not found!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    launcher = GameLauncher()
    launcher.show()
    sys.exit(app.exec_())
