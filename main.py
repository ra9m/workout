from workouts import program
import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class startScreen(QMainWindow):
    def __init__(self):
        super(startScreen, self).__init__()
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
        self.background = QLabel(self)
        self.background.setFixedSize(QSize(800,500))
        self.background.setStyleSheet("background-image : url(meme.jpg)")
        self.background.hide()

        try:
            self.message = QLabel(self)
            self.message.setFixedSize(QSize(200,100))
            self.message.setText('Welcome back, ' + self.name + '.')
            self.message.move(350,320)
        except AttributeError:
            self.gotoScreen2()

        # label 
        self.title = QLabel(self)
        self.title.setFixedSize(QSize(600,280))
        self.title.setText('Workout\nProgram')
        self.title.setFont(QFont('Arial', 90))
        self.title.move(180,50)

        # Fun button
        self.fun = QPushButton(self)
        self.fun.setFixedSize(QSize(150,50))
        self.fun.move(100,400)
        self.fun.setText('Mystery')
        self.fun.clicked.connect(self.mystery)

        # Main Menu button
        self.mainMenu = QPushButton(self)
        self.mainMenu.setFixedSize(QSize(150,50))
        self.mainMenu.move(330,400)
        self.mainMenu.setText('Main Menu')
        self.mainMenu.clicked.connect(self.gotoScreen3)

        # Timer button
        self.timer = QPushButton(self)
        self.timer.setFixedSize(QSize(150,50))
        self.timer.move(550,400)
        self.timer.setText('Timer')
        self.timer.clicked.connect(self.gotoScreen4)
    
    def gotoScreen2(self):
        screen2 = newPage()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen3(self):
        screen3 = mainMenu()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoScreen4(self):
        screen4 = timer()
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def mystery(self):
        self.background.show()

