#!/usr/bin/python

"""
Script to generate a list of maximum of 96 distinct sequences with no more than three consecutive bases matches.
--Written by G V Saripella
"""

from sklearn.utils import shuffle

#############
# Function to convert a list of string
def toStr(L):
	return ''.join(L)

# Store the permutations into a list
permlst=[]
# Main function for all permutations for a given string
def allrec(string, data, last, index):
	length = len(string)
	for i in range(length):
		# recursively call for higher
		data[index] = string[i]
		if(index==last):
			permlst.append(toStr(data))
		else:
			allrec(string, data, last, index+1)

# sub function to call main function to print all permutations
def alllex(string):
	length = len(string)
	data = [""] * (length+1)
	string = sorted(string)
	# all permutaions
	allrec(string, data, length-1, 0)

#############

#############
# Function for a sliding window
def window(fseq, window_size):
	b = [fseq[i:i+window_size] for i in range(len(fseq)-(window_size-1))]
	return(b)

# Function to form pairs of combinations
def combinations(ss):
    for i, v in enumerate(ss):
        for j in range(i+1, len(ss)):
            yield [v, ss[j]]

# Function to find pattern in a string
def findpat(pattern, text):
	import re
	for pat in pattern:
		if re.search(pat,text):
			#print('found a match!')
			break
		else:
			#print('no match')
			True
			return(text)

#########
# function to get unique values
def unique(list1):
	unique_list = []
	for x in list1:
		if x not in unique_list:
			unique_list.append(x)
	return unique_list


# function to generate distance Matrix
def Distance_Matrix(Target):
	###
	import pandas as pd
	from Levenshtein import distance
	import numpy as np
	###
	List1 = Target
	List2 = Target
	Matrix = np.zeros((len(List1),len(List2)),dtype=np.int)
	for i in range(0,len(List1)):
		for j in range(0,len(List2)):
			Matrix[i,j] = distance(List1[i],List2[j])
	return Matrix

# call functions to check 3 words match
def compall3strings(list_strings):
	cbn=0; lstout=[];lstoutnone=[];lstall=[];
	for comb in list(combinations(list_strings)):
		lst=[];
		for seq in window(comb[0], 3):
			lst.append(seq)
			fp = findpat(lst,comb[1])
			#print(lst,comb,fp)
			if fp == None:
				#if fp not in lstoutnone:
				lstoutnone.append(comb[1])
			else:
				#if fp not in lstout:
				lstout.append(comb[0])
				lstout.append(comb[1])
		cbn+=1

		########
	#print("total combinations pairs: "+ str(cbn))
	lstout_uniq = unique(lstout)
	lstoutnone_uniq = unique(lstoutnone)

	for i in lstout_uniq:
		if i not in lstoutnone_uniq:
			lstall.append(i)
	return lstall


#########
#generate permutations if the string is less than 4 bases
#########
finallistall =[]
DNA_string = input("Type your own DNA sequence here; or press enter for default sequence: ")

# function to generate less than 4 character
def ls4char(DNA_string):
	###
	allperm = alllex(DNA_string)
	finallistall = compall3strings(permlst)
	outstr1 = finallistall
	outstr2 = Distance_Matrix(finallistall)
	return outstr1, outstr2

def grt6char(DNA_string):
	###
	templist = [];x_shuff = []
	windsplit6 = window(DNA_string, 6)
	templist = compall3strings(windsplit6)
	for ii in range(len(templist)):
		if len(x_shuff) < 96:
			for ii in templist:
				if ii not in x_shuff:
					x_shuff.append("".join(shuffle(ii)))
		elif len(x_shuff) >= 96:
			break
	#print(len(x_shuff[0:96]))
	outstr1 = x_shuff[0:96]
	outstr2 = Distance_Matrix(x_shuff[0:96])
	return outstr1, outstr2

if len(DNA_string) == 0:
	#DNA_string = "atgc"
	DNA_string = "cccgacaagccaggtgctagcgcatttcatttcacgagcagctacctctcaggggagcccaggccaattctcatctcagcctcccacttaggcgtaccta"
	#DNA_string = "cattaccaacccgcgaccaatagccacgttaggagggaaccgtcataaaaaccgcatctcgtcaacgattctcggatttgcgaaccgcatagcaacctcgatatgtagcaattctgttataactattggtcgggctataaagcgtatttaaaacgacagcaacgcagagggtttcacatagttgtataatctttccacat"
	if len(DNA_string) <= 5:
		print("total list of words: "+ str(",".join(ls4char(DNA_string)[0])))
		print("word length: "+ str(len(ls4char(DNA_string)[0])))
		print("Distance_Matrix: "+ str(ls4char(DNA_string)[1]))
	else:
		print("total list of words: "+ str(",".join(grt6char(DNA_string)[0])))
		print("word length: "+ str(len(grt6char(DNA_string)[0])))
		print("Distance_Matrix: "+ str(grt6char(DNA_string)[1]))

elif len(DNA_string) != 0:
	if len(DNA_string) <= 5:
		print("total list of words: "+ str(",".join(ls4char(DNA_string)[0])))
		print("word length: "+ str(len(ls4char(DNA_string)[0])))
		print("Distance_Matrix: "+ str(ls4char(DNA_string)[1]))
	else:
		print("total list of words: "+ str(",".join(grt6char(DNA_string)[0])))
		print("word length: "+ str(len(grt6char(DNA_string)[0])))
		print("Distance_Matrix: "+ str(grt6char(DNA_string)[1]))

########
