from TEST.classes.AddressBook import AddressBook
from TEST.classes.Record import Record
from TEST.commands.Contacts import ContactsCommands
from TEST.commands.Emails import EmailCommands


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
            # DONE
            if command == "hello":
                print("What's up! Nice to see you.")
                continue
            # DONE
            if command == "add":
                result = ContactsCommands.add_contact(args.split(maxsplit=1), book)
                print(result)
            elif command == "add_email":
                result = EmailCommands.add_email(args.split(maxsplit=1), book)
                print(result)
            #DONE (формат 2003-03-03)
            elif command == "add_birthday":
                name, birthday = args.split(maxsplit=1)
                record = book.find(name) or Record(name)
                record.add_birthday(birthday)
                book.add_record(record)
                print(f"Birthday {birthday} added to contact {name}.")
            #DONE
            elif command == "add_address":
                name, address = args.split(maxsplit=1)
                record = book.find(name) or Record(name)
                record.add_address(address)
                book.add_record(record)
                print(f"Address {address} added to contact {name}.")
            # DONE
            elif command == "show":
                record = book.get_record_by_name(args)
                if record:
                    print(record)
                else:
                    print("Contact not found.")
            # DONE
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
