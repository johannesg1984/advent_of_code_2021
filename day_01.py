
"""
https://adventofcode.com/2021/day/1
"""



# name_of_file="day_01_data_test.txt"
name_of_file="day_01_data.txt"

with open("data\\"+name_of_file) as file:
    input_data=[]
    for line in file:
        input_data.append(int(line))

#part 1
increase_counter_part_1=0

i=1
while i<len(input_data):
    if input_data[i]>input_data[i-1]:
        increase_counter_part_1+=1
    i=i+1

#part 2
i=1
sums=[]
while i<len(input_data)-1:
    sums.append(input_data[i-1]+input_data[i]+input_data[i+1])
    i+=1


increase_counter_part_2=0
for i in range(1,len(sums)):
    if sums[i]>sums[i-1]:
        increase_counter_part_2+=1




print("The answer to day 1")
print("Part 1: {}".format(increase_counter_part_1))
print("Part 2: {}".format(increase_counter_part_2)) 