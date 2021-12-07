"""
https://adventofcode.com/2021/day/6
"""
import time as t

#recursion
def lanterfish_spawn_part_1(time,fish_timer):

    if time==run_time:
        return 1

    else:

        while fish_timer>=0:
        
            if time==run_time:
                return 1
        
            fish_timer-=1
            time+=1
        

        #just kill of the fish and assume that it spawns two new ones
        return lanterfish_spawn_part_1(time,spawn_time_new_fish-1)+lanterfish_spawn_part_1(time,spawn_time_old_fish-1)

def parse_data(inital_fishes):

    fish_counted=[0]*9

    for fish in inital_fishes:
        fish_counted[fish]+=1

    return fish_counted

def lantern_fish_spawn_2(initial_fishes,run_time):

    timer=0

    fishes=parse_data(initial_fishes)
    
    
    fishes_temp=[0]*9

    while timer<run_time:
        fishes_temp=[0]*9
        timer+=1

        #new fishes that will use more time to make baby-fishes
        fishes_temp[8]=fishes[0]
        #old fishes that can spawn faster
        fishes_temp[6]=fishes[0]

        #now move fishes around
        for i in range(1,len(fishes)):
            fishes_temp[i-1]+=fishes[i]

        fishes=fishes_temp
        
        summing=sum(fishes)
        print("")



    return sum(fishes)






if __name__ == "__main__":

    name_of_file="day_06_data.txt"
    # name_of_file="day_06_data_test.txt"

    #muna að spyrja Palla og Sigga um þetta
    with open("data\\"+name_of_file) as file:
        temp=file.readline()
        input_data=[]
        for no in temp.split(","):
            input_data.append(int(no))

    #all units are in days
    spawn_time_new_fish=7
    spawn_time_old_fish=9
    time=0 


    #part 1
    run_time=80
    fish_counter_part_1=0

    time_start=t.time()
    for fish in input_data:
        counter=0
        fish_counter_part_1+=lanterfish_spawn_part_1(counter,fish)

    
    #part 2 with the new function 
    run_time_part_2=256

    answer_part_2=lantern_fish_spawn_2(input_data,run_time_part_2)
    



    time_end=t.time()
    print("The answer to day 6")
    print("Part 1: {}".format(fish_counter_part_1))
    print("Part 2: {}".format(answer_part_2))
    print("Runtime: {} sec".format(round(time_end-time_start,4)))  
    
    





