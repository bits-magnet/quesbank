# return string code for solution length
# input: solutionHtml
def findLength(sol):
    ind = sol.find('<br')
    if ind != -1:
        sol = sol[:ind]
    if len(sol) < 100:
        return 'VSA'
    elif len(sol) > 300:
        return 'LA'
    return 'SA'
