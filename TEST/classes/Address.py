from TEST.classes.Field import Field


class Address(Field):
    def __init__(self, value):
        self.__value = None
        self.city, self.street, self.house_number = self._split_address(value)
        self.value = value

    def _split_address(self, value):

        parts = value.split(',')
        if len(parts) != 3:
            raise ValueError("Address should be in format: City, Street, House Number.")
        return parts[0].strip(), parts[1].strip(), parts[2].strip()

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        city, street, house_number = self._split_address(new_value)

        if not city:
            raise ValueError("City cannot be empty.")
        if not street:
            raise ValueError("Street cannot be empty.")
        if not house_number.isnumeric():
            raise ValueError("House number should be numeric.")


        self.__value = f"{city}, {street}, {house_number}"
