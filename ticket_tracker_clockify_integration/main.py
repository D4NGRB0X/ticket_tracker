import requests
import endpoint_config
from User import User
from datetime import datetime, timezone

user = User()
workspaceId = user.workspaces[0]["id"]
projects_endpoint = endpoint_config.default_endpoint + f"workspaces/{workspaceId}/projects"

projects = {
    client["clientName"]: client['id'] for client in requests.get(
        projects_endpoint, headers=endpoint_config.header
    ).json()
}

while True:
    ##### ON CLIENT SELECTION CLICK #####
    print(list(projects))  # turn this into buttons for UI
    client = input("Please select a client: ")  # this will be accomplished by buttons in UI

    if client.upper() == "QUIT":
        break

    start_timer = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")

    ##### ONCE SELECTION MADE NEW PAGE #####
    description = input("Ticket Number: ")

    if description.upper() == "QUIT":
        break

    ###### ON SUBMIT #####
    stop_timer = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")
    payload = {
        "start": start_timer,
        "description": description,
        "projectId": projects[client],
        "end": stop_timer,
    }
    time_entry_endpoint = endpoint_config.default_endpoint + f"workspaces/{workspaceId}/time-entries"
    add_time_entry = requests.post(time_entry_endpoint, headers=endpoint_config.header, json=payload)
