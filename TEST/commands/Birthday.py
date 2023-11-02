from datetime import datetime, timedelta

from TEST.classes.Record import Record
from TEST.helpers.decorators import input_error


class BirthdayCommands:
    # @input_error
    # def add_birthday(args, book):
    #     if len(args) != 2:
    #         raise IndexError("Usage: add-birthday <name> <YYYY-MM-DD>")
    #     name, date_str = args
    #     try:
    #         birthday = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    #         if birthday > datetime.date.today():
    #             raise IncorrectDateFormat("Birthday date cannot be in the future.")
    #     except ValueError:
    #         raise IncorrectDateFormat("Invalid date format. Use YYYY-MM-DD.")
    #
    #     record = book.find(name)
    #     record.add_birthday(birthday)
    #     return f"Birthday for {name} on {date_str} added."

    @input_error
    def show_birthday(args, book):
        if not args:
            raise IndexError("Usage: show-birthday <name>")
        name = args[0]
        record = book.find(name)
        birthday = record.get_birthday()
        if birthday:
            return f"Birthday for {name} is on {birthday}"
        else:
            raise KeyError(f"Birthday not found for {name}")

    @input_error
    @staticmethod
    def add_birthday(args, book):
        try:
            name, birthday = args
            record = book.find(name)
            if not record:
                record = Record(name)
                book.add_record(record)
            record.add_birthday(birthday)
            return f"Birthday {birthday} added to contact {name}."
        except ValueError as e:
            return str(e)

    @classmethod
    def show_upcoming_birthdays(cls, book):
        upcoming_birthdays = []
        today = datetime.today().date()
        in_one_week = today + timedelta(days=7)

        for name, record in book.items():
            if hasattr(record, 'birthday'):
                birthday_date = record.birthday.date()

                this_years_birthday = birthday_date.replace(year=today.year)
                if today <= this_years_birthday <= in_one_week:
                    days_until = (this_years_birthday - today).days
                    upcoming_birthdays.append(f"{name} has a birthday in {days_until} days.")

        return '\n'.join(upcoming_birthdays) if upcoming_birthdays else "No upcoming birthdays."