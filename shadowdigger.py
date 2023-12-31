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
                          date_of_birth TEXT,
                          phone_number TEXT,
                          email TEXT,
                          home_address TEXT,
                          city TEXT,
                          zip_postal TEXT,
                          state_province TEXT,
                          country TEXT,
                          facebook TEXT,
                          twitter TEXT,
                          instagram TEXT,
                          linkedin TEXT,
                          work_job_name TEXT,
                          work_address TEXT,
                          work_position TEXT,
                          other_work_info TEXT,
                          main_usernames TEXT,
                          data TEXT,
                          image BLOB
                          );''')
        print('Table created successfully')
    except Error as e:
        print(e)

def insert_entry(conn, entry):
    try:
        sql = ''' INSERT INTO entries(full_name, date_of_birth, phone_number, email, home_address, city, zip_postal, 
                  state_province, country, facebook, twitter, instagram, linkedin, work_job_name, work_address, 
                  work_position, other_work_info, main_usernames, data, image)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
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
    print(f"Date of Birth: {row[2]}")
    print(f"Phone Number: {row[3]}")
    print(f"Email: {row[4]}")
    print(f"Home Address: {row[5]}")
    print(f"City: {row[6]}")
    print(f"Zip/Postal: {row[7]}")
    print(f"State/Province: {row[8]}")
    print(f"Country: {row[9]}")
    print(f"Facebook: {row[10]}")
    print(f"Twitter: {row[11]}")
    print(f"Instagram: {row[12]}")
    print(f"LinkedIn: {row[13]}")
    print(f"Work Job Name: {row[14]}")
    print(f"Work Address: {row[15]}")
    print(f"Work Position: {row[16]}")
    print(f"Other Work Info: {row[17]}")
    print(f"Main Usernames: {row[18]}")
    print(f"Data: {row[19]}")
    print(f"Image: {row[20]}")

def update_entry(conn, entry):
    try:
        sql = ''' UPDATE entries SET full_name = ?, date_of_birth = ?, phone_number = ?, email = ?, home_address = ?, city = ?, 
                  zip_postal = ?, state_province = ?, country = ?, facebook = ?, twitter = ?, instagram = ?, linkedin = ?, 
                  work_job_name = ?, work_address = ?, work_position = ?, other_work_info = ?, main_usernames = ?, data = ?, 
                  image = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, entry)
        conn.commit()
        print(f'Entry updated: {entry[-1]}')
    except Error as e:
        print(e)

def delete_entry(conn, id):
    try:
        sql = ''' DELETE FROM entries WHERE id = ? '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        print(f'Entry deleted: {id}')
    except Error as e:
        print(e)

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
            print("3 - Edit entry")
            print("4 - Delete entry")
            print("5 - Exit")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                print("\nEnter the details below:")
                full_name = input("Full Name: ")
                date_of_birth = input("Date of Birth: ")
                phone_number = input("Phone Number: ")
                email = input("Email: ")
                home_address = input("Home Address: ")
                city = input("City: ")
                zip_postal = input("Zip/Postal: ")
                state_province = input("State/Province: ")
                country = input("Country: ")
                facebook = input("Facebook: ")
                twitter = input("Twitter: ")
                instagram = input("Instagram: ")
                linkedin = input("LinkedIn: ")
                work_job_name = input("Work Job Name: ")
                work_address = input("Work Address: ")
                work_position = input("Work Position: ")
                other_work_info = input("Other Work Info: ")
                main_usernames = input("Main Usernames: ")
                data = input("Data (all other information): ")
                image = input("Image (please provide path to image file): ")  

                entry = (full_name, date_of_birth, phone_number, email, home_address, city, zip_postal, state_province, 
                         country, facebook, twitter, instagram, linkedin, work_job_name, work_address, work_position, 
                         other_work_info, main_usernames, data, image)
                insert_entry(conn, entry)

            elif choice == 2:
                display_entries(conn)

            elif choice == 3:
                id = int(input("Enter the ID of the entry you want to edit: "))
                print("\nEnter the updated details below:")
                full_name = input("Full Name: ")
                date_of_birth = input("Date of Birth: ")
                phone_number = input("Phone Number: ")
                email = input("Email: ")
                home_address = input("Home Address: ")
                city = input("City: ")
                zip_postal = input("Zip/Postal: ")
                state_province = input("State/Province: ")
                country = input("Country: ")
                facebook = input("Facebook: ")
                twitter = input("Twitter: ")
                instagram = input("Instagram: ")
                linkedin = input("LinkedIn: ")
                work_job_name = input("Work Job Name: ")
                work_address = input("Work Address: ")
                work_position = input("Work Position: ")
                other_work_info = input("Other Work Info: ")
                main_usernames = input("Main Usernames: ")
                data = input("Data (all other information): ")
                image = input("Image (please provide path to image file): ")

                entry = (full_name, date_of_birth, phone_number, email, home_address, city, zip_postal, state_province, 
                         country, facebook, twitter, instagram, linkedin, work_job_name, work_address, work_position, 
                         other_work_info, main_usernames, data, image, id)  # ID added at the end
                update_entry(conn, entry)

            elif choice == 4:
                id = int(input("Enter the ID of the entry you want to delete: "))
                delete_entry(conn, id)

            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid choice. Please try again.")
            
    close_connection(conn)

if __name__ == "__main__":
    main()