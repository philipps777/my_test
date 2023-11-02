from datetime import datetime
from TEST.classes.Field import Field



class Birthday(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        try:
            # Перевіряємо, чи коректна дата
            datetime.datetime.strptime(new_value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date should be in YYYY-MM-DD format.")


        self.__value = new_value