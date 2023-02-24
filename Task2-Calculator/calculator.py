# Python program to create a simple GUI
# calculator using Tkinter

from tkinter import *
Expression = ""

# Function to update expression
def btnPress(num):
	global Expression

	expression = Expression + str(num)
	equation.set(Expression)

# Function to evaluate the final exbtnPression
def Equalpress():
	
	try:

		global Expression
		total = str(eval(Expression))
		equation.set(total)
		Expression = ""

	except:

		equation.set(" error ")
		Expression = ""

def clear():
	global Expression
	Expression = ""
	equation.set("")

# Driver code
if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="light cyan")
	gui.title("Code Clause Calculator")
	gui.geometry("270x150")
	equation = StringVar()

	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70)

	button1 = Button(gui, text=' 1 ', fg='black', bg='orange',
					command=lambda: btnPress(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='orange',
					command=lambda: btnPress(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='orange',
					command=lambda: btnPress(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='orange',
					command=lambda: btnPress(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='orange',
					command=lambda: btnPress(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='orange',
					command=lambda: btnPress(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='orange',
					command=lambda: btnPress(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='orange',
					command=lambda: btnPress(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='orange',
					command=lambda: btnPress(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='orange',
					command=lambda: btnPress(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='orange',
				command=lambda: btnPress("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='orange',
				command=lambda: btnPress("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='orange',
					command=lambda: btnPress("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='orange',
					command=lambda: btnPress("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='orange',
				command=Equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='orange',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='black', bg='orange',
					command=lambda: btnPress('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)
	
	gui.mainloop()
