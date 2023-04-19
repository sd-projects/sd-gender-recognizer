from os import listdir

from audio_func import global_result


def data_analyzer(p1, p2, p3, i1):
    res = [f"Coefficients: {p1}, {p2}, {p3}",
           analyzer("G:/ruls_data/train/audio/9014/11018/", "f", p1, p2, p3, i1, 1),
           analyzer("G:/ruls_data/train/audio/9014/8641/", "f", p1, p2, p3, i1, 1),
           analyzer("G:/ruls_data/test/audio/2671/2145/", "f", p1, p2, p3, i1, 1),
           analyzer("G:/ruls_data/test/audio/3056/2145/", "f", p1, p2, p3, i1, 1),
           analyzer("G:/ruls_data/dev/audio/5397/2145/", "f", p1, p2, p3, i1, 1),
           analyzer("G:/ruls_data/train/audio/8086/7771/", "m", p1, p2, p3, i1, 1),
           analyzer("G:/ruls_data/train/audio/8169/12256/", "m", p1, p2, p3, i1, 1),
           analyzer("G:/ruls_data/test/audio/2826/2145/", "m", p1, p2, p3, i1, 1),
           analyzer("G:/ruls_data/test/audio/4471/2145/", "m", p1, p2, p3, i1, 1),
           analyzer("G:/ruls_data/test/audio/4372/2145/", "m", p1, p2, p3, i1, 1)]


def analyzer(path, speaker_gender, p1, p2, p3, i1, i2):
    files = listdir(path=path)

    n = len(files)
    m_errs = [0 for _ in range(3)]
    f_errs = [0 for _ in range(3)]

    for i in range(n):
        r1, r2, r3 = global_result(path + str(files[i]), p1, p2, p3)

        print(f"Progress ({i1 + 1}/11)({i2}/10)({i + 1}/{n})")

        if speaker_gender == "m":
            if r1 == -1:
                m_errs[0] += 1
            if r2 == -1:
                m_errs[1] += 1
            if r3 == -1:
                m_errs[2] += 1
        elif speaker_gender == "f":
            if r1 == 1:
                f_errs[0] += 1
            if r2 == 1:
                f_errs[1] += 1
            if r3 == 1:
                f_errs[2] += 1

    errs = [m_errs, f_errs]

    return errs


mfccs_crit = 11
per_cri = -7.5
Xdb_crit = 168

for i in range(11):
    mfccs_crit += 1
    per_cri += 0.5
    Xdb_crit += 2

    data_analyzer(mfccs_crit, per_cri, Xdb_crit, i)

with open("results.txt", mode="w", encoding="utf-8") as file:
    for i in range(n):
       file.write(res[i])
