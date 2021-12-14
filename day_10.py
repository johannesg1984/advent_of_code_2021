"""
https://adventofcode.com/2021/day/10
"""

from statistics import median



def  parse_file(file_name):

    b=5 

    data = []

    with open(file_name) as file:
        lines=file.readlines()

        for line in lines:
            data.append(list(line.strip()))

 
    return data

def get_score_part_1(data):
    
    score_part_1 = 0
    scores_part_2 = []

    pairs = {")": "(",
                "]": "[",
                "}": "{",
                ">": "<"}

    scores = {")": 3, 
                "]": 57, 
                "}": 1197,
                ">": 25137,
                "(": 1,
                "[": 2, 
                "{": 3, 
                "<": 4}

    for line in data:

        
        line_corrupted=False
      
        stack = []
        autocomplete_score = 0

      

        for character in line:
            
            if character in pairs:
                opening = stack.pop()
                if opening != pairs[character]:
                    # Line is corrupted.
                    score_part_1 += scores[character]
                    line_corrupted=True
                    break
            else:
                stack.append(character)

        if line_corrupted==False:

            while stack:
                autocomplete_score = autocomplete_score * 5 + scores[stack.pop()]

            scores_part_2.append(autocomplete_score)
    
    
    score_part_2 = median(scores_part_2)


    return (score_part_1,score_part_2)



if __name__ == "__main__":
    # name_of_file="day_10_data_test.txt"
    name_of_file="day_10_data.txt"

    data=parse_file("data\\"+name_of_file)

    answer_part_1,answer_part_2=get_score_part_1(data)

    print("The answer to day 10")
    print("Part 1: {}".format(answer_part_1))
    print("Part 2: {}".format(answer_part_2))