#input the numbers from the dataset
#--------------------------------------------------------------
lst = open("input.dat").readlines()


count = 0
horizontal_position = 0
depth = 0
int_num = 0
aim = 0

def convert_direction(direction):
    num = ''.join([n for n in direction if n.isdigit()])
    int_num = int(num)
    return int_num


#for each directional value in the list, change the sub's position (either horizontally or it's depth (increase or decrease)
#--------------------------------------------------------------
for direction in lst:
    if 'forward' in str(direction):
        horizontal_position += convert_direction(direction)
        depth += aim * convert_direction(direction)
        print(str(direction) + ' adds ' + str(convert_direction(direction)) + ' to your horizontal position, a total of ' + str(horizontal_position))
        print(' your depth is now ' + str(depth))
    elif 'down' in str(direction):
        aim += convert_direction(direction)
        print(str(direction) + ' adds ' + str(convert_direction(direction)) + ' to your aim, resulting in a value of  ' + str(aim))
    elif 'up' in str(direction):
        aim -= convert_direction(direction)
        print(str(direction) + ' decreases your aim by ' + str(convert_direction(direction)) + ', resulting in a value of  ' + str(aim))

print('the horizontal_position is ' + str(horizontal_position))
print('the depth is ' + str(depth))

# the solution to day 2 is horizontal_position * depth
#--------------------------------------------------------------
ans = horizontal_position * depth

print('the solution to day 2 is ' + str(ans))
