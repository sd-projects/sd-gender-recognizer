import matplotlib.pyplot as plt
import os
from scripts.audio_func import wav_convert
import librosa
import numpy as np


def all_convert():
    for file in [file for file in os.listdir() if file[-4:] == ".mp3"]:
        wav_convert(file)


def del_mp3():
    for file in [file for file in os.listdir() if file[-4:] == ".mp3"]:
        os.remove(file)


def mfccs_rez():
    out_mfccs_rez = {}
    for i in [i for i in os.listdir() if i[-4:] == ".wav"]:
        y, sr = librosa.load(i)
        y_harmonic = librosa.effects.hpss(y)[0]
        out_mfccs_rez[i] = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=13)
    return out_mfccs_rez


def txt_mfccs_take_plt():
    with open("mfccs.txt", "r") as f:
        inpt = f.read().split("\n")
        for j in inpt:
            j = j.split(" ")
            if j[0][:1] == "f":
                color = "--r"
            else:
                color = ":b"
            plt.plot([i for i in range(1, 14, 1)], list(map(float, j[1:len(j)])), color)
    plt.show()


all_convert()


mfccs_out = mfccs_rez()


with open("mfccs.txt", "w") as f:
    for i in mfccs_out:
        f.write(i)
        for j in mfccs_out[i]:
            print(f"{np.max(j)}")
            f.write(f" {np.max(j)}")
        f.write("\n")

txt_mfccs_take_plt()
