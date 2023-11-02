# class IncorrectEmail(Exception):
#     def __init__(self, message, *args):
#         super().__init__(*args)
#         self.message = message
#
#
# class PhoneValueError(Exception):
#     def __init__(self, message, *args):
#         super().__init__(*args)
#         self.message = message
#
#
# class NameValueError(Exception):
#     def __init__(self, message, *args):
#         super().__init__(*args)
#         self.message = message
#
# from TEST.helpers.decorators import input_error
import TEST.helpers.decorators


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


import datetime


class IncorrectDateFormat(Exception):

    def __init__(self, message="Incorrect date format, should be YYYY-MM-DD"):
        self.message = message
        super().__init__(self.message)


class AddressFormatError(Exception):

    def __init__(self, message="Incorrect address format. Use: add-address <name> <city> <street> <number>"):
        self.message = message
        super().__init__(self.message)


# @TEST.helpers.decorators.input_error
# def add_address(args, book):
#     if len(args) < 4:
#         raise AddressFormatError()
#     name, city, street, number = args[0], ' '.join(args[1:-2]), args[-2], args[-1]
#
#     if not city.isalpha() or not street.replace(' ', '').isalpha():
#         raise AddressFormatError("City and street must contain only letters.")
#
#     if not number.isdigit():
#         raise AddressFormatError("House number must be numeric.")
#
#     book.add_address(name, {'city': city, 'street': street, 'number': number})
#     return f"Address for {name} updated to {city}, {street} {number}."
