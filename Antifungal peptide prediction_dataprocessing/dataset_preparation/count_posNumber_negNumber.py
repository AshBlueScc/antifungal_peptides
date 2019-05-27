# count the number of positive and negative peptides
with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_1.txt") as train_1,\
    open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_2.txt") as train_2,\
    open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_3.txt") as train_3,\
    open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_4.txt") as train_4,\
    open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_5.txt") as train_5,\
    open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\validation\test_1.txt") as test_1:
    pos_1 = 0
    neg_1 = 0
    for line in train_1:
        line = line[0:-1]
        if len(line) == 1 and int(line) == 1:
            pos_1 = pos_1+1
        if len(line) == 1 and int(line) == 0:
            neg_1 = neg_1 + 1
    print("pos_1:" + str(pos_1))
    print("neg_1:" + str(neg_1))

    pos_2 = 0
    neg_2 = 0
    for line in train_2:
        line = line[0:-1]
        if len(line) == 1 and int(line) == 1:
            pos_2 = pos_2 + 1
        if len(line) == 1 and int(line) == 0:
            neg_2 = neg_2 + 1
    print("pos_2:" + str(pos_2))
    print("neg_2:" + str(neg_2))

    pos_3 = 0
    neg_3 = 0
    for line in train_3:
        line = line[0:-1]
        if len(line) == 1 and int(line) == 1:
            pos_3 = pos_3 + 1
        if len(line) == 1 and int(line) == 0:
            neg_3 = neg_3 + 1
    print("pos_3:" + str(pos_3))
    print("neg_3:" + str(neg_3))

    pos_4 = 0
    neg_4 = 0
    for line in train_4:
        line = line[0:-1]
        if len(line) == 1 and int(line) == 1:
            pos_4 = pos_4 + 1
        if len(line) == 1 and int(line) == 0:
            neg_4 = neg_4 + 1
    print("pos_4:" + str(pos_4))
    print("neg_4:" + str(neg_4))

    pos_5 = 0
    neg_5 = 0
    for line in train_5:
        line = line[0:-1]
        if len(line) == 1 and int(line) == 1:
            pos_5 = pos_5 + 1
        if len(line) == 1 and int(line) == 0:
            neg_5 = neg_5 + 1
    print("pos_5:" + str(pos_5))
    print("neg_5:" + str(neg_5))

    test_pos_1 = 0
    test_neg_1 = 0
    for line in test_1:
        line = line[0:-1]
        if len(line) == 1 and int(line) == 1:
            test_pos_1 = test_pos_1 + 1
        if len(line) == 1 and int(line) == 0:
            test_neg_1 = test_neg_1 + 1
    print("test_pos_1:" + str(test_pos_1))
    print("test_neg_1:" + str(test_neg_1))