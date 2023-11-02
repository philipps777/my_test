from TEST.commands.System import SystemCommands
from TEST.commands.Contacts import ContactsCommands
from TEST.commands.Phone import PhoneCommands
from TEST.helpers.decorators import parse_input
from TEST.classes.AddressBook import AddressBook
from TEST.commands.Birthday import BirthdayCommands
from TEST.commands.Emails import EmailCommands
from TEST.commands.Address import AddressCommands
# def process_add_command(args, book):
#     try:
#         name, email = args
#         record = book.find(name) or Record(name)
#         record.add_email(email)
#         book.add_record(record)  # Add or update the record in the address book
#         print(f"Email {email} added to contact {name}.")
#     except ValueError as e:
#         print(e)
#
# def process_add_birthday_command(args, book):
#     try:
#         name, birthday = args
#         record = book.find(name)
#         if record:
#             record.add_birthday(birthday)
#             print(f"Birthday {birthday} added to contact {name}.")
#         else:
#             print("Contact not found.")
#     except ValueError as e:
#         print(e)
#
# def process_add_address_command(args, book):
#     try:
#         name, address = args
#         record = book.find(name)
#         if record:
#             record.add_address(address)
#             print(f"Address {address} added to contact {name}.")
#         else:
#             print("Contact not found.")
#     except ValueError as e:
#         print(e)

# def main():
#     book = AddressBook()
#     print("Welcome to the assistant bot!")
#
#     while True:
#         result = None
#         user_input = input("Enter a command: ")
#         command, *args = parse_input(user_input)
#
#         if command in ["close", "exit"]:
#             result = SystemCommands.show_goodbye()
#             print(result)
#             break
#         elif command == "hello":
#             result = SystemCommands.show_greeting()
#         elif command == "add":
#             result = ContactsCommands.add_contact(args, book)
#             name = args[0]
#             print(book.get_record_by_name(name))
#         elif command == "all":
#             result = ContactsCommands.show_all(book)
#         elif command == "show-phone":
#             result = PhoneCommands.show_phone(args, book)
#         elif command == "change-phone":
#             result = PhoneCommands.change_phone(args, book)

        #     11111111111111111111111111111111111111111111111111111111111
        # elif command == "add-emails":
        #     result = EmailCommands.add_email(args, book)
        # elif command == "show-emails":
        #     result = EmailCommands.show_mail(args, book)
        # elif command == "add-birthday":
        #     result = BirthdayCommands.add_birthday(args, book)
        # elif command == "show-birthday":
        #     result = BirthdayCommands.show_birthday(args, book)
        # elif command == "add-address":
        #     result = AddressCommands.add_address(args, book)
        # elif command == "show-address":
        #     result = AddressCommands.show_address(args, book)
        # else:
        #     result = SystemCommands.show_invalid()
        #11111111111111111111111111111111111111111111111111111111111111111111111
#         elif command == "add-emails":
#             name, email = args
#             record = book.find(name)
#             if record:
#                 record.add_email(email)
#                 print(f"Email {email} added to contact {name}.")
#             else:
#                 print("Contact not found.")
#         elif command == "add-birthday":
#             name, birthday_str = args
#             record = book.find(name)
#             if record:
#                 record.add_birthday(birthday_str)
#                 print(f"Birthday {birthday_str} added to contact {name}.")
#             else:
#                 print("Contact not found.")
#         elif command == "add-address":
#             name, address_str = args
#             record = book.find(name)
#             if record:
#                 record.add_address(address_str)
#                 print(f"Address {address_str} added to contact {name}.")
#             else:
#                 print("Contact not found.")
#         if result:
#             print(result)
#
#
# if __name__ == "__main__":
#     main()



