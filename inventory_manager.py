import math
import sys

# import tkinter

global numDays
global numHours
global numPeople
global neededRations
global neededCalories


def hurricane_shelter():
    # This function runs if the user selects "shelter" from the hChoice menu.
    # It asks the user basic questions about their household to determine how many supplies they'll need over the course of the next several days.
    print("How many people are in your household?")
    numPeople = int(input())
    # print("How many pets are in your household?")
    # petsInHouse = int(input())
    print("How many days will you be sheltering in place?")
    numDays = int(input())
    print("How many gallon jugs of water do you have?")
    waterGallons = int(input())
    print("How many individual water bottles do you have, excluding gallon jugs?")
    waterBottles = int(input())

    neededRations = (numPeople * numDays)
    # neededRations multiplies the number of people sheltering in place by the number of days one will be sheltering
    # in place, to get a base for each type of emergency supply.
    numHours = (numDays * 24)
    neededCalories = (neededRations * 2000)
    # In the aftermath of a disaster people typically need a minimum 2000 calories per day because being stressed out
    # burns more calories.
    # If the user wants to customize this number to determine how many meal replacement bags or #10 cans to buy,
    # just change the "2000" to the number of calories you personally require daily.
    numWeeks = math.ceil(numDays / 7)
    # These are self explanatory. We use math.ceil() so that numWeeks will always return an int rather than a float, and
    # round up to err on the side of caution. You can have too many rations, but you can't have too few.
    neededGallons = (neededRations * 3)
    # In the aftermath of a disaster people need 3 gallons of water per day for drinking and also for cooking.
    totalWater = (waterGallons + (waterBottles * 0.13203125))
    gPH = round((9.1 / 1.1), 2)
    # The average 2000w Honda Inverter Generator recommended for efficiency and also for quietness by the US Government
    # can run a modern fridge/freezer, an electric burner or microwave, plus a couple of lights and fans for 9.1 hours
    # on a full tank of 1.1 gallons of gas.
    neededGallonsGas = round(numHours / gPH, 2)

    # Rounded to the hundredths place because unlike water bottles, one can absolutely buy a fraction of a gallon of gas.

    def enough_water_shelter():
        # This function calculates how much water, in terms of either gallon jugs or 16.9L water bottles the user will
        # need over the course of sheltering in place, as defined by Ready.gov as 3 gallons per person, per day.
        # We round up to the nearest whole number because it doesn't make sense to buy half a bottle/gallon of water.
        if totalWater >= neededGallons:
            print("You have enough water.")
        else:
            print("You don't have enough water. You need an additional:", math.ceil(neededGallons - totalWater),
                  "gallons, or:", math.ceil((neededGallons - totalWater) / 0.13203125), "bottles of water.")
            print()

    def enough_food_shelter():
        print("You need a total of:", math.ceil(neededRations * 3), "meals.")
        print("This is the equivalent of", math.ceil(neededCalories), "calories, or:")
        print(math.ceil(neededCalories / 6800.0), "bags of Huel meal replacement, or:")
        # This number comes from the Huel website
        print(math.ceil((neededRations * 3) / 8), "Mountain House #10 Cans.")
        # This one isn't exact. Mountain House #10 cans contain either 7, 8, or 9 meals, depending on the flavor, but
        # most contain 8 meals. If the flavor you like contains a different amount of meals, replace the '8' with that number.
        print()

    def additional_supplies_shelter():
        print("You need a total of", math.ceil((numPeople * 2) * numWeeks),
              "N95 masks to reduce the spread of Covid-19.")
        # This is a rough estimate, you can be the judge of how many masks you go through.
        print("You need a total of", math.ceil((numPeople * numWeeks) / 2), "bottles of hand sanitizer.")
        # This is a rough estimate and probably needs to be retooled a bit. The formula makes sense when numDays is a
        # normal amount of days to shelter in place, between 3 and 28, but quickly spirals out of control when numDays
        # is a ridiculously huge number.
        print("You need enough prescription medication per person for", numDays, "days.")
        # You definitely need more than this to account for breaks in the supply chain, but there isn't really a great way
        # to determine exactly how much more. Originally I had 'numDays + 7' which is great for hurricanes but that
        # doesn't work as well when numDays is, say, over 350.
        print("You need", numPeople, "flashlights, and", numPeople, "headlamps.")
        # Again, the output for these makes sense when numDays is a normal amount of days but realistically one would need
        # more than this if numDays was a larger number.
        print("You need", math.ceil(numPeople * numDays * 1.5), "protein bars.")
        # Again, the output for this makes sense in a regular 'shelter in place' situation, originally I had it set to
        # 2 per person per day, but when numDays is a large number, it returned more protein bars than any family could
        # possibly want.
        print("You need", math.ceil((numPeople * numDays) / 3), "boxes of Cosmic Brownies.")
        # This is a New Orleans in-joke.
        print("You need approximately", neededGallonsGas,
              "gallons of gas for a standard 2000w Honda inverter generator.")

    def output_text():
        sys.stdout = open("Inventory_Report_Shelter_In_Place.txt", "w")
        # prints the number of supplies the user would need into a separate text file called "Inventory Report"
        enough_water_shelter()
        enough_food_shelter()
        additional_supplies_shelter()
        sys.stdout.close()

    output_text()


