import operator

# Prepare data-set (divide the dataset equally into 6 parts, 50% positive 50% negative is the best) into 6 parts, 5 for
# training and 1 for validation

#训练数据格式
# 名字
# 长度
# 序列
# 是否抗真菌 1-0

#read four files of peptides
neg_all = {}
pos_all = {}
with open(r"C:\Users\Administra tor\PycharmProjects\Antifungal peptide prediction\neg_test_ds1.txt") as neg_1, open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\neg_train_ds1.txt") as neg_2, open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\pos_test_ds1.txt") as pos_1, open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\pos_train_ds1.txt") as pos_2:
    # get all negative peptides into one single file
    for line in neg_1:
        line = line[0:-1]
        line_length = len(line)
        neg_all[line] = line_length
    for line in neg_2:
        line = line[0:-1]
        line_length = len(line)
        neg_all[line] = line_length
    neg_all = dict(sorted(neg_all.items(), key=operator.itemgetter(1)))

    # get all positive peptides into one single file
    for line in pos_1:
        line = line[0:-1]
        line_length = len(line)
        pos_all[line] = line_length
    for line in pos_2:
        line = line[0:-1]
        line_length= len(line)
        pos_all[line] = line_length
    pos_all = dict(sorted(pos_all.items(), key=operator.itemgetter(1)))

#divide the data-set equally into 6 parts

with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_1.txt", "w") as train_1, open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_2.txt", "w") as train_2, open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_3.txt", "w") as train_3,\
    open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_4.txt", "w") as train_4, open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_5.txt", "w") as train_5, open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\validation\test_0.txt", "w") as test_1:
    k = 1
    k1 = 1
    k2 = 1
    k3 = 1
    k4 = 1
    k5 = 1
    k6 = 1
    for item in pos_all.keys():
        # put into train_1 set
        if k % 6 == 1:
            train_1.write("train_1_pos_peptide_" + str(k1) + "\n")  # peptide name
            train_1.write(str(pos_all[item]) + "\n")   # peptide length
            train_1.write(item + "\n")  # peptide sequence
            train_1.write(str(1) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k1 = k1 + 1

        # put into train_2 set
        if k % 6 == 2:
            train_2.write("train_2_pos_peptide_" + str(k2) + "\n")  # peptide name
            train_2.write(str(pos_all[item]) + "\n")  # peptide length
            train_2.write(item + "\n")  # peptide sequence
            train_2.write(str(1) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k2 = k2 + 1

        # put into train_3 set
        if k % 6 == 3:
            train_3.write("train_3_pos_peptide_" + str(k3) + "\n")  # peptide name
            train_3.write(str(pos_all[item]) + "\n")  # peptide length
            train_3.write(item + "\n")  # peptide sequence
            train_3.write(str(1) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k3 = k3 + 1

        # put into train_4 set
        if k % 6 == 4:
            train_4.write("train_4_pos_peptide_" + str(k4) + "\n")  # peptide name
            train_4.write(str(pos_all[item]) + "\n")  # peptide length
            train_4.write(item + "\n")  # peptide sequence
            train_4.write(str(1) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k4 = k4 + 1

        # put into train_5 set
        if k % 6 == 5:
            train_5.write("train_5_pos_peptide_" + str(k5) + "\n")  # peptide name
            train_5.write(str(pos_all[item]) + "\n")  # peptide length
            train_5.write(item + "\n")  # peptide sequence
            train_5.write(str(1) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k5 = k5 + 1

        # put into train_3 set
        if k % 6 == 0:
            test_1.write("train_0_pos__peptide_" + str(k6) + "\n")  # peptide name
            test_1.write(str(pos_all[item]) + "\n")  # peptide length
            test_1.write(item + "\n")  # peptide sequence
            test_1.write(str(1) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k6 = k6 + 1
        k = k +1

    for item in neg_all.keys():
        # put into train_1 set
        if k % 6 == 1:
            train_1.write("train_1_neg_peptide_" + str(k1) + "\n")  # peptide name
            train_1.write(str(neg_all[item]) + "\n")  # peptide length
            train_1.write(item + "\n")  # peptide sequence
            train_1.write(str(2) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k1 = k1 + 1

        # put into train_2 set
        if k % 6 == 2:
            train_2.write("train_2_neg_peptide_" + str(k2) + "\n")  # peptide name
            train_2.write(str(neg_all[item]) + "\n")  # peptide length
            train_2.write(item + "\n")  # peptide sequence
            train_2.write(str(2) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k2 = k2 + 1

        # put into train_3 set
        if k % 6 == 3:
            train_3.write("train_3_neg_peptide_" + str(k3) + "\n")  # peptide name
            train_3.write(str(neg_all[item]) + "\n")  # peptide length
            train_3.write(item + "\n")  # peptide sequence
            train_3.write(str(2) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k3 = k3 + 1

        # put into train_4 set
        if k % 6 == 4:
            train_4.write("train_4_neg_peptide_" + str(k4) + "\n")  # peptide name
            train_4.write(str(neg_all[item]) + "\n")  # peptide length
            train_4.write(item + "\n")  # peptide sequence
            train_4.write(str(2) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k4 = k4 + 1

        # put into train_5 set
        if k % 6 == 5:
            train_5.write("train_5_neg_peptide_" + str(k5) + "\n")  # peptide name
            train_5.write(str(neg_all[item]) + "\n")  # peptide length
            train_5.write(item + "\n")  # peptide sequence
            train_5.write(str(2) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k5 = k5 + 1

        # put into train_3 set
        if k % 6 == 0:
            test_1.write("train_0_neg_peptide_" + str(k6) + "\n")  # peptide name
            test_1.write(str(neg_all[item]) + "\n")  # peptide length
            test_1.write(item + "\n")  # peptide sequence
            test_1.write(str(2) + "\n")  # if anti-fungal peptide, if it is then 1, else 0
            k6 = k6 + 1
        k = k + 1