import math
import time

PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25;

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
    for numDimes in range(int(cents / DIME), -1, -1):
        for numNickels in range(int(cents / NICKEL), -1, -1):
            for numPennies in range(int(cents / PENNY), -1, -1):
                if (numQuarters * QUARTER + numDimes * DIME + numNickels * NICKEL + numPennies * PENNY == cents):
                    ways += 1

totalTime = time.time() * 1000 - start

print(ways," found in ",round(totalTime),"ms")