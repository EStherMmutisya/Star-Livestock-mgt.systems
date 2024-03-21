import sqlite3

class Animal:
    def __init__(self, species, breed, date_of_birth):
        self.species = species
        self.breed = breed
        self.date_of_birth = date_of_birth

    def save_to_database(self):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Animal (species, breed, date_of_birth)
            VALUES (?, ?, ?)
        ''', (self.species, self.breed, self.date_of_birth))
        conn.commit()
        conn.close()

    def delete_from_database(self, animal_id):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Animal WHERE id = ?', (animal_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_animals():
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Animal')
        animals = cursor.fetchall()
        conn.close()
        return animals

    @staticmethod
    def find_by_id(animal_id):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Animal WHERE id = ?', (animal_id,))
        animal = cursor.fetchone()
        conn.close()
        return animal

    @staticmethod
    def filter_by_species(species):
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Animal WHERE species = ?', (species,))
        animals = cursor.fetchall()
        conn.close()
        return animals

    @staticmethod
    def sort_by_date_of_birth():
        conn = sqlite3.connect('animals.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Animal ORDER BY date_of_birth')
        animals = cursor.fetchall()
        conn.close()
        return animals