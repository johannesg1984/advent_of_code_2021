
"""
https://adventofcode.com/2021/day/3

Ekki mjög stoltur af þessu, en þetta virkar :)
"""
# from typing import Counter
import numpy as np
from collections import defaultdict
import copy



#part 1

def part_1(data_array):
    gammma_rate=""
    epsilon_rate=""

    for col in range(data_array.shape[1]):

        counter = defaultdict(int)

        column=(data_array[:, col])

        for item in column :
            counter[item]+=1
        
        if counter["1"]>counter["0"]:
            gammma_rate+="1"
            epsilon_rate+="0"
        elif counter["1"]<counter["0"]:
            gammma_rate+="0"
            epsilon_rate+="1"
        else:
            print("Can this happen?")

    answer_part_1=int(gammma_rate,2)*int(epsilon_rate,2)
    return  answer_part_1

#part 2



def part_2(data_array,rating):
    """rating is "o2" or "co2"
    """
    data_array_part_2=copy.deepcopy(data_array)

    run=True
    i=0
    while run:

        counter = defaultdict(int)

        column=(data_array_part_2[:, i])

        for item in column :
            counter[item]+=1
        
        
        if counter["1"]>=counter["0"] and rating=="o2":
            remove="0"
        elif rating=="o2":
            remove="1"
        elif counter["1"]>=counter["0"] and rating=="co2":
            remove="1"
        elif rating=="co2":
            remove="0"
      

        j=0

        while j<data_array_part_2.shape[0]:
            if data_array_part_2[j,i]==remove:
                data_array_part_2=np.delete(data_array_part_2,(j),axis=0)
            else:
                j+=1

            if data_array_part_2.shape[0]<=1:
                run=False
                break

        i+=1

    temp=data_array_part_2.tolist()
    
    string_temp=""
    string_temp=string_temp.join(temp[0])


    return int(string_temp,2)


if __name__ == "__main__":

    name_of_file="day_03_data.txt"
    # name_of_file="day_03_data_test.txt"

    with open("data\\"+name_of_file) as file:
        input_data=[]
        for line in file:
            temp=(line.strip())
            input_data.append(list(temp))

    data_array=np.array(input_data)


    answer_part_1=part_1(data_array)
    
    o2_rating=part_2(data_array,"o2")
    co2_rating=part_2(data_array,"co2")
    answer_part_2=o2_rating*co2_rating



print("The answer to day 3")
print("Part 1: {}".format(answer_part_1))
print("Part 2: {}".format(answer_part_2))





        