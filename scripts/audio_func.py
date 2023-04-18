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


def globalresult(file):
    file, remv = wav_convert(file)
    y, sr = librosa.load(file)
    result = mfccs_criterion(y, sr) + y_percussive_criterion(y) + Xdb_criterion(y)
    if remv == 1:
        os.remove(file)
    if result < 0:
        gender = "Female - "
    else:
        gender = "Male   - "
    return gender


def mfccs_criterion(y, sr):
    y_harmonic = librosa.effects.hpss(y)[0]
    mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=13)
    result = np.mean([max(i) for i in mfccs])
    result2 = max(mfccs[1])
    result3 = max(mfccs[2])
    if result > 17:
        result = 1
    else:
        result = -1
    return result


def y_percussive_criterion(y):
    y_percussive = round(np.mean(librosa.effects.hpss(y)[1]) * 10 ** 5, 2)
    if y_percussive > -3:
        result = -1
    else:
        result = 1
    return result


def Xdb_criterion(y):
    X = librosa.stft(y)
    Xdb = librosa.amplitude_to_db(abs(X))
    if np.var(Xdb) > 180:
        result = 1
    else:
        result = -1
    return result
