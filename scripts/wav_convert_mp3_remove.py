import os
from pydub import AudioSegment


# Для использования этой функции нужна программа "ffmpeg.exe"
# Так же её нужно добавить в "Advanced system settings" в "Environment Variables" в "System Variables" в "Path"
# В фукцию подается путь аудиофайла в формате mp3, например: "G:\sd-gender-recognizer\file.mp3"
def wav_convert(input_file):
    # Проверяем расширение конвертируемого файла feeflk
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


def all_convert(lstdir):
    # Перебор всех файлов из папки
    for i in [i for i in os.listdir(lstdir) if i[-4:] == ".mp3" or i[-4:] == "wav"]:
        wav_convert(i)
    mp3_remove(lstdir=lstdir)


def mp3_remove(lstdir):
    lstdir = os.listdir(lstdir)
    for i in lstdir:
        if i.endswith(".mp3"):
            os.remove(i)


all_convert(lstdir="")
