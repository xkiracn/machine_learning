# -*- coding: utf-8 -*-
u"""Implementation of KFold."""

import copy


def kfold(datas, n_splits=10):
    def split_data(datas, idx, counts):
        target = []
        for i in range(counts):
            target.append(datas.pop(idx))
        return datas, target

    if not isinstance(datas, list):
        raise(ValueError("Incorrect arguments: datas."))
    if len(datas) < n_splits:
        raise(ValueError("n_splits grater than number of datas."))

    step = len(datas) // n_splits
    remain = len(datas) % n_splits
    idx = 0
    while idx < len(datas):
        counts = step
        if remain > 0:
            counts += 1
            remain -= 1
        data_x, data_y = split_data(copy.copy(datas), idx, counts)
        yield data_x, data_y
        idx += counts


def main():
    datas = list(range(24))
    for x, y in kfold(datas, 10):
        print x, y

if __name__ == '__main__':
    main()
