

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
    except:
        return "You have entered insufficient data"
    if name not in contacts:
        contacts[name] = phone
    else:
        return "This contact already exists"
    return "Contact added."

def change_username_phone(args, contacts):
    try:
        name, phone = args
    except:
        return "You have entered insufficient data"
    if name in contacts:
        contacts[name] = phone
    else:
        return "There is no such contact"
    return f"Contact {name} changed his phone numer for {phone}"

def phone_username(args, contacts):
    try:
        name = args[1]
    except:
        return "That contact is not on the list"
    if name in contacts:
        phone = contacts[name]
    else:
        return "There is no such contact"
    return f"{name}`s phone numer is {phone}"

def all_contacts(args, contacts):
    phonebook = ""
    for name, phone in contacts.items():
        phonebook += f"{name}: {phone} \n"
    return phonebook

def main():
    contacts = {"Ilya": "015140749275", "Olya":"015172836348", "Denis":"017673560531" }
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(all_contacts(args,contacts))
        elif command == "change":
            print(change_username_phone(args,contacts))
        elif command == "phone" and "username" in user_input: 
            print(phone_username(args,contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

