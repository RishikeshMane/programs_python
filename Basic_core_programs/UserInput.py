"""
    * Author - Nitin Chandrakant Babar
    * Date -  14-12-2021
    * Time -  10.30pm
    * Title - User Input and Replace String Template
"""


                                                                 
text=input("User Name:")                                        #defining text variable
text=str(text)                                                  #converting input to string property with str function
text_length=len(text)                                           #finding out length of text variable
   
if text_length >= 3:
    print(text_length)
    print("Hello", text,"How are you?")
else:
    print("Inalid Name")