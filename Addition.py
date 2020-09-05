from tkinter import*
import tkinter.messagebox

class GUI_Beginners:
    def __init__(self, root):
        self.root = root
        self.root.title("Addition")
        self.root.geometry("600x300+0+0")
        
        frame1 = Frame(self.root)
        frame1.grid()
        
        frame2 = Frame(frame1, width = 600, height = 200, padx = 20,bd = 16, relief = RIDGE)
        frame2.grid(row = 0, column = 0)
        
        frame3 = Frame(frame1, width = 600, height = 150, padx = 36,bd = 16, relief = RIDGE)
        frame3.grid(row = 1, column = 0)
        
        FirstNum = StringVar()
        SecondNum = StringVar()
        Result = StringVar()
        
        self.lblFirstNum = Label(frame2, text = 'Enter First Number', font = ('arial', 14, 'bold'), bd = 12)
        self.lblFirstNum.grid(row = 0, column = 0, sticky = W)
        self.txtFirstNum = Entry(frame2, textvariable = FirstNum, font = ('arial', 14, 'bold'), bd = 12)
        self.txtFirstNum.grid(row = 0, column = 1)
        
        self.lblSecondNum = Label(frame2, text = 'Enter Second Number', font = ('arial', 14, 'bold'), bd = 12)
        self.lblSecondNum.grid(row = 1, column = 0, sticky = W)
        self.txtSecondNum = Entry(frame2, textvariable = SecondNum, font = ('arial', 14, 'bold'), bd = 12)
        self.txtSecondNum.grid(row = 1, column = 1)
        
        self.lblResult = Label(frame2, text = 'Show Result', font = ('arial', 14, 'bold'), bd = 12)
        self.lblResult.grid(row = 2, column = 0, sticky = W)
        self.txtResult = Entry(frame2, textvariable = Result, font = ('arial', 14, 'bold'), bd = 12)
        self.txtResult.grid(row = 2, column = 1)
       
        def add():
            f = float(FirstNum.get())
            s = float(SecondNum.get())
            r = f + s
            Result.set(r)
                
        def Reset():
            FirstNum.set("")
            SecondNum.set("")
            Result.set("")
            
        def Exit():
            root.destroy()
            
        self.btnTotal = Button(frame3, text = "Total",font = ('arial', 14, 'bold'), bd = 12, pady = 14, padx = 12, width = 7, command = add).grid(row =0, column = 0)
        self.btnReset = Button(frame3, text = "Reset",font = ('arial', 14, 'bold'), bd = 12, pady = 14, padx = 12, width = 7, command = Reset).grid(row =0, column = 1)
        self.btnExit = Button(frame3, text = "Exit",font = ('arial', 14, 'bold'), bd = 12, pady = 14, padx = 12, width = 7, command = Exit).grid(row =0, column = 2)
        
        
if __name__ == '__main__':
    root = Tk()
    application = GUI_Beginners(root)
    root.mainloop()