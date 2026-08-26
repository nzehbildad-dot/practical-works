# A small in-memory database of people.
people = {
    "Tunde": {
        "name": "Tunde",
        "age": 16,
        "city": "Ikeja"
    },
    "Ada": {
        "name": "Ada",
        "age": 12,
        "city": "London"
    }
}


def show_person(person):
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")


def find_person_key(name):
    name = name.casefold()
    return next(
        (key for key in people if key.casefold() == name),
        None
    )


while True:
    print("\n1. Show all people")
    print("2. Find a person")
    print("3. Add a person")
    print("4. Update a person")
    print("5. Delete a person")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        for person in people.values():
            show_person(person)
            print()

    elif choice == "2":
        name = input("Input the name: ").strip()
        person_key = find_person_key(name)
        person = people.get(person_key)
        if person:
            show_person(person)
        else:
            print("Person not found.")

    elif choice == "3":
        name = input("Input the name: ").strip()
        if find_person_key(name) is not None:
            print("That person already exists.")
        else:
            age = int(input("Input the age: "))
            city = input("Input the city: ").strip()
            people[name] = {"name": name, "age": age, "city": city}
            print("Person added.")

    elif choice == "4":
        name = input("Input the name: ").strip()
        person_key = find_person_key(name)
        person = people.get(person_key)
        if person:
            person["age"] = int(input("Input the new age: "))
            person["city"] = input("Input the new city: ").strip()
            print("Person updated.")
        else:
            print("Person not found.")

    elif choice == "5":
        name = input("Input the name: ").strip()
        person_key = find_person_key(name)
        if person_key is not None:
            people.pop(person_key)
            print("Person deleted.")
        else:
            print("Person not found.")

    elif choice == "6":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")


