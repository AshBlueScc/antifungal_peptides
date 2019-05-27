# exclude the dataset called test.dataset there are five datasets
# each time we choose three of the five datasets used as train datasets
# the rest two of them, on is used as test dataset, another is used as validation dataset
# so we can get five times to train the model

with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_1.txt", "r") as train_1, \
open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_2.txt", "r") as train_2, \
open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_3.txt", "r") as train_3,\
open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_4.txt", "r") as train_4, \
open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets\main\train_5.txt", "r") as train_5:
    with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_1\test.dataset", "w") as test, \
            open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_1\train.dataset", "a+") as train, \
            open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_1\validation.dataset", "w") as validation:
        #train_1 as validation data-set, train_2 as test data-set, the rest three as train data-set
        validation.write(str(487) + "\n")
        for line in train_1:
            validation.write(line)
        test.write(str(487) + "\n")
        for line in train_2:
            test.write(line)
        # 486*3
        train.write(str(1458) + "\n")
        for line in train_3:
            train.write(line)
        for line in train_4:
            train.write(line)
        for line in train_5:
            train.write(line)
    with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_2\test.dataset",
              "w") as test, \
            open(
                r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_2\train.dataset",
                "a+") as train, \
            open(
                r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_2\validation.dataset",
                "w") as validation:
        # train_2 as validation data-set, train_3 as test data-set, the rest three as train data-set
        validation.write(str(487) + "\n")
        train_2.seek(0)
        for line in train_2:
            validation.write(line)
        test.write(str(486) + "\n")
        train_3.seek(0)
        for line in train_3:
            test.write(line)
        # 486*2+487
        train.write(str(1459) + "\n")
        train_4.seek(0)
        for line in train_4:
            train.write(line)
        train_5.seek(0)
        for line in train_5:
            train.write(line)
        train_1.seek(0)
        for line in train_1:
            train.write(line)
    with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_3\test.dataset",
              "w") as test, \
            open(
                r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_3\train.dataset",
                "a+") as train, \
            open(
                r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_3\validation.dataset",
                "w") as validation:
        # train_3 as validation data-set, train_4 as test data-set, the rest three as train data-set
        validation.write(str(486) + "\n")
        train_3.seek(0)
        for line in train_3:
            validation.write(line)
        test.write(str(486) + "\n")
        train_4.seek(0);
        for line in train_4:
            test.write(line)
        # 486+487*2
        train.write(str(1460) + "\n")
        train_5.seek(0)
        for line in train_5:
            train.write(line)
        train_1.seek(0)
        for line in train_1:
            train.write(line)
        train_2.seek(0)
        for line in train_2:
            train.write(line)
    with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_4\test.dataset",
              "w") as test, \
            open(
                r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_4\train.dataset",
                "a+") as train, \
            open(
                r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_4\validation.dataset",
                "w") as validation:
        # train_4 as validation data-set, train_5 as test data-set, the rest three as train data-set
        validation.write(str(486) + "\n")
        train_4.seek(0)
        for line in train_4:
            validation.write(line)
        test.write(str(486) + "\n")
        train_5.seek(0)
        for line in train_5:
            test.write(line)
        # 486+487*2
        train.write(str(1460) + "\n")
        train_1.seek(0)
        for line in train_1:
            train.write(line)
        train_2.seek(0)
        for line in train_2:
            train.write(line)
        train_3.seek(0)
        for line in train_3:
            train.write(line)
    with open(r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_5\test.dataset",
              "w") as test, \
            open(
                r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_5\train.dataset",
                "a+") as train, \
            open(
                r"C:\Users\Administrator\PycharmProjects\Antifungal peptide prediction\datasets2\folder_5\validation.dataset",
                "w") as validation:
        # train_5 as validation data-set, train_1 as test data-set, the rest three as train data-set
        validation.write(str(486) + "\n")
        train_5.seek(0)
        for line in train_5:
            validation.write(line)
        test.write(str(487) + "\n")
        train_1.seek(0)
        for line in train_1:
            test.write(line)
        # 486*2+487
        train.write(str(1459) + "\n")
        train_2.seek(0)
        for line in train_2:
            train.write(line)
        train_3.seek(0)
        for line in train_3:
            train.write(line)
        train_4.seek(0)
        for line in train_4:
            train.write(line)