# function_name: categorize
# Inputs: Question html, solution html, Exercise Name
# return value: 'Subjective' or 'Objective' string
#               Fill in the Blanks and Tru/False questions are considered Subjective

#####################################################################
#   Approach:-                                                      #
#                                                                   #
#   1. Search if exercise Name has 'objective' substring            #
#   2. Search for various substrings that are often part of         #
#      objective questions such as 'choose the correct answer'      #
#                                                                   #
#   3. If the above fail to catch the objective question,           #
#      the question html and solution html is then calls            #
#      the find_options function and if options are found,          #
#      it is judged as an objective question                        #
#                                                                   #
#   4. If all the above fail, its assumed that its a subjective     #
#      question.                                                    #
#                                                                   #
#####################################################################

from .find_options import find_options

def categorize(ques, sol, exName):
    ques = ques.lower()
    exName = exName.lower()
    if 'objective' in exName \
    or 'against the correct answer' in ques \
    or 'mark the correct alternative' in ques \
    or 'choose the correct option' in ques \
    or 'select the correct option' in ques \
    or 'the correct answer is option' in sol:
        return 'Objective'

    D = find_options(ques, sol)
    if D['options'] != []:
        return 'Objective'

    return 'Subjective'