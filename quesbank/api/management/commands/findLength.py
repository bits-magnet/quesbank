def findLength(ques):
    ind = ques.find('<br')
    if ind != -1:
        ques = ques[:ind]
    if len(ques) < 100:
        return 'VSA'
    elif len(ques) > 300:
        return 'LA'
    return 'SA'

# Driver function to check
if __name__ == '__main__':
    ques = 'In a class test containing 10 questions, 5 marks are awarded for every correct answer and (&minus;2) marks are awarded for every incorrect answer and 0 for each question not attempted.<br \/>\r\n<br \/>\r\n(i) Ravi gets 4 correct and 6 incorrect answers. What is his score?<br \/>\r\n(ii) Reenu gets 5 correct and 5 incorrect answers. What is her score?<br \/>\r\n(iii) Heena gets 2 correct and 5 incorrect answers. What is her score?'
    print(findLength(ques))
