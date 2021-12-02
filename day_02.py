
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

directions_lib={"forward":[1,0],"down":[0,1],"up":[0,-1]}

pos_part_1=[0,0]

for instr in input_data:

    direction=instr[0]
    movement=int(instr[1])

    x_move=directions_lib[direction][0]
    y_move=directions_lib[direction][1]
    
    pos_part_1[0]+=x_move*movement
    pos_part_1[1]+=y_move*movement


#part 2

aim=0
pos_part_2=[0,0]

for instr in input_data:

    displ=int(instr[1])
    if instr[0]=="forward":
        x_move=displ
        y_move=aim*displ

        pos_part_2[0]+=x_move
        pos_part_2[1]+=y_move
    else:
        #only affected by "y"
        aim+=directions_lib[instr[0]][1]*displ


    


print("The answer to day 2")
print("Part 1: {}".format(pos_part_1[0]*pos_part_1[1]))
print("Part 2: {}".format(pos_part_2[0]*pos_part_2[1]))