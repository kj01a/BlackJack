try: 
    import tkinter
except ImportError:
    import Tkinter as tkinter

def onclick():
    text = tkinter.Text(mainWindow)
    text.insert(tkinter.INSERT, "test")
    text.pack()

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("800x600")

button1 = tkinter.Button(mainWindow, text="Click button and see", command=onclick)
button1.pack(side = "left")

mainWindow.mainloop()