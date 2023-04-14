import tkinter
import librosa
import numpy as np
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
from tkinter import messagebox as mb
import os

def sound_info(filename):
    audio_data = filename
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
    mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=20)
    X = librosa.stft(y)
    Xdb = librosa.amplitude_to_db(abs(X))
    cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    contrast = librosa.feature.spectral_contrast(y=y_harmonic, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    spectral_rolloff = librosa.feature.spectral_rolloff(y + 0.01, sr=sr)[0]
    spectral_bandwidth_2 = librosa.feature.spectral_bandwidth(y + 0.01, sr=sr)[0]
    spectral_bandwidth_3 = librosa.feature.spectral_bandwidth(y + 0.01, sr=sr, p=3)[0]
    spectral_bandwidth_4 = librosa.feature.spectral_bandwidth(y + 0.01, sr=sr, p=4)[0]

def zero_crossing():
    for i in range(0, len(y), step):
        