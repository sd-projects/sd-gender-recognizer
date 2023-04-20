import os
import librosa
from pydub import AudioSegment
import numpy as np


# Для использования этой функции нужна утилита "ffmpeg.exe"
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
    k1, k2, k3 = half_result(file)

    if k1 > p1:
        r1 = 1
    else:
        r1 = -1

    if k2 < p2:
        r2 = 1
    else:
        r2 = -1

    if k3 > p3:
        r3 = 1
    else:
        r3 = -1

    return r1, r2, r3


def half_result(file):
    file, remv = wav_convert(file)
    y, sr = librosa.load(file)

    k1, k2, k3 = mfccs_criterion(y, sr), y_percussive_criterion(y), xdb_criterion(y)

    if remv == 1:
        os.remove(file)

    return k1, k2, k3


def mfccs_criterion(y, sr):
    y_harmonic = librosa.effects.hpss(y)[0]
    mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=13)
    result = np.mean([max(i) for i in mfccs])

    return result


def y_percussive_criterion(y):
    y_percussive = round(np.mean(librosa.effects.hpss(y)[1]) * 10 ** 5, 2)

    return y_percussive


def xdb_criterion(y):
    x = librosa.stft(y)
    xdb = librosa.amplitude_to_db(abs(x))

    return np.var(xdb)