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
lst = open("input.dat").readlines()

arr = np.array(lst)

def find_gamma(arr,gamma_rate):
    #iterate through each column of the dataset
    for col in zip(*arr):
        #identify the mode (most common) character in the column
        most_frequent = st.mode(col)

        #add the mode to the gamma_rate list
        gamma_rate.append(most_frequent)

def find_epsilon(gamma_rate, epsilon_rate):
    #once we have the gamma_rate values, the epsilon_rate is the inverse:
    for i in gamma_rate:
        if i == "0":
            epsilon_rate.append("1")
        else:
            epsilon_rate.append("0")
    print('the gamma_rate is: ', gamma_rate)
    print('the epsilon_rate is: ', epsilon_rate)

def convert_to_decimal(gamma_rate, epsilon_rate):
    #convert the incomming list to a binary number
    gamma_binary = bin(int(''.join(map(str, gamma_rate)), 2) << 1)
    epsilon_binary = bin(int(''.join(map(str, epsilon_rate)), 2) << 1)

    #convert the binary number to a decimal
    #I don't know why I have to % by 2 here...
    gamma_decimal = (int(gamma_binary, 2)) / 2
    print('the gamma_decimal is: ', gamma_decimal)
    epsilon_decimal = (int(epsilon_binary, 2)) / 2
    print('the epsilon_decimal is: ', epsilon_decimal)

    power_consumption = gamma_decimal * epsilon_decimal
    print('the power consumption is: ', power_consumption)

def main():
    find_gamma(arr,gamma_rate)
    find_epsilon(gamma_rate, epsilon_rate)
    convert_to_decimal(gamma_rate, epsilon_rate)

if __name__ == "__main__":
    main()
