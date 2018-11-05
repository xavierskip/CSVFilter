#!/usr/bin/env python3
# coding:utf-8
"""项目地址:https://coding.net/u/skipto/p/CSVFilter
使用注意事项：
列数的计数从0开始
"""
import csv
import random
from collections import defaultdict

def read_csv_to_list(csvfile, encoding="GBK"):
    with open(csvfile, encoding=encoding) as fp:
        csvreader = csv.reader(fp)
        # 标题行去除？
        return  [row for row in csvreader]

def run(namesfile, cardsfile, columnfilter, outputfile, sample=0):
    # names_samples row[0] is the name for filter
    # names_samples row[1] is the int numbers to choose sample
    # sample = 0 means get all of it,don't sample
    names_samples = read_csv_to_list(namesfile)
    cards = read_csv_to_list(cardsfile)
    names = []
    samples = {}
    for row in names_samples:
        name = row[0]
        names.append(name)
        try:
            # row[1] maybe raise IndexErroe
            samples[name] = int(row[1])
        except IndexError:
            samples[name] = sample
    print("读取{}行".format(len(names)))
    # get the  name index of the cards
    name_index = defaultdict(list)
    for i, card in enumerate(cards):
        name = card[columnfilter]
        if name in names:
            name_index[name].append(i)
    
    for name in names:
        idxs = name_index[name]
        if idxs:
            k = samples[name]
            if k > 0 and k < len(idxs):
                name_index[name] = random.sample(idxs, k)
                print("{:<4}抽取{}个".format(name,k))
            else:  # select all, do not sample
                print("{:<4}在第{}行找到".format(name,
                    ','.join(map(str, idxs)))  # index start with zero
                    )
        else:
            print("{:<4}未找到".format(name))

    with open(outputfile, 'w', newline='') as fp:
        csvwriter = csv.writer(fp, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for name, idxs in name_index.items():
            for i in idxs:
                csvwriter.writerow(cards[i])