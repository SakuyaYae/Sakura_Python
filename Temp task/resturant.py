"""
The classes for resturants
"""
class resturant:
    pos = ""
    date_of_arival = ""
    resturant_info = ["", "", "", "", "", "", "", ""]
    def __init__(self):
        pass

class chem_lab_food(resturant):
    price_food = "from 100"
    price_drink = "from 15"
    pos = "Bukarest"
    posion = "85%"
    def __init__(self):
        pass

    def info(self):
        super().resturant_info[0] = "Chem Lab Food "
        super().resturant_info[1] = "Posision: "
        super().resturant_info[2] = self.pos
        super().resturant_info[3] = "Food Price: "
        super().resturant_info[4] = self.price_food
        super().resturant_info[5] = "Drink Price"
        super().resturant_info[6] = self.price_drink
        super().resturant_info[7] = "Risk of food posioning: "
        super().resturant_info[8] = self.posion

        return super().resturant_info

class monsters_food_bar(resturant):
    price_food = "from 55"
    price_drink = "from 20"
    pos = "Cluj-Napoca"
    posion = "95%"
    def __init__(self):
        pass

    def info(self):
        super().resturant_info[0] = "Monsters Food Bar "
        super().resturant_info[1] = "Posision: "
        super().resturant_info[2] = self.pos
        super().resturant_info[3] = "Food Price: "
        super().resturant_info[4] = self.price_food
        super().resturant_info[5] = "Drink Price"
        super().resturant_info[6] = self.price_drink
        super().resturant_info[7] = "Risk of food posioning: "
        super().resturant_info[8] = self.posion

        return super().resturant_info

class undead_armies(resturant):
    price_food = "from 50"
    price_drink = "from 10"
    pos = "Târgu Mureș"
    posion = "100%"
    def __init__(self):
        pass

    def info(self):
        super().resturant_info[0] = "Undead Armies Bar "
        super().resturant_info[1] = "Posision: "
        super().resturant_info[2] = self.pos
        super().resturant_info[3] = "Food Price: "
        super().resturant_info[4] = self.price_food
        super().resturant_info[5] = "Drink Price"
        super().resturant_info[6] = self.price_drink
        super().resturant_info[7] = "Risk of food posioning: "
        super().resturant_info[8] = self.posion

        return super().resturant_info

class vlad_draculas_castle(resturant):
    price_food = "from 125"
    price_drink = "from 20"
    pos = "Budapest"
    posion = "5%"
    def __init__(self):
        pass

    def info(self):
        super().resturant_info[0] = "Vlad Draculas Castle "
        super().resturant_info[1] = "Posision: "
        super().resturant_info[2] = self.pos
        super().resturant_info[3] = "Food Price: "
        super().resturant_info[4] = self.price_food
        super().resturant_info[5] = "Drink Price"
        super().resturant_info[6] = self.price_drink
        super().resturant_info[7] = "Risk of food posioning: "
        super().resturant_info[8] = self.posion

        return super().resturant_info
class resturant_info:
    vlad = vlad_draculas_castle()
    monsters = monsters_food_bar()
    chem = chem_lab_food()
    undead = undead_armies()
    def __init__(self):
        pass
    def info(self):
        print(self.vlad.info)
        print(self.monsters.info)
        print(self.chem.info)
        print(self.undead.info)
