from typing import Mapping
from abc import ABC, abstractmethod


class Ebook(ABC):
    @abstractmethod
    def show(self):
        pass


class RealEbook(Ebook):
    def __init__(self, filename) -> None:
        self.filename = filename
        self.load()

    def load(self):
        print("Loading the ebook ", self.filename)

    def show(self):
        print("Showing the ebook ", self.filename)


class EbookProxy(Ebook):
    def __init__(self, filename):
        self.filename = filename
        self.ebook: RealEbook = None

    def show(self):
        if not self.ebook:
            self.ebook = RealEbook(self.filename)

        self.ebook.show()


class LoggingEbookProxy(Ebook):
    def __init__(self, filename):
        self.filename = filename
        self.ebook: RealEbook = None

    def show(self):
        if not self.ebook:
            self.ebook = RealEbook(self.filename)

        print("Logging the action ...")
        self.ebook.show()


class Library:
    ebooks: Mapping[str, Ebook] = {}

    def add(self, ebook: Ebook):
        Library.ebooks[ebook.filename] = ebook

    def open_ebook(self, filename):
        if filename in Library.ebooks:
            Library.ebooks[filename].show()
