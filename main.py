#Welcome To Our Home!!
import random


print("Welcome to Our House, We hope you enjoy your stay!")

guests = int(input("How many Guests will be staying?" ))
timeline = int(input("How long will guests will stay at home? "))
bags = int(input("How much Luggage do you have? "))

print("Where would you like to sleep? \n(1) Upstairs\n(2) Downstairs")
location = input("Select where you would like to sleep:")




#------------------------- Prefrences -----------------------------------------------------------------------------------------------------
want_prefrences = input("Would you like some prefrences for your room? (Y/N)").strip().upper()


if want_prefrences == "Y":
    preferences = input("What are your room preferences?"
                        "(AC, Extra Blankets, Mini-Fridge, TV): ")
    preference_list = [pref.strip() for pref in preferences.split(",")]


    print("\nYou have selected the following room preferences/amenities:")
    for pref in preference_list:
        print(f"- {pref}")
elif want_prefrences == "N":
        print("Very Well Then")
#------------------------------------------------------------------------------------------------------------------------------------------------- 



#-------------------Activities-------------------------------------------------------------------------------------------------------------
wantActivities = input("Would you like some prefrences for your room? (Y/N)").strip().upper()

if wantActivities == "Y":
    activites = input("What activities would you like to do? \n"               
                    " \n(1)Go to the city"                                
                    "\n(2)Eat Out"
                    "\n(3)Watch Movies" 
                    "\n(4)Go to a Club"
                    "\nChoose your option:")
    if activites == "1":
        citychoice = input("Where in Atlanta would you like to visit?"
            "\n(1)Midtown"
            "\n(2)Buckhead"
            "\n(3)Buford"
            "\n(4)Dunwoody"
            "\n(5)Peachtree City"
            "\n Select City In Atlanta:")
        

        if citychoice == "1":
            print("You chose Midtown! 🌆")
        elif citychoice == "2":
            print("You chose Buckhead! 🏙️")
        elif citychoice == "3":
            print("You chose Buford! 🛍️")
        elif citychoice == "4":
            print("You chose Dunwoody! 🌳")
        elif citychoice == "5":
            print("You chose Peachtree City! ")

    if activites == "2":
        resturantchoice = input("Which type of resturant would you like to eat"
            "\n(1)American"
            "\n(2)Indian"
            "\n(3)Chinese"
            "\n(4)Italian"
            "\n(5)Mediterranian")
        restaurants = {
                "1": ["Applebee's", "Chili's", "LongHorn Steakhouse"],
                "2": ["Madras Chettinad", "Bombay Kitchen", "Tandoori Palace"],
                "3": ["Panda Express", "PF changs", "Masterpiece"],
                "4": ["Olive Garden", "Maggiano's", "Little Italy"],
                "5": ["Mezza Luna", "Mediterranean Grill", "Santorini's"]
            }
        if resturantchoice in restaurants:
                suggestion = random.choice(restaurants[resturantchoice])
                print(f"You chose {resturantchoice}. A great option is: {suggestion} it won't hurt to try one day")
        else:
                print("Don't be Like that Choose Something!")
                
                
    if activites == "3":
        print("Here is List of Movie Threaters in Area:"
            "\n(1)Regal Cinemas Avalon"
            "\n(2)AMC Dine In Movies"
            "\n(3)Movie Studio Grill"
            "\n(4)Regal Medlock Crossing"
            "\n(5)CMX CinéBistro Peachtree Corners"
            "\n(6)CMX CinéBistro Halcyon")
        
    if activites == "4":
        Clubs =  [
            "MJQ Concourse",
            "Tongue & Groove",
            "The Basement",
            "Buckhead Theatre",
            "Gold Room",
            "The Regent Cocktail Club",
            "Opera Nightclub",
            "Sound Table",
            "Corner Tavern",
            "Velvet Room",
            "Club Onyx",
            "The Mansion Club"
        ]
    print("List of Clubs:")
    for i, club in enumerate(Clubs, start=1):
        print(f"{i}. {club}")
        
elif wantActivities == "N":
    print("Your Loss")
#---------------------------------------------------------------------------------------------------------------------------    
    
def roomCost(guests,timeline,location):
    locationprices = {
        "1": 100,
        "2":50
    }
    
    base_price = locationprices.get(location, 80)
    
    if guests >= 2:
        extra_guest = (guests - 2) * 20
    else:
        extra_guest = 0

    
    
    
    total = (base_price + extra_guest) * timeline
    
    return total


cost = roomCost(guests,timeline,location)
print(f"\nTotal:${cost}")

