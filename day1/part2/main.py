# puzzle from https://adventofcode.com/2021/day/1

#input the numbers from the dataset
#--------------------------------------------------------------
lst = open("input.dat").readlines()


#for each sliding_window value in the list((i+1)+(i+2)+(i+3)), compare it to the next_sliding_window ((i)+(i+1)+(i+2))
#--------------------------------------------------------------
count = 0
for index, current_num in enumerate(lst[:-1]):
    if (index+3 < len(lst) and index >= 0):
        next_num = int(lst[index + 1])
        sliding_window = int(lst[index]) + int(lst[index + 1]) + int(lst[index + 2])
        next_sliding_window = int(lst[index + 1]) + int(lst[index + 2]) + int(lst[index + 3])

        if sliding_window < next_sliding_window:
            count += 1
            print(str(index) + ' ' + str(sliding_window) + ' ' + str(next_sliding_window) + ' ' + 'count ' +str(count))
        else:
            print(str(index) + ' ' + str(sliding_window) + ' ' + str(next_sliding_window))

print('the count of increasing sliding windows is ' + str(count))
