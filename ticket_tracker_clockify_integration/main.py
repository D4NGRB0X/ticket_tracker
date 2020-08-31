import requests
import pprint
import config
from User import User
from datetime import datetime, timezone
import time


thomas = User()
workspaceId = thomas.workspaces[0]["id"]
projects_endpoint = config.default_endpoint + f"workspaces/{workspaceId}/projects"

projects = {client["clientName"]: client['id'] for client in requests.get(projects_endpoint, headers=config.header).json()}

pprint.pprint(projects)
client = input("Please select a client:")
start_timer = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")
description = input("Ticket Number:")
time.sleep(10)
stop_timer = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")

payload = {
  "start": start_timer,
  "description": description,
  "projectId": projects[client],
  "end": stop_timer,
}

time_entry_endpoint = config.default_endpoint + f"workspaces/{workspaceId}/time-entries"

add_time_entry = requests.post(time_entry_endpoint, headers=config.header, json=payload)


pprint.pprint(add_time_entry)
