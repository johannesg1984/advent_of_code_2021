"""
https://adventofcode.com/2021/day/8
"""

def sort_string(string):
    """puts the charachters in the right order alphabetically"""

    string_sorted=sorted(string)
    return "".join(string_sorted)

def find_known_values(string_list):
    """find the known values based on unique lengths"""

    known_values={}
    for string in string_list:
        string_sorted=sort_string(string)
        if len(string)==2:
            known_values["1"]=string_sorted
        elif len(string)==4:
            known_values["4"]=string_sorted
        elif len(string)==3:
            known_values["7"]=string_sorted
        elif len(string)==7:
            known_values["8"]=string_sorted

    

    return known_values

def find_all_values(string_list):
    
    known_values=find_known_values(string_list)

    for string in string_list:
        string_sorted=sort_string(string)

        if len(string_sorted)==5:

            if known_values["1"] in string_sorted:
                known_values["3"]=string_sorted

            elif known_values["4"] in string_sorted:
                known_values["5"]=string_sorted

            else:
                known_values["2"]=string_sorted

        if len(string_sorted)==6:

            if known_values["1"] in string_sorted:
                known_values["9"]=string_sorted
            elif string_sorted in known_values["8"]:
                known_values["0"]=string_sorted
            else:
                known_values["6"]=string_sorted


    return known_values


        



def parsing_data(file_name):

    with open(file_name) as file:
        
        signal_patterns=[]
        digit_output_values=[]


        for line in file:
            [temp_signal,temp_digit]=line.strip().split(" | ")
            signal_patterns.append(temp_signal.split(" "))
            digit_output_values.append(temp_digit.split(" "))

    return [signal_patterns,digit_output_values]

def counting_unique_values(digit_output_values,list_of_string_lengths):
    #part 1
    
    unique_segments=list(list_of_string_lengths.values())
    counter=0
    for value in digit_output_values:
        for no in value:
            if len(no) in unique_segments:
                counter+=1
    
    return counter
    


if __name__ == "__main__":

    # name_of_file="day_08_data.txt"
    name_of_file="day_08_data_test_1.txt"

    [signal_patterns, digit_output_values]=parsing_data("data\\"+name_of_file)




    #part 1
    #{"no":no_of_segments}
    unique_segments={"1":2,
                    "4":4,
                    "7":3,
                    "8":7
                    }



    answer_part_1=counting_unique_values(digit_output_values,unique_segments)

    b=find_all_values(signal_patterns[0])


    print("The answer to day 8")
    print("Part 1: {}".format(answer_part_1))
    # print("Part 2: {}".format(answer_part_2))
    # print("Runtime: {} sec".format(round(time_end-time_start,4)))  