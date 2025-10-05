from enum import Enum
from constants import *

class map():
    def __init__(self, width=MAP_WIDTH, height=MAP_HEIGHT):
        self.width = width
        self.height = height
        self.rooms = ()

        for i in range(height):
            temp_width = ()
            for j in range(width):
                temp_width += (None,)
            self.rooms += (temp_width,)

        print(self.rooms)

class RoomType(Enum):
    HALL = "hall"
    LIVING_ROOM = "living_room"
    DINING_ROOM = "dining_room"
    STUDY = "study"
    LIBRARY = "library"
    KITCHEN = "kitchen"
    BEDROOM = "bedroom"
    

class Room():
    def __init__(self, coordinates):
        self.coordinates = coordinates

