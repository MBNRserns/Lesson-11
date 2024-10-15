from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.title("Multiplication")

def openFile():
    fin=askopenfile(title="Open File")
    if fin is not None:
        listbox.delete(0, END)
        items = fin.readlines()
        for item in items:
            listbox.insert(END, item.strip())

def delItem():
    index = listbox.curselection()
    if index:
        listbox.delete(index)

def saveFile():
    fout=asksaveasfile(defaultextension=".txt")
    if fout is not None:
        for item in listbox.get(0,END):
            print(item.strip(),file=fout)
        listbox.delete(0,END)

def addItem():
    listbox.insert(END,item.get())
    item.delete(0,END)

fOpen=Button(root,text="Open", command=openFile,width=15)
fOpen.pack(side=LEFT, padx=5,pady=5)

fDel=Button(root,text="Delete", command=delItem,width=15)
fDel.pack(side=RIGHT, padx=5,pady=5)

fSave=Button(root,text="Save", command=saveFile,width=15)
fSave.pack(padx=5,pady=5)

fAdd=Button(root,text="Add", command=addItem,width=15)
fAdd.pack(padx=5,pady=5)

item=Entry(root,width=35)
item.pack(padx=5,pady=5)

frame = Frame(root)
scrollbar = Scrollbar(frame, orient = "vertical")
scrollbar.pack(side = RIGHT, fill=Y)
listbox=Listbox(frame, width=70, yscrollcommand=scrollbar.set, bg="gray")
for i in range(101):
    listbox.insert(END,"List"+ str(i))
listbox.pack(side = LEFT, padx=5)
scrollbar.config(command=listbox.yview)
frame.pack(side=RIGHT)

root.mainloop()