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
        id = len(database.carsType.find()) + 1
        database.carsType.insert_one({"ID": id, "manufacturer" : manufacturer, "model" : model, "transmission type" : transmission_type.split(), "fuel" : fuel, "CO2 emissions (g/km)" : CO2_emissions})
    elif collection == 2:
        name = str(input("Which country do you want to add : "))
        population = int(input("What is the population of the country : "))
        id = len(database.countries.find()) + 1
        database.countries.insert_one({"Country_ID": id, "Name" : name, "Population" : population})
    elif collection == 3:
        year = int(input("Which year's emissions do you want to add : "))
        country_id = int(input("What is the country id related to : "))
        car_id = int(input("What is the car id related to : "))
        emissions = float(input("What is the quantity of emmissionss : "))
        database.country_emissions.insert_one({year: year, Country_ID: country_id, Car_ID: car_id, emissions: 50000})

def case3():
    return

def case5():
    return


def delete_an_elem():
    collection = int(input("which collection do you want to delete an element from : 1 for the cars 2 for the countries 3 for the country emissions : "))
    if collection == 1:
        elem = int(input("What is the id of the cars that you want to delete : "))
        database.carsType.delete_one({"ID": elem})
    elif collection == 2:
        elem = int(input("What is the id of the country that you want to delete : "))
        database.countries.delete_one({"ID": elem})
    elif collection == 3:
        elem = int(input("What is the id of the Country_ID that you want to delete from emmissions collection : "))
        database.country_emissions.delete_one({"Country_ID": elem})
    else:
        print("enter a valid collection")
        return

def exit_system():
    exit()

def default():
    print("Enter a valid option")

def switch_case(argument):
    switch_dict = {
        1: display_name,
        2: add_an_element,
        3: case3,
        4: delete_an_elem,
        5: case5,
        6: exit_system
    }
    switch_dict.get(argument, default)()

while True:
    try:
        a = int(input("Choose an option 1 Display a collection 2 Add a new item to a collection 3 Update an item of a collection 4 Delete an item from a colleciton 5 Find an item 6 Exit : "))
        switch_case(a)
    except ValueError:
        print("Veuillez entrer un nombre entier.")
