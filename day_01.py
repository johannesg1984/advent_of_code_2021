
#start 1. december


# name_of_file="day_01_data_test.txt"
name_of_file="day_01_data.txt"

with open("data\\"+name_of_file) as file:
    input_data=[]
    for line in file:
        input_data.append(int(line))

increase_counter=0

i=1
while i<len(input_data):
    if input_data[i]>input_data[i-1]:
        increase_counter+=1
    i=i+1



print("The answer to day 1")
print("Part 1: {}".format(increase_counter))
# print("Part 2: {}".format(part_2_answer)) 