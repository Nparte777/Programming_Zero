#!/bin/python3

#importing
print("Importing")

import sys 	#system functions
from datetime import datetime
print(datetime.now())

from datetime import datetime as dt #importing as alias
print(dt.now())

#Advanced Strings
print("\nAdvanced strings:")
my_name = "Nikhil"
print(my_name[0]) #first initial
print(my_name[-1]) #last letter

sentence = "This is a sentence."

print(sentence[:4])  #first word
print(sentence[-9:-1]) #last word

#print(sentence.split()) #split sentence with delimiter
sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print("\n".join(sentence_split))

print(sentence_join)
