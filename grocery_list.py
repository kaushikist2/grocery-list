import json
import os

FILE_NAME = "grocery_data.json"

def load_items():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_items(items):
    with open(FILE_NAME, "w") as file:
        json.dump(items, file, indent=4)

def show_items(items):
    if not items:
        print("\nYour grocery list is empty.")
    else:
        print("\nGrocery List:")
        for idx, item in enumerate(items, 1):
            print(f"{idx}. {item}")

def add_item(items):
    item = input("Enter item name: ").strip()
    if item:
        items.append(item)
        save_items(items)
        print(f"'{item}' added successfully!")

def remove_item(items):
    show_items(items)
    try:
        index = int(input("Enter item number to remove: "))
        removed = items.pop(index - 1)
        save_items(items)
        print(f"'{removed}' removed!")
    except (ValueError, IndexError):
        print("Invalid choice!")

def main():
    items = load_items()

    while True:
        print("\n--- Grocery List Menu ---")
        print("1. View items")
        print("2. Add item")
        print("3. Remove item")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_items(items)
        elif choice == "2":
            add_item(items)
        elif choice == "3":
            remove_item(items)
        elif choice == "4":
            print("Goodbye! 🛒")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
