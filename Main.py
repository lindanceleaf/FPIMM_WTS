from seperate import separate
from getFreq import getFreq
from getSheet import getSheet
from audioInfo import getInfo

def main():
    # get audio
    filename = 'Venus.mp3'
    audioPath = f'audio/{filename}'

    # separate the audio 
    separate(audioPath)

    kinds = ['piano', 'vocals', 'drums', 'bass', 'other']
    file = filename[:filename.find('.')]
    BPM, sr = getInfo(audioPath)
    for kind in kinds:
        splitPath = f'result/{file}/{kind}.wav'
        getFreq(splitPath, BPM, sr) # put the file in result/file/kind_Freq.txt
        FreqPath = f'result/{file}/{kind}_Freq.txt'
        getSheet(FreqPath)

if __name__ == "__main__":
    main()