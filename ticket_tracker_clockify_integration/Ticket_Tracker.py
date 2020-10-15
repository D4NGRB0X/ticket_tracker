import endpoint_config
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timezone
import requests
from user import User
from gui import Window, WindowFrame, ButtonFrame, ProjectButtons
from client import Client
from projects import Projects
from tags import Tags


user = User()
workspaceId = user.workspaces[0]["id"]
clients = Client(workspaceId)
tags = Tags(workspaceId)
project_name_and_id = {}
payload = {}


def tag_select():
    tag_list = [tag_var.get()]
    payload['tagIds'] = tag_list


def clear_data():
    ticket.set("")
    scratch_pad.delete('1.0', tk.END)
    client_label['text'] = "Client: "
    project_name_and_id.clear()
    toggle_submit()
    tag_var.set(None)
    payload.clear()


def set_button_location(buttons):
    for index, button in enumerate(buttons):
        button.grid(row=index, column=0, sticky=tk.EW, pady=1)


def toggle_client_selection_on():
    scratch_pad['state'] = 'disabled'
    ticket_number['state'] = 'disabled'
    for item in client_buttons:
        item['state'] = 'normal'


def toggle_client_selection_off():
    scratch_pad['state'] = 'normal'
    ticket_number['state'] = 'normal'
    for item in client_buttons:
        item['state'] = 'disable'


def toggle_submit(*_):
    if ticket_number.get():
        submit['state'] = 'normal'
    else:
        submit['state'] = 'disabled'


def select_project(project_id, project_frame):
    payload['projectId'] = project_id
    project_frame.destroy()
    project_name_and_id.clear()


def select_client(client_selection):
    client_label['text'] = f'Client: {client_selection}'
    project = Projects(workspaceId, clients.clients[client_selection])
    toggle_client_selection_off()
    scratch_pad.focus_set()
    payload['start'] = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")
    project_name_and_id.update({p['name']: p['id'] for p in project.project_client})
    if len(project_name_and_id) > 1:
        project_frame = ProjectButtons(button_frame, borderwidth=5)
        project_frame.grid(row=0, column=1, sticky=tk.NSEW)
        project_buttons = [ttk.Button(
            project_frame,
            text=project_item,
            command=lambda project_item=project_item: select_project(project_name_and_id[project_item], project_frame)
        ) for project_item in project_name_and_id.keys()]

        set_button_location(project_buttons)
    else:
        payload['projectId'] = [value for value in project_name_and_id.values()][0]


def submit():
    payload['end'] = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")
    payload['description'] = ticket.get()
    time_entry_endpoint = endpoint_config.default_endpoint + f"workspaces/{workspaceId}/time-entries"
    requests.post(time_entry_endpoint, headers=endpoint_config.header, json=payload)
    clear_data()
    toggle_client_selection_on()
    button_frame.lift()


main_window = Window(f'{user.name} Ticket Tracker', '750x425')

main_frame = WindowFrame(main_window, borderwidth=5)
main_frame.grid(row=0, rowspan=3, column=0, columnspan=3)

button_frame = ButtonFrame(main_frame, borderwidth=5, relief="sunken")
button_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)

client_frame = ProjectButtons(button_frame, borderwidth=5)
client_frame.grid(row=0, column=0, sticky=tk.NSEW)

client_buttons = [ttk.Button(client_frame,
                             text=client,
                             command=lambda client=client: select_client(client)
                             ) for client in clients.clients]

set_button_location(client_buttons)


user_input_frame = ttk.Frame(main_frame, borderwidth=5, relief="sunken")
user_input_frame.grid(row=0, column=1, padx=10, pady=20)

tag_select_frame = ttk.Frame(user_input_frame)
tag_select_frame.grid(row=0, column=0, sticky='w', padx=15)

tag_label = client_label = ttk.Label(tag_select_frame, text="Optional Tag:")
client_label.grid(row=0, column=0, sticky=tk.W)

tag_var = tk.StringVar()
tag_select = [ttk.Radiobutton(tag_select_frame,
                              text=tag,
                              variable=tag_var,
                              value=tags.tag_name[tag],
                              command=tag_select) for tag in tags.tag_name.keys()]
for index, tag in enumerate(tag_select):
    tag.grid(row=0, column=index + 1, ipadx=1)


client_label = ttk.Label(user_input_frame, text="Client:")
client_label.grid(row=1, column=0, sticky=tk.NW, padx=20, pady=10)

reset = ttk.Button(user_input_frame,
                   text="Reset",
                   command=lambda: [clear_data(), toggle_client_selection_on()])
reset.grid(row=1, column=0, sticky=tk.NE, padx=20, pady=10)

scratch_pad = tk.Text(user_input_frame, state='disabled', width=60, height=15,)
scratch_pad.grid(row=2, column=0, sticky='w', padx=10)

ticket_label_frame = ttk.Frame(user_input_frame)
ticket_label_frame.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
ticket_label = ttk.Label(ticket_label_frame, text="Ticket No. :")
ticket_label.pack(anchor='w')

ticket = tk.StringVar()
ticket_number = ttk.Entry(ticket_label_frame, state='disabled', textvariable=ticket)
ticket_number.pack(anchor='e')
ticket.trace_add('write', toggle_submit)

submit = ttk.Button(user_input_frame, text='Submit', state='disabled', command=submit)
submit.grid(row=3, column=0, sticky=tk.SE, padx=20, pady=10)

tk.mainloop()

