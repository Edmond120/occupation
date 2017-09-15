file = open("occupations.csv","r")
dic = {}
for line in file:
    length = len(line)
    inQuote = False
    lineEnd = None
    splitIndex = None
    for i in range(0,length):
        if(line[i] == '"'):
            inQuote = not inQuote
        elif((not inQuote) and line[i] == ','):
            splitIndex = i
            break
    i = -1
    while(i <= len(line)):
        if(line[i] == '\r' or line[i] == '\n'):
            lineEnd = i
        else:
            break
        i -= 1
    dic[line[0:splitIndex]] = line[splitIndex + 1:lineEnd]
print dic
