import os
contacts = []

print("Welcome to the Contact Manager!")
print("\n Available commands:")
print("1. add - Add a new contact")
print("2. read - Read all contacts")
print("3. exit - Exit the program")

opt = input("\nEnter your command: ").strip().lower()

def save_contacts_to_file(filename="contacts.txt"):
    with open(filename, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']}\n")

while opt != "exit":
    if opt == "add":
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact phone number: ").strip()
        contacts.append({"name": name, "phone": phone})
        save_contacts_to_file()
        print(f"Contact {name} added successfully!")

    elif opt == "read":
        if not os.path.exists("contacts.txt") or os.path.getsize("contacts.txt") == 0:
            print("No contacts found.")
        else:
            print("\nContacts List:")
            with open("contacts.txt", "r") as file:
                for line in file:
                    name, phone = line.strip().split(",")
                    print(f"Name: {name}, Phone: {phone}")
    else:
        print("Invalid command. Please try again.")

    opt = input("\nEnter your command: ").strip().lower()