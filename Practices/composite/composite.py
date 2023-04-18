from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @abstractmethod
    def deploy(self):
        pass


class HumanResource(Component):
    def __init__(self, name):
        self.name = name

    def deploy(self):
        print("Deploying a human resource named ", self.name)


class Truck(Component):
    def __init__(self, make):
        self.make = make

    def deploy(self):
        print(f"Deploying a \"{self.make}\" truck")


class Team(Component):
    def __init__(self):
        self.components: List[Component] = []

    def add(self, component: Component):
        self.components.append(component)

    def deploy(self):
        for component in self.components:
            component.deploy()


def main():
    jack = HumanResource("Jack")
    jim = HumanResource("Jim")
    mack = Truck("Mack")
    subteam1 = Team()
    for c in [jack, jim, mack]:
        subteam1.add(c)

    mike = HumanResource("Mike")
    leo = HumanResource("Leo")
    benz = Truck("Benz")
    subteam2 = Team()
    for c in [mike, leo, benz]:
        subteam2.add(c)

    team = Team()
    team.add(subteam1)
    team.add(subteam2)
    team.deploy()


if __name__ == '__main__':
    main()
