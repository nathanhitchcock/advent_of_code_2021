# puzzle from https://adventofcode.com/2021/day/2

#input the numbers from the dataset
#--------------------------------------------------------------
lst = open("input.dat").readlines()


count = 0
horizontal_position = 0
depth = 0
int_num = 0

def convert_direction(direction):
    num = ''.join([n for n in direction if n.isdigit()])
    int_num = int(num)
    return int_num


#for each directional value in the list, change the sub's position (either horizontally or it's depth (increase or decrease)
#--------------------------------------------------------------
for direction in lst:
    if 'forward' in str(direction):
        horizontal_position += convert_direction(direction)
        print(str(direction) + ' adds ' + str(convert_direction(direction)) + ' to your horizontal position, a total of ' + str(horizontal_position))
    elif 'down' in str(direction):
        depth += convert_direction(direction)
        print(str(direction) + ' adds ' + str(convert_direction(direction)) + ' to your depth, resulting in a value of  ' + str(depth))
    elif 'up' in str(direction):
        depth -= convert_direction(direction)
        print(str(direction) + ' decreases your depth by ' + str(convert_direction(direction)) + ', resulting in a value of  ' + str(depth))

print('the horizontal_position is ' + str(horizontal_position))
print('the depth is ' + str(depth))

# the solution to day 2 is horizontal_position * depth
#--------------------------------------------------------------
ans = horizontal_position * depth

print('the solution to day 2 is ' + str(ans))
