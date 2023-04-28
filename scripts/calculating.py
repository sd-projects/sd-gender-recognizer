import os
import numpy as np
from scipy.interpolate import CubicSpline
from scipy import optimize
import librosa
from scripts.audio_func import wav_convert
from multiprocessing import Process, Lock
from random import randint
from itertools import combinations_with_replacement

out = {}


# p1 = 24.25201138716356
# p2 = -4.021
# p3 = 178.41533381607533
def cjyvert():
    for file in [i for i in os.listdir("D:\github\sd-gender-recognizer\d_backend\Material_for_tests\others\_test") if
                 i[-4:] == ".wav"]:
        kof = []
        file = f"D:\github\sd-gender-recognizer\d_backend\Material_for_tests\others\_test\{file}"
        y, sr = librosa.load(file)
        X = librosa.stft(y)
        y_harmonic = librosa.effects.hpss(y)[0]
        mfccs = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_mfcc=13)
        kof.append(np.mean([max(i) for i in mfccs]))
        kof.append(round(np.mean(librosa.effects.hpss(y)[1]) * 10 ** 5, 4))
        kof.append(np.var(librosa.amplitude_to_db(abs(X))))
        out[file] = kof


# cjyvert()

# with open("k_out.txt", "w") as f:
#     for i in out:
#         f.write(f"{i} {out[i][0]} {out[i][1]} {out[i][2]}\n")

big = []


def func(x):
    ot = []
    for v in x:
        k = 0
        for i in out:
            result1 = (out[i][0])
            if result1 > v[0]:
                result1 = -1
            else:
                result1 = 1

            result2 = (out[i][1])
            if result2 > v[1]:
                result2 = -1
            else:
                result2 = 1

            result3 = (out[i][2])
            if result3 > v[2]:
                result3 = -1
            else:
                result3 = 1

            if result3 + result2 + result1 < 0:
                result = -1
            else:
                result = 1

            if (i[i.rfind("\\") + 1:i.rfind("\\") + 2] == "m" and result == -1) or (i[i.rfind("\\") + 1:i.rfind(
                    "\\") + 2] == "f" and result == 1):
                k += 1
        ot.append([v, k])

    return np.array(ot)

out = {}
with open("k_out.txt", "r") as f:
    for i in f.read().split("\n"):
        l = i.split(" ")
        print(l)
        out[l[0]] = [float(l[1]), float(l[2]), float(l[3])]

# k1 = [i / 1000 for i in range(9000, 25000, 1)]
# k2 = [i / 1000 for i in range(-7000, 7000, 1)]
# k3 = [i / 1000 for i in range(170000, 190000, 1)]
k11 = [randint(1100, 2500) / 100 for i in range(401)]
k12 = [randint(-500, 500) / 100 for i in range(401)]
k13 = [randint(17000, 19000) / 100 for i in range(401)]

for i in range(500):



    hlp = []
    for i in combinations_with_replacement([i for i in range(400)], 3):
        b = []
        i0 = i[0]
        i1 = i[1]
        i2 = i[2]
        b.append(k11[i0])
        b.append(k12[i1])
        b.append(k13[i2])
        hlp.append(b)
    x = np.array(hlp)
    y = func(x)
    p = []
    a = []
    for i in y:
        a.append(i[1])
    mn = min(a)
    for i in y:
        if i[1] == mn:
            p.append(i[0])
    print("")
    print("-------------------------------------------------------------------------------")
    print("")
    print("=======", mn)
    print("")
    print(p)
    alf = []
    alf.append(mn)
    alf.append(p)
    big.append(alf)
a1 = []
for i in big:
    a1.append(i[0])
a1 = min(a1)
o1 = []
for i in big:
    if i[0] == a1:
        o1.append(i[1])
print(o1)
