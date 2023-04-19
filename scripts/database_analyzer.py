from os import listdir

from audio_func import global_result


def data_analyzer(p1, p2, p3, i1):
    m_err = 0
    f_err = 0

    analyzer("G:/ruls_data/train/audio/9014/11018/", "f", p1, p2, p3, i1, 1)
    # G:/ruls_data/train/audio/9014/11018 f1 1271
    # G:\ruls_data\train\audio\9014\8641 f1 1188
    # G:\ruls_data\test\audio\2671\2145 f2 443
    # G:\ruls_data\test\audio\3056\2145 f3 236
    # G:\ruls_data\dev\audio\5397\2145 f4 1400
    # G:\ruls_data\train\audio\8086\7771 m1 3092
    # G:\ruls_data\train\audio\8086\11365 m1 1233
    # G:\ruls_data\train\audio\8169\10422 m2 2180
    # G:\ruls_data\train\audio\8169\12256 m2 2966
    # G:\ruls_data\test\audio\2826\2145 m3 147
    # G:\ruls_data\test\audio\4471\2145 m4 181
    # G:\ruls_data\test\audio\4372\2145 m5 169


def analyzer(path, speaker_gender, p1, p2, p3, i1, i2):
    files = listdir(path=path)

    n = len(files)
    res = ["" for i in range(n)]

    for i in range(n):
        p_res = global_result(self.file_ch_res[i], p1, p2, p3)

        if p_res[0].lower() == self.file_ch_res[i][self.file_ch_res[i].rfind("/") + 1]:
            res[i] = p_res + self.file_ch_res[i] + "\n"
        else:
            res[i] = p_res + "(err) - " + self.file_ch_res[i] + "\n"

        print(str(i + 1) + "/" + str(n))


mfccs_crit = 11
per_cri = -7.5
Xdb_crit = 168

for i in range(11):
    mfccs_crit += 1
    per_cri += 0.5
    Xdb_crit += 2

    data_analyzer(mfccs_crit, per_cri, Xdb_crit, i)

# with open("results.txt", mode="w", encoding="utf-8") as file:
#    for i in range(n):
#        file.write(res[i])
