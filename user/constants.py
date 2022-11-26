from util.enum import ChoiceEnum


class UserType(ChoiceEnum):
    ADMIN = 'ADMIN'
    STUDENT = 'STUDENT'
    STAFF = 'STAFF'
