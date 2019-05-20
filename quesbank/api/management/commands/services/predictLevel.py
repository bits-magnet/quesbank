# return dictionary (Quesid : QuesLevel)
# Input : L is List of json['Data']
import string

def extractNumber(s):
    for i in range(len(s)-1, -1, -1):
        if s[i].isdigit() == False:
            if (i+1) == len(s):
                break
            return int(s[i+1:])
    try:
        return int(s)
    except:
        return ord(s.lower()) - ord('a') + 1


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
        num = extractNumber(x['questionNo'])
        qid = x['id']
        if num <= total_questions * 0.25:
            level[qid] = 1          # Easy
        elif num <= total_questions * 0.75:
            level[qid] = 2          # Medium
        else:
            level[qid] = 3          #Hard

    return level

