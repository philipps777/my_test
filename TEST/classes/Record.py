from TEST.classes.Address import Address
from TEST.classes.Email import Email
from TEST.classes.Name import Name
from TEST.classes.Phone import Phone
from TEST.helpers.error import PhoneValueError, IncorrectEmail
from TEST.classes.Birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.emails = []
        self.email = None

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        phone = Phone(phone)
        if phone in self.phones:
            self.phones.remove(phone)

    def find_phone(self, phone_number):
        phone = None
        for p in self.phones:
            if p.value == phone_number:
                phone = p
                break
        return phone

    def edit_phone(self, old_phone, new_phone):
        if len(new_phone) != 10 or not new_phone.isdigit():
            raise PhoneValueError("New number must contain 10 digits.")

        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone
        else:
            raise PhoneValueError("Phone is not in the address book.")

    def add_email(self, email):
        try:
            email = Email(email)
            self.emails.append(email)
        except IncorrectEmail as e:
            print(e)

    def show_emails(self):
        return self.emails

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_address(self, address):
        self.address = Address(address)

    # def __str__(self):
    #     result = f"Contact name: {self.name.value},\n" \
    #              f"phones: {', '.join(p.value for p in self.phones)},\n" \
    #              f"emails: {', '.join(e.value for e in self.emails)},\n" \
    #              f"address: {self.address},\n" \
    #              f"birthday: {self.birthday}\n"
    #
    #     return result
    def get_emails(self):
        return ', '.join(email.value for email in self.emails)

    def get_address(self):
        return str(self.address) if self.address else 'Адрес не задан'

    def get_birthday(self):
        return str(self.birthday.value) if self.birthday.value else 'День народження не встановлено'

    def __str__(self):
        phones = ', '.join(phone.value for phone in self.phones)
        emails = self.get_emails()
        address = self.get_address()
        birthday = self.get_birthday()

        result = f"Имя: {self.name.value}\n" \
                 f"Телефон: {phones}\n" \
                 f"Email: {emails}\n" \
                 f"Адрес: {address}\n" \
                 f"День рождения: {birthday}\n"

        return result.strip()
