def getSheet(path: str, mode: str):
    FreqTable = 'FreqTable.txt'
    file = open(FreqTable, 'r')
    data = file.readlines()
    table = []
    for i in data:
        name, freq = i.split(' ')
        table.append((name, float(freq)))
    file.close()

    threshold = [(40.05, 403.64), (26.74, 4310.46), (127.15, 719.22), (40.05, 1077.61), (21.22, 7680.37)]
    modeMap = ['bass', 'piano', 'vocals', 'drums', 'other']
    index = modeMap.index(mode)
    freq_threshold = threshold[index]
    
    audio = open(path, 'r')
    outputPath = path.replace('Freq', 'sheet')
    out = open(outputPath, 'w')
    data = audio.readlines()
    
    fmin = freq_threshold[0]
    fmax = freq_threshold[1]
    for i in data:
        i = float(i)
        if i < fmin or i > fmax: out.write('_ ')
        else:
            for j in range(1, len(table)-1):
                left = (table[j][1] + table[j-1][1]) / 2
                right = (table[j][1] + table[j+1][1]) / 2
                if left <= i < right:
                    out.write(f'{table[j][0]} ')
                    break
    audio.close()
    out.close()