# To be used only with subjective questions
# function_name: find_length
# input: solutionHtml
# return value: string code for solution length (VSA, SA, LA)
# VSA-> Very Short Answer
# SA -> Short Answer
# LA -> Long Answer


#####################################
#                                   #
# If the length of the solution is  #
# -> less than 100 words, its VSA.  #
# -> between 100-300, its SA.       #
# -> above 300, its LA              #
#                                   #
#####################################

def find_length(sol):
    ind = sol.find('<br')
    if ind != -1:
        sol = sol[:ind]
    if len(sol) < 100:
        return 'VSA'
    elif len(sol) > 300:
        return 'LA'
    return 'SA'
