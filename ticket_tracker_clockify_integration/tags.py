import endpoint_config
import requests


class Tags:
    def __init__(self, workspace_id):
        self.tags = requests.get(
            endpoint_config.default_endpoint + f"workspaces/{workspace_id}/tags",
            headers=endpoint_config.header).json()

        self.tag_name = {tag['name']: tag['id'] for tag in self.tags}
