class PhoneNumber:
    def __init__(self, number):
        self.number = number

    def create_phone_number(self, phone_number):
        string = str(phone_number.number)
        string1 = string[0:3:1]
        string2 = string[3:6:1]
        string3 = string[6::1]
        new_phone_number=f"({string1}) {string2}-{string3}"
        return new_phone_number
