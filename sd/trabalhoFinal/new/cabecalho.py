from json import *

class Cabecalho:
    _requestId=0
    def __init__(self, messageType, requestId, objectreference, methodId, arguments):
        self.messageType=messageType
        self.requestId=Cabecalho._requestId 
        self.objectreference=objectreference
        self.methodId=methodId
        self.arguments=arguments
        Cabecalho._requestId+=1
        
    def to_json(self):
        return dumps(self.__dict)

    @classmethod
    def from_json(cls, json_str):
        header_data=loads(json_str)
        return cls(**header_data)