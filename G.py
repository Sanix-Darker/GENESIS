####################################
# => G E N E S I S <=              #
# By S4n1x D4rk3r                  #
# https://github.com/Sanix-Darker  #
# PYTHON-CAMEROUN                  #
####################################

import itertools
from collections import Counter
from datetime import datetime
import os.path


print ("\n  ---------------------------------------")
print ("  |    ---> G E N E S I S v 1.0.0 <---  |")
print ("  ---------------------------------------")
print ("  |    By S4n1x D4rk3r                  |")
print ("  |    https://github.com/Sanix-Darker  |")
print ("  =======================================\n")
print (">Description: Follow instructions to generate passwords from key Word of your target!\n")

keywords = input("Keywords about victim (Split with ','): ")
# keywords="hello,nous"
words=keywords.split(",")
length_words = len(words)

if(length_words<=0 or len(keywords.strip())<=0):
    print("\n\tSorry, you have to enter at least one word. GOODBYE!\n")
    exit()

length_numbers=0
numbers_entered = input("Numbers about victim (Split with ','): ")
numbers=numbers_entered.split(",")
length_numbers=len(numbers)

length_pointings=0
rule_pointings = input("Words contain these punctuations (Split with blank. Ex: '. , _'): ")
pointings=rule_pointings.split(" ")
length_pointings=len(pointings)

 
character_limit=None
try:
    character_limit=int(input("How many letters do words contain maximum? (Ex: 12): "))
except ValueError:
    print("\n\tYou have to enter a number. Please, again!\n")
    try:
        character_limit=int(input("How many letters do words contain maximum? (Ex: 12): "))
    except ValueError:
        print("\n\tGoodbye!")
        exit()

#Words lists for informatin about how many words contain
words_lists=[]
words_lists_with_number=[]
complex_words=[]
complex_words_removed=[]
#End of the algorithm, all words is going to be in one list.
all_words=[]

#This list keep how many keywords do in generated words...
for counter in range(0,length_words):
    words_lists.append([])

#We keep these lists separately because generating complex words more successfully
#This list keep words with numbers
for counter in range(0,length_words):
    words_lists_with_number.append([])

#Informations
print("\n\tWord(s):{}\n\tPunctuation(s):{}\n\tNumber(s):{}\n".format(length_words,length_pointings or None,length_numbers or None))

def generate_word(words, min, max):

    for i in range(int(min), int(max)+1):
        for j in itertools.product(words, repeat=i):
            #create a list and add items to this list
            #count same words in list, if a word repeats more 2 times, delete. I guess anybody don't repeat a word more 2 times.
            counter_for_join_word=len(j)
            #print(counter_for_join_word)
            counter_list = Counter(j)
            #print(counter_list)
            for element in j:
                if (counter_list[element]<3):
                    #Add all generated words to words_list for knowing how many keywords do genrated words contain
                    if not ''.join(j) in words_lists[counter_for_join_word-1]:
                        words_lists[counter_for_join_word-1].append(''.join(j))
                        #Check words contains numbers?
                        add_numbers(''.join(j),counter_for_join_word-1) if length_numbers>0 else False

                    #add pointings to one word
                    if(length_pointings>0 and len(j)==1):
                        for mark in pointings:
                            #add to end
                            if not j[0]+mark in words_lists[0]:
                                words_lists[0].append(j[0]+mark)
                                #Check words contains numbers?
                                add_numbers(j[0]+mark,0) if length_numbers>0 else False
                            #add to head
                            if not mark+j[0] in words_lists[0]:
                                words_lists[0].append(mark+j[0])
                                #Check words contains numbers?
                                add_numbers(mark+j[0],0) if length_numbers>0 else False


                    if(length_pointings > 0 and len(j) > 1):
                        for mark in pointings:
                            if not mark.join(j) in words_lists[counter_for_join_word-1]:
                                words_lists[counter_for_join_word-1].append(mark.join(j))
                                #yield mark.join(j)
                                add_numbers(mark.join(j),counter_for_join_word-1) if length_numbers>0 else False
    all_words.append(words_lists)

#howmanywords for same cause
def add_numbers(word_for_add, howmanywords):
    #print(word_for_add,howmanywords)
    for number in numbers:
        #add to end
        if not number+word_for_add in words_lists[howmanywords]:
            words_lists_with_number[howmanywords].append(number+word_for_add)
            #print(number+word_for_add)
        #add to head
        if not word_for_add+number in words_lists[howmanywords]:
            words_lists_with_number[howmanywords].append(word_for_add+number)
            #print(word_for_add+number)
    all_words.append(words_lists_with_number)

#this function generate keywords more complex but can't best complex.
def generate_complex():
    for words_list in words_lists:
        for word in words_list:
            for words_list_with_number in words_lists_with_number:
                for word_with_number in words_list_with_number:
                    complex_words.append(word+word_with_number)

    for complex_word in complex_words:
        for word_to_count in words:
            if(complex_word.count(word_to_count)>1):
                #print(word_to_count, complex_word, complex_word.count(word_to_count))
                complex_words_removed.append(complex_word)

    complex_words_finally=list(set(complex_words).difference(complex_words_removed))
    #print(complex_words_finally)
    #Add complex list to all words list
    all_words.append(complex_words_finally)

generate_word(words, 1, length_words)
generate_complex()

#Program is going to create a file every running,
#Algorithm contains reqursive function so we need this control
file_existed_checked=0

#Assign filename variable because function can get this value
#Another way -> write_words_from_list(item,last_filename)
filename=None

#Words counter
word_counter=0

#Prevent to duplicate words
added_words=[]
def write_words_from_list(all_words_list):
    global file_existed_checked
    global filename
    global word_counter
    global character_limit
    global added_words

    if(file_existed_checked==0):
        filename="password_list-{}.txt".format(datetime.now().strftime('%H-%M'))
        filename=file_existed(filename)
        file_existed_checked=1

    password_list_file=open(filename,mode='a')

    for item in all_words_list:
        if(type(item)==list):
            write_words_from_list(item)
        elif(type(item)==str):
            if(character_limit is not None):
                if(len(item)<=character_limit):
                    if(item not in added_words):
                        password_list_file.write("{}\n".format(item))
                        added_words.append(item)
                        word_counter+=1
            else:
                if(item not in added_words):
                    password_list_file.write("{}\n".format(item))
                    added_words.append(item)
                    word_counter+=1
        else:
            print("Unkown type: ",item)

    password_list_file.close()
    #print(added_words)

def file_existed(filename_for_check,counter=0):
    global filename
    if(os.path.isfile(filename_for_check)):
        new_counter=counter+1
        new_filename="password_list-{}({}).txt".format(datetime.now().strftime('%H-%M'),new_counter)
        return file_existed(new_filename,new_counter)
    else:
        #print(filename_for_check)
        filename=filename_for_check
        return filename

write_words_from_list(all_words)
print("\t{} words were generated. You can see these words at {}\n".format(word_counter,filename))