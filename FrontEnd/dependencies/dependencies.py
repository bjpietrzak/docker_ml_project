import json


server_json_path = "dependencies/servers.json"
storage_json_path = "dependencies/storage.json"

with open(server_json_path) as server_file:
  servers = json.load(server_file)

with open(storage_json_path) as storage_file:
  storage = json.load(storage_file)
