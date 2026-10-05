#Jonathan van Mourik
#Terrance Stemm
#Sword Price Calculator
#Adds prices of different swords together
#Display Total Price of Swords and the Date


#_________________ Test Plan
#Please enter Price of the Sword:
#Would you like to add another sword (y/n)?
#y
#Please enter Price of the Sword:
#Would you like to add another sword (y/n)?
#
#Date: x/y/z
#The total price of the swords is: X
#___________________________ Actual Output
#Please enter Name of the Sword: Flamberge
#Please enter Price of the Sword: 10.2
#Would you like to add another sword (y/n)? y
#Please enter Name of the Sword: zweihander
#Please enter Price of the Sword: 5.4
#Would you like to add another sword (y/n)? n

#Date:  2026-10-04
#Number of Swords: 2
#Flamberge: $10.20
#Zweihander: $5.40
#Total Sword Price: $15.60

import datetime


def main():
    swordPriceList = 0.0
    swordNameList = []
    swordTotalPrice = 0.0

    swordPriceList, swordNameList = get_swords()
    swordTotalPrice = calc_total_sword_price(swordPriceList)
    print_output(swordTotalPrice, swordNameList, swordPriceList)

def get_swords():
    #gets the price and name of any number of swords
    swordPrice = 0.0
    swordPriceList = []
    repeatVal = "y"
    swordName= ""
    swordNameList = []

    while repeatVal == "y":
        swordName = str(input("Please enter Name of the Sword: "))
        swordNameList.append(swordName)
        swordPrice = float(input("Please enter Price of the Sword: "))
        swordPriceList.append(swordPrice)
        repeatVal = input("Would you like to add another sword (y/n)? ")
    return(swordPriceList, swordNameList)

def calc_total_sword_price(swordPriceList):
    #calculates the total of all the swords
    totalSwordPrice = 0.0

    for i in range(len(swordPriceList)):
        totalSwordPrice += swordPriceList[i]
    round(totalSwordPrice, 2)
    return(totalSwordPrice)


def print_output(totalSwordPrice, swordNameList, swordPriceList):
    #Prints output
    print("\nDate: ", datetime.date.today(), "\nNumber of Swords: " + str(len(swordNameList)))

    for i in range(len(swordNameList)):
        print("{:}: ${:.2f}".format(swordNameList[i], swordPriceList[i]).capitalize())
    print("Total Sword Price: ${:.2f}".format(totalSwordPrice))


if __name__ == "__main__":
    main()