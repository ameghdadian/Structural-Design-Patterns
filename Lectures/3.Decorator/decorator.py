from __future__ import annotations
from abc import ABC, abstractmethod


'''
    When adding additional behaviour to an object.
'''


class Stream(ABC):
    @abstractmethod
    def write(self, data: str):
        pass


class CloudStream(Stream):
    def write(self, data: str):
        print("Storing", data)


# # Now, if we want to encrypt cloud data before sending it
# class EncryptedCloudStream(CloudStream):
#     def write(self, data: str):
#         encrypted = self.encrypt(data)
#         super().write(encrypted)

#     def encrypt(self, data: str):
#         return "!@!@#$%$^&%$"


# class CompressedCloudStream(CloudStream):
#     def write(self, data: str):
#         compressed = self.compress(data)
#         super().write(compressed)

#     def compress(self, data: str):
#         return data[:5]

class CompressedCloudStream(Stream):
    def __init__(self, stream: Stream):
        self.stream = stream

    def write(self, data: str):
        compressed = self.compress(data)
        self.stream.write(compressed)

    def compress(self, data: str):
        return data[:5]


class EncryptedCloudStream(Stream):
    def __init__(self, stream: Stream):
        self.stream = stream

    def write(self, data: str):
        encrypted = self.encrypt(data)
        self.stream.write(encrypted)

    def encrypt(self, data: str):
        return "!@!@#$%$^&%$"
