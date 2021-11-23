"""
The main file
@SakuyaYae
"""
from hotel import show_hotels
from bus import bus_info

def main():
    hotels = show_hotels()
    bus = bus_info()
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
            print("Bus: to see info on buses")
            print("")
main()
