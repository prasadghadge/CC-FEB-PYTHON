# Python program to create a simple GUI
# calculator using Tkinter

from tkinter import *

Expression = ""

def Press(a):
	
	global Expression

	Expression = Expression + str(a)

	equation.set(Expression)

def Equal():
	
	try:

		global Expression

		total = str(eval(Expression))

		equation.set(total)

		Expression = ""

	except:

		equation.set(" Error ")
		Expression = ""

def clear():
	global Expression
	Expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	
	gui = Tk()

	gui.configure(background="light green")

	gui.title("Code Clause Calculator")

	gui.geometry("540x270")

	equation = StringVar()

	
	expression_field = Entry(gui, textvariable=equation)

	expression_field.grid(columnspan=4, ipadx=200)

	
	button1 = Button(gui, text=' 1 ', fg='black', bg='orange',
					command=lambda: Press(1), height=2, width=14)
	button1.grid(row=3, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='orange',
					command=lambda: Press(2), height=2, width=14)
	button2.grid(row=3, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='orange',
					command=lambda: Press(3), height=2, width=14)
	button3.grid(row=3, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='orange',
					command=lambda: Press(4), height=2, width=14)
	button4.grid(row=4, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='orange',
					command=lambda: Press(5), height=2, width=14)
	button5.grid(row=4, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='orange',
					command=lambda: Press(6), height=2, width=14)
	button6.grid(row=4, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='orange',
					command=lambda: Press(7), height=2, width=14)
	button7.grid(row=5, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='orange',
					command=lambda: Press(8), height=2, width=14)
	button8.grid(row=5, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='orange',
					command=lambda: Press(9), height=2, width=14)
	button9.grid(row=5, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='orange',
					command=lambda: Press(0), height=2, width=14)
	button0.grid(row=6, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='orange',
				command=lambda: Press("+"), height=2, width=14)
	plus.grid(row=3, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='orange',
				command=lambda: Press("-"), height=2, width=14)
	minus.grid(row=4, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='orange',
					command=lambda: Press("*"), height=2, width=14)
	multiply.grid(row=5, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='orange',
					command=lambda: Press("/"), height=2, width=14)
	divide.grid(row=6, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='orange',
				command=Equal, height=2, width=14)
	equal.grid(row=6, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='orange',
				command=clear, height=2, width=14)
	clear.grid(row=6, column='1')

	Decimal= Button(gui, text='.', fg='black', bg='orange',
					command=lambda: Press('.'), height=2, width=14)
	Decimal.grid(row=7, column=0)
	
	gui.mainloop()
