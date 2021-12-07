"""
https://adventofcode.com/2021/day/7
"""

if __name__ == "__main__":

    # name_of_file="day_07_data.txt"
    name_of_file="day_07_data_test.txt"
   
    # with open("data\\"+name_of_file) as file:
   
    with open("data\\"+name_of_file,encoding = "utf-16") as file:
        temp=file.readline()
        input_data=[]
        for no in temp.split(","):
            input_data.append(int(no))