"""
https://adventofcode.com/2021/day/8
"""


def find_no_of_letter_matches(first_string,second_string):

    first_string_set=set(first_string)
    second_string_set=set(second_string)

    return len(set.intersection(first_string_set,second_string_set))

    

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
            known_values["1"]=(string,string_sorted)
        elif len(string)==4:
            known_values["4"]=(string,string_sorted)
        elif len(string)==3:
            known_values["7"]=(string,string_sorted)
        elif len(string)==7:
            known_values["8"]=(string,string_sorted)

    

    return known_values

def find_all_values(string_list):
    
    known_values=find_known_values(string_list)


    known_values_list=reverse_dictonary(known_values)
    known_values_list=list(known_values_list.keys())



    for string in string_list:


        string_sorted=sort_string(string)
        
        if string_sorted in known_values_list:
            pass
        else:

            if len(string_sorted)==5:

                if find_no_of_letter_matches(known_values["1"][1],string_sorted)==2:
                    known_values["3"]=(string,string_sorted)

                elif find_no_of_letter_matches(known_values["4"][1] ,string)==3:
                    known_values["5"]=(string,string_sorted)

                else:
                    known_values["2"]=(string,string_sorted)

            elif len(string_sorted)==6:

                if find_no_of_letter_matches(known_values["1"][1],string_sorted)==2 and find_no_of_letter_matches(known_values["4"][1],string_sorted)==4:
                    known_values["9"]=(string,string_sorted)
                
                elif find_no_of_letter_matches(known_values["8"][1],string_sorted)==6 and find_no_of_letter_matches(known_values["7"][1],string_sorted)==2:
                    known_values["6"]=(string,string_sorted)
                  
                else:
                    known_values["0"]=(string,string_sorted)
            else:
                print("something is wrong")


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


def decode(digit_output_values, catalog):

    new_catalog=reverse_dictonary(catalog)

    number_string=""
    for no in digit_output_values:
        number_string+=new_catalog[sort_string(no)]
    


    return int(number_string)


def reverse_dictonary(catalog):
    """returns only alphabet-ordered string and key(no)"""
    
    temp=catalog.items()

    new_catalog={}
    for item in temp:
        new_catalog[item[1][1]]=item[0]

    return new_catalog





def sum_encoded_no(signal_patterns, digit_output_values):

    assert len(digit_output_values)==len(signal_patterns), "something is wrong"
    
 
    i=0

    summ=0

    while i<len(digit_output_values):

        catalog = find_all_values(signal_patterns[i])

        summ+=decode(digit_output_values[i], catalog)


        i+=1

    return summ


if __name__ == "__main__":

    name_of_file="day_08_data.txt"
    # name_of_file="day_08_data_test_2.txt"

    [signal_patterns, digit_output_values]=parsing_data("data\\"+name_of_file)




    #part 1
    #{"no":no_of_segments}
    unique_segments={"1":2,
                    "4":4,
                    "7":3,
                    "8":7
                    }



    answer_part_1=counting_unique_values(digit_output_values,unique_segments)

    answer_part_2=sum_encoded_no(signal_patterns, digit_output_values)



    print("The answer to day 8")
    print("Part 1: {}".format(answer_part_1))
    print("Part 2: {}".format(answer_part_2))
    # print("Runtime: {} sec".format(round(time_end-time_start,4)))  