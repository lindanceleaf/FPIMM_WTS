def getSheet(path: str):
    FreqTable = 'FreqTable.txt'
    file = open(FreqTable, 'r')
    data = file.readlines()
    table = []
    for i in data:
        name, freq = i.split(' ')
        table.append((name, float(freq)))
    file.close()

    audio = open(path, 'r')
    outputPath = path.replace('Freq', 'sheet')
    out = open(outputPath, 'w')
    data = audio.readlines()
    for i in data:
        i = float(i)
        if i == 0: out.write('_ ')
        else:
            for j in range(len(table)-1):
                if table[j][1] <= i < table[j+1][1]:
                    out.write(f'{table[j][0]} ')
                    break
    audio.close()
    out.close()