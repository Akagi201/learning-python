#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

x = np.linspace(0, 2*np.pi+np.pi/4, 10)
y = np.sin(x)

x_new = np.linspace(0, 2*np.pi+np.pi/4, 100)
f_linear = interpolate.interp1d(x, y)

para_bspline = interpolate.splrep(x, y)
y_bspline = interpolate.splev(x_new, para_bspline)

plt.subplot(212)
plt.plot(x, y, "o", label=u"原始数据")
plt.plot(x_new, f_linear(x_new), label=u"线性插值")
plt.plot(x_new, y_bspline, label=u"B-spline插值")
plt.legend()
plt.grid(True)

plt.show()