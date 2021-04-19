# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:49:18 2021

@author: Hrithik
"""
# Thesaurus app where thesaurus data imported from mysql server(credentials given below)
from difflib import get_close_matches
import mysql.connector

conn = mysql.connector.connect(
    host="108.167.140.122",
    database="ardit700_pm1database",
    user="ardit700_student",
    password="ardit700_student")

cursor = conn.cursor()
query = cursor.execute("select * from Dictionary")
result = cursor.fetchall()

word = input("Please enter word - ")
word = word.lower()
def matcher(word):
    
    def thesaurus(wrd):
        query1 = cursor.execute("select * from Dictionary where Expression='%s'"%wrd)
        result1 = cursor.fetchall()
        return result1 
    
    if word in dict(result).keys():
        return thesaurus(word)
    
    elif word.upper() in dict(result).keys():
        return thesaurus(word.upper())
    
    elif word.title() in dict(result).keys():
        return thesaurus(word.title())
    
    elif len((get_close_matches(word,dict(result).keys()))) > 0:
        
        print("Did you mean %s"%get_close_matches(word,dict(result).keys())[0])
        response = input("Type Y for Yes and N for No...")
        if response.upper() == "Y":
           return thesaurus(get_close_matches(word,dict(result).keys())[0])
        elif response.upper() == "N":
           return "Please enter a Valid Word."
        else:
           return "Invalid Response"
       
    else:
        return "This word does not exist please double-check the word..."
    
output = matcher(word)

if type(output) == list:
    for item in range(0,len(output)):
        print(output[item][1])
else:
    print(output)
        
        

