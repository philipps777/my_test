from TEST.classes.Record import Record
from TEST.helpers.decorators import input_error


class EmailCommands:
    @input_error
    def show_email(self, args, book):
        name = args[0]
        record = book.find(name)
        if record:
            return record.get_emails()
        else:
            return "Contact not found."

    @staticmethod
    def add_email(args, book):
        name, email = args
        record = book.find(name) or Record(name)
        record.add_email(email)
        book.add_record(record)
        return f"Email {email} added to contact {name}."
