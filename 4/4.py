def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args 


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Usage: add <name> <phone>"
    name, phone = args
    if name in contacts:
        return "This name already in contacts"
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Usage: change <name> <phone>"
    name, phone = args
    if name not in contacts:
        return "There is no contact with this name"
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid arguments. Usage: show <name>"
    name = args[0]  
    if name not in contacts:
        return "There is no contact with this name"
    return f"{name}: {contacts[name]}"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "all":
            print("Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
