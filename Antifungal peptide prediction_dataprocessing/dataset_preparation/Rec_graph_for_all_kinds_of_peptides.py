# -*- coding: utf-8 -*-
import operator
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
neg_all = {}
pos_all = {}
with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\neg_test_ds1.txt") as neg_1, open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\neg_train_ds1.txt") as neg_2, open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\pos_test_ds1.txt") as pos_1, open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\pos_train_ds1.txt") as pos_2:
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
print(neg_all)
print(pos_all)
pos_peptide_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 #1-10, #11-20, #21-30, #31-40, #41-50, #51-60, #61-70, #71-80, #81-90, #91-100
for item in pos_all.keys():
    if pos_all[item] <= 10 & pos_all[item] >=1:
        pos_peptide_number[0] = pos_peptide_number[0] + 1
    elif pos_all[item] <= 20 & pos_all[item] >=11:
        pos_peptide_number[1] = pos_peptide_number[1] + 1
    elif pos_all[item] <= 30 & pos_all[item] >=21:
        pos_peptide_number[2] = pos_peptide_number[2] + 1
    elif pos_all[item] <= 40 & pos_all[item] >=31:
        pos_peptide_number[3] = pos_peptide_number[3] + 1
    elif pos_all[item] <= 50 & pos_all[item] >=41:
        pos_peptide_number[4] = pos_peptide_number[4] + 1
    elif pos_all[item] <= 60 & pos_all[item] >=51:
        pos_peptide_number[5] = pos_peptide_number[5] + 1
    elif pos_all[item] <= 70 & pos_all[item] >=61:
        pos_peptide_number[6] = pos_peptide_number[6] + 1
    elif pos_all[item] <= 80 & pos_all[item] >=71:
        pos_peptide_number[7] = pos_peptide_number[7] + 1
    elif pos_all[item] <= 90 & pos_all[item] >=81:
        pos_peptide_number[8] = pos_peptide_number[8] + 1
    elif pos_all[item] <= 100 & pos_all[item] >=91:
        pos_peptide_number[9] = pos_peptide_number[9] + 1
print(pos_peptide_number)

neg_peptide_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 #1-10, #11-20, #21-30, #31-40, #41-50, #51-60, #61-70, #71-80, #81-90, #91-100
for item in neg_all.keys():
    if neg_all[item] <= 10 & neg_all[item] >=1:
        neg_peptide_number[0] = neg_peptide_number[0] + 1
    elif neg_all[item] <= 20 & neg_all[item] >=11:
        neg_peptide_number[1] = neg_peptide_number[1] + 1
    elif neg_all[item] <= 30 & neg_all[item] >=21:
        neg_peptide_number[2] = neg_peptide_number[2] + 1
    elif neg_all[item] <= 40 & neg_all[item] >=31:
        neg_peptide_number[3] = neg_peptide_number[3] + 1
    elif neg_all[item] <= 50 & neg_all[item] >=41:
        neg_peptide_number[4] = neg_peptide_number[4] + 1
    elif neg_all[item] <= 60 & neg_all[item] >=51:
        neg_peptide_number[5] = neg_peptide_number[5] + 1
    elif neg_all[item] <= 70 & neg_all[item] >=61:
        neg_peptide_number[6] = neg_peptide_number[6] + 1
    elif neg_all[item] <= 80 & neg_all[item] >=71:
        neg_peptide_number[7] = neg_peptide_number[7] + 1
    elif neg_all[item] <= 90 & neg_all[item] >=81:
        neg_peptide_number[8] = neg_peptide_number[8] + 1
    elif neg_all[item] <= 100 & neg_all[item] >=91:
        neg_peptide_number[9] = neg_peptide_number[9] + 1
print(neg_peptide_number)

font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
plt.bar([2.5, 12.5, 22.5, 32.5, 42.5, 52.5, 62.5, 72.5, 82.5, 92.5], pos_peptide_number, label='pos_peptide_numbers', width=4)
plt.bar([7.5, 17.5, 27.5, 37.5, 47.5, 57.5, 67.5, 77.5, 87.5, 97.5], neg_peptide_number, label='neg_peptide_numbers', width=4)
plt.legend()
plt.xlabel('range(each 10)')
plt.ylabel('numbers')
plt.title(u'peptide_numbers', FontProperties=font)
plt.show()

