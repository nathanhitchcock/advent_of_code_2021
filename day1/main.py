# puzzle from https://adventofcode.com/2021/day/1

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
count = 0
for index, current_num in enumerate(lst[:-1]):
    next_num = lst[index + 1]
    if current_num < next_num:
        count += 1
        print(str(index) + ' ' + str(current_num) + ' ' + str(next_num) + ' ' + 'count ' +str(count))
    else:
        print(str(index) + ' ' + str(current_num) + ' ' + str(next_num))

print(count)
