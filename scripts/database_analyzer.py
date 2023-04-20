from os import listdir

from audio_func import half_result


def data_analyzer(data):

    for gender in range(len(data)):
        k1 = []
        k2 = []
        k3 = []

        for path_num in range(len(data[gender])):
            path = data[gender][path_num]
            files = listdir(path=path)

            for cur_file in range(len(files)):
                r1, r2, r3 = half_result(path + files[cur_file])

                k1.append(str(r1) + "\n")
                k2.append(str(r2) + "\n")
                k3.append(str(r3) + "\n")

                print(f"Progress: ({gender + 1}/2)({path_num + 1}/{len(data[gender])})({cur_file + 1}/{len(files)})")

        with open(f"results_{gender + 1}_1.txt", mode="w", encoding="utf-8") as rec_file:
            rec_file.writelines(k1)

        with open(f"results_{gender + 1}_2.txt", mode="w", encoding="utf-8") as rec_file:
            rec_file.writelines(k2)

        with open(f"results_{gender + 1}_3.txt", mode="w", encoding="utf-8") as rec_file:
            rec_file.writelines(k3)


def analyzer(k1, k2, k3):


analyze_files = True

data = [["D:/ruls_data/train/audio/8086/7771/", "D:/ruls_data/train/audio/8169/12256/",
         "D:/ruls_data/test/audio/2826/2145/", "D:/ruls_data/test/audio/4471/2145/",
         "D:/ruls_data/test/audio/4372/2145/", "D:/ruls_data/my/male/"],
        ["D:/ruls_data/train/audio/9014/11018/", "D:/ruls_data/train/audio/9014/8641/",
         "D:/ruls_data/test/audio/2671/2145/", "D:/ruls_data/test/audio/3056/2145/",
         "D:/ruls_data/dev/audio/5397/2145/", "D:/ruls_data/test/audio/5548/2145/",
         "D:/ruls_data/test/audio/4091/2145/", "D:/ruls_data/my/female/"]]

if analyze_files:
    data_analyzer(data)


analyze_results = False

mfccs_crit = 6
step_mfccs_crit = 1

per_cri = -11
step_per_cri = 0.5

xdb_crit = 158
step_xdb_crit = 2

if analyze_results:
    for i in range(21):
        mfccs_crit += step_mfccs_crit
        per_cri += step_per_cri
        xdb_crit += step_xdb_crit

        analyzer(mfccs_crit, per_cri, xdb_crit)
