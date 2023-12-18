from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date 
        self.last_service_date = last_service_date

    def needs_service(self):
        date_calc = self.last_service_date.replace(self.last_service_date.year + 2)
        return date_calc < self.current_date
 
 