import tkinter as tk
"""Very simple application which showcases a window with a clickable button.
When the button is clicked, "Action!" is written to the terminal.
"""
# We import tkinter as tk since we'll be using tkinter.something a lot
# This is common: e.g. `import numpy as np`

class Application(tk.Frame):
    def __init__(self, master=None):
        #Calls __init__ on our superclass, tk.Frame
        super().__init__(master)
        
        self.pack()
        self.create_widgets()
        
    def action(self):
        print("Action!")

    def create_widgets(self):
        #Creates a Button, with the text "Go". When pressed, the method
        # (= a function in a class) self.action will be called
        self.knapp = tk.Button(self, text="Go", command=self.action)
        
        #Packs the button into the layout
        self.knapp.pack()

#tk.Tk() is a "Toplevel widget of Tk which represents mostly the main window of
#              an application."
root = tk.Tk()
#help(root)


#Application is a "Frame widget which may contain other widgets and can have a
#                  3D border."
# Note that each Application must have a master, in this case to associate our
#frame widget with the main window.
app = Application(master=root)
#help(app)

#Uncomment the below line to see what'll happen if we use the base class
# tk.Frame
#app = tk.Frame(master=root)

app.mainloop()
