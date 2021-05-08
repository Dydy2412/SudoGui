import tkinter as tk
import tkinter.font as tkFont
from sudo_lib import displayer

TITLE = 'SudoDydy'

class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack(expand=True)

        self.helv36 = tkFont.Font(self, family='Helvetica', size=36, weight='bold')

        self.sudo = Sudoku(self)
        self.buttons = Commands(self)

        self.load_widget()

    def load_widget(self):
        pass

class Sudoku(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack()

        self.sudo_input = None

        self.load_widget()

    def load_widget(self):
        self.sudo_input = [[Patch(self,i,j) for i in range(3)]for j in range(3)]

    def set_input(self, x,y):
        pass

    def get_sudo(self):
        return self.sudo_input

class Patch(tk.Frame):

    def __init__(self, master=None, i=0, j=0):
        super().__init__(master=master, borderwidth=3, relief='sunken')
        self.grid(column=i, row=j)

        self.stringVars = None
        self.patch_input = None

        self.load_widget()

    def load_widget(self):
        self.stringVars = [[tk.StringVar(self) for i in range(3)] for j in range(3)]
        self.patch_input = [[tk.Entry(self, justify='center', width = 2, font=self.master.master.helv36, borderwidth=2, relief='groove', textvariable=self.stringVars[i][j]) for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                print(self.stringVars[i][j])
                self.stringVars[i][j].trace('w', self.on_input)
                self.patch_input[i][j].grid(column = i, row = j)

    def on_input(self, *args):
        var = self.getvar(args[0])
        print(var.get())

    def get_patchs(self):
        return self.patch_input

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
        Verif_Button = tk.Button(self, text='Check', font=self.master.helv36, relief='groove', borderwidth=3, command=self.on_check)
        Verif_Button.grid(column=1, row=0, sticky='nsew')

    def on_check(self):
        print(self.master.sudo.get_sudo()[0][0].get_patchs()[0][0].get())

root = tk.Tk()
app = App(root)
app.master.title(TITLE)
# app.master.resizable(False, False)
app.mainloop()