from tkinter import Tk, Entry, Label, Button, Text, END, LabelFrame, messagebox
from RandomApp import RandomApp
root = Tk()
root.title("Psychic advisor")
root.geometry("200x200")

obj = RandomApp()

def messageBox(title, message,sign=False):

	if sign:
		messagebox.showinfo(title, message)
	elif not(sign):
		message = "Failed"
		messagebox.showerror(title, message)

def addElement():
	ele = textBox.get(0.0, END)
	obj.addOption(ele.split(" "))
	textBox.delete(0.0, END)
	messageBox("Add option", "Added Successful", True)

def resetElement():
	ele = textBox.get(0.0, END)
	obj.setOption(ele.split(" "))
	textBox.delete(0.0, END)
	messageBox("Reset option", "Reseted Successful",True)

def randomChoose():
	messageBox("Universe's signal", f"It's: {str(obj.getChoice())}", True)

# make screen
textBox = Text(root, width=20, height=5)
textBox.grid(column=0, columnspan=2, row=0)

addBtn = Button(root, text="Add option", command=addElement)
addBtn.grid(column=0, row=1, pady=5)

resetBtn = Button(root, text="Reset option", command=resetElement)
resetBtn.grid(column=1, row=1, pady=5)

getBtn = Button(root, text="Receive universe's signal", command=randomChoose)
getBtn.grid(column=0, columnspan=2, row=2)

root.mainloop()