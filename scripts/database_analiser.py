from os import listdir

from audio_func import global_result


def data_analyzer(p1, p2, p3):
    m_err = 0
    f_err = 0

    analyzer("G:\ruls_data\train\audio\9014\11018")


def analyzer(path, speaker_gender):
    n = len(self.file_ch_res)
    res = ["" for i in range(n)]

    for i in range(n):
        p_res = global_result(self.file_ch_res[i])

        if p_res[0].lower() == self.file_ch_res[i][self.file_ch_res[i].rfind("/") + 1]:
            res[i] = p_res + self.file_ch_res[i] + "\n"
        else:
            res[i] = p_res + "(err) - " + self.file_ch_res[i] + "\n"

        print(str(i + 1) + "/" + str(n))

    with open(self.path_ch_res + "/results.txt", mode="w", encoding="utf-8") as file:
        for i in range(n):
            file.write(res[i])


mfccs_crit = 11
per_cri = -7.5
Xdb_crit = 168


for i in range(11):
    mfccs_crit += 1
    per_cri += 0.5
    Xdb_crit += 2

    data_analyzer(mfccs_crit, per_cri, Xdb_crit)


#with open("results.txt", mode="w", encoding="utf-8") as file:
#    for i in range(n):
#        file.write(res[i])