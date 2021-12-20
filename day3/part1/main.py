import numpy as np


#delcaring the variables
#--------------------------------------------------------------
#gamma rate is most common bit in each position
gamma_rate = []

#epsilon_rate is inverse of the gamma bit (least common)
epsilon_rate = []

#The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
power_consumption = gamma_rate * epsilon_rate

count_bit0 = 0
count_bit1 = 0

#input the numbers from the dataset
#--------------------------------------------------------------
lst = open("input.dat").readlines()

arr = np.array(lst)

#testing pulling the array elements
def most_frequent(i, gamma_rate, epsilon_rate):
    count_bit0 = 0
    count_bit1 = 0
    #print(type(i), i)
    if int(i) == 0:
        count_bit0 += 1
    else:
        count_bit1 += 1
    if count_bit0 > count_bit1:
        gamma_rate.append(i)
        return gamma_rate
    else:
        epsilon_rate.append(i)
        return epsilon_rate

def main():
    for col in zip(*arr):
        for i in col:
            print(i)
            most_frequent(i, gamma_rate, epsilon_rate)
    print('the gamma_rate is: ', gamma_rate)
    print('the epsilon_rate is: ', epsilon_rate)

if __name__ == "__main__":
    main()
