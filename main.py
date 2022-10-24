from workouts import program
import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QLabel, QLineEdit, QComboBox, QHBoxLayout
from PyQt6.QtGui import QIcon, QIntValidator
from PyQt6.QtCore import QSize

class main(QMainWindow):
    
    def __init__(self):
        super(main, self).__init__()
        self.check = 0
        self.initialCheck()
        self.initUI()

    def initialCheck(self):
        if os.path.exists('prs.txt'):
            with open('prs.txt') as file:
                lines = file.readlines()
                data = lines[0]
                li = list(data.split(" "))
                self.name = li[0]
                self.squat = li[1]
                self.bench = li[2]
                self.deadlift = li[3]
                self.data = [self.name, self.squat, self.bench, self.deadlift]
        else:
            self.gotoScreen2()
        
    def initUI(self):
        # label 
        self.label = QLabel(self)
        self.label.setFixedSize(QSize(200,100))

        self.label.setText('Welcome back.')
        self.label.move(350,100)

        # program button
        self.program = QPushButton(self)
        self.program.setFixedSize(QSize(150,50))
        self.program.move(100,300)
        self.program.setText('Program')
        self.program.clicked.connect(self.gotoScreen3)
        
        # dcp button
        self.dcp = QPushButton(self)
        self.dcp.setText('Display Current PR\'s')
        self.dcp.move(300,300)
        self.dcp.setFixedSize(QSize(150,50))
        self.dcp.clicked.connect(self.gotoScreen4)

        self.upr = QPushButton(self)
        self.upr.setText('Update Current PR\'s')
        self.upr.move(500,300)
        self.upr.setFixedSize(QSize(150,50))
        self.upr.clicked.connect(self.gotoScreen5)
    
    def gotoScreen2(self):
        screen2 = newPage()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen3(self):
        screen3 = programPage()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoScreen4(self):
        screen4 = PR_Page()
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoScreen5(self):
        screen5 = writeNewPRs()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class writeNewPRs(QMainWindow):
    def __init__(self):
        super(writeNewPRs, self).__init__()
        self.arr = []
        self.initUI()

    def display(self,x:int):
        if x == 0:
            self.label2 = QLabel(self)
            self.label2.setFixedSize(QSize(200,100))
            self.label2.setText('Enter your name:')
            self.label2.move(350,250)
            
        elif x == 1:
            self.label2.hide()
            self.label3 = QLabel(self)
            self.label3.setFixedSize(QSize(200,100))
            self.label3.setText('Enter your Squat PR:')
            self.label3.move(350,250)
            self.label3.show()
            
        elif x == 2:
            self.label3.hide()
            self.label4 = QLabel(self)
            self.label4.setFixedSize(QSize(200,100))
            self.label4.setText('Enter your Bench PR:')
            self.label4.move(350,250)
            self.label4.show()

        elif x == 3:
            self.label4.hide()
            self.label5 = QLabel(self)
            self.label5.setFixedSize(QSize(200,100))
            self.label5.setText('Enter your Deadlift PR:')
            self.label5.move(350,250)
            self.label5.show()
            
    def initUI(self):
        # Back button
        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoMainMenu)

        # label for Screen 2
        self.label = QLabel(self)
        self.label.setFixedSize(QSize(200,100))
        self.label.setText('Please Enter Your Current PR\'s:')
        self.label.move(300,100)
        
        self.counter = 0
        self.display(0)

        self.line = QLineEdit(self)
        self.line.move(350,250)
        self.line.returnPressed.connect(self.handleInput)
    
    def handleInput(self):
        self.counter += 1
        self.display(self.counter)
        self.temp = self.line.text()
        self.arr.append(self.temp)
        self.line.clear()
        if len(self.arr) == 4:
            self.keep = ' '.join(str(e) for  e in self.arr)
            f = open("prs.txt", 'a')
            f.write(self.keep)
            f.close()
            #self.gotoMainMenu()
            #mainWindow = main()
            #widget.addWidget(mainWindow)
            #widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            print(self.arr)
    
    def gotoMainMenu(self):
        main_screen = main()
        widget.addWidget(main_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class programPage(QMainWindow):
    def __init__(self):
        super(programPage, self).__init__()
        self.dataGrab()
        self.initUI()

    def initUI(self):
        # Back Button
        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoMainMenu)

        self.title = QLabel(self)
        self.title.setFixedSize(QSize(500,100))
        self.title.setText('Please Type Your Program Week #, Day #, and press \"Confirm\":')
        self.title.move(250,100)

        self.weeklabel = QLabel(self)
        self.weeklabel.setFixedSize(QSize(200,100))
        self.weeklabel.setText('Week #:')
        self.weeklabel.move(250,160)

        self.daylabel = QLabel(self)
        self.daylabel.setFixedSize(QSize(200,100))
        self.daylabel.setText('Day #:')
        self.daylabel.move(550,160)

        self.weekinput = QLineEdit(self)
        self.weekinput.move(250,220)
        self.weekinput.returnPressed.connect(self.handleWeekInput)
        weekvalidator = QIntValidator()
        self.weekinput.setValidator(weekvalidator)

        self.dayinput = QLineEdit(self)
        self.dayinput.move(550,220)
        self.dayinput.returnPressed.connect(self.handleDayInput)
        dayvalidator = QIntValidator()
        self.dayinput.setValidator(dayvalidator)

        self.readybutton = QPushButton(self)
        self.readybutton.move(400,260)
        self.readybutton.setText('Confirm')
        self.readybutton.clicked.connect(self.accessProgram)

        self.resetbutton = QPushButton(self)
        self.resetbutton.move(670,20)
        self.resetbutton.setText('Reset')
        self.resetbutton.clicked.connect(self.reset)
    
    def handleWeekInput(self):
        self.weektext = self.weekinput.text()
        self.week = QLabel(self)
        self.week.setText('Selected Week: ' + self.weektext)
        self.week.move(250,250)
        self.week.show()

    def handleDayInput(self):
        self.daytext = self.dayinput.text()
        self.day = QLabel(self)
        self.day.setText('Selected Day: ' + self.daytext)
        self.day.move(550,250)
        self.day.show()

    def accessProgram(self):
        x = program(self.squat, self.bench, self.deadlift, self.weektext, self.daytext)
        data_output = x.dataRetrieval()
        self.program_output = QLabel(self)
        self.program_output.setFixedSize(QSize(500,500))
        self.program_output.setText(data_output)
        self.program_output.move(200,150)
        self.program_output.show()
    
    def reset(self):
        try:
            self.program_output.hide()
            self.weekinput.clear()
            self.week.hide()
            self.dayinput.clear()
            self.day.hide()
        except AttributeError:
            pass

    def dataGrab(self):
        with open('prs.txt') as file:
            lines = file.readlines()
            data = lines[0]
            li = list(data.split(" "))
            self.name = li[0]
            self.squat = li[1]
            self.bench = li[2]
            self.deadlift = li[3]

    def gotoMainMenu(self):
        main_screen = main()
        widget.addWidget(main_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class PR_Page(QMainWindow):
    def __init__(self):
        super(PR_Page, self).__init__()
        self.dataGrab()
        self.initUI()

    def initUI(self):
        # Back Button
        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoMainMenu)

        # Title
        self.title = QLabel(self)
        self.title.setFixedSize(QSize(200,100))
        self.title.setText('Here are ' + self.name + '\'s current PR\'s:')
        self.title.move(300,100)

        self.squatlabel = QLabel(self)
        self.squatlabel.setFixedSize(QSize(200,100))
        self.squatlabel.setText('Squat: ' + self.squat)
        self.squatlabel.move(350,250)

        self.benchlabel = QLabel(self)
        self.benchlabel.setFixedSize(QSize(200,100))
        self.benchlabel.setText('Bench: ' + self.bench)
        self.benchlabel.move(350,300)

        self.deadliftlabel = QLabel(self)
        self.deadliftlabel.setFixedSize(QSize(200,100))
        self.deadliftlabel.setText('Deadlift: ' + self.deadlift)
        self.deadliftlabel.move(350,350)
    
    def dataGrab(self):
        with open('prs.txt') as file:
            lines = file.readlines()
            data = lines[0]
            li = list(data.split(" "))
            self.name = li[0]
            self.squat = li[1]
            self.bench = li[2]
            self.deadlift = li[3]
            
    def gotoMainMenu(self):
        main_screen = main()
        widget.addWidget(main_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class newPage(QMainWindow):
    def __init__(self):
        super(newPage, self).__init__()
        self.arr = []
        self.initUI()

    def display(self,x:int):
        if x == 0:
            self.label2 = QLabel(self)
            self.label2.setFixedSize(QSize(200,100))
            self.label2.setText('Enter your name:')
            self.label2.move(350,250)
            
        elif x == 1:
            self.label2.hide()
            self.label3 = QLabel(self)
            self.label3.setFixedSize(QSize(200,100))
            self.label3.setText('Enter your Squat PR:')
            self.label3.move(350,250)
            self.label3.show()
            
        elif x == 2:
            self.label3.hide()
            self.label4 = QLabel(self)
            self.label4.setFixedSize(QSize(200,100))
            self.label4.setText('Enter your Bench PR:')
            self.label4.move(350,250)
            self.label4.show()

        elif x == 3:
            self.label4.hide()
            self.label5 = QLabel(self)
            self.label5.setFixedSize(QSize(200,100))
            self.label5.setText('Enter your Deadlift PR:')
            self.label5.move(350,250)
            self.label5.show()
            
    def initUI(self):

        # label for Screen 2
        self.label = QLabel(self)
        self.label.setFixedSize(QSize(500,100))
        self.label.setText('New User, please enter your info below and press Enter to proceed to the next step:')
        self.label.move(200,100)
        
        self.counter = 0
        self.display(0)

        self.line = QLineEdit(self)
        self.line.move(350,250)
        self.line.returnPressed.connect(self.handleInput)
    
    def handleInput(self):
        self.counter += 1
        self.display(self.counter)
        self.temp = self.line.text()
        self.arr.append(self.temp)
        self.line.clear()
        if len(self.arr) == 4:
            self.keep = ' '.join(str(e) for  e in self.arr)
            f = open("prs.txt", 'a')
            f.write(self.keep)
            f.close()
            self.gotoMainMenu()
            mainWindow = main()
            widget.addWidget(mainWindow)
            widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoMainMenu(self):
        main_screen = main()
        widget.addWidget(main_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    mainWindow = main()
    widget.addWidget(mainWindow)
    widget.setWindowTitle('Workout Program')
    widget.setWindowIcon(QIcon('workout.png'))
    widget.setFixedSize(QSize(800,500)) 
    widget.show()
    sys.exit(app.exec())


