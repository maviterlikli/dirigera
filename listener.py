import json
from typing import Any
import os
import dirigera

dirigera_hub = dirigera.Hub(
    token=os.environ['DIRIGERA_TOKEN'],
    ip_address=os.environ['DIRIGERA_IP']
)


def on_message(ws: Any, message: str):
    message_dict = json.loads(message)
    data = message_dict["data"]
    print(data)
    with open("log.txt", "a") as myfile:
        myfile.write(str(data))
        myfile.write("\n")

def on_error(ws: Any, message: str):
    print(message)
    with open("error.txt", "a") as myfile:
        myfile.write(str(message))
        myfile.write("\n")


dirigera_hub.create_event_listener(
    on_message=on_message, on_error=on_error
)

