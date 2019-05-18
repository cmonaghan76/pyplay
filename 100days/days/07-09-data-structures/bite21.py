cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    jeeps = str()
    for x in range(len(cars['Jeep'])):
        jeeps += cars['Jeep'][x]
        if x < (len(cars['Jeep'])-1):
            jeeps += ", "
    return jeeps

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
   first_cars = list()
   for car in cars.values():
       first_cars.append(car[0])
    return first_cars

def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matches = list()
    for carlist in cars.values():
        for car in carlist:
            if grep.lower() in car.lower():
                matches.append(car)
    matches.sort()
    return matches

def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    for carlist in cars.values():
        carlist = carlist.sort()
    return cars