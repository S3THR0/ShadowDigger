# Shadow Digger

Shadow Digger is a Python-based doxing/people database tool that uses SQLite3 for storing and retrieving personal data. The application presents a CLI (Command Line Interface) to interact with the user, allowing the addition of new entries and displaying all stored entries.

**Disclaimer: This tool is intended for legal and ethical use only, such as data management for investigative journalism, security research, or any other lawful purpose. Misuse of this tool for illegal activities is strictly prohibited. The creator assumes no liability and is not responsible for any misuse or damage caused by this program.**

## Installation

This application requires Python3 and a couple of Python libraries: `sqlite3` and `pyfiglet`.

First, make sure that Python3 is installed on your system. If not, you can download it from the [official Python website](https://www.python.org/).

Once Python3 is installed, you can download the required Python libraries using pip:

```
pip install sqlite3 pyfiglet
```

## Usage

To start the application, run the following command:

```
python shadowdigger.py
```

After starting, the application will present a menu with three options:

1. Add new entry: Allows you to add a new entry into the database. The following information will be asked:
    - Full Name
    - Main Usernames
    - Home Address
    - City
    - Zip/Postal
    - State/Province
    - Country
    - Data (all other information)
  
2. Display entries: Displays all the entries stored in the database.
   
3. Exit: Closes the application.

## Code Structure

- `print_banner()`: Prints an ASCII banner at the start of the application.
- `create_connection()`: Creates a connection to the SQLite database.
- `close_connection(conn)`: Closes the SQLite database connection.
- `create_table(conn)`: Creates a new table in the SQLite database.
- `insert_entry(conn, entry)`: Inserts a new entry into the SQLite database.
- `display_entries(conn)`: Displays all entries from the SQLite database.
- `main()`: The main function to run the program.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
