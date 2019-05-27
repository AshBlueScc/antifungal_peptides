import matplotlib.pyplot as plt
with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\Roc\ITS.dataset.predictions") as its:
    max = int(its.readline())
    k=0
    Num= [i for i in range(1, max+1)]
    for line in its:
        temp = []
        if line[-1] == '\n':
            line = line[0:-1]
        line = line.split(" ")
        if len(line) == 2 and (line[0] =="1" or line[0] =="2"):
            temp.append(str(int(line[0])-1))
            line = its.readline()
            if line[-1] == '\n':
                line = line[0:-1]
            line = line.split(" ")
            temp.append(line[0])
            Num[k] = temp
            k = k + 1
print(Num)
k = 1
with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\Roc\ITS.result", "w") as res:
    res.write("Num Obs Pred\n")
    for list in Num:
        res.write(str(k) + " " + list[0] + " " + list[1] + "\n")
        k = k + 1
fs_p = []
tr_p = []
pos_all = 0
neg_all = 0
Num = sorted(Num, key=lambda x:x[1], reverse=True)
for list in Num:
    if list[0] == "0":
        pos_all = pos_all + 1
    else:
        neg_all = neg_all + 1
pos = 0
neg = 0
for list in Num:
    if list[0] == "0":
        pos = pos +  1
    else:
        neg = neg + 1
    true_positive = pos/pos_all
    fasle_postive = neg/neg_all
    tr_p.append(true_positive)
    fs_p.append(fasle_postive)

area = 0
pre_x = 0
for i in range(0, len(tr_p)):
    area = area + tr_p[i]*(fs_p[i]-pre_x)
    pre_x = fs_p[i]
print(area)

plt.plot(fs_p, tr_p, color="red", linewidth=1)
plt.plot([0,1], [0,1],color="blue", linewidth=1)
plt.xlabel("False Positive Rate")
plt.ylabel("True positive Rate")
plt.title("ROC(AUC = " + str(area) + ")")
# plt.ylim(0, 1)
# plt.xlim(0, 1)
plt.legend()
plt.show()
