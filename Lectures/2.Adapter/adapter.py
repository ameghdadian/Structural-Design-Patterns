from __future__ import annotations
from abc import ABC, abstractmethod
'''
    Converting the interface of a class to a
    different form
'''


class Image:
    pass


class Filter(ABC):
    @abstractmethod
    def apply(self, image: Image):
        pass


class VividFilter(Filter):
    def apply(self, image: Image):
        print("Applying Vivid Filter")


class ImageView:
    def __init__(self, image: Image):
        self.image = image

    def apply(self, filter: Filter):
        filter.apply(self.image)


# Now, lets imagine we know about a third
# party library that contains lots of beautiful
# filters, we don't want to code these from scratch.
# So, we use this package. But here comes a problem:
# Filters inside this package doesn't have the same
# interface as our currently implemented filters.
# Adapter pattern comes to the rescue!
# HERE IS THE THIRD-PARTY PACKAGE CODE
class Caramel:
    # Imagine it's required to call this init method
    # first, then use this class.
    def init(self):
        print("Initializing Caramel filter")

    def render(self, image: Image):
        print("Applying Caramel filter")


# Adapter
class CaramelFilter(Filter):
    def __init__(self, caramel: Caramel):
        self.caramel = caramel

    def apply(self, image: Image):
        self.caramel.init()
        self.caramel.render(image)
