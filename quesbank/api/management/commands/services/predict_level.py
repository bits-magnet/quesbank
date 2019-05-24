# function_name: predict_level
# input : L is List of json['Data']
# return value: dictionary (Quesid : ques_level)
#               ques_level is integer



#############################################################
#                                                           #
#   First 25% questions of the exercise :   EASY(1)         #
#                                                           #
#   Next 50% questions of the exercise :    MEDIUM(2)       #
#                                                           #
#   Last 25% questions of the exercise :    HARD(3)         #
#                                                           #
#############################################################

def extract_number(ques_no):
    for i in range(len(ques_no)-1, -1, -1):                   # Iterating in reverse to handle exercise names such as
        if ques_no[i].isdigit() == False:                     # 'A.2', 'A.1.1', 'S2', etc.
            if (i+1) == len(ques_no):                         #
                break                                   # If no integers can be found, we assume question number
            return int(ques_no[i+1:])                         # is alphabetical and try to return its alphabetic postion
    try:                                                # e.g. 'c' is ques no 3
        return int(ques_no)
    except:
        return ord(ques_no.lower()) - ord('a') + 1


def predict_level(L):
    prev_ex = L[0]['exerciseName']
    ques_count = dict()
    ques_count[prev_ex] = 1
    for x in L[1:]:
        if x['exerciseName'] == prev_ex:
            ques_count[prev_ex] += 1
        else:
            prev_ex = x['exerciseName']
            ques_count[prev_ex] = 1

    level = dict()
    for x in L:
        total_questions = int(ques_count[x['exerciseName']])
        num = extract_number(x['questionNo'])
        qid = x['id']
        if num <= total_questions * 0.25:
            level[qid] = 1          # Easy
        elif num <= total_questions * 0.75:
            level[qid] = 2          # Medium
        else:
            level[qid] = 3          #Hard

    return level

