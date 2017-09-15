filename = "occupations.csv"
file = open(filename, "r")
dict = {}
quoteOpened = False
for line in file:
    index = 0
    mark = -1
    while index < len(line):
        if(line[index] == '"'):
            quoteOpened = not quoteOpened
        elif(not quoteOpened and line[index] == ","):
            mark = index
            break
        else:
            index += 1
    dict[line[0:mark]] = line[mark + 1:]
print dict
