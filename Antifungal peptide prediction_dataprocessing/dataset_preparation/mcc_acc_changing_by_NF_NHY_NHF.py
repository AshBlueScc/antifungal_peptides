import matplotlib.pyplot as plt

NF_NHY_NHF = [5, 7, 9, 11, 13, 15]

axis_fold1_mcc = [0.549244, 0.571148, 0.606798, 0.577033, 0.552596, 0.576364]
axis_fold1_acc = [77.0021, 78.0287, 80.2875, 78.8501, 77.0021, 78.4394]

axis_fold2_mcc = [0.592598, 0.576723, 0.534411, 0.596708, 0.593442, 0.547685]
axis_fold2_acc = [79.6296, 78.8066, 76.3374, 79.8354, 79.6296, 77.1605]

axis_fold3_mcc = [0.588657, 0.580326, 0.646288, 0.576254, 0.630999, 0.584486]
axis_fold3_acc = [79.4239, 79.0123, 80.3045, 78.8066, 81.4815, 79.2181]

axis_fold4_mcc = [0.57326, 0.530882, 0.523982, 0.586557, 0.594048, 0.531513]
axis_fold4_acc = [78.6008, 76.5432, 75.9259, 79.2181, 79.6296, 76.5432]

axis_fold5_mcc = [0.60834, 0.585464, 0.610442, 0.646049, 0.587922, 0.601677]
axis_fold5_acc = [79.8768, 79.0554, 80.4928, 82.1355, 79.2608, 80.0821]

axis_fold6_mcc = [0.58242, 0.568909, 0.584384, 0.59652, 0.591801, 0.568345]
axis_fold6_acc = [78.90664, 78.28924, 78.66962, 79.76914, 79.40072, 78.28866]

# plt.plot(NF_NHY_NHF, axis_fold1_mcc, label="$fold1-mcc$", color="red", linewidth=1)
# plt.plot(NF_NHY_NHF, axis_fold2_mcc, label="$fold2-mcc$", color="green", linewidth=1)
# plt.plot(NF_NHY_NHF, axis_fold3_mcc, label="$fold3-mcc$", color="gold", linewidth=1)
# plt.plot(NF_NHY_NHF, axis_fold4_mcc, label="$fold4-mcc$", color="magenta", linewidth=1)
# plt.plot(NF_NHY_NHF, axis_fold5_mcc, label="$fold5-mcc$", color="aqua", linewidth=1)
# plt.plot(NF_NHY_NHF, axis_fold6_mcc, label="$average-mcc$", color="purple", linewidth=1)
# plt.xlabel("NF_NHY_NHF")
# plt.ylabel("mcc")
# plt.title("mcc changing by NF_NHY_NHF")
# plt.ylim(0.5, 0.7)
# plt.legend()
# plt.show()

plt.plot(NF_NHY_NHF, axis_fold1_acc, label="$fold1-acc$", color="red", linewidth=1)
plt.plot(NF_NHY_NHF, axis_fold2_acc, label="$fold2-acc$", color="green", linewidth=1)
plt.plot(NF_NHY_NHF, axis_fold3_acc, label="$fold3-acc$", color="gold", linewidth=1)
plt.plot(NF_NHY_NHF, axis_fold4_acc, label="$fold4-acc$", color="magenta", linewidth=1)
plt.plot(NF_NHY_NHF, axis_fold5_acc, label="$fold5-acc$", color="aqua", linewidth=1)
plt.plot(NF_NHY_NHF, axis_fold6_acc, label="$average-acc$", color="purple", linewidth=1)
plt.xlabel("NF_NHY_NHF")
plt.ylabel("acc")
plt.title("acc changing by NF_NHY_NHF")
plt.ylim(75, 85)
plt.legend()
plt.show()