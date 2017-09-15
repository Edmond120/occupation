file = open("occupations.csv","r")
dic = {}
for line in file:
    length = len(line)
    inQuote = False
    lineEnd = -2
    splitIndex = None
    for i in range(0,length):
        if(line[i] == '"'):
            inQuote = not inQuote
        elif((not inQuote) and line[i] == ','):
            splitIndex = i
            break
    dic[line[0:splitIndex]] = line[splitIndex + 1:lineEnd]
print dic
