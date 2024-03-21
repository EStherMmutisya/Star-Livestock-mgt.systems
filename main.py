from lib.models.animal import Animal
from lib.models.vaccination import Vaccination
from lib.models.medication import Medication
from database import create_tables

def main():
    # Create the database tables
    create_tables()

    # Create some animals
    animal1 = Animal('Dog', 'Labrador', '2022-01-01')
    
    animal2 = Animal('Cow', 'Holstein-Friesian', '2022-01-01'),  # Commonly found in East Africa
    animal3= Animal('Goat', 'Saanen', '2021-12-15'),  # Commonly found in East Africa
    animal4= Animal('Sheep', 'Dorper', '2022-02-20'),  # Commonly found in East Africa
    animal5=Animal('Chicken', 'Kienyeji', '2022-03-10'),  # Commonly found in East Africa
    animal6=Animal('Pig', 'Large White', '2022-04-05'),  # Commonly found in East Africa
    animal7=Animal('Duck', 'Khaki Campbell', '2022-05-15'),  # Commonly found in East Africa
    animal8=Animal('Turkey', 'Bourbon Red', '2022-06-20'),  # Commonly found in East Africa
    animal9=Animal('Rabbit', 'New Zealand White', '2022-07-25'),  # Commonly found in East Africa
    animal10=Animal('Guinea Fowl', 'Helmeted', '2022-08-30')
    animal1.save_to_database()

    # Create some medications
    medication1 = Medication('Painkiller', '2022-01-05', '2 tablets')
    medication1.save_to_database()

    # Create some vaccinations
    vaccination1 = Vaccination(animal_id=1, vaccine_type='Rabies', date_administered='2022-03-15', next_due_date='2022-04-15')
    vaccination1.save_to_database()

    # Print all animals
    print("All Animals:")
    all_animals = Animal.get_all_animals()
    for animal in all_animals:
        print(animal)

    # Print all medications
    print("\nAll Medications:")
    all_medications = Medication.get_all_medications()
    for medication in all_medications:
        print(medication)

    # Print all vaccinations
    print("\nAll Vaccinations:")
    all_vaccinations = Vaccination.get_all_vaccinations()
    for vaccination in all_vaccinations:
        print(vaccination)

    # Delete a vaccination
    print("\nDeleting Vaccination:")
    vaccination_id_to_delete = 1
    vaccination_to_delete = Vaccination.find_by_id(vaccination_id_to_delete)
    if vaccination_to_delete:
        vaccination_to_delete.delete_from_database(vaccination_id_to_delete)
        print(f"Vaccination with ID {vaccination_id_to_delete} deleted.")
    else:
        print(f"Vaccination with ID {vaccination_id_to_delete} not found.")

if __name__ == "__main__":
    main()
