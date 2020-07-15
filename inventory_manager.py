print("How many people are in your household?");
peopleInHouse = int(input())
print("How many days will you be sheltering in place?");
numDays = int(input())

print("How many water bottles do you have?");
waterBottles = int(input());
if waterBottles >= (peopleInHouse * numDays):
    print("You have enough water bottles.");
else:
    print("You don't have enough water bottles. You need ", ((peopleInHouse*numDays)-waterBottles)), " more watter bottles";
