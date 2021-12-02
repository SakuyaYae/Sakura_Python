"""
The classes for trains
"""

class train:
        train_ticket_fee_adult = "100/a day"
        train_ticket_fee_kid = "40/a day"
        train_ticket_fee_baby = "free"
        avaleble_day = " Mon-Sun"
        avaleble_trips_Mon_fre = ["07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
        avaleble_trips_sat_sun = ["10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
        def __init__(self):
            pass
class train_info:
    trains = train()
    def __init__(self):
        pass
    def time_info(self):
        print("Avaleble days: " + self.trains.avaleble_day)
        print("Avaleble times mon-fre: ", self.trains.avaleble_trips_Mon_fre)
        print("Avaleble times sat-sun: ", self.trains.avaleble_trips_sat_sun)
    def price_info(self):
        print("Price adult: " + self.trains.train_ticket_fee_adult)
        print("Price kid: " + self.trains.train_ticket_fee_kid)
        print("Price baby: " + self.trains.train_ticket_fee_baby)
