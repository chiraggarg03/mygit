from .git_object import GitObject

class Blob(GitObject):
    def __init__(self, payload: bytes) -> None:
        self._payload = payload


    @property
    def payload(self) -> bytes:
        return self._payload
    

    @property
    def object_type(self) -> str:
        return "blob"
    
