from tires.tires import Tires

class CarriganTire(Tires):
    '''
    tire_worn: array of 4 numbers, each number between 0 and 1 inclusive
    any number is greater than or equal to 0.9
    '''
    def __init__(self, tire_worn):
        self.tire_worn = tire_worn
        
    def needs_service(self):
        return max(self.tire_worn) >= 0.9 