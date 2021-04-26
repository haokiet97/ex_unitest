import enum


class GenderEnum(enum):
    MALE = 0
    FEMALE = 1


class Player:

    def __init__(self, age=0, gender=GenderEnum.FEMALE.value):
        self.age = age
        self.gender = gender
