# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:49:18 2021

@author: Hrithik
"""

from difflib import get_close_matches 
#Loading Json file containing thesaurus data
import json
data = json.load(open(r"data.json"))

#Creating a function that matches input word with the one in json file

def matcher(word):
    word = word.lower()
    if word in data:
        return data[word]
    
    elif word.title() in data:
        return data[word.title()]
    
    elif word.upper() in data:
        return data[word.upper()]
    
    elif len( get_close_matches(word,data.keys())) > 0:  #get_close_matches function returns a list of possibilities of best possible matches from the keys given in 'data' json file.
        print( "Did you mean %s ?" %get_close_matches(word,data.keys())[0])
        response=input("Type Y for yes and N for No : ")
        if response == "Y":
            return matcher(get_close_matches(word,data.keys())[0])
        elif response == "N":
            return "please enter a valid word."
        else:
            return "Invalid Response. Please run the program again."
        
    else:
        return "This word does not exist. Please double-check it."

word = input("Please enter a word : ")     
output = matcher(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)