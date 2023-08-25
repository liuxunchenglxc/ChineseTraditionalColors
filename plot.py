# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:55:46 2023

@author: FlyingNbF4
"""

import json
import colorsys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.font_manager import FontProperties
from math import log2

zh_font = FontProperties(fname='C:\Windows\Fonts\simkai.ttf')

with open('colors.json', 'r') as file:
    colors = json.load(file)

def rgb_to_hls(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h * 360.0, l * 100.0, s * 100.0

for i in range(len(colors)):
    colors[i]["HLS"]=rgb_to_hls(*colors[i]["RGB"])

colors = sorted(colors, key=lambda x: x["HLS"][0])

def put_color_pos(colors, ncol, nrow):
    for i in range(ncol):
        first = i * nrow
        tail = min(first + nrow, len(colors))
        colors[first: tail] = sorted(colors[first: tail], 
                                     key=lambda x: (60 - 0.6 * (x["HLS"][1] - 60))*log2(x["HLS"][2])
                                     if x["HLS"][1] > 60 
                                     else x["HLS"][1]*log2(x["HLS"][2]))
        for j in range(first, tail):
            colors[j]["xy"] = (i, j + nrow - tail)
    return colors

def plot_hls_color_blocks(colors, ncol, nrow, fname):
    fig, ax = plt.subplots(figsize=(ncol, nrow * 2))

    for color in colors:
        x, y = color["xy"]
        x *= 10
        y *= 20
        rgb = color["hex"]
        rect = Rectangle((x+0.5, y+5), 9, 15, color=rgb)
        ax.add_patch(rect)
        ax.text(x + 5, y + 4, f'{color["name"]}', ha='center', va='center', fontsize=8, fontproperties=zh_font)
        ax.text(x + 5, y + 2.5, f'RGB: {rgb}', ha='center', va='center', fontsize=8)

    ax.set_xlim(0, ncol * 10)
    ax.set_ylim(0, nrow * 20)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(fname + '.pdf')
    print(fname + '.pdf' + " done")
    plt.close()

colors = put_color_pos(colors, 88, 6)
plot_hls_color_blocks(colors, 88, 6, "中国传统色")

def select_color(colors, min_s, max_s, min_l, max_l):
    for color in colors:
        h, l, s = color["HLS"]
        if min_s <= s and s < max_s and min_l <= l and l < max_l:
            yield color

selected_colors = list(select_color(colors, 80.0, 100.1, 45.0, 70.0))
# print(len(selected_colors))
selected_colors = put_color_pos(selected_colors, 26, 4)
plot_hls_color_blocks(selected_colors, 26, 4, "中国传统色高饱和中亮度")

selected_colors = list(select_color(colors, 40.0, 80.5, 41.0, 70.0))
# print(len(selected_colors))
selected_colors = put_color_pos(selected_colors, 24, 4)
plot_hls_color_blocks(selected_colors, 24, 4, "中国传统色中饱和中亮度")

selected_colors = list(select_color(colors, 0, 40.0, 45.0, 70.0))
# print(len(selected_colors))
selected_colors = put_color_pos(selected_colors, 13, 4)
plot_hls_color_blocks(selected_colors, 13, 4, "中国传统色低饱和中亮度")

selected_colors = list(select_color(colors, 80.0, 100.1, 70.0, 100.1))
# print(len(selected_colors))
selected_colors = put_color_pos(selected_colors, 9, 2)
plot_hls_color_blocks(selected_colors, 9, 2, "中国传统色高饱和高亮度")

selected_colors = list(select_color(colors, 40.0, 80.5, 70.0, 100.1))
# print(len(selected_colors))
selected_colors = put_color_pos(selected_colors, 17, 3)
plot_hls_color_blocks(selected_colors, 17, 3, "中国传统色中饱和高亮度")

selected_colors = list(select_color(colors, 0, 40.0, 70.0, 100.1))
# print(len(selected_colors))
selected_colors = put_color_pos(selected_colors, 13, 3)
plot_hls_color_blocks(selected_colors, 13, 3, "中国传统色低饱和高亮度")

selected_colors = list(select_color(colors, 80.0, 100.1, 0, 45.0))
# print(len(selected_colors))
selected_colors = put_color_pos(selected_colors, 6, 2)
plot_hls_color_blocks(selected_colors, 6, 2, "中国传统色高饱和低亮度")

selected_colors = list(select_color(colors, 40.0, 80.5, 0, 41.0))
# print(len(selected_colors))
selected_colors = put_color_pos(selected_colors, 24, 4)
plot_hls_color_blocks(selected_colors, 24, 4, "中国传统色中饱和低亮度")

selected_colors = list(select_color(colors, 0, 40.0, 0, 45.0))
# print(len(selected_colors))
selected_colors = put_color_pos(selected_colors, 18, 4)
plot_hls_color_blocks(selected_colors, 18, 4, "中国传统色低饱和低亮度")

