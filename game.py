import tkinter as tk


#This sets up the TK inter
root = tk.Tk()
#This sets the size of th window
root.geometry('1250x700')
#This sets up the Title of the Window
root.title("Into the Forest")
root.resizable(False,False)

def submit(name):
    text = ("Welcome {} !").format(name.get())
    Ltext = tk.Label(root, text = text, font = ("arial", 18))
    Ltext.pack()

intro = "Welcome to Into the Forest. Please enter your name."
name = tk.StringVar()
Lname = tk.Label(root, text = intro, font = ("arial", 18))
Ename = tk.Entry(root, textvariable = name, font = ("arial", 18))
bSubmit = tk.Button(root, text = 'Submit', command = lambda: submit(name))
Lname.pack()
Ename.pack()
bSubmit.pack()





root.mainloop()
