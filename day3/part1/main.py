import numpy as np


#delcaring the variables
#--------------------------------------------------------------
#gamma rate is most common bit in each position
gamma_rate = 0

#epsilon_rate is inverse of the gamma bit (least common)
epsilon_rate = 0

#The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
power_consumption = gamma_rate * epsilon_rate


#input the numbers from the dataset
#--------------------------------------------------------------
lst = open("input.dat").readlines()

arr = np.array(lst)

for x in arr[1]:
    for y in x:
        print(y)
