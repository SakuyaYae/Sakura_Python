"""
The main file
@SakuyaYae
"""
from hotel import show_hotels
from bus import bus_info
from resturant import resturant_info
from train import train_info


# Två flygbolag som flyger till Târgu Mureș, Budapest, Cluj-Napoca och Bukarest.
# Det statliga järnvägsbolaget som kör tåg mellan de fyra städerna.
# Ett bussbolag som kör rundturer från Târgu Mureș och Cluj-Napoca till häftiga platser i Transsylvanien.
# Tre suspekta hotell med märkliga ägare.
# Fyra restauranger med risk för matförgiftning.

def main():
    hotels = show_hotels()
    bus = bus_info()
    resturant = resturant_info()
    train = train_info()
    while True:
        print("")
        print("==============")
        print("==== Menu ====")
        print("==============")
        print("")
        print("chose one of: ")
        print(" q/Q: to quit")
        print("")
        print("Hotel: to see avaleble hotels")
        print("")
        print("Bus Price: to see price info on buses")
        print("Bus: to see all info on buses")
        print("Bus Time: to see when buses are avaleble ")
        print("")
        print("Resturant: to see avaleble resturants")
        print("")
        print("Train Price: to see price info on Trains")
        print("Train: to see all info on Trains")
        print("Train Time: to see when Trains are avaleble ")
        choice = input("--> ")
        choice = choice.lower()

        if choice == "q":
            print("Thank you")
            break

        elif "hotel" in choice:
            hotels.show()

        elif "bus price" in choice:
            bus.price_info()
        elif "bus time" in choice:
            bus.time_info()
        elif "bus" in choice:
            bus.price_info()
            bus.time_info()
        elif "resturant" in choice:
            resturant.info()
        elif "train price" in choice:
            train.price_info()
        elif "train time" in choice:
            train.time_info()
        elif "train" in choice:
            train.price_info()
            train.time_info()
        else:
            print("")
            print("==============")
            print("==== Menu ====")
            print("==============")
            print("")
            print("chose one of: ")
            print(" q: to quit")
            print("")
            print("Hotel: to see avaleble hotels")
            print("")
            print("Bus Price: to see price info on buses")
            print("Bus: to see all info on buses")
            print("Bus Time: to see when buses are avaleble ")
            print("")
            print("Resturant: to see avaleble resturants")
            print("")
            print("Train Price: to see price info on Trains")
            print("Train: to see all info on Trains")
            print("Train Time: to see when Trains are avaleble ")
main()
