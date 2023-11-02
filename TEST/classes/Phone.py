from TEST.helpers.error import PhoneValueError


class Phone:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not (len(str(value)) == 10 and value.isdigit()):
            raise PhoneValueError(
                "Invalid phone number. The number must contain 10 digits.")

        self.__value = value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)
