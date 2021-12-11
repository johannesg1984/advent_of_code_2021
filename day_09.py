"""
https://adventofcode.com/2021/day/9
"""

import numpy as np

def parse_file(file_name):


    data=[]

    with open(file_name) as file:
        lines=file.readlines()

        for line in lines:
            output_list = [int(no) for no in list(line.strip())]
            data.append(output_list)

        np_data=np.array(data)
            
    return np_data

def generate_adjacents(x,y,matrix_dim,relative=True):

    adjacents=[[-1,0],[1,0],[0,-1],[0,1]]

    if x==0:
        adjacents.remove([-1,0])
    if x==matrix_dim[1]-1:
        adjacents.remove([1,0])
    
    if y==0:
        adjacents.remove([0,-1])
    if y==matrix_dim[0]-1:
        adjacents.remove([0,1])

    
    if relative:
        return adjacents
    else:
        i=0
        while i<len(adjacents):
            adjacents[i]=[adjacents[i][0]+x,adjacents[i][1]+y]
            i+=1
        return adjacents
        
        




def find_low_points(file_name):

    data=parse_file(file_name)

    low_points=[] #(x,y,h)
    [m_dim_y,m_dim_x]=data.shape

    m_dim=[m_dim_y,m_dim_x]

    for y in range(m_dim_y):
        for x in range(m_dim_x):

            adjacents=generate_adjacents(x,y,m_dim)
            heights=[]
            for adj in adjacents:
                heights.append(data[y+adj[1]][x+adj[0]])
            
            if data[y][x]<min(heights):
                low_points.append((x,y,data[y][x]))

    return low_points


def calc_risk_levels(file_name):
    low_points=find_low_points(file_name)

    #low_point=[x,y,h]
    risk_level=0
    for point in low_points:
        risk_level+=point[-1]+1

    return risk_level

def calc_basin_sizes(file_name):
    
    data=parse_file(file_name)
    low_points=find_low_points(file_name)

    basins_areas=[]

    for point in low_points:
        x=point[0]
        y=point[1]

        basins_areas.append(calc_basin_size(data,[x,y]))
        

    return basins_areas



def calc_basin_size(data,start_point):
    queue=[start_point]
    visited_points=set()

    [m_dim_y,m_dim_x]=data.shape
    m_dim=[m_dim_y,m_dim_x]

    while len(queue)>0:
        temp_queue=[]
        for point in queue:
            visited_points.add(tuple(point))

            adjacents=generate_adjacents(point[0],point[1],m_dim,relative=False)

            for adj in adjacents:
                if data[adj[1]][adj[0]]!=9 and tuple(adj) not in visited_points:
                    temp_queue.append(adj)
            
        queue=temp_queue
        
    return len(visited_points)








if __name__ == "__main__":

    # name_of_file="day_09_data_test.txt"
    name_of_file="day_09_data.txt"

    answer_part_1=calc_risk_levels("data\\"+name_of_file)

    basin_areas=calc_basin_sizes("data\\"+name_of_file)

    basin_areas.sort()

    answer_part_2=basin_areas[-1]*basin_areas[-2]*basin_areas[-3]

    print("The answer to day 9")
    print("Part 1: {}".format(answer_part_1))
    print("Part 2: {}".format(answer_part_2))
