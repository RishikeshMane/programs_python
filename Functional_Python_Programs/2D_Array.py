"""
    * Author - Nitin Chandrakant Babar
    * Date -  15-12-2021
    * Time -  9Am
    * Title - 2D-Array 
"""

def Input2DArray(Number):
    """
    Description: we are taking Input2DArray as a function and passing Number as Parameter
    Parameter: Number
    Number as a input
    
    """

    for i in range(2):                                          #defining nested for loops
        for j in range(2):
             print(Number,end=" ")
        print()

Number=input("Enter a Number : ")                               #takinging input and converting to all properties of int , float and boolean by using their functions
Input2DArray(int(Number))
Input2DArray(float(Number))
Input2DArray(bool(Number))