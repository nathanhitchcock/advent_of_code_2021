# puzzle from https://adventofcode.com/2021/day/1

count = 0

'''
#input the numbers from the dataset
--------------------------------------------------------------
'''
file = open("input.dat")
lst=[]

#Extract all integers from the file into a list
def extract_to_list(file, lst):
    for line in file:
        lst.append(line.strip())
    return(lst)

extract_to_list(file,lst)


'''
for each value in the list(index), compare it to the next value (index + 1)
--------------------------------------------------------------
'''
for index, elem in enumerate(lst):
    # checking to make sure we don't go out of bounds
    if (index - 1 >= 0):
        # defining the positional elements
        prev_el = str(lst[index-1])
        curr_el = str(elem)

        # performing the check to see if the next element is larger than the current element
        if prev_el < curr_el:
            print ('the previous value ' + prev_el + ' is smaller than the next value ' + curr_el + ' yay!!')
            count += 1
            print('count UPDATE: ' + str(count))

        else:
            print ('the previous value ' + prev_el + ' is NOT smaller than the next value ' + curr_el + ' BOO!!')
            print('the count is STILL ' + str(count))
            continue


'''
print the output
--------------------------------------------------------------
'''
print("count of integers larger than the previous integers: " + str(count))
