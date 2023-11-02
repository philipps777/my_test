from TEST.classes.Record import Record
from TEST.helpers.decorators import input_error


class EmailCommands:
    # @input_error
    # def add_email(args, book):
    #     name, email = args
    #     record = book.find(name)
    #     if record:
    #         record.add_email(email)
    #         return f"Email {email} added to contact {name}."
    #     else:
    #         return "Contact not found."

    @input_error
    def show_email(args, book):
        name = args[0]
        record = book.find(name)
        if record:
            return record.get_emails()
        else:
            return "Contact not found."

    @input_error
    @staticmethod
    def add_email(args, book):
        try:
            name, email = args
            record = book.find(name) or Record(name)
            record.add_email(email)
            book.add_record(record)
            return f"Email {email} added to contact {name}."
        except ValueError as e:
            return str(e)