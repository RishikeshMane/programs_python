"""
    * Author - Nitin Chandrakant Babar
    * Date -  14-12-2021
    * Time -  10pm
	* Title - Harmonic Series Check
"""

# Use try except block.
try:                                                           #using try catch methods

	n=int(input("Enter nth number:"))                          #taking input
	def harmonic_sum(n):
		
		if n < 2:
			return 1
		else:
	    		return 1 / n + (harmonic_sum(n - 1))
	    
	print(harmonic_sum(n))
	
except Exception as e:                           
	print("Enter Numeric Value" ,e) 