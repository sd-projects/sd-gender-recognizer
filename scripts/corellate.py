import pandas as pd
import librosa
import os
import numpy as np
import seaborn as sns
from scipy.io import wavfile
import matplotlib as mpl
import matplotlib.pyplot as plt

inpt = os.listdir("D:\github\sd-gender-recognizer\d_backend\Material for tests\others")
audio_dt_name = inpt
st = ""
k = 0
for i in range(22):
    if k < 15:
        colr = "--g"
    else:
        colr = ":m"
    k += 1
    st += f"[i for i in range(len(mfccsdf[{i}]))], mfccsdf[{i}], '{colr}', "
print(st)
df = []
mfccsdf = []
for i, audio_data in enumerate(audio_dt_name):
    a = 0
    if audio_data[:3] == "man":
        a = 1
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
    mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=13)
    X = librosa.stft(y)
    Xdb = librosa.amplitude_to_db(abs(X))
    cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    contrast = librosa.feature.spectral_contrast(y=y_harmonic, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zero_crossing = []
    shag = 500
    zero_count = len(y) // shag
    counter = 0
    print(audio_data)
    sample_rate, audio = wavfile.read(audio_data)
    tm = (len(audio) / sample_rate)
    print(np.mean(mfccsdf))
    print(tm)
    for i in range(zero_count):
        zero_crossing.append(sum(librosa.zero_crossings(y[counter:counter + shag], pad=False)))
        counter += shag
    mfccsdf.append([np.max(mfccs[0]), max(mfccs[1]), max([2]), max(mfccs[3]), max(mfccs[4]), max(mfccs[5]),
                    max(mfccs[6]), max(mfccs[7]), max(mfccs[8]), max(mfccs[9]), max(mfccs[10]),
                    max(mfccs[11]), max(mfccs[12])])

    df.append([a, audio_data, tm, np.max(rolloff), np.mean(mfccsdf), np.sum(y_harmonic) / tm, np.sum(y_percussive) / tm,
               np.mean(y_harmonic) * 10 ** 10, np.mean(y_percussive) * 10 ** 10, np.var(y_harmonic) * 10 ** 4
                  , np.var(y_percussive) * 10 ** 4, np.median(y_harmonic) * 10 ** 10,
               np.median(y_percussive) * 10 ** 10,
               np.sum(mfccs) / tm, np.mean(mfccs), np.var(mfccs)
                  , np.sum(Xdb) / tm, np.mean(Xdb), np.var(X), np.var(Xdb), np.var(zero_crossing),
               np.mean(zero_crossing),
               np.sum(zero_crossing) / tm, np.median(zero_crossing)])
print(df)

df = pd.DataFrame(df,
                  columns=[" sex", " audio_data", "time", "np.mean(contrast)", "np.mean(mfccsdf)", "np.sum(y_harmonic)",
                           " np.sum(y_percussive)", " np.mean(y_harmonic)*10**10", " np.mean(y_percussive)*10**10",
                           " np.var(y_harmonic)*10**4", "np.var(y_percussive)*10**4",
                           " np.median(y_harmonic)*10**10", " np.median(y_percussive)*10**10",
                           " np.sum(mfccs)", " np.mean(mfccs)", " np.var(mfccs)", " np.sum(Xdb)",
                           " np.mean(Xdb)", " np.var(X)", "np.var(Xdb)", "np.var(zero_crossing)",
                           "np.mean(zero_crossing)", "np.sum(zero_crossing)", "np.median(zero_crossing)"])

df.to_excel("data.xlsx", index=False)

df = pd.read_excel("data.xlsx")
df.dropna()
df1 = df

# plt.plot([i for i in range(len(mfccsdf[0]))], mfccsdf[0], '--g', [i for i in range(len(mfccsdf[1]))], mfccsdf[1],
#          '--g', [i for i in range(len(mfccsdf[2]))], mfccsdf[2], '--g', [i for i in range(len(mfccsdf[3]))], mfccsdf[3],
#          '--g', [i for i in range(len(mfccsdf[4]))], mfccsdf[4], '--g', [i for i in range(len(mfccsdf[5]))], mfccsdf[5],
#          '--g', [i for i in range(len(mfccsdf[6]))], mfccsdf[6], '--g', [i for i in range(len(mfccsdf[7]))], mfccsdf[7],
#          '--g', [i for i in range(len(mfccsdf[8]))], mfccsdf[8], '--g', [i for i in range(len(mfccsdf[9]))], mfccsdf[9],
#          '--g', [i for i in range(len(mfccsdf[10]))], mfccsdf[10], '--g', [i for i in range(len(mfccsdf[11]))], mfccsdf[11],
#          '--g', [i for i in range(len(mfccsdf[12]))], mfccsdf[12], '--g', [i for i in range(len(mfccsdf[13]))], mfccsdf[13],
#          '--g', [i for i in range(len(mfccsdf[14]))], mfccsdf[14], '--g', [i for i in range(len(mfccsdf[15]))], mfccsdf[15],
#          ':m', [i for i in range(len(mfccsdf[16]))], mfccsdf[16], ':m', [i for i in range(len(mfccsdf[17]))], mfccsdf[17],
#          ':m', [i for i in range(len(mfccsdf[18]))], mfccsdf[18], ':m', [i for i in range(len(mfccsdf[19]))], mfccsdf[19],
#          ':m', [i for i in range(len(mfccsdf[20]))], mfccsdf[20], ':m',[i for i in range(len(mfccsdf[21]))], mfccsdf[21], ':m')


plt.figure(figsize=(12, 10), dpi=80)
sns.heatmap(df1.corr(), xticklabels=df1.corr().columns, yticklabels=df1.corr().columns, cmap='RdYlGn', center=0,
            annot=True)
plt.title('Correlogram', fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
