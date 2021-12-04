"""
https://adventofcode.com/2021/day/4
"""

from dataclasses import dataclass
import numpy as np

@dataclass
class Bingo_no:
    no:int
    drawn:bool=False



class Bingo_card:
    #the dimension of the bingo card, 5x5
    bingo_dimension=5

    def __init__(self, bingo_matrix):
        #bingo matrix is a lists of lists with Bingo_numbers (see dataclass)
        self.bingo_matrix=bingo_matrix
        self.bingo_won=False
    
    def sum_of_rest_no(self):
        """sum of rest numbers """

        summ=0
        for line in self.bingo_matrix:
            for item in line:
                if item.drawn==False:
                    summ+=item.no
        return summ


    def check_bingo_no(self,no_drawn):
        """checks if the no is on the card and flips the "drawn" parameter to "True" """
        for line in self.bingo_matrix:
            for item in line:
                if item.no==no_drawn:
                    item.drawn=True
                    break
        if any([self.check_columns(),self.check_rows()]):
            return True
        else:
            return False

    def  check_rows(self):
        """check if there is a winning on any row"""
        i=0
        while i<Bingo_card.bingo_dimension:
            j=0
            counter=0
            while j<Bingo_card.bingo_dimension:
                if self.bingo_matrix[i][j].drawn==True:
                    counter+=1
                j+=1
            
            i+=1
            
            if counter==5:
                self.bingo_won=True
                return True
        return False
    
    def check_columns(self):
        """check if there is a winning on any row"""
        i=0
        while i<Bingo_card.bingo_dimension:
            j=0
            counter=0
            while j<Bingo_card.bingo_dimension:
                if self.bingo_matrix[j][i].drawn==True:
                    counter+=1
                j+=1
            
            i+=1
            
            if counter==5:
                self.bingo_won=True
                return True
        return False
    
    def __str__(self):
        
        string="\n"

        for line in self.bingo_matrix:
            
            for item in line:
                string+=" "+str(item.no)
            string+="\n"
            
            

        
        return string
    
    @classmethod
    def generate_bingo_card(cls, strings):
        """generates a Bingo card from lines of text (the input)"""

        bingo_card=[]

        for line in strings:
            temp=[]
            for no in line.split(" "):
                if no.strip()=="":
                    pass
                else:
                    temp.append(Bingo_no(int(no)))
            bingo_card.append(temp)
        return cls(bingo_card)

    @classmethod
    def generate_bingo_cards(cls,lines):
        "generates a list with bingo cards, takes in all the input"

        bingo_cards=[]

        i=0
        temp=[]

        while i<len(lines):

            if lines[i]=="":
                i=i+1
            else:
                temp.append(lines[i])
                if len(temp)==Bingo_card.bingo_dimension: #the  dimension of the bingo_card
                    bingo_cards.append(cls.generate_bingo_card(temp))
                    temp=[]


                i=i+1
        return bingo_cards



        

        

if __name__ == "__main__":
    
    # name_of_file="day_04_data_test.txt"
    name_of_file="day_04_data.txt"



    with open("data\\"+name_of_file) as file:
        input_data=[]
        for line in file:
            input_data.append(line.strip())

    no_drawn=input_data.pop(0).split(",")
    del input_data[0]

    #part 1
    bingo_cards_part_1=Bingo_card.generate_bingo_cards(input_data)

    card_found=False
    for no in no_drawn:
        if card_found:
            break
    
        for card in bingo_cards_part_1:
            card.check_bingo_no(int(no))
            if card.bingo_won:
                print("something happened")
                print(card)
                summ=card.sum_of_rest_no()
                card_found=True
                answer_part_1=summ*int(no)
                break
    #part 2
    bingo_cards_part_2=Bingo_card.generate_bingo_cards(input_data)

    i=0
    card_found=False  
    while len(bingo_cards_part_2)>1:
        for no in no_drawn:
            if card_found:
                break
            
            i=0
            while i<len(bingo_cards_part_2):
                card=bingo_cards_part_2[i]
                card.check_bingo_no(int(no))
                if card.bingo_won:
                    if len(bingo_cards_part_2)==1:
                        card_found=True
                        answer_part_2=card.sum_of_rest_no()*int(no)
                        break
                    
                    else:
                        bingo_cards_part_2.pop(i)
                else:
                    i=i+1




                




    print("The answer to day 4")
    print("Part 1: {}".format(answer_part_1))
    print("Part 2: {}".format(answer_part_2))



                







# test=["1 2 3 4 5","6 7 8 9 10","11 12 13 14 15 ","16 17 18 19 20 ","21 22 23 24 25 "]

# b=Bingo_card.generate_bingo_card(test)
# print(b)

# for i in range(1,6):
#     b.check_bingo_no(i)

# b.check_rows()
# print(b.bingo_won)

# test_array=range(21,26)

# for i in test_array:
#     print(b.check_bingo_no(i))

# print("b")


        

    
    