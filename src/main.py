import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import time
import subprocess
import custom

form_class = uic.loadUiType("console.ui")[0]

class cmd_Thread(QThread):
    def __init__(self, parent, arg = ''):
        super().__init__(parent) 
        self.parent = parent 
        self.cmd = arg

    def run(self):
        flag = True
        cmd = self.cmd
        if cmd != '':
            if flag:
                result = custom.result(cmd)
                if self.parent.stepCount[self.parent.gameStep] < custom.semStep(self.parent.gameStep):
                    if custom.isCorrect(cmd, self.parent.gameStep,self.parent.stepCount[self.parent.gameStep]):
                        self.parent.tips.append(custom.newTip(self.parent.gameStep,self.parent.stepCount[self.parent.gameStep]))
                        self.parent.stepCount[self.parent.gameStep] += 1
                self.parent.textEdit.append(result)
                print('1')
                self.parent.cursor.movePosition(QTextCursor.End)
                print('1')
                self.parent.textEdit.setTextCursor(self.parent.cursor)
                print('1')
                self.parent.textEdit.append('Console >> ')
                print('1')
                self.parent.cursor.movePosition(QTextCursor.End)
                print('1')
                self.parent.textEdit.setTextCursor(self.parent.cursor)
            else:
                app = cmd.split(' ')[0]
                p = subprocess.Popen(cmd, shell=True, bufsize=0,stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                self.parent.tbextEdit.append('')
                while True:
                    try:
                        line = p.stdout.readline()
                    except:
                        line = ''
                    if not line:
                        self.parent.textEdit.insertPlainText(p.stderr.readline().decode('cp949'))
                        self.parent.cursor.movePosition(QTextCursor.End)
                        self.parent.textEdit.setTextCursor(self.parent.cursor)
                        break
                    #print(line)
                    self.parent.textEdit.insertPlainText(line.decode('cp949'))
                    self.parent.cursor.movePosition(QTextCursor.End)
                    self.parent.textEdit.setTextCursor(self.parent.cursor)

                self.parent.textEdit.append('Console >> ')
                self.parent.cursor.movePosition(QTextCursor.End)
                self.parent.textEdit.setTextCursor(self.parent.cursor)
        else:
            self.parent.textEdit.append('Console >> ')
            self.parent.cursor.movePosition(QTextCursor.End)
            self.parent.textEdit.setTextCursor(self.parent.cursor)

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("background-color: black;")
        self.textEdit.setStyleSheet("color: white;")
        self.lineEdit.setStyleSheet("color: white;")

        self.pushButton.setStyleSheet("color: white;")
        self.prev_btn.setStyleSheet("color: white;")

        self.mainText.setStyleSheet("color: white;")

        self.step.setStyleSheet("color: green;")
        self.tips.setStyleSheet("color: yellow;")
        self.step.setAlignment(Qt.AlignCenter)
        self.stepCount = [0,0,0,0,0,0,0]
        self.updateGame(1)
        self.cursor = self.textEdit.textCursor()
        self.gameStep = 1

        self.textEdit.setText('Console >> ')
        self.cursor.movePosition(QTextCursor.End)
        self.textEdit.setTextCursor(self.cursor)
        
        self.lineEdit.returnPressed.connect(self.lReturn)
        self.pushButton.clicked.connect(self.next_step)
        self.prev_btn.clicked.connect(self.prev_step)

    def next_step(self):
        self.gameStep += 1
        self.updateGame(self.gameStep)

    def prev_step(self):
        if self.gameStep <= 0:
            return(0)
        self.gameStep -= 1
        self.updateGame(self.gameStep)

    def updateGame(self, step: int):
        self.step.setText(f'Step {step}')
        self.tips.setText(custom.tip(step))
        if step == 1:
            self.prev_btn.setStyleSheet("color: black;")
        elif step == 7:
            self.pushButton.setStyleSheet("color: black;")
        else:
            self.prev_btn.setStyleSheet("color: white;")
            self.pushButton.setStyleSheet("color: white;")

    def lReturn(self):
        cmd = self.lineEdit.text()
        self.textEdit.insertPlainText(cmd)
        self.cursor.movePosition(QTextCursor.End)
        self.textEdit.setTextCursor(self.cursor)
        self.lineEdit.setText('')
        self.consoleDo(cmd)

    def consoleDo(self, cmd: str):
        if cmd == 'cls':
            self.textEdit.setText('Console >> ')
            self.cursor.movePosition(QTextCursor.End)
            self.textEdit.setTextCursor(self.cursor)
        else:
            cm = cmd_Thread(self, arg = cmd)
            cm.start()

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()