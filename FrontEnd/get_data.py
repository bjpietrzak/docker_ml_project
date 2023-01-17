import redis
import json

from dependencies.dependencies import servers


address, port = (servers["database_server"]["address"],
                 servers["database_server"]["port"])
rd = redis.Redis(address, port)

if rd.dbsize() == 0:
    raise RuntimeError("Database is empty")
else:
    database_values = {}
    for key in rd.keys():
        database_values[key.decode()] = rd.get(key).decode()
    with open('dump.json', 'w') as f:
        json.dump(database_values,f,indent=4)