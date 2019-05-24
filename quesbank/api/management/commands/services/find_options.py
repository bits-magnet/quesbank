# To be used only with objective questions
# function_name: find_options
# input: Question and Solution HTML
# return value: dictionary with two keys, 'options' and 'correct'
#                'options' is mapped to a list with all options with its text
#                'correct' is mapped to just option number, e.g. (a), (b), etc.


###########################################################################
# Approach :-                                                               #
#                                                                           #
# 1. Traverse alphabetically to find optiosn (a), (b), (c), etc.            #
# 2. If option found, get_text() gets the text in option.                   #
#    If not found, loop breaks assuming options are there                   #
#       only till that character                                            #
# 3. get_text() catches text by finding the first tab or first              #
#    newline in the html.                                                   #
#                                                                           #
# 4. To find the correct option, multiple approaches are used,              #
#    to compensate for multiple formats of different books                  #
#   4.1 If 'the correct answer is option' string is found in solution,      #
#       the option number following this line is assumed correct.           #
#   4.2 If the option number with parenthesis(e.g 'a'), is present          #
#       in solution, that option is assumed correct.                        #
#   4.3 If the entire html text for any of the options is found in the      #
#       solution, that option is considered correct.                        #
#                                                                           #
#############################################################################


import string
def get_text(option, ques):
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

def find_options(ques, sol):
    ans = dict()
    ans['options'] = []
    ans['correct'] = None

    alpha = string.ascii_lowercase

    for x in alpha:
        s = '(' + x + ')'
        if s in ques:
            opt = get_text(s, ques)
            ans['options'].append(opt.strip())
        else:
            break

    ind = sol.find('the correct answer is option')
    if ind != -1:
        cor = (sol[ind:])[-4:-1]
        ans['correct'] = cor
    else:
        for x in ans['options']:
            if x[:3] in sol:
                ans['correct'] = x[:3]
                break
            if x[3:] in sol:
                ans['correct'] = x[:3]
                break
    return ans


# Driver function to check the working of this script
if __name__ == '__main__':
    ques = '<em><strong>Mark </strong></em><strong>(✓)</strong><em><strong> against the correct answer</strong></em><br/> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>5</mn></mfrac></math> of a cistern is filled in 1 minute, how much more time will be required to fill the rest of it?<br/> <br/> (a) 20 seconds<br/> (b) 15 seconds<br/> (c) 12 seconds<br/> (d) 10 seconds'
    sol = "<p>Time taken to fill 45 of a cistern = 1 min<br /> Time taken to fill 1 cistern =54 min<br /> Time taken to fill 15 of a cistern = 54&times;15=14 min = 15 seconds<br /> <br /> Hence, it will take 15 seconds to fill the rest of the cistern.<br /> <br /> Thus, the correct option is (b).</p>"
    ans = findOptions(ques,sol)
    print(ans)