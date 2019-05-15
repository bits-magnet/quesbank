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

    
        

# Driver function to check
if __name__ == '__main__':
    ques_html = '<em><strong>Mark (\u2713) against the corect answer<\/strong><\/em><br \/>\r\n<br \/>\r\n6 &minus; (&minus;8) = ?<br \/>\r\n<br \/>\r\n(a) &minus;2<br \/>\r\n(b) 2<br \/>\r\n(c) 14<br \/>\r\n(d) none of these'
    sol_html = '(c) 14<br \/>\r\nGiven:<br \/>\r\n6&nbsp;&minus; (&minus;8)<br \/>\r\n= 6 + 8<br \/>\r\n= 14'
    exName = 'Objective Type Questions'
    ans = categorize(ques_html, sol_html, exName)
    print(ans)
    
