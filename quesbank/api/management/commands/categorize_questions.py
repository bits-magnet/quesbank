# return Subjective or Objective string
# Inputs: Question html, solution html, Exercise Name
import string

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

    alpha = string.ascii_lowercase
    D = findOptions(ques, sol)
    if D['options'] != []:
        for x in D['options']:
            if x in sol:
                return 'Objective'

    return 'Subjective'

def getText(option, ques):
    ind = ques.find(option)
    newL = ques[ind:].find('<br')
    tab = ques[ind:].find('&nbsp')

    if tab == -1 and newL == -1:
        return ques[ind:]
    else:
        end = min(tab, newL)
        if end == -1:
            end = max(tab, newL)
        end += ind
        return ques[ind:end]

# Input: Question and Solution Html
def findOptions(ques, sol):
    ans = dict()
    ans['options'] = []

    alpha = string.ascii_lowercase

    for x in alpha:
        s = '(' + x + ')'
        if s in ques:
            opt = getText(s, ques)
            ans['options'].append(opt.strip())
        else:
            break
    return ans
