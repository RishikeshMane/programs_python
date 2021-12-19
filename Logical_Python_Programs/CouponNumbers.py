"""
   * Author - Nitin Babar
   * Date -  15-DEC-2021
   * Time -  10:10 AM
   * Title - Coupon Number
"""



import random                                                        #using random module

class CouponNumber():                                                #defining class for couponnumber
    def __init__(self, take_number):
        """
            constructor initialize using parameter
        """
        self.take_number = take_number

    def calculateDistinctNumber(self):

        distict_number = []
        while len(distict_number) < self.take_number:
            rand = random.randrange(0, self.take_number)
            if rand not in distict_number:
                distict_number.append(rand)
            else:
                pass
        return distict_number


while True:                                                        #using while loop with try except block
    try:
        take_number = int(input("Enter the distinct number : "))
        if take_number < 0:
            print("Please Enter Positive Digits")
            continue
            """
                taking input from user
            """
        coupon_number_object = CouponNumber(take_number)
        total_random_number = coupon_number_object.calculateDistinctNumber()
        print("Total Distinct Coupon Number : ", total_random_number)
    except ValueError:
        print("Please Enter Digit Value")
    except:
        print("Exception Occured")