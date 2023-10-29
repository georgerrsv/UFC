from json import *

class Cabecalho:
    _requestId = 0

    def __init__(self, messageType, objectreference, methodId, arguments, requestId):
        self.messageType = messageType
        self.objectreference = objectreference
        self.methodId = methodId
        self.arguments = arguments
        self.requestId = requestId

    def to_json(self):
        header_data = {
            "messageType": self.messageType,
            "objectreference": self.objectreference,
            "methodId": self.methodId,
            "arguments": self.arguments,
            "requestId": self.requestId
        }
        return dumps(header_data)

    @classmethod
    def from_json(cls, json_str):
        header_data = loads(json_str)
        return cls(
            header_data["messageType"],
            header_data["objectreference"],
            header_data["methodId"],
            header_data["arguments"],
            header_data.get("requestId", 0)  # Use 0 se 'requestId' não estiver presente no JSON
        )

    @classmethod
    def increment_request_id(cls):
        cls._requestId += 1
        return cls._requestId