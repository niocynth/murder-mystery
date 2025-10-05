class CastMember():
    def __init__(self, name, age, gender, relation):
        self.name = name
        self.age = age
        self.gender = gender
        self.relation = relation

class StaffMember(CastMember):
    def __init__(self, name, age, gender, position):
        super().__init__(name, age, gender, relation="Employee")
        self.position = position

class FamilyMember(CastMember):
    def __init__(self, name, age, gender, relation):
        super().__init__(name, age, gender, relation)

