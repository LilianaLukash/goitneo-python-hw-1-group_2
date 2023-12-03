def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    # update existing phone in the list
    name, phone = args
    contacts[name] = phone
    return f"Phone of {name} changed to {phone}"
 
def phone_username(args, contacts):
    # return phone from username
    username = args
    return contacts[username]    

def all(contacts):
    # return and print all contacts and phobnes
    contacts_list = [f"{name} {phone}" for name, phone in contacts.items()]
    contacts_line = "\n".join(contacts_list)
    return contacts_line

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
            print(change_username_phone(args, contacts))
        
        elif command == "all":
            print(all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()