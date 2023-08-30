# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:09:10 2023

@author: FlyingNbF4
"""

import json
import colorsys
from math import sin, cos, pi
from mayavi import mlab

with open('colors.json', 'r') as file:
    colors = json.load(file)

def rgb_to_hls(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h * 360.0, l * 100.0, s * 100.0

# 创建Mayavi场景
mlab.figure()

# Plot points
for color in colors:
    h, l, s = color["HLS"] = rgb_to_hls(*color["RGB"])
    z0 = l - 50
    rate = (50 - abs(z0)) / 50 * s
    hr = h / 180.0 * pi
    x = rate * cos(hr)
    y = rate * sin(hr)
    z = z0 * 2
    # 绘制3D散点图
    r, g, b = color["RGB"]
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mlab.points3d(x, y, z, color=(r, g, b), mode='cube', scale_factor=2, resolution=8)
    mlab.text3d(x, y, z, "   " + color["pinyin"] + "\n   " + color["hex"], color=(r, g, b))

# Plot L layers
for l in range(5):
    z = l * 25 - 50
    z *= 2
    mlab.text3d(0, 0, z, f" L={l * 25}", color=(1, 1, 1))
    if l > 0 and l < 4:
        # Plot S circles
        for r in [100, 75, 50, 25]:
            rate = (50 - abs(z/2)) / 50
            x = [(rate * r * cos(a / 180.0 * pi)) for a in range(360)]
            y = [(rate * r * sin(a / 180.0 * pi)) for a in range(360)]
            z2 = [z for _ in range(360)]
            mlab.plot3d(x, y, z2, color=(1, 1, 1))
            mlab.text3d(0, rate * r, z, f" S={r}", color=(1, 1, 1))
            mlab.text3d(0, rate * -r, z, f" S={r}", color=(1, 1, 1))

# Plot links
for a in [30, 90, 150, 210, 270, 330]:
    x = cos(a/180.0*pi) * 100
    y = sin(a/180.0*pi) * 100
    mlab.plot3d([0, x, 0], [0, y, 0], [100, 0, -100], color=(1, 1, 1))
    mlab.plot3d([0, x * 0.00001, 0], [0, y * 0.00001, 0], [100, 0, -100], color=(1, 1, 1))

# 显示Mayavi场景
mlab.view(azimuth=300, elevation=80)
mlab.show()