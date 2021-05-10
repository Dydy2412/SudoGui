import tkinter as tk
import tkinter.font as tkFont
from sudo_lib import displayer
from time import time
from uuid import uuid1

TITLE = 'SudoDydy'

class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack(expand=True)

        self.helv36 = tkFont.Font(self, family='Helvetica', size=36, weight='bold')
        self.helv20 = tkFont.Font(self, family='Helvetica', size=20, weight='bold')

        self.sudo = Sudoku(self, self.helv36)
        self.buttons = Commands(self, font=self.helv36, sudoku=self.sudo)

        self.load_widget()

    def load_widget(self):
        pass

class Sudoku(tk.Frame):

    def __init__(self, master=None, font=None):
        super().__init__(master=master)
        self.pack()

        self.sudo_input = None
        self.font = font

        self.load_widget()

    def load_widget(self):
        self.sudo_input = [[Patch(self, i,j, self.font) for i in range(3)]for j in range(3)]

    def set_input(self, x, y, data):
        self.get_var(x,y).set(data)

    def get_sudo(self):
        return self.sudo_input

    def get_cell(self,x,y):
        return self.sudo_input[x//3][y//3].get_patchs()[x%3][y%3]

    def get_var(self, x, y):
        return self.get_cell(x, y).var

class Patch(tk.Frame):

    def __init__(self, master=None, i=0, j=0, font=None):
        super().__init__(master=master, borderwidth=3, relief='sunken')
        self.grid(column=i, row=j)

        self.font = font
        self.stringVars = None
        self.patch_input = None

        self.load_widget()

    def load_widget(self):
        self.patch_input = [[SudoEntry(self, justify='center', width = 2, font=self.font, borderwidth=2, relief='groove', row=i, column=j) for i in range(3)] for j in range(3)]

    def on_input(self, var_name):
        print(self.getvar(var_name))

    def get_patchs(self):
        return self.patch_input

class Commands(tk.Frame):

    def __init__(self, master=None, font=None, sudoku=None):
        super().__init__(master=master, bg='#000')
        self.pack(fill=tk.BOTH)

        self.font = font
        self.sudoku = sudoku

        self.load_widget()

    def load_widget(self):
        
        numpad = Numpad(master=self, font=self.font, sudoku=self.sudoku, relief='groove')

        self.columnconfigure(0, weight=1)
        Gen_Button = tk.Button(self, text='Generate', font=self.font, relief='groove', borderwidth=3)
        Gen_Button.grid(column=0, row=1, sticky='nsew')

        self.columnconfigure(1, weight=1)
        Verif_Button = tk.Button(self, text='Check', font=self.font, relief='groove', borderwidth=3, command=self.on_check)
        Verif_Button.grid(column=1, row=1, sticky='nsew')

    def on_check(self):
        self.sudoku.set_input(0, 0, '5')

class SudoEntry(tk.Entry):

    def __init__(self, master=None, font=None, justify=None, width = 1, borderwidth=0, relief=None, row=0, column=0):
        super().__init__(master=master, justify=justify, width = width, font=font, borderwidth=borderwidth, relief=relief)
        self.grid(row=row, column=column)

        self.var = tk.StringVar(self)
        self.config(textvariable=self.var)
        self.var.trace_add('write', lambda *args : self.on_write(self.var))

    def on_write(self, var):
        if len(var.get()) > 0:
            var.set(var.get()[:1])
            try:
                int(var.get())
            except:
                var.set('')

    def set(self, value):
        self.var.set(value)

class Numpad(tk.Frame):

    def __init__(self, master, font, sudoku, relief):
        super().__init__(master=master)
        self.grid(row=0, column=0, columnspan=2)

        self.numkeys = [NumKey(self, i, font, sudoku, relief) for i in range(0,10)]

class NumKey(tk.Button):

    def __init__(self, master=None, index=None, font=None, sudoku=None, relief=None):
        super().__init__(master=master, font=font, text=str(index) if index > 0 else 'X', relief=relief, command= lambda *args : self.on_input(index, sudoku))
        self.grid(row=0, column=index)

    def on_input(self, index, sudoku):
        try:
            sudoku.focus_get().set(index if index > 0 else '')
        except:
            print('select any column')

root = tk.Tk()
app = App(root)
app.master.title(TITLE)
app.mainloop()