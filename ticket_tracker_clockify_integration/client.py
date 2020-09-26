import endpoint_config
import requests


class Client:
    def __init__(self, workspace_id):
        self.endpoint = requests.get(endpoint_config.default_endpoint + f"workspaces/{workspace_id}/clients",
                                     headers=endpoint_config.header).json()
        self.clients = {client['name']: client['id'] for client in self.endpoint}
