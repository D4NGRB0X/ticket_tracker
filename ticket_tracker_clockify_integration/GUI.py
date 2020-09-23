from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self, title, geometry, *args, **kwargs):
        # Tk.__init__(self, *args, **kwargs)
        super(Window, self).__init__()
        self.title(title)
        self.geometry(geometry)
        container = Frame(self)
        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

    #     self.frames = {}
    #     frame = WindowFrame(container, self)
    #     self.frames[WindowFrame] = frame
    #     frame.grid(row=0, column=0, sticky=NSEW)
    #
    # def show_frame(self, controller):
    #     frame = self.frame[controller]
    #     frame.tkraise()


class WindowFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)


class ButtonFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)


class UserInputFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)


class ClientButtons(ButtonFrame):
    def __init__(self):
        super().__init__()


class ProjectButtons(ButtonFrame):
    def __init__(self):
        super().__init__()
