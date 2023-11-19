from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['cars']

def display_name():
    collection = int(input("which collection do you want to see : 1 for the cars 2 for the countries 3 for the country emissions : "))
    if collection == 1:
        result = database.carsType.find()
    elif collection == 2:
        result = database.countries.find()
    elif collection == 3:
        result = database.country_emissions.find()
    else:
        print("enter a valid collection")
        return
    for document in result:
        print(document)
    
def add_an_element():
    collection = int(input("which collection do you want to add an item ? : 1 for the cars 2 for the countries 3 for the country emissions : "))
    if collection != 1 and collection != 2 and collection != 3:
        print("enter a valid collection")
        return
    if collection == 1:
        manufacturer = str(input("manufacturer of the car : "))
        model = str(input("model of the car : "))
        transmission_type = str(input("transmission type of the car : "))
        fuel = str(input("fuel of the car : "))
        CO2_emissions = str(input("CO2 emissions (g/km) of the car : "))
        id = len(list(database.carsType.find())) + 1
        database.carsType.insert_one({"ID": id, "manufacturer" : manufacturer, "model" : model, "transmission type" : transmission_type, "fuel" : fuel.split(), "CO2 emissions (g/km)" : CO2_emissions})
    elif collection == 2:
        name = str(input("Which country do you want to add : "))
        population = int(input("What is the population of the country : "))
        id = len(list(database.countries.find())) + 1
        database.countries.insert_one({"Country_ID": id, "Name" : name, "Population" : population})
    elif collection == 3:
        year = int(input("Which year's emissions do you want to add : "))
        country_id = int(input("What is the country id related to : "))
        car_id = int(input("What is the car id related to : "))
        emissions = float(input("What is the quantity of emmissionss : "))
        database.country_emissions.insert_one({year: year, Country_ID: country_id, Car_ID: car_id, emissions: 50000})

def update_fields(collection, identifier):
    new_data = {}
    for field in ["manufacturer", "model", "transmission type", "fuel", "CO2 emissions (g/km)"]:
        new_data[field] = str(input(f"New {field}: "))
    if collection == 1:
        database.carsType.update_one({"manufacturer": identifier}, {"$set": new_data})
    elif collection == 2:
        database.countries.update_one({"Country_ID": identifier}, {"$set": new_data})
    elif collection == 3:
        database.country_emissions.update_one({"Country_ID": identifier}, {"$set": new_data})

def update_an_element():
    collection = int(input("Which collection do you want to update an item? 1 for the cars, 2 for the countries, 3 for the country emissions: "))
    if collection != 1 and collection != 2 and collection != 3:
        print("Enter a valid collection")
        return
    if collection == 1:
        manufacturer = str(input("Manufacturer of the car to update: "))
        if database.carsType.find_one({"manufacturer": manufacturer}):
            update_fields(collection, manufacturer)
        else:
            print(f"The car with manufacturer '{manufacturer}' does not exist in the carsType collection.")
    elif collection == 2:
        country_id = int(input("Country_ID of the country to update: "))
        if database.countries.find_one({"Country_ID": country_id}):
            update_fields(collection, country_id)
        else:
            print(f"The country with Country_ID '{country_id}' does not exist in the countries collection.")
    elif collection == 3:
        country_id = int(input("Country_ID of the country emissions to update: "))
        if database.country_emissions.find_one({"Country_ID": country_id}):
            update_fields(collection, country_id)
        else:
            print(f"The country emissions with Country_ID '{country_id}' does not exist in the country_emissions collection.")

def find_item_by_text():
    search_text = input("Enter text to search for in stock items: ")
    result_carsType = database.carsType.find({"$or": [
        {"manufacturer": {"$regex": search_text, "$options": "i"}},
        {"model": {"$regex": search_text, "$options": "i"}},
        {"transmission_type": {"$regex": search_text, "$options": "i"}},
        {"fuel": {"$regex": search_text, "$options": "i"}},
        {"CO2_emissions_g_km": {"$regex": search_text, "$options": "i"}}
    ]})
    result_countries = database.countries.find({"$or": [
        {"Name": {"$regex": search_text, "$options": "i"}},
        {"Population": {"$regex": search_text, "$options": "i"}}
    ]})
    result_country_emissions = database.country_emissions.find({"$or": [
        {"year": {"$regex": search_text, "$options": "i"}},
        {"Country_ID": {"$regex": search_text, "$options": "i"}},
        {"Car_ID": {"$regex": search_text, "$options": "i"}},
        {"Quantity": {"$regex": search_text, "$options": "i"}}
    ]})
    print(f"Search Results for '{search_text}' in carsType:")
    for document in result_carsType:
        print(document)
    print(f"Search Results for '{search_text}' in countries:")
    for document in result_countries:
        print(document)
    print(f"Search Results for '{search_text}' in country_emissions:")
    for document in result_country_emissions:
        print(document)

def delete_an_elem():
    collection = int(input("which collection do you want to delete an element from : 1 for the cars 2 for the countries 3 for the country emissions : "))
    if collection == 1:
        elem = int(input("What is the id of the cars that you want to delete : "))
        database.carsType.delete_one({"ID": elem})
    elif collection == 2:
        elem = int(input("What is the id of the country that you want to delete : "))
        database.countries.delete_one({"Country_ID": elem})
    elif collection == 3:
        elem = int(input("What is the id of the Country_ID that you want to delete from emmissions collection : "))
        database.country_emissions.delete_one({"Country_ID": elem})
    else:
        print("Enter a valid collection")
        return

def exit_system():
    exit()

def default():
    print("Enter a valid option")

def switch_case(argument):
    switch_dict = {
        1: display_name,
        2: add_an_element,
        3: update_an_element,
        4: delete_an_elem,
        5: find_item_by_text,
        6: exit_system
    }
    switch_dict.get(argument, default)()

while True:
    try:
        a = int(input("Choose an option 1 Display a collection 2 Add a new item to a collection 3 Update an item of a collection 4 Delete an item from a colleciton 5 Find an item 6 Exit : "))
        switch_case(a)
    except ValueError:
        print("Enter an integer")
