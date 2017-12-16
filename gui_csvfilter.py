#!/usr/bin/env python3
# coding:utf-8
from gooey import Gooey, GooeyParser
from csvfilter import run
from csvfilter import __doc__ as usage


@Gooey(
    program_name='抽卡',
    language='chinese',
)
def main():
    parser = GooeyParser(description=usage)
    parser.add_argument("names", help="名字csv文件", widget='FileChooser')
    parser.add_argument("cards", help="卡片csv文件", widget='FileChooser')
    parser.add_argument("-c", "--column", type=int,
                        default=4, help="名字所在的列数")
    parser.add_argument("-o", "--output", default='结果.csv',
                        help="输出结果的文件", widget="FileSaver")
    args = parser.parse_args()
    run(
        args.names,
        args.cards,
        args.column,
        args.output
    )


if __name__ == '__main__':
    # issue: https://github.com/chriskiehl/Gooey/issues/230
    # hack: https://stackoverflow.com/a/3597849/1265727
    # import os
    # import sys
    # utf8_stdout = os.fdopen(sys.stdout.fileno(), mode='w', encoding='utf-8', closefd=False)
    # sys.stdout = utf8_stdout
    main()
