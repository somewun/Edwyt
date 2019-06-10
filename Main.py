
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *

def save():
    #showinfo("Save as", "This will be a save as function")
    name = asksaveasfile(mode='w', defaultextension=".txt")
    text2saveas = text.get(1.0, END)
    name.write(text2saveas)

def open():
    #showinfo("Open", "This will be an open function.")
    name = askopenfile(defaultextension=".txt")
    text2open = text.insert(1.0, name.read())
    text.write(text2open)
    name.close()

def help():
    showinfo("Help", "This is going to be a help list.")

def license():
    showinfo("License",
             """Edwyt, a simple lightweight text editor. Version 0.2
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
#root.iconbitmap(default="Edwyt Logo.png")

#app = interface.gui(root)

frame = Frame(root)
frame.pack(side=LEFT, fill=BOTH, expand = YES)

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
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
            bg="light blue",
            fg="black",
            font="verdana 10"
            )
text.pack(side=LEFT, fill=BOTH, expand = YES)

root.mainloop()






