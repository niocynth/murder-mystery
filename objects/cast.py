from enum import Enum

class CastMember():
    def __init__(self, name, age, gender, relation):
        self.name = name
        self.age = age
        self.gender = gender
        self.relation = relation
        self.motive = None
        self.alibi = None
        self.prop = None
        self.murderer = False

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

class StaffMember(CastMember):
    def __init__(self, name, age, gender, job):
        super().__init__(name, age, gender, relation=StaffRelation.EMPLOYEE)
        self.job = job

class FamilyMember(CastMember):
    def __init__(self, name, age, gender, relation):
        super().__init__(name, age, gender, relation)

class Victim(CastMember):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, relation=None)