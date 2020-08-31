import config
import requests


class User:
    def __init__(self):
        self.endpoint = requests.get(config.default_endpoint + "user", headers=config.header).json()
        self.name = self.endpoint['name']
        self.workspace_id = self.endpoint["activeWorkspace"]
        self.user_id = self.endpoint["id"]
        self.email = self.endpoint["email"]
        self.info = [self.name, self.email, self.user_id, self.workspace_id]
        self.workspaces = requests.get(config.default_endpoint + "workspaces", headers=config.header).json()

    def start_timer(self):
        pass

    def end_timer(self):
        pass
