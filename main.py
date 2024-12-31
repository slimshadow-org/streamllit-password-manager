import getpass
import pyperclip
from storage.password_store import PasswordStore
from utils.password_generator import generate_password, check_password_strength

def main():
    print("=== Simple Password Manager ===")
    
    # Login/Initialize
    master_password = getpass.getpass("Enter master password: ")
    store = PasswordStore(master_password)
    
    while True:
        print("\nOptions:")
        print("1. Add new password")
        print("2. View passwords")
        print("3. Search passwords")
        print("4. Generate password")
        print("5. Edit password")
        print("6. Delete password")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        try:
            if choice == "1":
                service = input("Service name: ")
                username = input("Username: ")
                password = input("Password (press Enter to generate): ")
                
                if not password:
                    length = int(input("Password length (default 16): ") or "16")
                    password = generate_password(length)
                    print(f"Generated password: {password}")
                
                strength, feedback = check_password_strength(password)
                print(f"\nPassword strength: {strength}/5")
                print(f"Feedback: {feedback}")
                
                notes = input("Notes (optional): ")
                entry = store.add_entry(service, username, password, notes)
                print(f"\nPassword saved for {service}")
                
            elif choice == "2":
                for entry in store.entries:
                    print(f"\nService: {entry.service}")
                    print(f"Username: {entry.username}")
                    print(f"Password: {'*' * len(entry.password)}")
                    if entry.notes:
                        print(f"Notes: {entry.notes}")
                
            elif choice == "3":
                query = input("Search query: ")
                results = store.search_entries(query)
                
                if results:
                    for entry in results:
                        print(f"\nService: {entry.service}")
                        print(f"Username: {entry.username}")
                        show = input("Show password? (y/n): ").lower() == 'y'
                        if show:
                            print(f"Password: {entry.password}")
                else:
                    print("No matches found")
                    
            elif choice == "4":
                length = int(input("Password length (default 16): ") or "16")
                password = generate_password(length)
                print(f"Generated password: {password}")
                strength, feedback = check_password_strength(password)
                print(f"\nPassword strength: {strength}/5")
                print(f"Feedback: {feedback}")
                
            elif choice == "5":
                service = input("Enter service name to edit: ")
                entries = store.search_entries(service)
                
                if entries:
                    for i, entry in enumerate(entries):
                        print(f"{i+1}. {entry.service} ({entry.username})")
                    
                    idx = int(input("Select entry number: ")) - 1
                    if 0 <= idx < len(entries):
                        entry = entries[idx]
                        print("\nLeave blank to keep current value")
                        username = input(f"New username [{entry.username}]: ") or entry.username
                        password = input("New password (Enter to keep current): ") or entry.password
                        notes = input(f"New notes [{entry.notes}]: ") or entry.notes
                        
                        store.update_entry(entry.id, username=username, password=password, notes=notes)
                        print("Entry updated successfully")
                else:
                    print("No matching entries found")
                    
            elif choice == "6":
                service = input("Enter service name to delete: ")
                entries = store.search_entries(service)
                
                if entries:
                    for i, entry in enumerate(entries):
                        print(f"{i+1}. {entry.service} ({entry.username})")
                    
                    idx = int(input("Select entry number to delete: ")) - 1
                    if 0 <= idx < len(entries):
                        confirm = input("Are you sure? (y/n): ").lower() == 'y'
                        if confirm:
                            store.delete_entry(entries[idx].id)
                            print("Entry deleted successfully")
                else:
                    print("No matching entries found")
                    
            elif choice == "7":
                break
                
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()