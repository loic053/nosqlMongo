from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['cars']

hybrids = database.hybrid
petrols = database.petrol
electricities = database.electricity

def display_name():
    collection = int(input("which collection do you want to see : 1 for hybrid \n\t2 for petrol \n\t3 for electricity : "))
    if collection == 1:
        result = hybrids.find()
    elif collection == 2:
        result = petrols.find()
    elif collection == 3:
        result = electricities.find()
    else:
        print("enter a valid collection")
        return
    for document in result:
        print(document)
    
def add_an_element():
    collection = int(input("which collection do you want to add an item ? : 1 for hybrid \n\t2 for petrol \n\t3 for electricity : "))
    if collection != 1 and collection != 2 and collection != 3:
        print("enter a valid collection")
        return
    manufacturer = str(input("manufacturer of the car : "))
    model = str(input("model of the car : "))
    transmission_type = str(input("transmission type of the car : "))
    fuel = str(input("fuel of the car : "))
    CO2_emissions = str(input("CO2 emissions (g/km) of the car : "))
    if collection == 1:
        database.hybrid.insert_one({"manufacturer" : manufacturer, "model" : model, "transmission type" : transmission_type, "fuel" : fuel, "CO2 emissions (g/km)" : CO2_emissions})
    elif collection == 2:
        database.petrol.insert_one({"manufacturer" : manufacturer, "model" : model, "transmission type" : transmission_type, "fuel" : fuel, "CO2 emissions (g/km)" : CO2_emissions})
    elif collection == 3:
        database.electricity.insert_one({"manufacturer" : manufacturer, "model" : model, "transmission type" : transmission_type, "fuel" : fuel, "CO2 emissions (g/km)" : CO2_emissions})

def case3():
    exit()

def default():
    print("C'est le cas par défaut")

def switch_case(argument):
    switch_dict = {
        1: display_name,
        2: add_an_element,
        3: case3
    }
    switch_dict.get(argument, default)()

while True:
    try:
        a = int(input("Entrez une valeur (1, 2 ou 3) : "))
        switch_case(a)
    except ValueError:
        print("Veuillez entrer un nombre entier.")
