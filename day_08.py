"""
https://adventofcode.com/2021/day/8
"""


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

    name_of_file="day_08_data.txt"
    # name_of_file="day_08_data_test_2.txt"

    [signal_patterns, digit_output_values]=parsing_data("data\\"+name_of_file)


    decoder={
       "abcefg":0,
       "cf": 1,
       "acdeg":2,
       "acdfg":3,
       "bcdf":4,
       "abdfg":5,
       "abdefg":6,
       "acf":7,
       "abcdef":8,
       "abcdfg":9
       }

    #part 1
    #{"no":no_of_segments}
    unique_segments={"1":2,
                    "4":4,
                    "7":3,
                    "8":7
                    }



    answer_part_1=counting_unique_values(digit_output_values,unique_segments)


    print("The answer to day 8")
    print("Part 1: {}".format(answer_part_1))
    # print("Part 2: {}".format(answer_part_2))
    # print("Runtime: {} sec".format(round(time_end-time_start,4)))  