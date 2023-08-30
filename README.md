# ChineseTraditionalColors
中国传统色

## Setup
The python version used by author is 3.11.
`pip install matplotlib`

## Run
`python plot.py`

## Data Source
http://zhongguose.com/colors.json

对json中的玫瑰灰的RGB值进行了修正。

## Extra 3D Plot
将每种颜色绘制到HLS/HSL颜色空间中，H为平面上的角度，S为平面上的距离，L映射到垂直的Z轴上。L=50映射到Z=0，并且越远离Z=0的平面，S被映射到的距离越近，形成双圆椎体的形状。

Plot each color of Chinese traditional colors in the HLS/HSL color space, in which H is as the angle, S as distence, L as the Z-axis. L=50 is mapped to Z=0, and the color space is plotted as BiCone.

### Setup
The python version used by author is 3.11.
`pip install PySide6`
`pip install mayavi`

### Run
`python plot3d.py`
