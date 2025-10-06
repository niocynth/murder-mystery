from enum import Enum
from constants.enums import *

class CastMember():
    def __init__(self, name, age, gender, relation):
        self.name = name
        self.age = age
        self.gender = gender
        self.pronouns = None
        self.relation = relation
        self.motive = None
        self.alibi = None
        self.prop = None
        self.murderer = False

        match gender:
            case Gender.MALE:
                self.pronouns = (He, Him, His)
            case Gender.FEMALE:
                self.pronouns = (She, Her, Hers)
            case _:
                raise Exception("Gender does not exist")

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