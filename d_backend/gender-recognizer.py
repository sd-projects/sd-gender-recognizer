import tkinter
import librosa
import numpy as np
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
from tkinter import messagebox as mb
import os
import pandas as pd

def start():
    window = tk.Tk()
    window.title("Определение голоса")
    window["bg"] = "lightblue2"
    window.geometry('660x430+0+0')

    btn_file = tk.Button(window, text="Выбрать файл",
                         command=choose_file, bg="MediumOrchid1",
                         borderwidth=0, height=3, width=15)
    btn_file.pack(padx=60, pady=100)
    global otvmsg
    otvmsg = tkinter.StringVar()

    otv_lable = ttk.Label(foreground="red", textvariable=otvmsg,
                          wraplength=250, background="lightblue2",
                          font=("Arial", 14))
    otv_lable.pack(padx=5, pady=5)
    otvmsg.set("Open a WAV or MP3 file ")
    window.mainloop()


def check(filename):
    if filename[-3:] != "wav":
        if filename[-3:] == "mp3":
            file = os.path.splitext(filename)[0]
            os.rename(filename, file + ".wav")
            filename = filename.replace("mp3", "wav")
            otvmsg.set(obrabotka(filename))
            file = os.path.splitext(filename)[0]
            os.rename(filename, file + ".mp3")
            filename = filename.replace("wav", "mp3")
        else:
            mb.showinfo("ERROR", "Invalid file type     \nOpen an WAV file      ")
            otvmsg.set("Open a WAV or MP3 file ")
    else:
        otvmsg.set(obrabotka(filename))


def choose_file():
    filetypes = (("аудио", "*.wav"), ("аудио", "*.mp3"), ("Любой", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
    if filename:
        print(filename)
        print(filename[filename.rfind("/")+1:])
        check(filename)


def obrabotka(filename):
    audio_data = filename
    y, sr = librosa.load(audio_data)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
    mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=20)
    X = librosa.stft(y)
    Xdb = librosa.amplitude_to_db(abs(X))
    print(np.sum(X))
    print(np.sum(Xdb))
    print(np.mean(X))
    print(np.mean(Xdb))
    print(np.var(X))
    print(np.var(Xdb))
    print(np.median(X))
    print(np.median(Xdb))
    df =pd.DataFrame({})
    dlina_razb = 500
    razb = len(y) // dlina_razb
    k = 0
    for i in range(0, razb, dlina_razb):

        zero_crossings = librosa.zero_crossings(y[i:i + dlina_razb], pad=False)
        if sum(zero_crossings) >= 20:
            k += 1
        elif sum(zero_crossings) < 9:
            k += 0
        elif sum(zero_crossings) < 20:
            k -= 1

    if k > 0:
        return "woman"
    elif k == 0:
        return"woman"
    else:
        return "man"


start()
