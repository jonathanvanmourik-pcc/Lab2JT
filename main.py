#Jonathan van Mourik
#Terrance Stemm
#Sword Price Calculator
#Adds prices of different swords together
#Display Total Price of Swords and the Date
#_________________
#Please enter Price of the Sword:
#Would you like to add another sword (y/n)?
#y
#Please enter Price of the Sword:
#Would you like to add another sword (y/n)?
#
#Date: x/y/z
#The total price of the swords is: X
import datetime


def main():
    swordPriceList = 0.0
    swordNameList = []
    swordTotalPrice = 0.0

    swordPriceList, swordNameList = get_swords()
    swordTotalPrice = calc_total_sword_price(swordPriceList)
    print_output(swordTotalPrice, swordNameList, swordPriceList)

def get_swords():
    swordPrice = 0.0
    swordPriceList = []
    repeatVal = "y"
    swordName= ""
    swordNameList = []

    while repeatVal == "y":
        swordPrice = float(input("Please enter Price of the Sword: "))
        swordPriceList.append(swordPrice)
        swordName = str(input("Please enter Name of the Sword: "))
        swordNameList.append(swordName)
        repeatVal = input("Would you like to add another sword (y/n)? ")
    return(swordPriceList, swordNameList)

def calc_total_sword_price(swordPriceList):
    totalSwordPrice = 0.0

    for i in range(len(swordPriceList)):
        totalSwordPrice += swordPriceList[i]
    return(totalSwordPrice)


def print_output(totalSwordPrice, swordNameList, swordPriceList):
    print("\nDate: ", datetime.date.today())

    for i in range(len(swordNameList)):
        print(swordNameList[i] + ":", swordPriceList[i])
    print("Total Sword Price: $", (totalSwordPrice))


if __name__ == "__main__":
    main()