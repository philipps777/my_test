from TEST.classes.Record import Record
from TEST.helpers.decorators import input_error


class AddressCommands:
    @input_error
    def show_address(args, book):
        name = args[0]
        record = book.find(name)
        if record:
            return record.get_address()
        else:
            return "Contact not found."



    @input_error
    @staticmethod
    def add_address(args, book):
        try:
            name, address = args
            record = book.find(name)
            if not record:
                record = Record(name)
                book.add_record(record)
            record.add_address(address)
            return f"Address {address} added to contact {name}."
        except ValueError as e:
            return str(e)