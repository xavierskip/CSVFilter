#!/usr/bin/env python3
# coding:utf-8
import argparse
from csvfilter import run

parser = argparse.ArgumentParser()
parser.add_argument("names", help="名字csv文件")
parser.add_argument("cards", help="卡片csv文件")
parser.add_argument("-c", "--column", type=int,
                    default=4, help="名字所在的列数")
parser.add_argument("-k", "--sample", type=int,
                    default=0,help="抽样数目")
parser.add_argument("-o", "--output", default='结果.csv',
                    help="输出结果的文件")
args = parser.parse_args()
run(
    args.names,
    args.cards,
    args.column,
    args.output,
    args.sample
)
