try:
    import endpoint_config
except:
    pass

import requests


class User:
    def __init__(self):
        self.endpoint = requests.get(endpoint_config.default_endpoint + "user", headers=endpoint_config.header).json()
        self.name = self.endpoint['name']
        self.workspace_id = self.endpoint["activeWorkspace"]
        self.user_id = self.endpoint["id"]
        self.email = self.endpoint["email"]
        self.info = [self.name, self.email, self.user_id, self.workspace_id]
        self.workspaces = requests.get(
            endpoint_config.default_endpoint + "workspaces", headers=endpoint_config.header
        ).json()

