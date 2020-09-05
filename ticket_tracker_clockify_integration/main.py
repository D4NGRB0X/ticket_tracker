from datetime import datetime, timezone
from ticket_logger import does_log_dir_exist, does_daily_log_file_exist, daily_log_add_entry
import endpoint_config
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


def main():
    does_log_dir_exist()
    does_daily_log_file_exist()

    while True:
        ##### ON CLIENT SELECTION CLICK #####
        print(list(projects))  # turn this into buttons for UI
        client = input("Please select a client: ").upper()  # this will be accomplished by buttons in UI

        if client.upper() == "Q":
            break

        if client.upper() == "RESET":
            continue
        start_timer = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")

        ##### ONCE SELECTION MADE NEW PAGE #####
        description = input("Ticket Number: ")

        if description.upper() == "Q":
            break
        if description.upper() == "RESET":
            continue

        ###### ON SUBMIT #####
        stop_timer = datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")
        payload = {
            "start": start_timer,
            "description": description,
            "projectId": projects[client],
            "end": stop_timer,
        }
        time_entry_endpoint = endpoint_config.default_endpoint + f"workspaces/{workspaceId}/time-entries"
        requests.post(time_entry_endpoint, headers=endpoint_config.header, json=payload)
        daily_log_add_entry(client, payload)


if __name__ == "__main__":
    main()
