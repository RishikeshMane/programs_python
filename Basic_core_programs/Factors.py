"""
   * Author - Nitin Chandrakant Babar
   * Date -  14-12-2021
   * Time -  9pm
   * Title - Print the prime factors of number N.
"""
f = 0
num = int(input("Enter the number: "))              #taking input and asign it to num variable

for i in range(2, num + 1):                         #using for loop in range function with nested for loop in if statements
    if num % i == 0:
        for j in range(2, int(i / 2)):
            if i % j == 0:
                f = 1
                break
        if f == 0:
            print(i)