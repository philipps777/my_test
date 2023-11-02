from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_records(self):
        return self.data

    def get_record_by_name(self, name):
        for record_name, record in self.data.items():
            if record_name == name:
                return record

    def get_record_by_phone(self, phone_number):
        for record in self.data.values():
            if any(phone.value == phone_number for phone in record.phones):
                return record
        return None

    def get_record_by_email(self, email):
        for record in self.data.values():
            if email in (e.value for e in record.emails):
                return record
        return None

    def get_record_by_birthday(self, birthday_str):
        for record in self.data.values():
            if record.birthday and record.birthday.value == birthday_str:
                return record
        return None

    def get_record_by_address(self, address_str):
        for record in self.data.values():
            if record.address and record.address.value == address_str:
                return record
        return None


    def __str__(self):
        result = ""
        if len(self.data) == 0:
            result = "Address book is empty."
        else:
            for record in self.data.values():
                result += str(record) + "\n"

        return result.rstrip()
