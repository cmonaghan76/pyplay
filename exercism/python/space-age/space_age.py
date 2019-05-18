class SpaceAge(object):
    """Given an earth age, in seconds, calculates how old
    someone would be on different planets."""

    
    def __init__(self, seconds):
        self.seconds = seconds
        self.__seconds_in_earthyear = 31557600


    def on_mercury(self):
        orbital_period = 0.2408467 #earth years
        return self.__calculate_age(orbital_period)


    def on_venus(self):
        orbital_period = 0.61519726 #earth years
        return self.__calculate_age(orbital_period)


    def on_earth(self):
        orbital_period = 1.0 #earth years
        return self.__calculate_age(orbital_period)


    def on_mars(self):
        orbital_period = 1.8808158 #earth years
        return self.__calculate_age(orbital_period)


    def on_jupiter(self):
        orbital_period = 11.862615 #earth years
        return self.__calculate_age(orbital_period)


    def on_saturn(self):
        orbital_period = 29.447498 #earth years
        return self.__calculate_age(orbital_period)


    def on_uranus(self):
        orbital_period = 84.016846 #earth years
        return self.__calculate_age(orbital_period)


    def on_neptune(self):
        orbital_period = 164.79132 #earth years)
        return self.__calculate_age(orbital_period)


    def __calculate_age(self, orbital_period):
        return round((self.seconds / (orbital_period * self.__seconds_in_earthyear)), 2)
