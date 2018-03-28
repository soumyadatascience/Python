"""
@FunctionName - NthE
@Date : 27th March 2018
@author: Soumya Chatterjee
"""
#!/usr/bin/env python3
import decimal
import math


def NthE():
    '''
    NthE(digits) --->Value
      Input: digits = Number of decimal places to calculate the value of e
      Output:Value of e to the folating precision entered as Input
      Example - Input 10 , e = 2.7182818284
    '''
    D = decimal.Decimal
    while True:
        try:
            digits = int(input('Enter number of digits for e approximation(max-1000): '))
        except:
            print("Looks like you did not enter an integer , Try Agin!")
            continue
        if digits > 1000:
            print("Looks like Entered a Higer number!Try again")
            continue
        else:
            break

    decimal.getcontext().prec = digits
    e = D(0)
    counter = 0
    while counter <= digits:
        # e = sum (0 to n)(1/n!)
        e+=D(1)/D(math.factorial(counter))
        counter += 1
    return e


if __name__ == '__main__':
    print(NthE())