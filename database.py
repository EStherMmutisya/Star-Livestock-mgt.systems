import sqlite3

def create_tables():
    # Connect to the SQLite database
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()

    # Creating the Animal table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Animal (
            id INTEGER PRIMARY KEY,
            species TEXT,
            breed TEXT,
            date_of_birth DATE
        )
    ''')

    # Creating the Vaccination table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vaccination (
            id INTEGER PRIMARY KEY,
            animal_id INTEGER,
            vaccine_type TEXT,
            date_administered DATE,
            next_due_date DATE,
            FOREIGN KEY (animal_id) REFERENCES Animal(id)
        )
    ''')

    # Creating the Medication table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Medication (
            id INTEGER PRIMARY KEY,
            animal_id INTEGER,
            medication_type TEXT,
            date_administered DATE,
            dosage TEXT,
            FOREIGN KEY (animal_id) REFERENCES Animal(id)
        )
    ''')

    # Commit and close changes
    conn.commit()
    conn.close()

# Call the function to create tables when this module is executed
if __name__ == "__main__":
    create_tables()
