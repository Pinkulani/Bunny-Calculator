from tkinter import *

class CalcGUI():
    def __init__(self):
        self.Window = Tk()
        self.Window.title('Calc')
        self.Window.geometry('500x500')
        
        self.LabelFrame = LabelFrame(self.Window, text = 'Calculator', bg = 'red')
        self.LabelFrame.place(x = 0, y = 0, width = 500, height = 100)

        self.LabelInput = Label(self.LabelFrame, text = 'Input', bg = 'red')
        self.LabelInput.place(x = 20, y = 20, width = 50, height = 20)

        mainloop()

class Controller():
    def __init__(self):
        CalcGUI()

if __name__ == '__main__':
    App = Controller()