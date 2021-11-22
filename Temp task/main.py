"""
The main file
@SakuyaYae
"""
from hotel import show_hotels

def main():
    hotels = show_hotels()
    while True:
        choice = input("--> ")
        choice.lower()

        if choice == "q":
            print("Bye, bye - Lets meet again sometime!")
            break

        elif "hotel" in choice:
            hotels.show()
            
            
