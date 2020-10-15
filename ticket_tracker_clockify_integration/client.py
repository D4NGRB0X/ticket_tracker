import endpoint_config
import requests


class Client:
    def __init__(self, workspace_id):
        self.endpoint = requests.get(endpoint_config.default_endpoint + f"workspaces/{workspace_id}/projects",
                                     headers=endpoint_config.header).json()
        self.clients = {client['clientName']: client['clientId']
                        for client in self.endpoint if client['clientName'] != ''}
