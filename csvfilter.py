#!/usr/bin/env python3
# coding:utf-8
"""项目地址:https://coding.net/u/skipto/p/CSVFilter
使用注意事项：
列数的计数从0开始
"""
import csv
from collections import defaultdict

def names_list(csvfile):
    with open(csvfile, encoding="GBK") as fp:
        csvreader = csv.reader(fp)
        namelist = [''.join(row) for row in csvreader]
    return namelist

def cards_list(csvfile):
    with open(csvfile, encoding="GBK") as fp:
        csvreader = csv.reader(fp)
        cardslist = [row for row in csvreader]
    return cardslist  # 标题行去除？

def run(namesfile, cardsfile, columnfilter, outputfile):
    names = names_list(namesfile)
    cards = cards_list(cardsfile)
    print("{}\n读取{}个名字".format(','.join(names), len(names)))

    name_index = defaultdict(list)
    for i,card in enumerate(cards):
        name = card[columnfilter]
        if name in names:
            name_index[name].append(i)

    for name in names:
        idxs = name_index[name]
        if idxs:
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