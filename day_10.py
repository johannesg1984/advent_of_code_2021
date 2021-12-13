"""
https://adventofcode.com/2021/day/10
"""

def  parse_file(file_name):

    b=5 

    data = []

    with open(file_name) as file:
        lines=file.readlines()

        for line in lines:
            data.append(list(line))

 
    return data

def get_score_part_1(data):
    
    score = 0
    for line in data:

      
        stack = []

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

        for character in line:
            if character in pairs:
                opening = stack.pop()
                if opening != pairs[character]:
                    # Line is corrupted.
                    score += scores[character]
                    break
            else:
                stack.append(character)


    return score



if __name__ == "__main__":
    name_of_file="day_10_data_test.txt"
    # name_of_file="day_10_data.txt"

    data=parse_file("data\\"+name_of_file)

    answer_part_1=get_score_part_1(data)

    print("The answer to day 10")
    print("Part 1: {}".format(answer_part_1))
