import os
from os import path
import librosa
from pydub import AudioSegment
import numpy as np


# Для использования этой функции нужна программа "ffmpeg.exe"
# Так же её нужно добавить в "Advanced system settings" в "Environment Variables" в "System Variables" в "Path"
# В фукцию подается путь аудиофайла в формате mp3, например: "G:\sd-gender-recognizer\file.mp3"
def wav_convert(input_file):
    # Проверяем расширение конвертируемого файла
    if input_file[-4:] == ".mp3":
        # Задаем путь финального файла
        output_file = input_file[:-4] + ".wav"
        try:
            # Пробуем провести конвертацию из обычного mp3 файла
            sound = AudioSegment.from_file(input_file, "mp3")
        except:
            # При неудаче пробуем провести конвертацию из mp3 файла, формат контейнера которого - mpeg4
            sound = AudioSegment.from_file(input_file, format="mp4")
        # Сохраняем финальный файл
        sound.export(output_file, format="wav")


def all_convert():
    # Перебор всех файлов из папки
    for i in [i for i in os.listdir() if i[-4:] == ".mp3" or i[-4:] == "wav"]:
        wav_convert(i)


def s_sr(lstdir):
    for i in lstdir:
        y, sr = librosa.load(i)
        print(Xdb_criterion(y=y), i)
        # print(y_percussive_criterion(y)[1], mfccs_criterion(y, sr)[1], mfccs_criterion(y, sr)[2], mfccs_criterion(y, sr)[3], i)


def mfccs_criterion(y, sr):
    y_harmonic = librosa.effects.hpss(y)[0]
    mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=13)
    result1 = np.mean([max(i) for i in mfccs])
    result2 = max(mfccs[1])
    result3 = max(mfccs[2])
    if result1 > 17:
        gender = 1
    else:
        gender = 0
    return result1, result2, result3, gender


def y_percussive_criterion(y):
    y_percussive = round(np.mean(librosa.effects.hpss(y)[1]) * 10 ** 5, 2)
    if y_percussive > -6:
        gender = 0
    else:
        gender = 1
    return y_percussive, gender


def Xdb_criterion(y):
    X = librosa.stft(y)
    Xdb = librosa.amplitude_to_db(abs(X))
    if np.var(Xdb) > 180:
        result = 1
    else:
        result = 0
    return np.var(Xdb), result


s_sr([i for i in os.listdir() if i[-4:] == ".wav"])
