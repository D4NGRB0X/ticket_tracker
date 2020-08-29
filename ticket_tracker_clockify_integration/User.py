import config as c
import requests


class User:
    def __init__(self):
        self.endpoint = requests.get(c.default_endpoint + "user", headers=c.header).json()
        self.name = self.endpoint['name']
        self.workspace_id = self.endpoint["activeWorkspace"]
        self.user_id = self.endpoint["id"]
        self.email = self.endpoint["email"]
        self.info = [self.name, self.email, self.user_id, self.workspace_id]
        self.workspaces = requests.get(c.default_endpoint + "workspaces", headers=c.header).json()

    def start_timer(self):
        pass

    def end_timer(self):
        pass
