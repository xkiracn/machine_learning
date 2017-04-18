# -*- coding: utf-8 -*-
u"""Calculation of confusion matrix for binary classification."""


def confusion_mat(y_true, y_pred):
    """
    Return:
        TP, FN, FP, TN
    """
    indexes = list(range(len(y_true)))
    t_pred = [i for i in indexes if y_true[i] == y_pred[i]]
    tp = len([i for i in t_pred if y_pred[i] == 1])
    tn = len([i for i in t_pred if y_pred[i] == 0])
    f_pred = [i for i in indexes if y_true[i] != y_pred[i]]
    fp = len([i for i in f_pred if y_pred[i] == 1])
    fn = len([i for i in f_pred if y_pred[i] == 0])

    return tn, fp, fn, tp


def main():
    y_true = [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1]
    y_pred = [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
    print(confusion_mat(y_true, y_pred))

if __name__ == '__main__':
    main()
