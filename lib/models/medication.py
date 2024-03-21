import sqlite3

class Medication:
    def __init__(self, medication_type, date_administered, dosage):
        self.medication_type = medication_type
        self.date_administered = date_administered
        self.dosage = dosage

    def save_to_database(self):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Medication (medication_type, date_administered, dosage)
            VALUES (?, ?, ?)
        ''', (self.medication_type, self.date_administered, self.dosage))
        conn.commit()
        conn.close()

    def add_animal(self, animal_id):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO MedicationAnimal (medication_id, animal_id)
            VALUES (?, ?)
        ''', (self.id, animal_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_medications_for_animal(animal_id):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Medication.*
            FROM Medication
            JOIN MedicationAnimal ON Medication.id = MedicationAnimal.medication_id
            WHERE MedicationAnimal.animal_id = ?
        ''', (animal_id,))
        medications = cursor.fetchall()
        conn.close()
        return medications

    @staticmethod
    def get_all_medications():
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Medication')
        medications = cursor.fetchall()
        conn.close()
        return medications

    @staticmethod
    def find_by_id(medication_id):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Medication WHERE id = ?', (medication_id,))
        medication = cursor.fetchone()
        conn.close()
        return medication

    @staticmethod
    def filter_by_type(medication_type):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Medication WHERE medication_type = ?', (medication_type,))
        medications = cursor.fetchall()
        conn.close()
        return medications

    @staticmethod
    def sort_by_date_administered():
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Medication ORDER BY date_administered')
        medications = cursor.fetchall()
        conn.close()
        return medications
