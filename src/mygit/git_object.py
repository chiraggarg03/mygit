from abc import ABC
from abc import abstractmethod
from hashlib import sha1


class GitObject(ABC):

    @property
    @abstractmethod
    def object_type(self) -> str:
        pass


    @property
    @abstractmethod
    def payload(self) -> bytes:
        pass


    @property
    def size(self) -> int:
        return len(self.payload)


    def serialize(self) -> bytes:
        return f"{self.object_type} {self.size}\0".encode() + self.payload


    def object_id(self) -> str:
        return sha1(self.serialize()).hexdigest()
    
