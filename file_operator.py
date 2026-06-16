from datetime import datetime
import os

class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        print("\nEnter your journal entry:")
        entry_text = input().strip()
        
        if not entry_text:
            print("Error: Entry cannot be empty!")
            return
            
        # Current timestamp format: YYYY-MM-DD HH:MM:SS
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            # 'a' mode use kiya hai taaki new entry last me append ho aur file na ho to create ho jaye
            with open(self.filename, 'a', encoding='utf-8') as file:
                file.write(f"[{timestamp}]\n")
                file.write(f"{entry_text}\n\n")
            print("\nEntry added successfully!")
        except PermissionError:
            print("Error: Permission denied. Cannot write to the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_all_entries(self):
        try:
            # File ko read mode 'r' me open kar rahe hain
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                
            if not content:
                print("\nNo journal entries found. Start by adding a new entry!")
                return
                
            print("\nYour Journal Entries:")
            print("-" * 50)
            print(content)
            print("-" * 50)
            
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")

    def search_entry(self):
        try:
            # Pehle check kar rahe hain file khul rahi hai ya nahi
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Nothing to search.")
            return
        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")
            return

        keyword = input("\nEnter a keyword or date to search: ").strip().lower()
        if not keyword:
            print("Error: Search term cannot be empty.")
            return

        # Entries ko block wise read karne ke liye logic
        found = False
        current_timestamp = ""
        current_entry_text = ""
        matching_entries = []

        # File content ko split karke individual entries parse karna
        with open(self.filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()

        if not content:
            print(f"\nNo entries were found for the keyword: {keyword}")
            return

        # Double newline (\n\n) se entries separated hain
        entries = content.split("\n\n")
        
        for entry in entries:
            if entry.strip() and keyword in entry.lower():
                matching_entries.append(entry)
                found = True

        if found:
            print("\nMatching Entries:")
            print("-" * 50)
            for match in matching_entries:
                print(match)
                print()
            print("-" * 50)
        else:
            print(f"\nNo entries were found for the keyword: {keyword}")

    def delete_all_entries(self):
        if not os.path.exists(self.filename):
            print("\nOutput (If the file does not exist):")
            print("No journal entries to delete.")
            return

        confirm = input("\Are you sure you want to delete all entries? (yes/no): ").strip().lower()
        if confirm == 'yes':
            try:
                os.remove(self.filename)
                print("\nOutput (If the file is deleted successfully):")
                print("All journal entries have been deleted.")
            except PermissionError:
                print("Error: Permission denied. Cannot delete the file.")
            except Exception as e:
                print(f"Error deleting file: {e}")
        else:
            print("Deletion cancelled.")


def main():
    manager = JournalManager()
    
    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        
        user_input = input("\nUser Input:\n").strip()
        
        if user_input == '1':
            manager.add_entry()
        elif user_input == '2':
            manager.view_all_entries()
        elif user_input == '3':
            manager.search_entry()
        elif user_input == '4':
            manager.delete_all_entries()
        elif user_input == '5':
            print("\nOutput:")
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("\nOutput:")
            print("Invalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()