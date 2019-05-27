import matplotlib.pyplot as plt
with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\Roc\ITS.dataset.predictions") as its:
    max = int(its.readline())
    tr_pos = 0
    fl_pos = 0
    tr_neg = 0
    fl_neg = 0
    Num= [i for i in range(1, max+1)]
    for line in its:
        temp=[]
        if line[-1]=='\n':
            line=line[0:-1]
        line = line.split(" ")
        if len(line) == 2 and (line[0] == "1" or line[0] == "2"):
            if line[0]=="1" and line[1]=="1":
                tr_pos=tr_pos + 1
            if line[0]=="1" and line[1]=="2":
                fl_neg=fl_neg + 1
            if line[0]=="2" and line[1]=="2":
                tr_neg=tr_neg + 1
            if line[0]=="2" and line[1]=="1":
                fl_pos=fl_pos + 1
print(str(tr_pos) + " " + str(fl_neg) + " " + str(tr_neg) + " " + str(fl_pos))
