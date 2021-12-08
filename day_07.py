"""
https://adventofcode.com/2021/day/7
"""

import time

def parse_file(file_name):

    with open(file_name) as file:
        temp=file.readline()
        input_data=[]
        for no in temp.split(","):
            input_data.append(int(no))

    return input_data


def check_fuel_cons(targe_pos, input_data,constant_burn_rate=False):
    #move all the crabs in input_data to pos

    fuel=0

    

    for crab_pos in input_data:
        
        if constant_burn_rate:
            #part 1
            fuel+=abs(crab_pos-targe_pos)
        else:
            #part 2
            fuel+=sum(range(1,abs(crab_pos-targe_pos)+1))
    

    return fuel

def minimize_fuel_consumption(input_data,constant_burn_rate):

    fuel_connsumptions=[]

    input_data.sort()

    for i in range(min(input_data),max(input_data)+1):

        fuel_connsumptions.append(check_fuel_cons(i,input_data,constant_burn_rate))


    return min(fuel_connsumptions)







if __name__ == "__main__":

   
    name_of_file="day_07_data.txt"
    # name_of_file="day_07_data_test.txt"


    input_data=parse_file("data\\"+name_of_file)

    time_start=time.time()

    answer_part_1=minimize_fuel_consumption(input_data,constant_burn_rate=True)
    answer_part_2=minimize_fuel_consumption(input_data,constant_burn_rate=False)
 
 
   

    time_end=time.time()
    print("The answer to day 7")
    print("Part 1: {}".format(answer_part_1))
    print("Part 2: {}".format(answer_part_2))
    print("Runtime: {} sec".format(round(time_end-time_start,4)))  


 
