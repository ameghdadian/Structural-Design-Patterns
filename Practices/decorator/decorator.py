from abc import ABC, abstractmethod
from typing import List


class Artefact(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Icon(Artefact):
    def __init__(self, name: str) -> None:
        self.name = name

    def render(self):
        return f"{self.name} Icon"


# Decorator
class ErrorIcon(Artefact):
    def __init__(self, artefact: Artefact):
        self.artefact = artefact

    def render(self):
        data = self.add_error_icon()
        return data + self.artefact.render()

    def add_error_icon(self):
        return f"[Error]"


# Decorator
class MainIcon(Artefact):
    def __init__(self, artefact: Artefact):
        self.artefact = artefact

    def render(self):
        data = self.add_main_icon()
        return data + self.artefact.render()

    def add_main_icon(self):
        return f"[Main]"


class Editor:
    def __init__(self):
        self.artefacts: List[Artefact] = []

    def open_project(self, path: str):
        self.artefacts.append(Icon("Main"))
        self.artefacts.append(Icon("Demo"))
        self.artefacts.append(Icon("EmailClient"))
        self.artefacts.append(Icon("EmailProvider"))

        self.artefacts[0] = ErrorIcon(MainIcon(self.artefacts[0]))
        self.artefacts[2] = ErrorIcon(self.artefacts[2])

    def render(self):
        for artefact in self.artefacts:
            print(artefact.render())


def main():
    editor = Editor()
    editor.open_project("...")
    editor.render()


if __name__ == '__main__':
    main()
