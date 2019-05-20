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
            if x[:3] in sol:
                ans['correct'] = x[:3]
                break
        if ans['correct'] == None:
            for x in ans['options']:
                if x in sol:
                    ans['correct'] = x[:3]
                    break
        if ans['correct'] == None:
            for x in alpha:
                s = '(' + x + ')'
                if s in sol:
                    ans['correct'] = s
        if ans['correct'] == None:
            for x in ans['options']:
                y = x[3:]
                if y in sol:
                    ans['correct'] = x[:3]
    return ans

if __name__ == '__main__':
    ques = '<em><strong>Mark </strong></em><strong>(✓)</strong><em><strong> against the correct answer</strong></em><br/> If <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mn>4</mn><mn>5</mn></mfrac></math> of a cistern is filled in 1 minute, how much more time will be required to fill the rest of it?<br/> <br/> (a) 20 seconds<br/> (b) 15 seconds<br/> (c) 12 seconds<br/> (d) 10 seconds'
    sol = "<p>Time taken to fill 45 of a cistern = 1 min<br /> Time taken to fill 1 cistern =54 min<br /> Time taken to fill 15 of a cistern = 54&times;15=14 min = 15 seconds<br /> <br /> Hence, it will take 15 seconds to fill the rest of the cistern.<br /> <br /> Thus, the correct option is (b).</p>"
    ans = findOptions(ques,sol)
    print(ans)