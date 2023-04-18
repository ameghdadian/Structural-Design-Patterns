from __future__ import annotations
from enum import Enum, auto
from typing import List, Mapping


'''
    We use this pattern where we have a large number of objects and these objects
    take a significant amount of memory.
    With FlyWeight pattern, we can reduce the amount of memory consumed by these
    objects.
'''

# Simulating a navigator application


'''
class Point:
    def __init__(self, x, y, point_type: PointType, icon):
        self.x = x      # 4 bytes
        self.y = y      # 4 bytes
        self.type = point_type  # 4 bytes
        # Repeating icon for each object consumes a big amount of memory
        self.icon = icon        # ~20KB

    def draw(self):
        print(f"{self.type} at ({self.x}, {self.y})")
'''


class Point:
    def __init__(self, x, y, point_icon: PointIcon):
        self.x = x
        self.y = y
        self.icon = point_icon

    def draw(self):
        print(f"{self.icon} at ({self.x}, {self.y})")


class PointIcon:
    def __init__(self, point_type: PointType, icon: str):
        self.point_type = point_type
        self.icon = icon

    def __str__(self):
        return "{}, {}".format(self.point_type, self.icon)


class PointIconFactory:
    icons: Mapping[PointType, PointIcon] = {}

    @staticmethod
    def get_point_icon(point_type: PointType):
        if point_type in PointIconFactory.icons:
            return PointIconFactory.icons[point_type]

        icon = PointIconFactory._create(point_type)
        PointIconFactory.icons[point_type] = icon
        return icon

    @staticmethod
    def _create(point_type: PointType):
        print("Creating point icon")
        icon = PointIcon(point_type, f"{point_type} icon")
        return icon


class PointService:
    def get_points(self) -> List[Point]:
        points: List[Point] = []
        points.append(Point(1, 2, PointIconFactory.get_point_icon(
            PointType.CAFE
        )))
        points.append(Point(3, 4, PointIconFactory.get_point_icon(
            PointType.CAFE
        )))
        points.append(Point(3, 4, PointIconFactory.get_point_icon(
            PointType.RESTAURANT
        )))

        return points


class PointType(Enum):
    HOSPITAL = auto()
    CAFE = auto()
    RESTAURANT = auto()

    def __str__(self):
        return self.name.capitalize()
