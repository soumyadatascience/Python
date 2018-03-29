"""
@FunctionName - fib_seq
@Date : 27th March 2018
@author: Soumya Chatterjee
"""
#!/usr/bin/env python3

def fib_seq():
    '''
    fib_seq(num) --->Value
      Input: num = Nth number to which need to generate the fibonacci sequence
      Output:Fibonacci sequence to that number or to the Nth number
      Example - Input 5 , [1,2,3,5,8]
      '''
    while True:
        try:
            num = int(input('Enter number of digits for fib sequence: '))
        except:
            print("Looks like you did not enter an integer , Try Agin!")
            continue
        if num > 1000:
            print("Looks like Entered a Higer number!Try again")
            continue
        else:
            break
    a=1          # setting up the base cases 1
    b=1          # setting up the base cases 1  
    sequence=[1,1]
    for _ in range(2,num):
        a , b = b, a+b   # using swap generating fibonacci number of the next digit
        sequence.append(b)
    return sequence

def fib_sol2():

    while True:
        try:
            num = int(input('Enter number of digits for fib sequence: '))
        except:
            print("Looks like you did not enter an integer , Try Agin!")
            continue
        if num > 1000:
            print("Looks like Entered a Higer number!Try again")
            continue
        else:
            break  
            
    sequence=[1,1]
    for _ in range(2,num):
        sequence.append(sequence[-1]+sequence[-2])
    return sequence

def fib_gen_sol():
    while True:
        try:
            num = int(input('Enter number of digits for fib sequence: '))  
        except:
            print("Looks like you did not enter an integer , Try Agin!")
            continue
        if num > 1000:
            print("Looks like Entered a Higer number!Try again")
            continue
        else:
            break
    a=1
    b=1
    for _ in range(num):
        yield a
        a ,b = b, a+b

if __name__ == '__main__':
    print(fib_seq())    