import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.input_text_variable = tk.StringVar()
        self.output_text_variable = tk.StringVar()
        
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        ACTION_BUTTON_TEXT = "Show backwards"
        
        DESCRIPTION_TEXT = "Type something into the box, then press " \
            + ACTION_BUTTON_TEXT
        self.description_label = tk.Label(self, text=DESCRIPTION_TEXT)
        self.description_label.pack()
        
        self.input_entry = tk.Entry(self,
            textvariable=self.input_text_variable)
        self.input_entry.pack()
        
        self.action_button = tk.Button(self, text=ACTION_BUTTON_TEXT,
            command=self.update_backwards_text_variable)
        self.action_button.pack()
        
        self.text_label = tk.Label(self, textvariable=self.output_text_variable)
        self.text_label.pack()
        
    def update_backwards_text_variable(self):
        backward_text = self.input_text_variable.get()[::-1]
        self.output_text_variable.set(backward_text)
        print("Output text was set to", backward_text)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
