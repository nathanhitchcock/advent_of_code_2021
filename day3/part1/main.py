import numpy as np

import statistics as st

#delcaring the variables
#--------------------------------------------------------------
#gamma rate is most common bit in each position
gamma_rate = []

#epsilon_rate is inverse of the gamma bit (least common)
epsilon_rate = []

#The power consumption can then be found by multiplying the gamma rate by the epsilon rate (decimal format).
#power_consumption = gamma_rate * epsilon_rate

#input the numbers from the dataset
#--------------------------------------------------------------
lst = open("input2.dat").readlines()

arr = np.array(lst)

def main():
    #iterate through each column of the dataset
    for col in zip(*arr):
        #identify the mode (most common) character in the column
        most_frequent = st.mode(col)

        #add the mode to the gamma_rate list
        gamma_rate.append(most_frequent)

    #once we have the gamma_rate values, the epsilon_rate is the inverse:
    for i in gamma_rate:
        if i == "0":
            epsilon_rate.append("1")
        else:
            epsilon_rate.append("0")
    print('the gamma_rate is: ', gamma_rate)
    print('the epsilon_rate is: ', epsilon_rate)

if __name__ == "__main__":
    main()
