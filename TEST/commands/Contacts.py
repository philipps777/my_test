from TEST.helpers.decorators import input_error
from TEST.classes.Record import Record


class ContactsCommands:
    @staticmethod
    def add_contact(args, book):
        name, phone = args
        record = book.find(name) or Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return f"Contact {name} added with phone number {phone}."

    # @input_error
    # @staticmethod
    # def add_contact(args, book):
    #     name, phone = args
    #     record = book.find(name)
    #
    #     if not record:
    #         record = Record(name)
    #         record.add_phone(phone)
    #         book.add_record(record)
    #         return f"{name} is added to the address book"
    #
    #     record.add_phone(phone)
    #     return f"New phone is added to {name}'s record"

    @input_error
    def show_all(book):
        return str(book)


