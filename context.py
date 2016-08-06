import fileinput

def getContext(user):
    with open('context.txt', 'r') as context:
        for line in context:
            data = line.split('\t')
            if (data[0] == user):
                return data[1]
    return ''

def writeContext(user, data):
    wroteData = False
    for line in fileinput.input(['context.txt'], inplace = 1): 
        if (user in line):
            print user + '\t' + data
            wroteData = True
        else:
            print line

    if (not wroteData):
        with open('context.txt', 'a') as context:
            context.write(user + '\t' + data)