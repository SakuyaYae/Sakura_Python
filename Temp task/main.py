"""
The main file
@SakuyaYae
"""
from hotel import show_hotels

def main():
    hotels = show_hotels()
    while True:
        Print("==============")
        print("==== Menu ====")
        Print("==============")
        print("")
        print("chose one of: ")
        print(" q/Q: to quit")
        print("")
        print("Hotel: to see avaleble hotels")
        print("")
        print("")
        print("")
        choice = input("--> ")
        choice.lower()

        if choice == "q":
            print("Thank you")
            break

        elif "hotel" in choice:
            hotels.show()
        else:
            Print("==============")
            print("==== Menu ====")
            Print("==============")
            print("")
            print("chose one of: ")
            print(" q/Q: to quit")
            print("")
            print("Hotel: to see avaleble hotels")
            print("")
            print("")
            print("")
