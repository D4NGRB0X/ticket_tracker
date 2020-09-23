import endpoint_config
import requests


class Projects:
    def __init__(self, workspace_id, client_id):
        self.projects = requests.get(
            endpoint_config.default_endpoint + f"workspaces/{workspace_id}/projects",
            headers=endpoint_config.header).json()

        self.project_client = requests.get(
            endpoint_config.default_endpoint + f"workspaces/{workspace_id}/projects",
            params={'clients': client_id},
            headers=endpoint_config.header).json()
