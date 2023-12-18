from tires.tires import Tires
import math

class Octoprime(Tires):
    '''
    @tire_worn: array of 4 numbers, each number between 0 and 1 inclusive
    when the sum of all values in 
    the tire wear array is greater than or equal to 3.
    '''
    def __init__(self, tire_worn):
        self.tire_worn = tire_worn

    def needs_service(self):
        return round(sum(self.tire_worn), 9)  >= 3.0