from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod


'''
    Treating individual and group of objects the
    same way.
'''


'''
    Define operations common between leaves and
    containers(composite objects)
'''


class Component(ABC):
    @abstractmethod
    def render(self):
        pass


class Shape(Component):
    def render(self):
        print("Render shape")


class Group(Component):
    def __init__(self):
        self.components: List[Component] = []

    def add(self, component: Component):
        self.components.append(component)

    def render(self):
        for component in self.components:
            component.render()
