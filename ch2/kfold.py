# -*- coding: utf-8 -*-
u"""Implementation of KFold."""

import numpy


def kfold(datas, n_splits=10):
    def split_data(datas, idx, counts):
        target = datas[slice(idx, idx + counts)]
        datas = numpy.delete(datas, slice(idx, idx + counts), axis=0)
        return datas, target

    if isinstance(datas, list):
        datas = numpy.array(datas)
    if not isinstance(datas, numpy.ndarray):
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
        data_x, data_y = split_data(datas.copy(), idx, counts)
        yield data_x, data_y
        idx += counts


def main():
    datas = list(range(24))
    for x, y in kfold(datas, 10):
        print(x, y)

if __name__ == '__main__':
    main()
