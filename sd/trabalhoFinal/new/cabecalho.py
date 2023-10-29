from json import *

class Cabecalho:
    def __init__(self, messageType, objectreference, methodId, arguments):
        self.messageType = messageType
        self.objectreference = objectreference
        self.methodId = methodId
        self.arguments = arguments

    def to_json(self):
        header_data = {
            "messageType": self.messageType,
            "objectreference": self.objectreference,
            "methodId": self.methodId,
            "arguments": self.arguments
        }
        return dumps(header_data)

    @classmethod
    def from_json(cls, json_str):
        header_data = loads(json_str)
        return cls(**header_data)