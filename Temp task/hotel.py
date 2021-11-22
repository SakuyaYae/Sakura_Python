"""
The file containing classes for hotels
@author SakuyaYae
"""

class hotel:
    pos = ""
    date_of_arival = ""
    hotel_info = []
    def __init__(self, pos):
        self.pos = pos

    def check_pos():
        pass


class terror_hotel(hotel):
    price = "from 250/night"
    def __init__(self, pos, date_of_arival):
        self.pos = pos
        self.date_of_arival = date_of_arival
        
    def info(self):
        super().hotel_info[0] = "Posision: "
        super().hotel_info[1] = self.pos
        super().hotel_info[2] = " Date of arrival: "
        super().hotel_info[3] = self.date_of_arival
        super().hotel_info[4] = " price: "
        super().hotel_info[5] = self.price

