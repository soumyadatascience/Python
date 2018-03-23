"""
@FunctionName - NthPI
@Date : 21st March 2018
@author: Soumya Chatterjee
"""
#!/usr/bin/env python3
import decimal


def NthPI():
    '''
    NthPI(digits) --->Value
      Input: digits = Number of decimal places to calculate the value of PI
      Output:Value of PI to the folating precision entered as Input
      Example - Input 10 , Pi = 3.1415926535
    '''
    D = decimal.Decimal
    while True:
        try:
            digits = int(input('Enter number of digits for PI approximation: max-1000- '))
        except:
            print("Looks like you did not enter an integer , Try Agin!")
            continue
        if digits > 1000:
            print("Looks like Entered a Higer number!Try again")
            continue
        else:
            break

    decimal.getcontext().prec = digits
    pi = D(0)
    counter = 0
    while counter <= digits:
        # pi = sum (0 to n )([ 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6) ])
        m1 = D(16) ** D((-counter))
        el1 = D(4) / D(((8 * counter) + 1))  # 4/(8k+1)
        el2 = D(2) / D(((8 * counter) + 4))  # 2/(8k+4)
        el3 = D(1) / D(((8 * counter) + 5))  # 1/(8k+5)
        el4 = D(1) / D(((8 * counter) + 6))  # 1/(8k+6)
        pi += D(m1) * D((el1 - el2 - el3 - el4))
        counter += 1
    return pi


if __name__ == '__main__':
    print(NthPI())
