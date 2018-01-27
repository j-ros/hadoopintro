#!/usr/bin/python

# We receive data in the format id\t'Q'\tlength(body) for questions
# and parent_id\t'A'\tlength(body) for answers
#
# Have to compute mean length of answers for each question, data is sorted by id/parent_id (question id). Output will be
# id\t\tlength(question)\t avg length(answer)
#
# We will use a temp list to store answers for each question and compute avg when id changes.

import sys

def reducer():
    oldKey = None
    answer_length = []
    question_length = None

    for line in sys.stdin:
        data_mapped = line.strip().split('\t')
	if len(data_mapped) == 3:
		thisKey, thisTag, thisLen = data_mapped
	
		#Check if key changed and process oldKey saved answers
		if oldKey and oldKey != thisKey: 
		    #Find sum of answer length (0 if no answers)
		    if len(answer_length)>0:
			    sum_question_len = 0
			    for length in answer_length:
				sum_question_len += length
			    question_len = float(sum_question_len)/len(answer_length)
		    else:
			    question_len = 0
		    print oldKey, '\t', question_length, '\t', question_len
		    #reset temp variables
		    answer_length = []
		    question_length = None

		oldKey = thisKey

		#Process thisKey length
		if thisTag == 'Q':
			question_length = int(thisLen)
		elif thisTag == 'A':
			answer_length.append(int(thisLen))
		else:
			continue
		

    if oldKey != None: #last key
        	#Find sum of answer length (0 if no answers)
		if len(answer_length)>0:
		    sum_question_len = 0
		    for length in answer_length:
			sum_question_len += length
	                question_len = float(sum_question_len)/len(answer_length)
		else:
		    question_len = 0
		print oldKey, '\t', question_length, '\t', question_len

reducer()
        
