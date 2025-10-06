from enum import Enum
from constants.enums import *

class Prop():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.description = None
        self.owner = None
        self.room = None

class Weapon(Prop):
    def __init__(self, name, blood=False):
        super().__init__(name, PropType.WEAPON)
        self.blood = blood

class Clue(Prop):
    def __init__(self, name):
        super().__init__(name, PropType.CLUE)

class RedHerring(Prop):
    def __init__(self, name):
        super().__init__(name, PropType.RED_HERRING)

