from tkinter import *
from tkinter import ttk
from ticket_tracker_clockify_integration import utils


class Window(Tk):
    def __init__(self, title, geometry, *args, **kwargs):
        # Tk.__init__(self, *args, **kwargs)
        super(Window, self).__init__()
        self.title(title)
        self.geometry(geometry)
        self._frame = None


class WindowFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)


class ButtonFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)


class ProjectButtons(ButtonFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