def hurricane_evacuation():
    print("How many people will you be traveling with?")
    numPeople = int(input())
    # print("How many pets will you be traveling with?")
    # petsInCar = int(input())
    print("How many days will your journey be? (Always plan for travel delays when evacuating.)")
    numDays = int(input())
    print("How many gallon jugs of water do you have in your vehicle?")
    waterGallonsEvac = int(input())
    print("How many individual water bottles do you have, excluding gallon jugs?")
    waterBottlesEvac = int(input())
    totalWaterEvac = (waterGallonsEvac + (waterBottlesEvac * 0.13203125))

    neededRations = (numPeople * numDays)
    neededCalories = (neededRations * 2000)
    numWeeks = math.ceil(numDays / 7)

    def enough_water_evac():
        if totalWaterEvac >= neededRations:
            print("You have enough water.")
        else:
            print("You don't have enough water. You need an additional:", math.ceil(neededRations - totalWaterEvac),
                  "gallons, or:", math.ceil((neededRations - totalWaterEvac) / 0.13203125), "bottles of water.")
            print()

    def enough_food_evac():
        print("You need a total of:", math.ceil(neededRations * 3), "meals.")
        print("This is the equivalent of", math.ceil(neededCalories), "calories, or:")
        print(math.ceil(neededCalories / 6800.0), "bags of Huel meal replacement, or:")
        # This number comes from the Huel website
        print(math.ceil((neededRations * 3) / 8), "Mountain House #10 Cans.")
        # This one isn't exact. Mountain House #10 cans contain either 7, 8, or 9 meals, depending on the flavor, but
        # most contain 8 meals. If the flavor you like contains a different amount of meals, replace the '8' with that number.
        print()

    def additional_supplies_evac():
        print("You need a total of", math.ceil((numPeople * 2) * numWeeks),
              "N95 masks to reduce the spread of Covid-19.")
        print("You need a total of", math.ceil((numPeople * numWeeks) / 2), "bottles of hand sanitizer.")
        print("You need enough prescription medication per person for", numDays + 7, "days.")
        print("You need", numPeople, "flashlights, and", numPeople, "headlamps.")
        print("You need", math.ceil(numPeople * numDays * 1.5), "protein bars.")
        print("You need", math.ceil((numPeople * numDays) / 3), "boxes of Cosmic Brownies.")

    def output_text():
        sys.stdout = open("Inventory_Report_Evac.txt", "w")
        # prints the number of supplies the user would need into a separate text file called "Inventory Report_Evac"
        enough_water_evac()
        enough_food_evac()
        additional_supplies_evac()
        sys.stdout.close()

    output_text()


def hurricane_choice():
    hChoice = input("Are you evacuating or sheltering in place? Please enter either 'evacuating' or 'sheltering'.")
    if hChoice == "evacuating":
        hurricane_evacuation()
    elif hChoice == "sheltering":
        hurricane_shelter()
    else:
        print("Please enter either 'evacuating' or 'sheltering'.")
        hurricane_choice()


def hurricane_CAT():
    stormTypes = ['TS', '1', '2', '3', '4', '5']
    hCAT = input("What Category is the storm? Please enter either TS, 1, 2, 3, 4, or 5. ")
    if hCAT not in stormTypes:
        print("Please enter either TS, 1, 2, 3, 4, or 5.")
        hurricane_CAT()
    elif hCAT == "4" or hCAT == "5":
        print("We strongly recommend you evacuate for a Category 4 or 5 storm.")
        hurricane_choice()
    else:
        hurricane_choice()


def main():
    print("Hurricane Survival - Inventory Management v0.4")
    hurricane_CAT()


main()
