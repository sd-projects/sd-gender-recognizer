import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import librosa
import os
import openpyxl

inpt = os.listdir("D:\github\sd-gender-recognizer\d_backend\Material for tests\others")
audio_dt_name = inpt


df = []
for i, audio_data in enumerate(audio_dt_name):
    a=0
    if audio_data[:3]=="man":
        a=1
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,sr=sr)
    mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=20)
    X = librosa.stft(y)
    Xdb = librosa.amplitude_to_db(abs(X))
    cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    contrast=librosa.feature.spectral_contrast(y=y_harmonic,sr=sr)
    zero_crossing = []
    shag = 500
    zero_count = len(y)//shag
    counter = 0
    print(audio_data)
    print(np.mean(mfccs)+np.std(mfccs))
    for i in range(zero_count):
        zero_crossing.append(sum(librosa.zero_crossings(y[counter:counter+shag], pad=False)))
        counter+=shag
    df.append([a, audio_data, np.sum(y_harmonic), np.sum(y_percussive), np.mean(y_harmonic)*10**10, np.mean(y_percussive)*10**10, np.var(y_harmonic)*10**4
               , np.var(y_percussive)*10**4, np.median(y_harmonic)*10**10, np.median(y_percussive)*10**10, np.sum(mfccs), np.mean(mfccs), np.var(mfccs)
               , np.sum(Xdb), np.mean(Xdb), np.var(X), np.var(Xdb), np.var(zero_crossing), np.mean(zero_crossing), np.sum(zero_crossing), np.median(zero_crossing)])
print(df)
df = pd.DataFrame(df, columns=[" sex", " audio_data", " np.sum(y_harmonic)", " np.sum(y_percussive)", " np.mean(y_harmonic)*10**10", " np.mean(y_percussive)*10**10", " np.var(y_harmonic)*10**4"
               , "np.var(y_percussive)*10**4", " np.median(y_harmonic)*10**10", " np.median(y_percussive)*10**10", " np.sum(mfccs)", " np.mean(mfccs)", " np.var(mfccs)"
               , " np.sum(Xdb)", " np.mean(Xdb)", " np.var(X)", "np.var(Xdb)", "np.var(zero_crossing)", "np.mean(zero_crossing)", "np.sum(zero_crossing)", "np.median(zero_crossing)"])
df.to_excel("data.xlsx", index=False)