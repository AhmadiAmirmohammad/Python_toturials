# structural design adapter
# adapter is a class for work 2 incompatible class
# ex. Wall plug (client) with your laptop's three-prong (old system)

from abc import ABC, abstractmethod


class TwoPinSocket(ABC):
    @abstractmethod
    def plug_into_two_pin(self):
        pass


class ThreePinSocket(ABC):
    def plug_into_three_pin(self) -> str:
        return "device powered via three pins"


class ThreeToTwoAdapter(TwoPinSocket):
    def __init__(self, three_pin_device: ThreePinSocket):
        self.three_pin_device = ThreePinSocket()
    def plug_into_two_pin(self):
        print("adapter: converting two-pin request to three pin")
        return self.three_pin_device.plug_into_three_pin()

class WallSocket:
    def power_device(self, device: TwoPinSocket):
        print("Wall socket powering ... ")
        return device.plug_into_two_pin()

three_pin_device = ThreePinSocket()
adapter = ThreeToTwoAdapter(three_pin_device)

wall = WallSocket()
wall.power_device(adapter)
