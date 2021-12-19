"""
   * Author - Nitin Babar
   * Date -  15-DEC-2021
   * Time -  9:00 AM
   * Title - Stopwatch
"""

import time                                                     #importing time library
input("Press enter to start time")                              #taking input to convert for time property
start_time = time.time()
input("Press enter to end time")
end_time = time.time()
elapsed_time = end_time - start_time
print("The time elapsed is : ",elapsed_time)