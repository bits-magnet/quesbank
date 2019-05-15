import json

with open('1179_5754_textbooksolution_html.json', 'r') as f:
    data = json.load(f)
#print( data['data'])


for x in data['data']:
#    print("%s: %s" % (x, data['data'][x]))
    for y in x:
        print(y,':::', x[y])
    print()
    print()
    print()
