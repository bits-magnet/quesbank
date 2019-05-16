import string
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
    ans['correct'] = None

    alpha = string.ascii_lowercase

    for x in alpha:
        s = '(' + x + ')'
        if s in ques:
            opt = getText(s, ques)
            ans['options'].append(opt.strip())
        else:
            break

    ind = sol.find('the correct answer is option')
    if ind != -1:
        cor = (sol[ind:])[-4:-1]
        ans['correct'] = cor
    else:
        for x in ans['options']:
            if x in sol:
                ans['correct'] = x[:3]
                break
        if 'correct' not in ans.keys():
            for x in alpha:
                s = '(' + x + ')'
                if s in sol:
                    ans['correct'] = s
        if 'correct' not in ans.keys():
            for x in ans['options']:
                y = x[3:]
                if y in sol:
                    ans['correct'] = x[:3]
    return ans

