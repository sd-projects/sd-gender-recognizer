import os
import librosa
from pydub import AudioSegment
import numpy as np


# Для использования этой функции нужна программа "ffmpeg.exe"
# Так же её нужно добавить в "Advanced system settings" в "Environment Variables" в "System Variables" в "Path"
# В фукцию подается путь аудиофайла в формате mp3, например: "G:\sd-gender-recognizer\file.mp3"
def wav_convert(input_file):
    remv = 0
    # Проверяем расширение конвертируемого файла
    output_file = input_file[:-4] + ".wav"
    if input_file[-4:] == ".mp3":
        # Задаем путь финального файла
        remv = 1
        try:
            # Пробуем провести конвертацию из обычного mp3 файла
            sound = AudioSegment.from_file(input_file, "mp3")
        except:
            # При неудаче пробуем провести конвертацию из mp3 файла, формат контейнера которого - mpeg4
            sound = AudioSegment.from_file(input_file, format="mp4")
        # Сохраняем финальный файл
        sound.export(output_file, format="wav")
    return output_file, remv


def global_result(file, p1, p2, p3):
    file, remv = wav_convert(file)
    y, sr = librosa.load(file)
    r1, r2, r3 = mfccs_criterion(y, sr, p1), y_percussive_criterion(y, p2), Xdb_criterion(y, p3)
    if remv == 1:
        os.remove(file)
    return r1, r2, r3


def mfccs_criterion(y, sr, x):
    y_harmonic = librosa.effects.hpss(y)[0]
    mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=13)
    result = np.mean([max(i) for i in mfccs])
    if result > x:
        result = 1
    else:
        result = -1
    return result


def y_percussive_criterion(y, x):
    y_percussive = round(np.mean(librosa.effects.hpss(y)[1]) * 10 ** 5, 2)
    if y_percussive > x:
        result = -1
    else:
        result = 1
    return result


def Xdb_criterion(y, x):
    X = librosa.stft(y)
    Xdb = librosa.amplitude_to_db(abs(X))
    if np.var(Xdb) > x:
        result = 1
    else:
        result = -1
    return result
