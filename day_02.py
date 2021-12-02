
"""
https://adventofcode.com/2021/day/2
"""



# name_of_file="day_02_data_test.txt"
name_of_file="day_02_data.txt"

with open("data\\"+name_of_file) as file:
    input_data=[]
    for line in file:
        temp=line.strip().split(" ")
        # temp=[direction,movement]
        input_data.append(temp)

#part 1

directions={"forward":[1,0],"down":[0,1],"up":[0,-1]}

pos=[0,0]

for instr in input_data:

    direction=instr[0]
    movement=int(instr[1])

    x_move=directions[direction][0]
    y_move=directions[direction][1]
    
    pos[0]+=x_move*movement
    pos[1]+=y_move*movement



print("The answer to day 2")
print("Part 1: {}".format(pos[0]*pos[1]))
# print("Part 2: {}".format(increase_counter_part_2)) 