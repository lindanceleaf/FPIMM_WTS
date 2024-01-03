from seperate import separate
from getFreq import getFreq
from getSheet import getSheet
from audioInfo import getInfo
from choose_mode import choose_mode, get_option, kill_window
from choose_path import select_file
from getLily import getLily

def main():
    # get audio
    filename = select_file()  # end with .wav
    if not filename: return
    # print(filename)
    audioPath = f'audio/{filename}'
    # print(audioPath)

    choose_mode()
    kinds = get_option()
    kill_window()

    # separate the audio 
    separate(audioPath)

    file = filename[:filename.find('.')]
    BPM, sr = getInfo(audioPath)
    for kind in kinds:
        splitPath = f'result/{file}/{kind}.wav'
        getFreq(splitPath, BPM, sr) # put the file in result/file/kind_Freq.txt
        FreqPath = f'result/{file}/{kind}_Freq.txt'
        getSheet(FreqPath, kind)
        getLily(f'result/{file}', kind, BPM)
        print(f'{kind} finished')

if __name__ == "__main__":
    main()