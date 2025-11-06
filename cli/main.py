def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "You need to write more arguments."


def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact changed."
        else:
            return "Contact is not in array."
    except ValueError:
        return "You need to write more arguments."
    

def all_contact(contacts):
    if not contacts:
        return "Contacts are empty"
    
    lines = []
    for name, phone in contacts.items():
        lines.append(f"Name: {name}, Phone: {phone}")
    
    return "\n".join(lines)



def phone_contact(name, contacts):
    if len(name) == 0:
        return "You need to write name"
    elif not len(contacts):
        return "Contacts are empty"
    else:
        if name[0] in contacts:
            return f"{name[0]}, Phone: {contacts[name[0]]}"
        return f"There is no {name[0]} in contacts."
    

def main():
    contacts = {}
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
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
