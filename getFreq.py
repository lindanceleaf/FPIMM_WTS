import librosa
import numpy as np

def getFreq(path: str, BPM: int, sr: int):
    output_path = path.replace('.wav', '_Freq.txt')
    output = open(output_path, 'w')

    audio_data, sr = librosa.load(path, sr=sr)

    slice_rate = 2584 / (BPM * 4)
    # get the magnitudes
    pitches, magnitudes = librosa.piptrack(y=audio_data, sr=sr)
    # turn the amplitude to db
    magnitudes_db = librosa.amplitude_to_db(magnitudes)
    # # 获取音高（频率）数据
    frequencies = np.argmax(magnitudes_db, axis=0)
    # # pitch_times = librosa.times_like(frequencies, sr=sr)
    pitch_times = librosa.times_like(frequencies, sr=sr)

    # # 打印每个时间点的音高（频率）
    pitch_list = []
    for time, pitch in zip(pitch_times, frequencies):
        pitch_list.append((time, pitch))
        # output.write(f"Time: {time:.2f}s, Pitch: {pitch} Hz\n")

    cnt = 1
    while True:
        index = int(slice_rate * cnt)
        if index > len(pitch_list): break
        output.write(f"{pitch_list[index][1]}\n")
        cnt += 1

    output.close()