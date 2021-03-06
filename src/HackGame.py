import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import time
import subprocess
import custom
import os
import requests

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

### Version Control ###
new_version = int(requests.get('https://raw.githubusercontent.com/jeonmogeon/HackGame/main/src/version').content.decode())
old_version = int(open(resource_path('version')).read())
print(old_version)
if old_version < new_version:
    f = open('update.bat', 'w')
    f.write('del HackGame.exe\ncurl https://raw.githubusercontent.com/jeonmogeon/HackGame/main/src/HackGame.exe -o HackGame.exe\ndel update.bat')
    f.close()
    os.startfile("update.bat")
    sys.exit()
### ### ### ### ### ###

form = resource_path('console.ui')
form_class = uic.loadUiType(form)[0]

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

        self.step.setStyleSheet("color: white;")
        self.tips.setStyleSheet("color: yellow; line-height:130%;")
        self.step.setAlignment(Qt.AlignCenter)
        self.stepCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
        elif step == 14:
            self.pushButton.setStyleSheet("color: black;")
            os.system('timeout /t 2 && explorer http://sv.m03.pw/video/03.mp4')
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
        requests.get(f'http://sv.m03.pw/log/{cmd}')
        if cmd == 'cls':
            self.textEdit.setText('Console >> ')
            self.cursor.movePosition(QTextCursor.End)
            self.textEdit.setTextCursor(self.cursor)
        else:
            flag = True
            if cmd != '':
                if flag:
                    result = custom.result(cmd)
                    if self.stepCount[self.gameStep] < custom.semStep(self.gameStep):
                        if custom.isCorrect(cmd, self.gameStep,self.stepCount[self.gameStep], self):
                            self.tips.append(custom.newTip(self.gameStep,self.stepCount[self.gameStep]))
                            self.stepCount[self.gameStep] += 1
                    if 'on:parent' in result:
                        self.mainText.setText('')
                        self.mainText.append(result)
                    else:
                        self.textEdit.append(result)
                    self.cursor.movePosition(QTextCursor.End)
                    self.textEdit.setTextCursor(self.cursor)
                    self.textEdit.append('Console >> ')
                    self.cursor.movePosition(QTextCursor.End)
                    self.textEdit.setTextCursor(self.cursor)
                else:
                    app = cmd.split(' ')[0]
                    p = subprocess.Popen(cmd, shell=True, bufsize=0,stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                    self.tbextEdit.append('')
                    while True:
                        try:
                            line = p.stdout.readline()
                        except:
                            line = ''
                        if not line:
                            self.textEdit.insertPlainText(p.stderr.readline().decode('cp949'))
                            self.cursor.movePosition(QTextCursor.End)
                            self.textEdit.setTextCursor(self.cursor)
                            break
                        #print(line)
                        self.textEdit.insertPlainText(line.decode('cp949'))
                        self.cursor.movePosition(QTextCursor.End)
                        self.textEdit.setTextCursor(self.cursor)

                    self.textEdit.append('Console >> ')
                    self.cursor.movePosition(QTextCursor.End)
                    self.textEdit.setTextCursor(self.cursor)
            else:
                self.textEdit.append('Console >> ')
                self.cursor.movePosition(QTextCursor.End)
                self.textEdit.setTextCursor(self.cursor)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass()
    myWindow.setWindowTitle(f'HackGame.exe Ver.{old_version}')
    myWindow.show()
    app.exec_()