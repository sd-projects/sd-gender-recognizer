from os import listdir

from audio_func import global_result

import time


start = time.time()


def data_analyzer(p1, p2, p3, i1):
    m_data = ["D:/ruls_data/train/audio/8086/7771/", "D:/ruls_data/train/audio/8169/12256/",
              "D:/ruls_data/test/audio/2826/2145/", "D:/ruls_data/test/audio/4471/2145/",
              "D:/ruls_data/test/audio/4372/2145/"]
    m_errs = [0 for _ in range(4)]

    f_data = ["D:/ruls_data/train/audio/9014/11018/", "D:/ruls_data/train/audio/9014/8641/",
              "D:/ruls_data/test/audio/2671/2145/", "D:/ruls_data/test/audio/3056/2145/",
              "D:/ruls_data/dev/audio/5397/2145/"]
    f_errs = [0 for _ in range(4)]

    for i in range(5):
        temp_errs = analyzer(m_data[i], "m", p1, p2, p3, i1, i)

        for j in range(4):
            m_errs[j] += temp_errs[j]

    for i in range(5):
        temp_errs = analyzer(f_data[i], "f", p1, p2, p3, i1, i + 5)

        for j in range(4):
            f_errs[j] += temp_errs[j]

    res = [f"Coefficients: {p1}, {p2}, {p3}", m_errs, f_errs]

    return res


def analyzer(path, speaker_gender, p1, p2, p3, i1, i2):
    files = listdir(path=path)

    n = len(files)
    errs = [0 for _ in range(4)]

    for i in range(n):
        r1, r2, r3 = global_result(path + str(files[i]), p1, p2, p3)

        print(f"Progress ({i1 + 1}/11)({i2 + 1}/10)({i + 1}/{n})")

        if speaker_gender == "m":
            if r1 == -1:
                errs[0] += 1
            if r2 == -1:
                errs[1] += 1
            if r3 == -1:
                errs[2] += 1
            if r1 + r2 + r3 < 0:
                errs[3] += 1
        elif speaker_gender == "f":
            if r1 == 1:
                errs[0] += 1
            if r2 == 1:
                errs[1] += 1
            if r3 == 1:
                errs[2] += 1
            if r1 + r2 + r3 > 0:
                errs[3] += 1

    return errs


mfccs_crit = 11
per_cri = -7.5
Xdb_crit = 168

fin_res = [[] for _ in range(11)]

for i in range(11):
    mfccs_crit += 1
    per_cri += 0.5
    Xdb_crit += 2

    fin_res[i] = data_analyzer(mfccs_crit, per_cri, Xdb_crit, i)

with open("results.txt", mode="w", encoding="utf-8") as file:
    for i in range(11):
        for j in range(3):
            if type(fin_res[i][j]) == type([]):
                for k in range(4):
                    file.write(str(fin_res[i][j][k]) + " ")
                file.write("\n")
            else:
                file.write(str(fin_res[i][j]) + "\n")
        file.write("\n")

print("Результаты анализа сохранены")


end = time.time() - start

print(end)
