import librosa

def getInfo(path: str) -> (int, int):

    audio_data, sr = librosa.load(path)

    tempo = int(librosa.beat.tempo(y=audio_data, sr=sr))

    return (tempo, sr)
