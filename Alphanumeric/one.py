def store_details(filename):
    with open(filename, 'a') as file:
        name = input('Enter name: ')
        person_id = input('Enter ID: ')
        age = input('Enter age: ')
        address = input('Enter address: ')
        phone = input('Enter phone number: ')

        file.write(f'{name}\n{person_id}\n{age}\n{address}\n{phone}\n')
    print('Details saved successfully!')


if __name__ == "__main__":
    filename = 'person_details.txt'
    store_details(filename)
