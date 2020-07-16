import math
import sys

print("Welcome to our Hurricane Preparedness App")
print("How many people are in your household?")
peopleInHouse = int(input())
print("How many days will you be sheltering in place?")
numDays = int(input())

print("How many gallon jugs of water do you have?")
waterGallons = int(input())
print("How many individual water bottles do you have, excluding gallon jugs?")
waterBottles = int(input())
neededGallons = (peopleInHouse * numDays * 3)
totalWater = (waterGallons + (waterBottles * 0.13203125))


def enough_water():
    if totalWater >= neededGallons:
        print("You have enough water.")
    else:
        print("You don't have enough water. You need an additional:", math.ceil(neededGallons - totalWater), "gallons, or:", math.ceil((neededGallons - totalWater) / 0.13203125), "bottles of water.")


def output_text():
    sys.stdout = open("test.txt", "w")
    enough_water()
    sys.stdout.close()



output_text()
