# limit parameters with enum

from enum import Enum


class Protocol(Enum):
    HTTP: str = 'http'
    HTTPS: str = 'https'


def use_protocol(protocol: Protocol) -> None:
    if type(protocol) != Protocol:
        raise TypeError

    print(protocol.value)


use_protocol(Protocol.HTTP)

# this will fail
use_protocol('https')
