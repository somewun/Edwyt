
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *

def new():
    
    result = askyesno("New File","Do you want to open a new file, all unsaved work will be lost.")
    if result == True:
        text.delete(1.0, END)
    else:
        return

def save():

    name = asksaveasfile(mode='w', defaultextension=".txt")
    text2saveas = text.get(1.0, END)
    name.write(text2saveas)

def open():
    
    name = askopenfile(defaultextension=".txt")
    result = askyesno("Open File","Do you want to open a new file, all unsaved work will be lost.")
    if result == True:
        text.delete(1.0, END)
        text2open = text.insert(1.0, name.read())
        text.write(text2open)
    else:
        return

def help():
    
    showinfo("Help", "This is going to be a help list.")

def license():
    
    showinfo("License",
             """Edwyt, a simple lightweight text editor. Version 0.2.2
                Copyright (C) 2019  Somewun

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.""")

root = Tk()
root.title("Edwyt")
root.minsize(200,100)

frame = Frame(root)
frame.pack(side=LEFT, fill=BOTH, expand = YES)

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open...", command=open)
filemenu.add_command(label="Save...", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="About", menu=helpmenu)
helpmenu.add_command(label="About", command=help)
helpmenu.add_command(label="license", command=license)

text = ScrolledText(
            frame, width=50, height=25,
            bg="LightGoldenrod1",
            fg="black",
            font=("Comic Sans MS", 12),
            wrap=WORD
            )
text.pack(side=LEFT, fill=BOTH, expand = YES)

root.mainloop()






