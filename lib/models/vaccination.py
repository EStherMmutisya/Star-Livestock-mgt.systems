import sqlite3

class Vaccination:
    def __init__(self, animal_id, vaccine_type, date_administered, next_due_date):
        self.animal_id = animal_id
        self.vaccine_type = vaccine_type
        self.date_administered = date_administered
        self.next_due_date = next_due_date

    def save_to_database(self):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Vaccination (animal_id, vaccine_type, date_administered, next_due_date)
            VALUES (?, ?, ?, ?)
        ''', (self.animal_id, self.vaccine_type, self.date_administered, self.next_due_date))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_vaccinations():
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Vaccination')
        vaccinations = cursor.fetchall()
        conn.close()
        return vaccinations

    @staticmethod
    def find_by_id(vaccination_id):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT animal_id, vaccine_type, date_administered, next_due_date FROM Vaccination WHERE id = ?', (vaccination_id,))
        vaccination_data = cursor.fetchone()
        conn.close()
        if vaccination_data:
            # Create a Vaccination instance from the fetched data
            vaccination_instance = Vaccination(*vaccination_data)
            return vaccination_instance
        else:
            return None

    @staticmethod
    def filter_by_criteria(criteria):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Vaccination WHERE ?', (criteria,))
        vaccinations = cursor.fetchall()
        conn.close()
        return vaccinations

    @staticmethod
    def sort_by_attribute(attribute):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Vaccination ORDER BY ?', (attribute,))
        vaccinations = cursor.fetchall()
        conn.close()
        return vaccinations

    def delete_from_database(self, vaccination_id):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Vaccination WHERE id = ?', (vaccination_id,))
        conn.commit()
        conn.close()
