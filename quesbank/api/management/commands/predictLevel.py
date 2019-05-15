# return dictionary (Quesid : QuesLevel)
# Input : L is List of json['Data']
def predictLevel(L):
    prevEx = L[0]['exerciseName']
    quesCount = dict()
    quesCount[prevEx] = 1
    for x in L[1:]:
        if x['exerciseName'] == prevEx:
            quesCount[prevEx] += 1
        else:
            prevEx = x['exerciseName']
            quesCount[prevEx] = 1

    level = dict()
    for x in L:
        total_questions = int(quesCount[x['exerciseName']])
        num = int(x['questionNo'])
        qid = x['id']
        if num <= total_questions * 0.25:
            level[qid] = 1          # Easy
        elif num <= total_questions * 0.75:
            level[qid] = 2          # Medium
        else:
            level[qid] = 3          #Hard

    return level
