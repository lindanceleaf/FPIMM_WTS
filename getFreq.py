import librosa
import numpy as np

def getFreq(path: str, BPM: int, sr: int):
    output_path = path.replace('.wav', '_Freq.txt')
    output = open(output_path, 'w')

    y, sr = librosa.load(path)
    beat_interval = 60 / BPM

    # get the time of every beat
    beat_times = np.arange(0, librosa.get_duration(y=y, sr=sr), beat_interval)

    pitches, magnitudes = librosa.piptrack(y=y, sr=sr, fmin=20, fmax=8000)

    for beat_time in beat_times:
        # find the closest frame
        frame_idx = np.argmin(np.abs(librosa.time_to_frames(beat_time, sr=sr) - np.arange(pitches.shape[1])))
        # find the max magnitude pitch
        max_pitch_idx = np.argmax(magnitudes[:, frame_idx])
        # turn pitch index to real freqency
        frequency = pitches[max_pitch_idx, frame_idx]
        output.write(f'{frequency:.2f}\n')
    output.close()