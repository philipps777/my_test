from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        # Add a record to the address book
        self.data[record.name.value] = record

    def find(self, name):
        # Find a record by name
        return self.data.get(name)

    def delete(self, name):
        # Delete a record by name
        if name in self.data:
            del self.data[name]

    def get_records(self):
        # Get all records in the address book
        return self.data

    def get_record_by_name(self, name):
        # Get a record by name
        return self.data.get(name)

    def get_record_by_phone(self, phone_number):
        # Get a record by phone number
        for record in self.data.values():
            for phone in record.phones:
                if phone.value == phone_number:
                    return record
        return None

    def get_record_by_email(self, email):
        # Get a record by email
        for record in self.data.values():
            for email_obj in record.emails:
                if email_obj.value == email:
                    return record
        return None

    def get_record_by_birthday(self, birthday_str):
        # Get a record by birthday
        for record in self.data.values():
            if record.birthday and record.birthday.value == birthday_str:
                return record
        return None

    def get_record_by_address(self, address_str):
        # Get a record by address
        for record in self.data.values():
            if record.address and record.address.value == address_str:
                return record
        return None

    def __str__(self):
        # Return a string representation of the address book
        if len(self.data) == 0:
            return "Address book is empty."
        else:
            return "\n".join(str(record) for record in self.data.values())
