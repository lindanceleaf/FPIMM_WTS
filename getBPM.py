import librosa

file_path = 'audio/leonell.mp3'
audio, sr = librosa.load(file_path)

print(librosa.beat.tempo(audio))