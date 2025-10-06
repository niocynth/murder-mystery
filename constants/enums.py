from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class MaleRelation(Enum):
    GRANDFATHER = "grandfather"
    FATHER = "father"
    BROTHER = "brother"
    UNCLE = "uncle"
    COUSIN = "cousin"

class FemaleRelation(Enum):
    GRANDMOTHER = "grandmother"
    MOTHER = "mother"
    SISTER = "sister"
    AUNT = "aunt"
    COUSIN = "cousin"

class StaffRelation(Enum):
    EMPLOYEE = "employee"

class MaleJob(Enum):
    BUTLER = "butler"
    COOK = "cook"
    VALET = "valet"
    FOOTMAN = "footman"
    GROOM = "groom"
    COACHMAN = "coachman"
    GARDENER = "gardener"
    STEWARD = "steward"

class FemaleJob(Enum):
    HOUSEKEEPER = "housekeeper"
    COOK = "cook"
    GOVERNESS = "governess"
    HOUSE_MAID = "house_maid"
    KITCHEN_MAID = "kitchen_maid"
    LAUNDRY_MAID = "laundry_maid"
    NURSE_MAID = "nurse_maid"
    NANNY = "nanny"

class PropType(Enum):
    WEAPON = "weapon"
    CLUE = "clue"
    RED_HERRING = "red_herring"

class RoomType(Enum):
    HALL = "hall"
    LIVING_ROOM = "living_room"
    DINING_ROOM = "dining_room"
    STUDY = "study"
    LIBRARY = "library"
    KITCHEN = "kitchen"
    BEDROOM = "bedroom"