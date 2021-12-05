"""
https://adventofcode.com/2021/day/5
"""

import numpy as np

from day_03 import part_1



def parse_data(line):

    temp=line.split(" -> ")
    #coord=[x_1,y_1,x_2,y_2]
    coord=[]
    for item in temp:
        for no in item.split(","):
          coord.append(int(no))
    return coord

def find_coord_lines_part_1(line):
    """Takes in a line from part 1, and returns array with coordinates that the line covers"""
    
    #simplify, start with the lower coordinate
    x_1=min((line[0],line[2]))
    y_1=min((line[1],line[3]))
    x_2=max((line[0],line[2]))
    y_2=max((line[1],line[3]))

    coords_of_line=[]
    # [(node_1_x,node_1_y),.....]

    if x_1==x_2:
        # horisontal line
        for y in range(y_1,y_2+1):
            coords_of_line.append((x_1,y))
    elif y_1==y_2:
        for x in range(x_1,x_2+1):
            coords_of_line.append((x,y_1))
    else:
        print("something is wrong")
    
    return coords_of_line

def count_crossings(numpy_array):
    """loops over the numpy array and finds values that are >1"""

    return len(numpy_array[numpy_array>1])


if __name__ == "__main__":
    #get the input

    # [x1,y1,x2,y2]

    name_of_file="day_05_data.txt"
    # name_of_file="day_05_data_test.txt"

    with open("data\\"+name_of_file) as file:
        
        #input
        input_data_part_1=[]
        input_data_part_2=[]
        
        #have to decide the dimension of the matrix
        max_y=0
        max_x=0

        for line in file:
            
            temp=parse_data(line.strip())

            max_x=max([max_x,max(temp[0],temp[2])])
            max_y=max([max_y,max(temp[1],temp[3])])


            #only vertical or horisontal lines for part 1
            if temp[0]==temp[2] or temp[1]==temp[3]:
                input_data_part_1.append(temp)

            input_data_part_2.append(temp)

            part_1_matrix=np.zeros((max_x+1,max_y+1))


            #part 1
        for line in input_data_part_1:
   
            coords_of_line=find_coord_lines_part_1(line)

            for coord in coords_of_line:
                part_1_matrix[coord[1]][coord[0]]+=1

        answer_part_1=count_crossings(part_1_matrix)
    
    print("The answer to day 5")
    print("Part 1: {}".format(answer_part_1))
    # print("Part 2: {}".format(answer_part_2))



 


    