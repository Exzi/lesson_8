class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, first_name, last_name, phone_number):
        self.contacts.append({
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number
        })

    def find_contact(self, name):
        for contact in self.contacts:
            if contact['first_name'] == name or contact['last_name'] == name:
                return contact
        return None

    def update_contact(self, name, new_first_name=None, new_last_name=None, new_phone_number=None):
        contact = self.find_contact(name)
        if contact:
            if new_first_name:
                contact['first_name'] = new_first_name
            if new_last_name:
                contact['last_name'] = new_last_name
            if new_phone_number:
                contact['phone_number'] = new_phone_number
            return True
        return False

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            return True
        return False

    def display_contacts(self):
        for contact in self.contacts:
            print(f"{contact['first_name']} {contact['last_name']}: {contact['phone_number']}")

    def save_to_file(self, filename='contacts.txt'):
        with open(filename, 'w') as f:
            for contact in self.contacts:
                f.write(f"{contact['first_name']},{contact['last_name']},{contact['phone_number']}\n")

    def load_from_file(self, filename='contacts.txt'):
        self.contacts.clear()
        with open(filename, 'r') as f:
            for line in f:
                first_name, last_name, phone_number = line.strip().split(',')
                self.contacts.append({
                    'first_name': first_name,
                    'last_name': last_name,
                    'phone_number': phone_number
                })

    def copy_line_to_another_file(self, source_file, target_file, line_number):
        with open(source_file, 'r') as src:
            lines = src.readlines()
        if line_number < 1 or line_number > len(lines):
            print("Неверный номер строки")
            return
        line_to_copy = lines[line_number - 1]
        with open(target_file, 'a') as tgt:
            tgt.write(line_to_copy)

def main():
    phone_book = PhoneBook()

    while True:
        print("\nМеню телефонной книги: ")
        print("1. Добавить контакт ")
        print("2. Обновить контакт ")
        print("3. Удалить контакт ")
        print("4. Показать контакты ")
        print("5. Сохранить контакт ")
        print("6. Загрузить контакт ")
        print("7. Скопировать контакт из одного файла в другой")
        print("8. Выход ")
        
        choice = input("Выбери вариант: ")

        if choice == '1':
            first_name = input("Имя ")
            last_name = input("Фамилия ")
            phone_number = input("Номер телефона: ")
            phone_book.add_contact(first_name, last_name, phone_number)
        elif choice == '2':
            name = input("Имя и фамилия контакта которого хотите обновить ")
            new_first_name = input("Введите новое имя ")
            new_last_name = input("Введите новую фамилию ")
            new_phone_number = input("Введите новый номер телефона ")
            updated = phone_book.update_contact(name, new_first_name, new_last_name, new_phone_number)
            if updated:
                print("Успешно обновлено ")
            else:
                print("Контакт не найден ")
        elif choice == '3':
            name = input("Имя и фамилия контакта которого хотите удалить ")
            deleted = phone_book.delete_contact(name)
            if deleted:
                print("Успешно удалено ")
            else:
                print("Контакт не найден ")
        elif choice == '4':
            phone_book.display_contacts()
        elif choice == '5':
            phone_book.save_to_file()
            print("Контакт сохранен")
        elif choice == '6':
            phone_book.load_from_file()
            print("Контакт загружен")
        elif choice == '7':
            source_file = 'contacts.txt'
            target_file = 'copied_contacts.txt'
            line_number = int(input("Номер строки для копирования: "))
            phone_book.copy_line_to_another_file(source_file, target_file, line_number)
            print(f"Строка {line_number} скопирована из {source_file} в {target_file}.")
        elif choice == '8':
            break
        else:
            print("Неверно.Попробуйте снова ")

if __name__ == "__main__":
    main()