# def main():
#     book = AddressBook()
#     print("Welcome to the assistant bot!")
#
#     while True:
#         user_input = input("Enter a command: ")
#         command, *args = parse_input(user_input)
#
#         if command in ["close", "exit"]:
#             print(SystemCommands.show_goodbye())
#             break
#         elif command == "hello":
#             print(SystemCommands.show_greeting())
#         elif command == "add":
#             if len(args) != 2:
#                 print("Give me the correct command, please. Usage: add [name] [phone]")
#             else:
#                 print(ContactsCommands.add_contact(args, book))
#         elif command == "change":
#             print(PhoneCommands.change_phone(args, book))
#         elif command == "phone":
#             print(PhoneCommands.show_phone(args, book))
#         elif command == "all":
#             print(ContactsCommands.show_all(book))
#         elif command == "add-email":
#             if len(args) != 2:
#                 print("Please enter the correct command. Usage: add-email [name] [email]")
#             else:
#                 print(EmailCommands.add_email(args, book))
#         elif command == "show-email":
#             print(EmailCommands.show_email(args, book))
#         elif command == "add-birthday":
#             if len(args) != 2:
#                 print("Please enter the correct command. Usage: add-birthday [name] [birthday]")
#             else:
#                 print(BirthdayCommands.add_birthday(args, book))
#         elif command == "show-birthday":
#             print(BirthdayCommands.show_birthday(args, book))
#         elif command == "birthdays":
#             print(BirthdayCommands.show_upcoming_birthdays(book))
#         elif command == "add-address":
#             print(AddressCommands.add_address(args, book))
#         elif command == "show-address":
#             print(AddressCommands.show_address(args, book))
#         else:
#             print(SystemCommands.show_invalid())
#
# if __name__ == "__main__":
#     main()


# def main():
#     book = AddressBook()
#
#     while True:
#         command = input("Enter a command: ").strip().lower()
#         args = command.split()[1:]  # Игнорируем первую часть как команду, остальное аргументы
#         command = command.split()[0]  # Первая часть ввода это команда
#
#         if command == "add":
#             result = ContactsCommands.add_contact(args, book)
#             name = args[0]
#             print(book.get_record_by_name(name))
#
#         elif command == "add_phone":
#             result = PhoneCommands.add_phone(args, book)
#             print(result)
#
#         elif command == "add_email":
#             result = EmailCommands.add_email(args, book)
#             print(result)
#
#         elif command == "add_birthday":
#             result = BirthdayCommands.add_birthday(args, book)
#             print(result)
#
#         elif command == "add_address":
#             result = AddressCommands.add_address(args, book)
#             print(result)
#
#         elif command == "show":
#             name = args[0]
#             print(book.get_record_by_name(name))
#
#         elif command == "show_all":
#             print(book)
#
#         elif command == "delete":
#             result = ContactsCommands.delete_contact(args, book)
#             print(result)
#
#         # Добавьте дополнительные команды по мере необходимости
#
#         elif command == "exit":
#             break
#         else:
#             print("Unknown command. Please try again.")
#
# if __name__ == "__main__":
#     main()


def main():
    book = AddressBook()

    while True:
        command_input = input("Enter a command: ").strip()
        if not command_input:
            continue

        command_parts = command_input.split(maxsplit=1)
        command = command_parts[0].lower()
        args = command_parts[1] if len(command_parts) > 1 else ""

        try:
            if command == "add":
                name, phone = args.split(maxsplit=1)
                result = ContactsCommands.add_contact([name, phone], book)
                print(result)
            elif command == "add_email":
                name, email = args.split(maxsplit=1)
                result = EmailCommands.add_email([name, email], book)
                print(result)
            elif command == "add_birthday":
                name, birthday = args.split(maxsplit=1)
                # Допустим, у нас есть метод add_birthday в классе Record
                record = book.find(name) or Record(name)
                record.add_birthday(birthday)
                book.add_record(record)
                print(f"Birthday {birthday} added to contact {name}.")
            elif command == "add_address":
                name, address = args.split(maxsplit=1)
                # Допустим, у нас есть метод add_address в классе Record
                record = book.find(name) or Record(name)
                record.add_address(address)
                book.add_record(record)
                print(f"Address {address} added to contact {name}.")
            elif command == "show":
                name = args
                record = book.get_record_by_name(name)
                if record:
                    print(record)
                else:
                    print("Contact not found.")
            elif command == "exit":
                print("Exiting the address book.")
                break
            else:
                print("Unknown command")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()