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
