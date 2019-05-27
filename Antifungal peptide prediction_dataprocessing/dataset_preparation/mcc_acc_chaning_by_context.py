import matplotlib.pyplot as plt

axis_context = [11, 13, 15, 17, 19, 21]

axis_fold1_mcc = [0.593996, 0.542774, 0.558278, 0.586004, 0.626887, 0.585583]
axis_fold1_acc = [79.6715, 77.0021, 77.8234, 79.2608, 81.3142, 79.2608]

axis_fold2_mcc = [0.57873, 0.576254, 0.580739, 0.568739, 0.606998, 0.608701]
axis_fold2_acc = [78.8066, 78.8066, 79.0123, 78.1893, 80.2469, 79.8354]

axis_fold3_mcc = [0.604028, 0.559789, 0.572968, 0.609927, 0.609927, 0.605773]
axis_fold3_acc = [80.0412, 77.9835, 78.6008, 80.4527, 80.4527, 80.0412]

axis_fold4_mcc = [0.555556, 0.622158, 0.63375, 0.573592, 0.587479, 0.551445]
axis_fold4_acc = [77.7778, 81.07, 81.6872, 78.6008, 79.2181, 77.572]

axis_fold5_mcc = [0.578832, 0.516195, 0.593429, 0.605952, 0.618301, 0.62629]
axis_fold5_acc = [78.8501, 75.77, 79.6715, 80.2875, 80.9035, 81.3142]

axis_fold6_mcc = [0.582228, 0.563434, 0.587833, 0.588843, 0.609918, 0.595558]
axis_fold6_acc = [79.02944, 78.12644, 79.35904, 79.35822, 80.42708, 79.60472]

# plt.plot(axis_context, axis_fold1_mcc, label="$fold1-mcc$", color="red", linewidth=1)
# plt.plot(axis_context, axis_fold2_mcc, label="$fold2-mcc$", color="green", linewidth=1)
# plt.plot(axis_context, axis_fold3_mcc, label="$fold3-mcc$", color="gold", linewidth=1)
# plt.plot(axis_context, axis_fold4_mcc, label="$fold4-mcc$", color="magenta", linewidth=1)
# plt.plot(axis_context, axis_fold5_mcc, label="$fold5-mcc$", color="aqua", linewidth=1)
# plt.plot(axis_context, axis_fold6_mcc, label="$average-mcc$", color="purple", linewidth=1)
# plt.xlabel("Context")
# plt.ylabel("mcc")
# plt.title("mcc changing by context")
# plt.ylim(0.5, 0.7)
# plt.legend()
# plt.show()

plt.plot(axis_context, axis_fold1_acc, label="$fold1-acc$", color="red", linewidth=1)
plt.plot(axis_context, axis_fold2_acc, label="$fold2-acc$", color="green", linewidth=1)
plt.plot(axis_context, axis_fold3_acc, label="$fold3-acc$", color="gold", linewidth=1)
plt.plot(axis_context, axis_fold4_acc, label="$fold4-acc$", color="magenta", linewidth=1)
plt.plot(axis_context, axis_fold5_acc, label="$fold5-acc$", color="aqua", linewidth=1)
plt.plot(axis_context, axis_fold6_acc, label="$average-acc$", color="purple", linewidth=1)
plt.xlabel("Context")
plt.ylabel("acc")
plt.title("acc changing by context")
plt.ylim(75, 85)
plt.legend()
plt.show()