class timer(QMainWindow):
    def __init__(self):
        super(timer, self).__init__()
        self.initUI()
    
    def initUI(self):
        # Setting necessary variables
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.startwatch = False

        # Title
        self.title = QLabel(self)
        self.title.setFixedSize(QSize(200,100))
        self.title.setText('Timer')
        self.title.setFont(QFont('Arial', 30))
        self.title.move(350,20)

        # Timer Object
        timer = QTimer(self)
        timer.timeout.connect(self.timeobject)
        timer.start(100)

        # Time Display
        self.label = QLabel(self)
        self.label.move(350,200)

        # Start button
        self.startbutton = QPushButton(self)
        self.startbutton.move(150,350)
        self.startbutton.setText('Start')
        self.startbutton.clicked.connect(self.startTimer)

        # Stop button
        self.stopbutton = QPushButton(self)
        self.stopbutton.move(350,350)
        self.stopbutton.setText('Stop')
        self.stopbutton.clicked.connect(self.stopTimer)

        # Reset button
        self.resetbutton = QPushButton(self)
        self.resetbutton.move(550,350)
        self.resetbutton.setText('Reset')
        self.resetbutton.clicked.connect(self.resetTimer)

        # Back button
        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoHomeScreen)
    
    def timeobject(self):
        # Check the value of startWatch  variable to start or stop the Stop Watch
        if self.startwatch:
            # Increment counter by 1
            self.counter += 1

            # Count and set the time counter value
            cnt = int((self.counter/10 - int(self.counter/10))*10)
            self.count = '0' + str(cnt)

            # Set the second value
            if int(self.counter/10) < 10 :
                self.second = '0' + str(int(self.counter / 10))
            else:
                self.second = str(int(self.counter / 10))
                # Set the minute value
                if self.counter / 10 == 60.0 :
                    self.second == '00'
                    self.counter = 0
                    min = int(self.minute) + 1
                    if min < 10 :
                        self.minute = '0' + str(min)
                    else:
                        self.minute = str(min)

        # Merge the mintue, second and count values
        text = self.minute + ':' + self.second + ':' + self.count
        # Display the stop watch values in the label
        self.label.setText('<h1 style="color:black">' + text + '</h1>')

    def startTimer(self):
        self.startwatch = True

    def stopTimer(self):
        self.startwatch = False

    def resetTimer(self):
        self.startwatch = False
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        
    
    def gotoHomeScreen(self):
        homeScreen = startScreen()
        widget.addWidget(homeScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class mainMenu(QMainWindow):
    
    def __init__(self):
        super(mainMenu, self).__init__()
        self.check = 0
        self.dataGrab()
        self.initUI()

    def dataGrab(self):
        with open('prs.txt') as file:
            lines = file.readlines()
            data = lines[0]
            li = list(data.split(" "))
            self.name = li[0]
            self.squat = li[1]
            self.bench = li[2]
            self.deadlift = li[3]
        
    def initUI(self):
        # Back button
        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoHomeScreen)

        # Title
        self.title = QLabel(self)
        self.title.setFixedSize(QSize(600,100))
        self.title.setFont(QFont('Arial', 80))
        self.title.setText('Main Menu')
        self.title.move(150,170)

        # program button
        self.program = QPushButton(self)
        self.program.setFixedSize(QSize(150,50))
        self.program.move(50,350)
        self.program.setText('Program')
        self.program.clicked.connect(self.gotoScreen3)
        
        # dcp button
        self.dcp = QPushButton(self)
        self.dcp.setText('Display Current PR\'s')
        self.dcp.move(325,350)
        self.dcp.setFixedSize(QSize(150,50))
        self.dcp.clicked.connect(self.gotoScreen4)

        self.upr = QPushButton(self)
        self.upr.setText('Update Current PR\'s')
        self.upr.move(600,350)
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
        screen4 = displayPRs()
        widget.addWidget(screen4)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoScreen5(self):
        screen5 = updatePRs()
        widget.addWidget(screen5)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoHomeScreen(self):
        homeScreen = startScreen()
        widget.addWidget(homeScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class updatePRs(QMainWindow):
    def __init__(self):
        super(updatePRs, self).__init__()
        self.arr = []
        self.initUI()

    def display(self,x:int):
        if x == 0:
            self.label2 = QLabel(self)
            self.label2.setFixedSize(QSize(200,100))
            self.label2.setText('Enter your name and press Enter:')
            self.label2.move(350,180)
            
        elif x == 1:
            self.label2.hide()
            self.label3 = QLabel(self)
            self.label3.setFixedSize(QSize(200,100))
            self.label3.setText('Enter your Squat PR and press Enter:')
            self.label3.move(350,180)
            self.label3.show()
            
        elif x == 2:
            self.label3.hide()
            self.label4 = QLabel(self)
            self.label4.setFixedSize(QSize(200,100))
            self.label4.setText('Enter your Bench PR and press Enter:')
            self.label4.move(350,180)
            self.label4.show()

        elif x == 3:
            self.label4.hide()
            self.label5 = QLabel(self)
            self.label5.setFixedSize(QSize(200,100))
            self.label5.setText('Enter your Deadlift PR and press Enter:')
            self.label5.move(350,180)
            self.label5.show()
            
    def initUI(self):

        self.title = QLabel(self)
        self.title.setFixedSize(QSize(500,50))
        self.title.setText('Update Personal Records')
        self.title.move(200,30)
        self.title.setFont(QFont('Arial', 30))

        # Back button
        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoMainMenu)
        
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
            os.remove('prs.txt')
            self.keep = ' '.join(str(e) for  e in self.arr)
            f = open("prs.txt", 'a')
            f.write(self.keep)
            f.close()
            self.gotoMainMenu()
            mainWindow = mainMenu()
            widget.addWidget(mainWindow)
            widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoMainMenu(self):
        main_screen = mainMenu()
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
        self.title.setFixedSize(QSize(400,50))
        self.title.setText('Program')
        self.title.move(330,30)
        self.title.setFont(QFont('Arial', 30))

        self.instructions = QLabel(self)
        self.instructions.setFixedSize(QSize(600,100))
        self.instructions.setText('Instructions: Enter your week and day desired, press enter to confirm, and press the \"Confirm\" button to proceed.')
        self.instructions.move(100,50)

        self.weeklabel = QLabel(self)
        self.weeklabel.setFixedSize(QSize(200,100))
        self.weeklabel.setText('Week #:')
        self.weeklabel.move(200,110)

        self.daylabel = QLabel(self)
        self.daylabel.setFixedSize(QSize(200,100))
        self.daylabel.setText('Day #:')
        self.daylabel.move(500,110)

        self.weekinput = QLineEdit(self)
        self.weekinput.move(200,170)
        self.weekinput.returnPressed.connect(self.handleWeekInput)
        weekvalidator = QIntValidator()
        self.weekinput.setValidator(weekvalidator)

        self.dayinput = QLineEdit(self)
        self.dayinput.move(500,170)
        self.dayinput.returnPressed.connect(self.handleDayInput)
        dayvalidator = QIntValidator()
        self.dayinput.setValidator(dayvalidator)

        self.readybutton = QPushButton(self)
        self.readybutton.move(350,220)
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
        self.week.move(200,200)
        self.week.show()

    def handleDayInput(self):
        self.daytext = self.dayinput.text()
        self.day = QLabel(self)
        self.day.setText('Selected Day: ' + self.daytext)
        self.day.move(500,200)
        self.day.show()

    def accessProgram(self):
        try:
            x = program(self.squat, self.bench, self.deadlift, self.weektext, self.daytext)
            data_output = x.dataRetrieval()
            self.program_output = QLabel(self)
            self.program_output.setFixedSize(QSize(500,500))
            self.program_output.setText(data_output)
            self.program_output.move(200,120)
            self.program_output.show()
        except AttributeError:
            pass
    
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
        main_screen = mainMenu()
        widget.addWidget(main_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class displayPRs(QMainWindow):
    def __init__(self):
        super(displayPRs, self).__init__()
        self.dataGrab()
        self.initUI()

    def initUI(self):
        # Back Button
        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoMainMenu)
        
        self.title = QLabel(self)
        self.title.setFixedSize(QSize(350,50))
        self.title.setText('Personal Records')
        self.title.move(230,30)
        self.title.setFont(QFont('Arial', 30))

        # Title
        self.description = QLabel(self)
        self.description.setFixedSize(QSize(200,200))
        self.description.setText('Here are ' + self.name + '\'s current PR\'s:\n-----------------------------')
        self.description.move(325,100)

        self.squatlabel = QLabel(self)
        self.squatlabel.setFixedSize(QSize(200,100))
        self.squatlabel.setText('Squat: ' + self.squat)
        self.squatlabel.move(350,200)

        self.benchlabel = QLabel(self)
        self.benchlabel.setFixedSize(QSize(200,100))
        self.benchlabel.setText('Bench: ' + self.bench)
        self.benchlabel.move(350,250)

        self.deadliftlabel = QLabel(self)
        self.deadliftlabel.setFixedSize(QSize(200,100))
        self.deadliftlabel.setText('Deadlift: ' + self.deadlift)
        self.deadliftlabel.move(350,300)

        self.updatebutton = QPushButton(self)
        self.updatebutton.move(670,20)
        self.updatebutton.setText('Update PR\'s')
        self.updatebutton.clicked.connect(self.gotoUpdatePRs)
    
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
        main_screen = mainMenu()
        widget.addWidget(main_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoUpdatePRs(self):
        updateprs = updatePRs()
        widget.addWidget(updateprs)
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
            self.gotoHomeScreen()
    
    def gotoHomeScreen(self):
        home_screen = startScreen()
        widget.addWidget(home_screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    mainWindow = startScreen()
    widget.addWidget(mainWindow)
    widget.setWindowTitle('Workout Program')
    widget.setWindowIcon(QIcon('workout.png'))
    widget.setFixedSize(QSize(800,500)) 
    widget.show()
    sys.exit(app.exec())
