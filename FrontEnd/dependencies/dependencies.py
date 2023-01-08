import json


server_path_json = "dependencies/servers.json"

with open(server_path_json) as f:
  servers = json.load(f)
