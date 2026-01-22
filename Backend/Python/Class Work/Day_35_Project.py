import mysql.connector
from mysql.connector import Error

# --- Configuration ---
# IMPORTANT: Update these with your actual MySQL credentials
DB_CONFIG = {
    "host": "localhost",
    "database": "contact_db",
    "user": "your_mysql_user",   # e.g., "root"
    "password": "your_mysql_password" # e.g., "secret"
}
# ---------------------
















# create table contacts()
# create table contacts(
# name varchar(100),
# id int primary key auto_increment,
# phn_num bigint,);








def get_db_connection():
    """Establishes and returns a MySQL database connection."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
    return None

def show_contacts():
    """1. Shows all available contacts."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, phone FROM contacts ORDER BY name")
        records = cursor.fetchall()
        
        if not records:
            print("\n--- 📖 Contacts List ---")
            print("No contacts found.")














        else:
            print("\n--- 📖 Contacts List ---")
            print("{:<5} {:<20} {:<15}".format("ID", "Name", "Phone"))
            print("-" * 40)
            for (contact_id, name, phone) in records:
                print("{:<5} {:<20} {:<15}".format(contact_id, name, phone))
        
    except Error as e:
        print(f"❌ Failed to show contacts: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

def create_contact():
    """2. Creates a new contact."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    
    if not name or not phone:
        print("🛑 Name and phone cannot be empty.")
        return

    conn = get_db_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        query = "INSERT INTO contacts (name, phone) VALUES (%s, %s)"
        cursor.execute(query, (name, phone))
        conn.commit()
        print(f"✅ Contact '{name}' created successfully.")
        
    except mysql.connector.IntegrityError as e:
        # Handles duplicate phone number error (UNIQUE constraint violation)
        print(f"❌ Failed to create contact: A contact with phone number {phone} already exists.")
    except Error as e:
        print(f"❌ Failed to create contact: {e}")
        conn.rollback() # Rollback changes on failure
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

def update_contact():
    """3. Updates an existing contact by ID."""
    show_contacts() # Show list to help user choose ID
    
    try:
        contact_id = int(input("\nEnter the ID of the contact to update: "))
    except ValueError:
        print("🛑 Invalid ID format. Must be a number.")
        return

    name = input("Enter new name (leave blank to keep current): ").strip()
    phone = input("Enter new phone number (leave blank to keep current): ").strip()

    if not name and not phone:
        print("🛑 No changes specified.")
        return

    conn = get_db_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True) # dictionary=True makes result a dict
        
        # 1. Fetch current contact data
        cursor.execute("SELECT name, phone FROM contacts WHERE id = %s", (contact_id,))
        record = cursor.fetchone()
        
        if not record:
            print(f"❌ Contact with ID {contact_id} not found.")
            return

        # Use current values if input is empty
        new_name = name if name else record['name']
        new_phone = phone if phone else record['phone']

        # 2. Update the contact
        query = "UPDATE contacts SET name = %s, phone = %s WHERE id = %s"
        cursor.execute(query, (new_name, new_phone, contact_id))
        
        if cursor.rowcount > 0:
            conn.commit()
            print(f"✅ Contact ID {contact_id} updated successfully.")
        else:
             print(f"🛑 Contact ID {contact_id} not found or no new changes were applied.")

    except mysql.connector.IntegrityError:
        print(f"❌ Failed to update contact: The phone number '{new_phone}' is already in use by another contact.")
    except Error as e:
        print(f"❌ Failed to update contact: {e}")
        conn.rollback()
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
            
def search_contact():
    """4. Searches for a contact by name or number."""
    search_term = input("Enter name or phone number to search: ").strip()
    
    if not search_term:
        print("🛑 Search term cannot be empty.")
        return

    conn = get_db_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        # Use LIKE for partial matches (wildcard search)
        query = ("SELECT id, name, phone FROM contacts "
                 "WHERE name LIKE %s OR phone LIKE %s "
                 "ORDER BY name")
        
        # Add wildcards to the search term
        search_pattern = f"%{search_term}%"
        cursor.execute(query, (search_pattern, search_pattern))
        records = cursor.fetchall()
        
        if not records:
            print(f"\n Search Results ")
            print(f"No contacts found matching '{search_term}'.")
        else:
            print(f"\n Search Results for '{search_term}' ---")
            print("{:<5} {:<20} {:<15}".format("ID", "Name", "Phone"))
            print("-" * 40)
            for (contact_id, name, phone) in records:
                print("{:<5} {:<20} {:<15}".format(contact_id, name, phone))

    except Error as e:
        print(f" Failed to search contacts: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

def delete_contact():
    """5. Deletes a contact by ID."""
    show_contacts() # Show list to help user choose ID
    
    try:
        contact_id = int(input("\nEnter the ID of the contact to delete: "))
    except ValueError:
        print(" Invalid ID format. Must be a number.")
        return

    conn = get_db_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        query = "DELETE FROM contacts WHERE id = %s"
        cursor.execute(query, (contact_id,))
        
        if cursor.rowcount > 0:
            conn.commit()
            print(f" Contact ID {contact_id} deleted successfully.")
        else:
            print(f"Contact with ID {contact_id} not found.")

    except Error as e:
        print(f" Failed to delete contact: {e}")
        conn.rollback()
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

def display_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 40)
    print("  Contact Management System")
    print("=" * 40)
    print("1. MENU -> TO SHOW CONTACTS WHICH ARE AVAILABLE")
    print("2. TO CREATE THE CONTACT")
    print("3. UPDATE THE CONTACT")
    print("4. SEARCH FOR THE CONTACT WITH NAME OR NUMBER")
    print("5. DELETE THE CONTACT")
    print("6. Exit")
    print("-" * 40)

def main():
    """Main function to run the application loop."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            show_contacts()
        elif choice == '2':
            create_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("🛑 Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()