from datetime import datetime, timezone
from ticket_logger import *
import endpoint_config
import requests
from pprint import pprint
from collections import defaultdict
from user import User
from client import Client
from projects import Projects


user = User()
workspaceId = user.workspaces[0]["id"]
client = Client(workspaceId)
# projects = [(project['clientName'], {project['name']: project['id']}) for project in requests.get(projects_endpoint, headers=endpoint_config.header).json()]
# project_by_client = defaultdict(list)
#
# for client, project in projects:
#     project_by_client[client].append(project)





def main():
    does_log_dir_exist()
    does_daily_log_file_exist()

    while True:
        ##### ON CLIENT SELECTION CLICK #####
        for item in client.clients.keys():
            pprint(item)
        # pprint(list(clients.items()))  # turn this into buttons for UI
        select_client = input("Please select a client or Q to cancel: ")  # this will be accomplished by buttons in UI

        if select_client.upper() == "Q":
            break

        client_id = client.clients[select_client]
        projects = Projects(workspaceId, client_id)

        start_timer = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")
        if len(projects.project_client) > 1:
            for item in projects.project_client:
                print(item['name'])

            task = input("Please select a task: ")
            project_name_and_id = {project['name']: project['id'] for project in projects.project_client }
            project_id = project_name_and_id[task]

        ##### ONCE SELECTION MADE NEW PAGE #####
        notes = input("Notes: ")
        if notes.upper() == "RESET":
            continue

        description = input("Ticket Number: ")

        ###### ON SUBMIT #####
        stop_timer = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")
        payload = {
            "start": start_timer,
            "description": description,
            "projectId": project_id,
            "end": stop_timer,
        }
        time_entry_endpoint = endpoint_config.default_endpoint + f"workspaces/{workspaceId}/time-entries"
        this = requests.post(time_entry_endpoint, headers=endpoint_config.header, json=payload)
        daily_log_add_entry(client, payload, notes)
        print(this)
        print(client)
        print(payload)


if __name__ == "__main__":
    main()
