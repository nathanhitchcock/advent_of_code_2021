import numpy as np


#delcaring the variables
#--------------------------------------------------------------
#gamma rate is most common bit in each position
gamma_rate = 0

#epsilon_rate is inverse of the gamma bit (least common)
epsilon_rate = 0

#The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
power_consumption = gamma_rate * epsilon_rate

count_bit0 = 0
count_bit1 = 0

#input the numbers from the dataset
#--------------------------------------------------------------
lst = open("input.dat").readlines()

arr = np.array(lst)

#testing pulling the array elements
for x in arr:
    if x[0] == "0":
        count_bit0 += 1
    else:
        count_bit1 += 1
if count_bit0 > count_bit1:
    print("the first bit is 0")
else:
    print("the first bit is 1")

for x in arr:
    if x[1] == "0":
        count_bit0 += 1
    else:
        count_bit1 += 1
if count_bit0 > count_bit1:
    print("the second bit is 0")
else:
    print("the second bit is 1")
