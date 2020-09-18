import endpoint_config
from tkinter import *
from tkinter import ttk
from datetime import datetime, timezone
import requests
from user import User


user = User()
workspaceId = user.workspaces[0]["id"]
projects_endpoint = endpoint_config.default_endpoint + f"workspaces/{workspaceId}/projects"
projects = {
    client["clientName"].upper(): client['id'] for client in requests.get(
        projects_endpoint, headers=endpoint_config.header
    ).json()
    }

payload = {}


def clear_data():
    ticket.set("")
    scratch_pad.delete('1.0', END)
    client_label['text'] = "Client: "


def toggle_client_selection_on():
    scratch_pad['state'] = 'disabled'
    ticket_number['state'] = 'disabled'
    for item in buttons:
        item['state'] = 'normal'


def toggle_client_selection_off():
    scratch_pad['state'] = 'normal'
    ticket_number['state'] = 'normal'
    for item in buttons:
        item['state'] = 'disable'


def toggle_submit(*_):
    if ticket_number.get():
        submit['state'] = 'normal'
    else:
        submit['state'] = 'disabled'


def start_timer(client, project):
    client_label['text'] = f'Client: {client}'
    toggle_client_selection_off()
    scratch_pad.focus_set()
    payload['start'] = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")
    payload['projectId'] = project


def stop_timer():
    payload['end'] = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")


def submit():
    stop_timer()
    payload['description'] = ticket.get()
    time_entry_endpoint = endpoint_config.default_endpoint + f"workspaces/{workspaceId}/time-entries"
    requests.post(time_entry_endpoint, headers=endpoint_config.header, json=payload)
    clear_data()
    toggle_submit()
    toggle_client_selection_on()
    print(payload)


def reset():
    clear_data()
    toggle_submit()
    toggle_client_selection_on()


root = Tk()
root.title(f"{user.name} Ticket Tracker")
root.geometry("800x450")


main_frame = ttk.Frame(root)
main_frame.grid(row=0, rowspan=3, column=0, columnspan=3)

button_frame = Frame(main_frame, borderwidth=5, relief="sunken")
button_frame.grid(row=0, rowspan=3, column=0, sticky=NS)

buttons = [ttk.Button(
                button_frame,
                text=client,
                command=lambda client=client: start_timer(client, projects[client])
                ) for client in sorted(projects)]

for index, button in enumerate(buttons):
    button.grid(row=index, column=0, sticky=EW, pady=1)


user_input_frame = Frame(main_frame, borderwidth=5, relief="sunken")
user_input_frame.grid(row=0, column=1, pady=20)

client_label = ttk.Label(user_input_frame, text="Client:")
client_label.grid(row=0, column=0, sticky=NW, padx=20, pady=10)

reset = ttk.Button(user_input_frame, text="Reset", command=reset)
reset.grid(row=0, column=2, sticky=NE, padx=20, pady=10)

scratch_pad = Text(user_input_frame, state='disabled', width=60, height=15,)
scratch_pad.grid(row=1, column=0, columnspan=3, padx=20)


ticket_label = ttk.Label(user_input_frame, text="Ticket No. :")
ticket_label.grid(row=2, column=0, sticky=W, padx=10, pady=10)

ticket = StringVar()
ticket_number = ttk.Entry(user_input_frame, state='disabled', textvariable=ticket)
ticket_number.grid(row=2, column=0, sticky=E, pady=10)
ticket.trace_add('write', toggle_submit)

submit = ttk.Button(user_input_frame, text='Submit', state='disabled', command=submit)
submit.grid(row=2, column=2, sticky=SE, padx=20, pady=10)


mainloop()
