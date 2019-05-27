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

    # get all positive peptides into one single file
    for line in pos_1:
        line = line[0:-1]
        line_length = len(line)
        pos_all[line] = line_length
    for line in pos_2:
        line = line[0:-1]
        line_length= len(line)
        pos_all[line] = line_length

    neg_all = dict(sorted(neg_all.items(), key=operator.itemgetter(1)))
    pos_all = dict(sorted(pos_all.items(), key=operator.itemgetter(1)))

# print(str(len(neg_all)))
print(neg_all)
# print(str(len(pos_all)))
print(pos_all)

peptide_number = [0] * 101
for item in neg_all.keys():
    peptide_number[neg_all[item]] = peptide_number[neg_all[item]] + 1
print(peptide_number)

index = range(101)
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
plt.bar(index, peptide_number, label='peptide_numbers', width=0.5)
plt.legend()
plt.xlabel('length_range')
plt.ylabel('numbers')
plt.title(u'neg_peptide_length/number', FontProperties=font)
plt.show()

# peptide_number = [0] * 101
# for item in pos_all.keys():
#     peptide_number[pos_all[item]] = peptide_number[pos_all[item]] + 1
# print(peptide_number)
#
# index = range(101)
# font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
# plt.bar(index, peptide_number, label='peptide_numbers', width=0.5)
# plt.legend()
# plt.xlabel('length_range')
# plt.ylabel('numbers')
# plt.title(u'pos_peptide_length/number', FontProperties=font)
# plt.show()