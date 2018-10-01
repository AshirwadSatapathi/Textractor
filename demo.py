import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import io
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract


root = tk.Tk()
root.title("Textractor")

locationS = ''
destination = ''
locationF = ''
l = ''



def openfile():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename)
    global locationS
    locationS = root.filename
    print(locationS)
    def set_text(locationS):
        entry1.delete(0,END)
        entry1.insert(0,locationS)
        return
    set_text(locationS)
    
def destination():
    #root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    root.filename = filedialog.askdirectory()
    print (root.filename)
    global destination
    destination=root.filename
    print(destination)
    def set_text(destination):
        entry2.delete(0,END)
        entry2.insert(0,destination)
        return
    set_text(destination)
    #destination = destination.replace("\\", "/")
    #print(destination)
    
def check():
    filename = entry3.get()
    if(len(filename)!=0):
        global locationF
        locationF = destination+"/"+filename
        print(locationF)
        if(os.path.isfile(destination+"/"+filename)):
            print("True")
            messagebox.showinfo("Textractor","File Exists......Be more creative with the name.")
        else:
            messagebox.showinfo("Textractor", "File does not exit...you are ready to go.")
            print("False")
    else:
        messagebox.showinfo("Textractor","Please enter a file name.")

def abc():
    print("this starts executing")
    print(locationS)
    print(destination)
    print(locationF)

def callback(locationS,l):
    print('hello world')
#    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract"
#    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe' 
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    print("working still")
    result = pytesseract.image_to_string(Image.open(locationS), lang=l)

    with io.open(locationF, mode='w',encoding="utf-8") as file:
        file.write(result)
        print('See the magic file dude!')

    print(result)

def convert():
    print(number.get())
    global l
    l = ''
    if(number.get() == "Select a Languag"):
        messagebox.showinfo("Textractor","Please choose a valid language")
    elif(number.get() == "English"):
        l = 'eng'
        print(l)
    elif(number.get() == "Hindi"):
        l = 'hin'
        print(l)
    elif(number.get() == "Tamil"):
        l = 'tam'
        print(l)
    elif(number.get() == "Odiya"):
        l= 'ori'
        print(l)
    else:
        l = 'tel'
        print(l)
        
    callback(locationS,l)
    # If you don't have tesseract executable in your PATH, include the following:
   
       
label1 = Label(root, text = 'Enter source location:')
label1.grid(row=0,column=0)
label2 = Label(root, text = 'Enter Destination:')
label2.grid(row=1,column=0)
label3 = Label(root, text = 'Enter the name of the file')
label3.grid(row=2, column=0)
label4 = Label(root, text = 'Select the language')
label4.grid(row=3, column=0)

entry1 = Entry(root, width = 50)
entry1.grid(row=0,column = 1)
entry2 = Entry(root, width = 50)
entry2.grid(row = 1, column =1)
entry3 = Entry(root, width = 50)
entry3.grid(row = 2, column = 1)





    
#ttk.Label(win, text="Choose a number:").grid(column=1, row=0)  # 1
number = tk.StringVar()                         # 2
numberChosen = ttk.Combobox(root, width=47, textvariable=number) #3
numberChosen['values'] = ('Select a Language','English','Hindi','Tamil','Odiya','Telegu')     # 4
numberChosen.grid(column=1, row=3)              # 5
numberChosen.current(0)   
    
submit = Button(root, text = "Convert", command = convert)
submit.grid(row = 4, column = 1)
open1 = Button(root, text = "open", command = openfile)
open1.grid(row = 0,column = 2)
dest1 = Button(root, text = "dest", command = destination)
dest1.grid(row = 1,column = 2)
check = Button(root, text = "check", command = check)
check.grid(row=2, column=2)


root.mainloop()
