from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import QIcon


class MsgBox(QMessageBox):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)
        
    def set_custom_icon(self, icon):
        self.setIconPixmap(icon)
        q_icon = QIcon(icon)
        self.setWindowIcon(q_icon)

    def set_yes_no_buttons(self):
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No )
               

def correct_msgbox(title, text):
    icon = 'pyside2_msgboxes/icons/correct.png'
    msg_box = MsgBox(title, text)
    msg_box.set_custom_icon(icon)
    msg_box.exec_()

def input_error_msgbox(title, text):
    icon = 'pyside2_msgboxes/icons/input_error.png'
    msg_box = QMessageBox()
    msg_box.setWindowTitle (title)
    msg_box.setText(text)
    msg_box.setIconPixmap(icon)
    q_icon = QIcon(icon)
    msg_box.setWindowIcon(q_icon)
    msg_box.exec_()
    
def warning_msgbox(title, text):
    icon = 'pyside2_msgboxes/icons/warning.png'
    msg_box = MsgBox(title, text)
    msg_box.set_custom_icon(icon)
    msg_box.set_yes_no_buttons()
    resp = msg_box.exec_()
    return resp

