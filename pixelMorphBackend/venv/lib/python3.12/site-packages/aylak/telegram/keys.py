import random

KEYS = [
    {"b63d319588b3950a6ad531bbb162b38d": 26016190},
    {"b6060c4b9aa4725b1c65f85e4da214bb": 26552289},
    {"45a7b70fa0c9984f0bba82e77d77c183": 28853360},
    {"d97f522d1badff170babf25dc48073e2": 29928232},
    {"dd4784e8a9722f1780ad3d910c0b1736": 20055942},
    {"e9344dd447b9a930206260c9ea0f101f": 25749871},
    {"fe492468db1a862b02b75a3477342658": 3477342658},
    {"db5cd23c23a7d21a20c0ad15c196645a": 28590864},
    {"ff0ed77e7d14172f91da353c469110c8": 23312051},
    {"e045afc1ef7410e7cb2b0e5cf8064611": 13753812},
    {"53ea88aba8b6f1a2fcd4f17252aaad78": 8365793},
    {"d5e5f3b8e415f3c99eb6cad2c1fb666c": 23622341},
    {"78ab84d76e1ae0bf1e11d45672fbb6ec": 27166094},
]


def get_keys() -> list:
    keys = list(random.choice(KEYS).items())
    return keys[0]
