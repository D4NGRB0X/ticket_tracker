from tkinter import *
from main import projects

root = Tk()
root.title("Ticket Tracker")
root.geometry("1600x900")

main_frame = Frame(root)
main_frame.pack(pady=20)

button_frame = Frame(main_frame, label="Clients")
button_frame.grid(row=0, column=0)

user_input_frame = Frame(main_frame,)
user_input_frame.grid(row=1, column=0, pady=20)

buttons = [Button(button_frame, text=project) for project in projects]
for index, button in enumerate(buttons):
    button.grid(row=0, column=index, padx=10)

text_input = Entry(user_input_frame)
text_input.pack()

mainloop()
