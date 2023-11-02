
class IncorrectEmail(Exception):
    def __init__(self, message="Invalid emails format. Use: add-emails <name> <emails>"):
        self.message = message
        super().__init__(self.message)


class PhoneValueError(Exception):
    def __init__(self, message="Invalid phone format. Use: add <name> <phone>"):
        self.message = message
        super().__init__(self.message)


class NameValueError(Exception):
    def __init__(self, message="Invalid name format. Use: add <name> <phone>"):
        self.message = message
        super().__init__(self.message)


class IncorrectDateFormat(Exception):

    def __init__(self, message="Incorrect date format, should be YYYY-MM-DD"):
        self.message = message
        super().__init__(self.message)


class AddressFormatError(Exception):

    def __init__(self, message="Incorrect address format. Use: add-address <name> <city> <street> <number>"):
        self.message = message
        super().__init__(self.message)

