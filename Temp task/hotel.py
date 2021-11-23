"""
The file containing classes for hotels
@author SakuyaYae
"""

class hotel:
    pos = ""
    date_of_arival = ""
    hotel_info = ["", "", "", "", ""]
    def __init__(self):
        pass


class terror_hotel(hotel):
    price = "from 250/night"
    pos = "Târgu Mureș"
    def __init__(self):
        pass

    def info(self):
        super().hotel_info[0] = "Terror Hotel"
        super().hotel_info[1] = " Posision: "
        super().hotel_info[2] = self.pos
        super().hotel_info[3] = " price: "
        super().hotel_info[4] = self.price

        return super().hotel_info

class spooky_hotel(hotel):
    price = "from 350/night"
    pos = "Budapest"
    def __init__(self):
        pass

    def info(self):
        super().hotel_info[0] = "Spooky Hotel"
        super().hotel_info[1] = " Posision: "
        super().hotel_info[2] = self.pos
        super().hotel_info[3] = " price: "
        super().hotel_info[4] = self.price

        return super().hotel_info

class doomed_hotel(hotel):
    price = "from 381/night"
    pos = "Cluj-Napoca"
    def __init__(self):
        pass

    def info(self):
        super().hotel_info[0] = "Doomed Hotel"
        super().hotel_info[1] = " Posision: "
        super().hotel_info[2] = self.pos
        super().hotel_info[3] = " price: "
        super().hotel_info[4] = self.price

        return super().hotel_info

class show_hotels:
    spooky = spooky_hotel()
    terror = terror_hotel()
    doomed = doomed_hotel()
    def __init__(self):
        pass
    def show(self):
        print(self.spooky.info())
        print(self.terror.info())
        print(self.doomed.info())
