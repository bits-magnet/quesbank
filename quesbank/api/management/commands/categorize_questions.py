# return Subjective or Objective string
# Inputs: Question html, solution html, Exercise Name
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

    return 'Subjective'
