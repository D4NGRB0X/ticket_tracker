import requests
import pprint
import config as c
from User import User


thomas = User()
workspaceId = thomas.workspaces[0]["id"]
clients = c.default_endpoint + f"workspaces/{workspaceId}/projects"

projects = {client["name"]: client['id'] for client in requests.get(clients, headers=c.header).json()}

pprint.pprint(projects.values())

