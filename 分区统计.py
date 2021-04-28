# -*- coding: utf-8 -*-
"""
@Time: 2021/4/28 16:02
@Author: puffy
@FileName: aa_test.py
"""
import numpy as np
import pandas as pd

aa = np.ones((10, 10))
aa[1:3, 2:4] = 3
aa[5:8, 6:9] = 2

bb = np.ones((10, 10)) + 200
bb[4:9, 3:8] = 100


def max_square_dist(x):
    res = (x-np.nanmean(x))**2
    return np.nanmax(res)


def statistics_by_zone(area, img, func=None):
    """

        :param area: 2D-numpy
        :param img: 2D-numpy
        :param func: 自定义函数， 默认均值
        :return:
        """
    info = {'area': area.flatten(),
            'img': img.flatten()}
    ds = pd.DataFrame(info)
    if func is not None:
        stat = ds.groupby('area').agg(func)
    else:
        stat = ds.groupby('area').agg('mean')

    return stat


print(statistics_by_zone(aa, bb, [max_square_dist]))
