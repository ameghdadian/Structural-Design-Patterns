'''
    We use Bridge pattern whenever we have a hierarchy that grows in two different 
    dimensions(i.e., feature and implementation).
'''
from abc import ABC, abstractmethod


# Universal remote control app


# RemoteControl
#   SonyRemoteControl
#   SamsungRemoteControl
#   AdvancedRemoteControl
#       SonyAdvancedRemoteControl
#       SamsungAdvancedRemoteControl

# Currently we have 2 types of remote control -> For each brand we create 2 new
# classes!
# class RemoteControl(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def turn_off(self):
#         pass


# class AdvancedRemoteControl(RemoteControl):
#     @abstractmethod
#     def set_channel(number: int):
#         pass

# class SonyRemoteControl(RemoteControl):
#     def turn_on(self):
#         print("Sony: turn on")

#     def turn_off(self):
#         print("Sony: turn off")


# class SonyAdvancedRemoteControl(AdvancedRemoteControl):
#     @abstractmethod
#     def set_channel(number: int):
#         pass

#     def turn_on(self):
#         print("Sony: turn on")

#     def turn_off(self):
#         print("Sony: turn off")


# Implementation Hierarchy
class Device:
    def turn_on(self): pass
    def turn_off(self): pass
    def set_channel(self, number: int): pass


class SonyTv(Device):
    def turn_on(self):
        print("Sony: Turn on")

    def turn_off(self):
        print("Sony: Trun off")

    def set_channel(self, number: int):
        print("Sony: Set Channel")


class SamsungTv(Device):
    def turn_on(self):
        print("Samsung: Turn on")

    def turn_off(self):
        print("Samsung: Trun off")

    def set_channel(self, number: int):
        print("Samsung: Set Channel")


# Feature Hierarchy
class RemoteControl:
    def __init__(self, device: Device) -> None:
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()


class AdvancedRemoteControl(RemoteControl):
    def set_channel(self, number: int):
        self.device.set_channel(number)
