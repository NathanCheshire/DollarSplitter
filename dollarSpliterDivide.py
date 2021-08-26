import math
import time

PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25

#ONLY CHANGE THE NUMBER HERE
dollarAmount = 5

if (math.floor(dollarAmount) == dollarAmount):
    print('Provided dollar amount: ', dollarAmount)
else:
    print('Specified amount was not an integer so we\'ve floored your value')
    dollarAmount = math.floor(dollarAmount)
    print('Provided dollar amount: ', dollarAmount)

ways = 0
cents = dollarAmount * 100

start = time.time() * 1000

for numQuarters in range(int(cents / QUARTER), -1, -1):
    centsAfterQuartersLeft = cents - numQuarters * QUARTER

    #quarters alone made amount, example, 4 for $1 or 8 for $2
    if (centsAfterQuartersLeft == 0):
        ways += 1
    else:
        maxDimes = int(math.floor(centsAfterQuartersLeft / DIME))
        for numDimes in range(maxDimes, -1, -1):
            centsAfterDimesLeft = centsAfterQuartersLeft - numDimes * DIME

            #quarters and dimes alone made amount
            if (centsAfterDimesLeft == 0):
                ways += 1
            else:
                maxNickels = int(math.floor(centsAfterDimesLeft / NICKEL))
                for numNickels in range(maxNickels, -1, -1):
                    centsAfterNickelsLeft = centsAfterDimesLeft - numNickels * NICKEL

                    #quarters, dimes, and nickels made dollar amount
                    if (centsAfterNickelsLeft == 0):
                        ways += 1
                    else:
                        maxPennies = int(math.floor(centsAfterNickelsLeft / PENNY))
                        for numPennies in range(maxPennies, -1, -1):
                            centsAfterPenniesLeft = centsAfterNickelsLeft - numPennies * PENNY

                            if (centsAfterPenniesLeft == 0):
                                ways += 1


totalTime = time.time() * 1000 - start

print(ways," found in ",round(totalTime),"ms")