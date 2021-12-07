"""
https://adventofcode.com/2021/day/6
"""
import time as t

#recursion
def lanterfish_spawn(time,fish_timer):

    if time==run_time:
        return 1

    else:

        while fish_timer>=0:
        
            if time==run_time:
                return 1
        
            fish_timer-=1
            time+=1
        

        #just kill of the fish and assume that it spawns two new ones
        return lanterfish_spawn(time,spawn_time_new_fish-1)+lanterfish_spawn(time,spawn_time_old_fish-1)
        



if __name__ == "__main__":

    name_of_file="day_06_data.txt"
    # name_of_file="day_06_data_test.txt"

    #muna að spyrja Palla og Sigga um þetta
    with open("data\\"+name_of_file) as file:
    # with open("data\\"+name_of_file,encoding = "utf-16") as file:
        temp=file.readline()
        input_data=[]
        for no in temp.split(","):
            input_data.append(int(no))

    #all units are in days
    spawn_time_new_fish=7
    spawn_time_old_fish=9
    time=0 

    run_time=80
    fish_counter_part_1=0

    time_start=t.time()
    for fish in input_data:
        counter=0
        fish_counter_part_1+=lanterfish_spawn(counter,fish)

    #does not work
    # run_time=256 
    # fish_counter_part_2=0
    # for fish in input_data:
    #     counter=0
    #     print(fish)
    #     fish_counter_part_1+=lanterfish_spawn(counter,fish)

    time_end=t.time()
    print("The answer to day 5")
    print("Part 1: {}".format(fish_counter_part_1))
    # print("Part 2: {}".format(answer_part_2))
    print("Runtime: {} sec".format(round(time_end-time_start,4)))  
    
    





