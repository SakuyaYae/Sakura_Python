"""
The file containing the bus classes
@author SakuyaYae
"""

class buses:
    bus_ticket_fee = "100/a day"
    avaleble_day = " Mon-Fri"
    avaleble_trips_a_day = "09:00 - 12:00 or 14:00 - 17:00"
    def __init__(self):
        pass

class bus_info():
    bus = buses()
    def __init__(self):
        pass
    def price_info(self):
        print("Price: " + self.bus.bus_ticket_fee)
    def time_info(self):
        print("Days whit bus trips: " + self.bus.avaleble_day)
        print("Buses are avaleble: " + self.bus.avaleble_trips_a_day)
