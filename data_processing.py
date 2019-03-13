import os
import csv
import numpy as np


def get_line(file_path):
    f = open(file_path, 'r', errors='ignore', encoding='GB2312')
    line = f.readline()
    line = line.strip('\n')

    line.encode("utf-8")

    f.close()
    return line


if __name__ == '__main__':
    root_dir = 'data/2000/'
    folders = ['neg/', 'pos/']

    output_path = 'data/'

    train_path = output_path + 'train.tsv'
    train = open(train_path, 'w', encoding='utf-8', newline='')
    train_writer = csv.writer(train, delimiter='\t')

    dev_path = output_path + 'dev.tsv'
    dev = open(dev_path, 'w', encoding='utf-8', newline='')
    dev_writer = csv.writer(dev, delimiter='\t')

    test_path = output_path + 'test.tsv'
    test = open(test_path, 'w', encoding='utf-8', newline='')
    test_writer = csv.writer(test, delimiter='\t')

    length_list = []

    for folder in folders:
        input_path = root_dir + folder

        i = 0

        for parent, directories, files in os.walk(input_path):

            file_count = len(files)
            print(file_count)

            for file in files:
                content = get_line(input_path + file)
                length_list.append(len(content))

                if i < int(file_count*0.8):
                    train_writer.writerow([content, folder])
                elif int(file_count*0.8) <= i < int(file_count*0.9):
                    dev_writer.writerow([content, folder])
                else:
                    test_writer.writerow([content, folder])

                i = i + 1

    train.close()
    dev.close()
    test.close()

    print(np.max(length_list))
    print(np.mean(length_list))



