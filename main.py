import tkinter as tk
import tkinter.font as tkFont

TITLE = 'SudoDydy'

class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack()

        self.helv36 = tkFont.Font(self, family='Helvetica', size=36, weight='bold')

        self.load_widget()

    def load_widget(self):
        sudo = Sudoku(self)
        buttons = Commands(self)

class Sudoku(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack()

        self.sudo_input = None

        self.load_widget()

    def load_widget(self):
        self.sudo_input = [[Patch(self,i,j) for i in range(3)]for j in range(3)]

class Patch(tk.Frame):

    def __init__(self, master=None, i=0, j=0):
        super().__init__(master=master, borderwidth=3, relief='sunken')
        self.grid(column=i, row=j)

        self.patch_input = None

        self.load_widget()

    def load_widget(self):
        self.patch_input = [[tk.Entry(self, justify='center', width = 2, font=self.master.master.helv36, borderwidth=2, relief='groove') for i in range(3)]for j in range(3)]

        for i in range(3):
            for j in range(3):
                self.patch_input[i][j].grid(column = i, row = j)

class Commands(tk.Frame):

    def __init__(self, master=None, i=0, j=0):
        super().__init__(master=master, bg='#000')
        self.pack(fill=tk.BOTH)

        self.load_widget()

    def load_widget(self):

        self.columnconfigure(0, weight=1)
        Gen_Button = tk.Button(self, text='Generate', font=self.master.helv36, relief='groove', borderwidth=3)
        Gen_Button.grid(column=0, row=0, sticky='nsew')

        self.columnconfigure(1, weight=1)
        Verif_Button = tk.Button(self, text='Check', font=self.master.helv36, relief='groove', borderwidth=3)
        Verif_Button.grid(column=1, row=0, sticky='nsew')

root = tk.Tk()
app = App(root)
app.master.title(TITLE)
app.master.resizable(False, False)
app.mainloop()