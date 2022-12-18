import tkinter
import librosa
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import mutagen
from mutagen.wave import WAVE
import audioread
from pathlib import Path

def check(filename):
    if filename[-3:]!="wav":
        mb.showinfo("ERROR", "Invalid file type     \nOpen an WAV file      ")
        otvmsg.set("Open a WAV file ")
    else:
        otvmsg.set(obrabotka(filename))


def choose_file():
    filetypes = (("аудио", "*.wav"), ("Любой", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
    if filename:
        print(filename)
        check(filename)


def obrabotka(filename):
    audio_data = filename
    y, sr = librosa.load(audio_data)
    y.shape

    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=8192, n_mfcc=12)
    print("tempo",tempo)
    print("-------------------------")
    print("beat_frames",beat_frames)
    print("-------------------------")
    s=0
    for i in mfcc:
        s += sum(i)
    print("mfcc", s)
    print("-------------------------")
    print(y_harmonic, y_percussive)
    razb = len(y) // 100
    k = 0
    for i in range(0, razb, 100):

        zero_crossings = librosa.zero_crossings(y[i:i + 100], pad=False)
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


window = tk.Tk()
window.title("Определение голоса")
window["bg"] = "lightblue2"
window.geometry('960x540+0+0')

btn_file = tk.Button(window, text="Выбрать файл",
                     command=choose_file, bg="MediumOrchid1",
                     borderwidth=0, height=3, width=15)
btn_file.pack(padx=60, pady=100)

otvmsg = tkinter.StringVar()
otv_lable = ttk.Label(foreground="red", textvariable=otvmsg,
                      wraplength=250, background="lightblue2",
                      font=("Arial", 14))
otv_lable.pack(padx=5, pady=5)
otvmsg.set("Open a WAV file ")
window.mainloop()