"""
https://adventofcode.com/2021/day/5
"""

import numpy as np
import time



def parse_data(line):

    temp=line.split(" -> ")
    #coord=[x_1,y_1,x_2,y_2]
    coord=[]
    for item in temp:
        for no in item.split(","):
          coord.append(int(no))
    return coord




def find_coord_lines(line):
    """Takes in a line from part 1, and returns array with coordinates that the line covers"""

    def generate_1d_line(point_1,point_2):
        """generate 1d line from to points, direction depended, used to generate diagonal lines"""
        if point_1<point_2:
            direction=1
        else:
            direction=-1
        
        iterate_no=point_1
        array_with_no=[]
        while True:
          

            array_with_no.append(iterate_no)
            
            if iterate_no==point_2:
                break
           
            iterate_no+=direction

        return array_with_no


    
    #simplify, start with the lower coordinate
    x_1=line[0]
    y_1=line[1]
    x_2=line[2]
    y_2=line[3]

    coords_of_line=[]
    # [(node_1_x,node_1_y),.....]

    if x_1==x_2:
        # horisontal line
        for y in generate_1d_line(y_1,y_2):
            coords_of_line.append((x_1,y))
    elif y_1==y_2:
        for x in generate_1d_line(x_1,x_2):
            coords_of_line.append((x,y_1))
    else:
        #diagonal

        x_vector=generate_1d_line(x_1,x_2)
        y_vector=generate_1d_line(y_1,y_2)

        assert len(x_vector)==len(y_vector),"x and y are not the same lengths"
        
        i=0
        while i<len(x_vector):
            coords_of_line.append((x_vector[i],y_vector[i]))
            i+=1


    
    return coords_of_line



def count_crossings(input_data,max_dim):

    geysir_matrix=np.zeros((max_dim+1,max_dim+1))
    for line in input_data:
   
            coords_of_line=find_coord_lines(line)

            for coord in coords_of_line:
                geysir_matrix[coord[1]][coord[0]]+=1

    return len(geysir_matrix[geysir_matrix>1])


if __name__ == "__main__":

    time_start=time.time()

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

        max_dim=max(max_x,max_y)

        #part 1
        answer_part_1=count_crossings(input_data_part_1,max_dim)
        answer_part_2=count_crossings(input_data_part_2,max_dim)

   


    time_end=time.time()
    print("The answer to day 5")
    print("Part 1: {}".format(answer_part_1))
    print("Part 2: {}".format(answer_part_2))
    print("Runtime: {} sec".format(round(time_end-time_start,4)))  



 


    