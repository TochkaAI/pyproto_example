import sys

from pyproto import REGISTRY_COMMAND

PingCommand = "PING_COMMAND"
WhatIsTime = "WHAT_IS_TIME"


# Каждая команда обязана иметь уникальное имя и UUID
PING_COMMAND = REGISTRY_COMMAND(PingCommand,         "13903403-e03a-450f-a508-a8e1dc52e29e")
WHAT_IS_TIME = REGISTRY_COMMAND(WhatIsTime,          "67adef57-ec0b-4efd-8161-bd21d4dc0a19")