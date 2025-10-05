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

class StaffMember(CastMember):
    def __init__(self, name, age, gender, job):
        super().__init__(name, age, gender, relation="Employee")
        self.job = job

class FamilyMember(CastMember):
    def __init__(self, name, age, gender, relation):
        super().__init__(name, age, gender, relation)
        