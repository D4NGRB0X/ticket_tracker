import requests
import pprint
import config
from User import User
from datetime import datetime, timezone
import time


start_timer = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")
start_payload = {
  "start": datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z"),
  "projectId": "5f499d8cae312e0f227fd624",
}

thomas = User()
workspaceId = thomas.workspaces[1]["id"]
projects_endpoint = config.default_endpoint + f"workspaces/{workspaceId}/projects"

projects = {client["name"]: client['id'] for client in requests.get(projects_endpoint, headers=config.header).json()}

timer_start_response = requests.post(
  config.default_endpoint + f"workspaces/{workspaceId}/time-entries", headers=config.header, json=start_payload)

time.sleep(10)

stop_payload = {
  "end": datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z"),
}
timer_stop_response = requests.patch(
  config.default_endpoint + f"workspaces/{workspaceId}/user/{thomas.user_id}/time-entries",
  headers=config.header, json=stop_payload
  )