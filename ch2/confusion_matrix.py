# -*- coding: utf-8 -*-
u"""Calculation of confusion matrix for binary classification."""


def confusion_mat(y_true, y_pred):
    """
    Return:
        TP, FN, FP, TN
    """
    indexes = list(range(len(y_true)))
    t_pred = filter(lambda i: y_true[i] == y_pred[i], indexes)
    tp = len(filter(lambda i: y_pred[i] == 1, t_pred))
    tn = len(filter(lambda i: y_pred[i] == 0, t_pred))
    f_pred = filter(lambda i: y_true[i] != y_pred[i], indexes)
    fp = len(filter(lambda i: y_pred[i] == 1, f_pred))
    fn = len(filter(lambda i: y_pred[i] == 0, f_pred))
    return tn, fp, fn, tp


def main():
    y_true = [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1]
    y_pred = [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
    print confusion_mat(y_true, y_pred)

if __name__ == '__main__':
    main()
