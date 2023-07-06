import sqlite3
from sqlite3 import Error
import pyfiglet

def print_banner():
    banner_text = "Shadow Digger"
    creator_text = "Created by S3THR0"
    figlet_banner = pyfiglet.figlet_format(banner_text, font="banner")
    print(figlet_banner)
    print(creator_text.center(len(banner_text)))

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('shadowdigger.db')
        print(f'Successful connection to sqlite version {sqlite3.version}')
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    if conn:
        conn.close()
        print('Connection closed.')

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                          id INTEGER PRIMARY KEY,
                          full_name TEXT NOT NULL,
                          main_usernames TEXT,
                          home_address TEXT,
                          city TEXT,
                          zip_postal TEXT,
                          state_province TEXT,
                          country TEXT,
                          data TEXT
                          );''')
        print('Table created successfully')
    except Error as e:
        print(e)

def insert_entry(conn, entry):
    try:
        sql = ''' INSERT INTO entries(full_name, main_usernames, home_address, city, zip_postal, state_province, country, data)
                  VALUES(?,?,?,?,?,?,?,?) '''
        cursor = conn.cursor()
        cursor.execute(sql, entry)
        conn.commit()
        print(f'Entry added: {entry[0]}')
    except Error as e:
        print(e)

def display_entries(conn):
    try:
        print("Options:")
        print("1 - Display data for all entries")
        print("2 - Display data for a specific entry")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            return

        if choice == 1:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM entries")
            rows = cursor.fetchall()

            for row in rows:
                print_entry(row)

        elif choice == 2:
            try:
                specific_id = int(input("Enter specific ID to search: "))
            except ValueError:
                print("Invalid ID. Please try again.")
                return

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM entries WHERE id = ?", (specific_id,))
            rows = cursor.fetchall()

            for row in rows:
                print_entry(row)

        else:
            print("Invalid choice. Please try again.")
    except Error as e:
        print(e)

def print_entry(row):
    print(f"\nEntry ID: {row[0]}")
    print(f"Full Name: {row[1]}")
    print(f"Main Usernames: {row[2]}")
    print(f"Home Address: {row[3]}")
    print(f"City: {row[4]}")
    print(f"Zip/Postal: {row[5]}")
    print(f"State/Province: {row[6]}")
    print(f"Country: {row[7]}")
    print(f"Data: {row[8]}")

def main():
    print_banner()
    conn = create_connection()
    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")
        return

    while True:
        try:
            print("\nOptions:")
            print("1 - Add new entry")
            print("2 - Display entry")
            print("3 - Exit")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                print("\nEnter the details below:")
                full_name = input("Full Name: ")
                main_usernames = input("Main Usernames: ")
                home_address = input("Home Address: ")
                city = input("City: ")
                zip_postal = input("Zip/Postal: ")
                state_province = input("State/Province: ")
                country = input("Country: ")
                data = input("Data (all other information): ")

                entry = (full_name, main_usernames, home_address, city, zip_postal, state_province, country, data)
                insert_entry(conn, entry)
            elif choice == 2:
                display_entries(conn)
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid choice. Please try again.")
            
    close_connection(conn)

if __name__ == "__main__":
    main()
