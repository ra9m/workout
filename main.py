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
        # If there is PR data in the folder, it will be grabbed and user will be directed to home screen.
        # Otherwise, user will be prompted to enter in their info in New User Screen.
 
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
            self.gotoNewUserScreen()
    
    def initUI(self):
        # Doesn't work yet.
        #self.background = QLabel()
        #self.image = QPixmap('meme.png')
        #self.background.setPixmap(self.image)
        #self.background.hide()

        try:
            self.message = QLabel(self)
            self.message.setFixedSize(QSize(200,100))
            self.message.setText('Welcome back, ' + self.name + '.')
            self.message.move(350,320)
        except AttributeError:
            self.gotoNewUserScreen()

        self.title = QLabel(self)
        self.title.setFixedSize(QSize(600,280))
        self.title.setText('Workout\nProgram')
        self.title.setFont(QFont('Arial', 90))
        self.title.move(180,50)

        self.mysterybutton = QPushButton(self)
        self.mysterybutton.setFixedSize(QSize(150,50))
        self.mysterybutton.move(100,400)
        self.mysterybutton.setText('Mystery')
        self.mysterybutton.clicked.connect(self.mystery)

        self.mainMenubutton = QPushButton(self)
        self.mainMenubutton.setFixedSize(QSize(150,50))
        self.mainMenubutton.move(330,400)
        self.mainMenubutton.setText('Main Menu')
        self.mainMenubutton.clicked.connect(self.gotoMainMenu)

        self.timerbutton = QPushButton(self)
        self.timerbutton.setFixedSize(QSize(150,50))
        self.timerbutton.move(550,400)
        self.timerbutton.setText('Timer')
        self.timerbutton.clicked.connect(self.gotoTimer)
    
    def gotoNewUserScreen(self):
        widget.addWidget(newUserScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoMainMenu(self):
        widget.addWidget(mainMenuScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoTimer(self):
        widget.addWidget(timerScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def mystery(self):
        pass
        #self.background.show()

class timerScreen(QMainWindow):
    def __init__(self):
        super(timerScreen, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.title = QLabel(self)
        self.title.setFixedSize(QSize(200,100))
        self.title.setText('Timer')
        self.title.setFont(QFont('Arial', 30))
        self.title.move(350,20)

        self.startbutton = QPushButton(self)
        self.startbutton.move(150,350)
        self.startbutton.setText('Start')
        self.startbutton.clicked.connect(self.startTimer)

        self.stopbutton = QPushButton(self)
        self.stopbutton.move(350,350)
        self.stopbutton.setText('Stop')
        self.stopbutton.clicked.connect(self.stopTimer)

        self.resetbutton = QPushButton(self)
        self.resetbutton.move(550,350)
        self.resetbutton.setText('Reset')
        self.resetbutton.clicked.connect(self.resetTimer)

        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Home')
        self.backbutton.clicked.connect(self.gotoHomeScreen)

        # Initialize variables.
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.startwatch = False

        # Create time object.
        timer = QTimer(self)
        timer.timeout.connect(self.timeobject)
        timer.start(100)

        self.timedisplay = QLabel(self)
        self.timedisplay.move(350,200)
    
    def timeobject(self):
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
        self.timedisplay.setText('<h1 style="color:black">' + text + '</h1>')

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
        widget.addWidget(startScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class mainMenuScreen(QMainWindow):
    
    def __init__(self):
        super(mainMenuScreen, self).__init__()
        self.dataRetrieval()
        self.initUI()

    def dataRetrieval(self):
        with open('prs.txt') as file:
            lines = file.readlines()
            data = lines[0]
            li = list(data.split(" "))
            self.name = li[0]
            self.squat = li[1]
            self.bench = li[2]
            self.deadlift = li[3]
        
    def initUI(self):
        self.title = QLabel(self)
        self.title.setFixedSize(QSize(600,100))
        self.title.setFont(QFont('Arial', 80))
        self.title.setText('Main Menu')
        self.title.move(150,170)

        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoHomeScreen)

        self.programbutton = QPushButton(self)
        self.programbutton.setFixedSize(QSize(150,50))
        self.programbutton.move(50,350)
        self.programbutton.setText('Program')
        self.programbutton.clicked.connect(self.gotoProgramScreen)
        
        self.displaybutton = QPushButton(self)
        self.displaybutton.setText('Display Current PR\'s')
        self.displaybutton.move(325,350)
        self.displaybutton.setFixedSize(QSize(150,50))
        self.displaybutton.clicked.connect(self.gotoDisplayScreen)

        self.updatebutton = QPushButton(self)
        self.updatebutton.setText('Update Current PR\'s')
        self.updatebutton.move(600,350)
        self.updatebutton.setFixedSize(QSize(150,50))
        self.updatebutton.clicked.connect(self.gotoUpdateScreen)

    def gotoProgramScreen(self):
        widget.addWidget(programScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoDisplayScreen(self):
        widget.addWidget(displayScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoUpdateScreen(self):
        widget.addWidget(updateScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoHomeScreen(self):
        widget.addWidget(startScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class updateScreen(QMainWindow):
    def __init__(self):
        super(updateScreen, self).__init__()
        self.arr = []
        self.initUI()

    def display(self,x:int): # Display Message 
        if x == 0:
            self.message1 = QLabel(self)
            self.message1.setFixedSize(QSize(200,100))
            self.message1.setText('Enter your name and press Enter:')
            self.message1.move(350,180)
            
        elif x == 1:
            self.message1.hide()
            self.message2 = QLabel(self)
            self.message2.setFixedSize(QSize(200,100))
            self.message2.setText('Enter your Squat PR and press Enter:')
            self.message2.move(350,180)
            self.message2.show()
            
        elif x == 2:
            self.message2.hide()
            self.message3 = QLabel(self)
            self.message3.setFixedSize(QSize(200,100))
            self.message3.setText('Enter your Bench PR and press Enter:')
            self.message3.move(350,180)
            self.message3.show()

        elif x == 3:
            self.message3.hide()
            self.message4 = QLabel(self)
            self.message4.setFixedSize(QSize(200,100))
            self.message4.setText('Enter your Deadlift PR and press Enter:')
            self.message4.move(350,180)
            self.message4.show()
            
    def initUI(self):
        self.title = QLabel(self)
        self.title.setFixedSize(QSize(500,50))
        self.title.setText('Update Personal Records')
        self.title.move(200,30)
        self.title.setFont(QFont('Arial', 30))

        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoHomeScreen)
        
        # Initializes display messages
        self.counter = 0
        self.display(0)

        self.userinput = QLineEdit(self)
        self.userinput.move(350,250)
        self.userinput.returnPressed.connect(self.handleInput)
    
    def handleInput(self):
        self.counter += 1
        self.display(self.counter)
        self.temp = self.userinput.text()
        self.arr.append(self.temp)
        self.userinput.clear()
        if len(self.arr) == 4: # Once all the data necessary is entered, user is automatically directed to Home Screen.
            os.remove('prs.txt')
            data = ' '.join(str(e) for  e in self.arr)
            f = open("prs.txt", 'a')
            f.write(data)
            f.close()
            self.gotoHomeScreen()
    
    def gotoHomeScreen(self):
        widget.addWidget(startScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class programScreen(QMainWindow):
    def __init__(self):
        super(programScreen, self).__init__()
        self.dataRetrieval()
        self.initUI()

    def initUI(self):
        self.title = QLabel(self)
        self.title.setFixedSize(QSize(400,50))
        self.title.setText('Program')
        self.title.move(330,30)
        self.title.setFont(QFont('Arial', 30))

        self.readybutton = QPushButton(self)
        self.readybutton.move(350,220)
        self.readybutton.setText('Confirm')
        self.readybutton.clicked.connect(self.accessProgram)

        self.resetbutton = QPushButton(self)
        self.resetbutton.move(670,20)
        self.resetbutton.setText('Reset')
        self.resetbutton.clicked.connect(self.reset)

        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoMainMenu)

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
        self.weekinput.setValidator(QIntValidator())

        self.dayinput = QLineEdit(self)
        self.dayinput.move(500,170)
        self.dayinput.returnPressed.connect(self.handleDayInput)
        self.dayinput.setValidator(QIntValidator())
    
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

    def dataRetrieval(self):
        with open('prs.txt') as file:
            lines = file.readlines()
            data = lines[0]
            li = list(data.split(" "))
            self.name = li[0]
            self.squat = li[1]
            self.bench = li[2]
            self.deadlift = li[3]

    def gotoMainMenu(self):
        widget.addWidget(mainMenuScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class displayScreen(QMainWindow):
    def __init__(self):
        super(displayScreen, self).__init__()
        self.dataRetrieval()
        self.initUI()

    def initUI(self):
        self.title = QLabel(self)
        self.title.setFixedSize(QSize(350,50))
        self.title.setText('Personal Records')
        self.title.move(230,30)
        self.title.setFont(QFont('Arial', 30))

        self.description = QLabel(self)
        self.description.setFixedSize(QSize(200,200))
        self.description.setText('Here are ' + self.name + '\'s current PR\'s:\n-----------------------------')
        self.description.move(325,100)

        self.backbutton = QPushButton(self)
        self.backbutton.move(20,20)
        self.backbutton.setText('Back')
        self.backbutton.clicked.connect(self.gotoMainMenu)

        self.updatebutton = QPushButton(self)
        self.updatebutton.move(670,20)
        self.updatebutton.setText('Update PR\'s')
        self.updatebutton.clicked.connect(self.gotoUpdateScreen)

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
    
    def dataRetrieval(self):
        with open('prs.txt') as file:
            lines = file.readlines()
            data = lines[0]
            li = list(data.split(" "))
            self.name = li[0]
            self.squat = li[1]
            self.bench = li[2]
            self.deadlift = li[3]
            
    def gotoMainMenu(self):
        widget.addWidget(mainMenuScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoUpdateScreen(self):
        widget.addWidget(updateScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class newUserScreen(QMainWindow):
    def __init__(self):
        super(newUserScreen, self).__init__()
        self.arr = []
        self.initUI()

    def display(self,x:int): # Display Messages
        if x == 0:
            self.message1 = QLabel(self)
            self.message1.setFixedSize(QSize(200,100))
            self.message1.setText('Enter your name:')
            self.message1.move(350,250)
            
        elif x == 1:
            self.message1.hide()
            self.message2 = QLabel(self)
            self.message2.setFixedSize(QSize(200,100))
            self.message2.setText('Enter your Squat PR:')
            self.message2.move(350,250)
            self.message2.show()
            
        elif x == 2:
            self.message2.hide()
            self.message3 = QLabel(self)
            self.message3.setFixedSize(QSize(200,100))
            self.message3.setText('Enter your Bench PR:')
            self.message3.move(350,250)
            self.message3.show()

        elif x == 3:
            self.message3.hide()
            self.message4 = QLabel(self)
            self.message4.setFixedSize(QSize(200,100))
            self.message4.setText('Enter your Deadlift PR:')
            self.message4.move(350,250)
            self.message4.show()
            
    def initUI(self):
        self.instructions = QLabel(self)
        self.instructions.setFixedSize(QSize(500,100))
        self.instructions.setText('New User, please enter your info below and press Enter to proceed to the next step:')
        self.instructions.move(200,100)
        
        # Initializes the display messages.
        self.counter = 0
        self.display(0)

        self.userinput = QLineEdit(self)
        self.userinput.move(350,250)
        self.userinput.returnPressed.connect(self.handleInput)
    
    def handleInput(self):
        self.counter += 1
        self.display(self.counter)
        self.temp = self.userinput.text()
        self.arr.append(self.temp)
        self.userinput.clear()
        if len(self.arr) == 4: # Once all the data necessary is entered, user is automatically directed to Home Screen.
            self.keep = ' '.join(str(e) for  e in self.arr)
            f = open("prs.txt", 'a')
            f.write(self.keep)
            f.close()
            self.gotoHomeScreen()
    
    def gotoHomeScreen(self):
        widget.addWidget(startScreen())
        widget.setCurrentIndex(widget.currentIndex() + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    widget.addWidget(startScreen())
    widget.setWindowTitle('Workout Program')
    widget.setWindowIcon(QIcon('workout.png'))
    widget.setFixedSize(QSize(800,500)) 
    widget.show()
    sys.exit(app.exec())
