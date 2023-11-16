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
        return
    for document in result:
        print(document)
    
def case2():
    print("C'est le cas 2")
    
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
