import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['savefig.dpi'] = 300
# 计算曲线上的点的和y坐标
x = np.arange(0, 3*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
#使用Matplotlib绘制点，并添加fmt和kwargs属性
plt.plot(x, y_sin, '-',
        label='Sine Wave',#图例标签
        linewidth=1,#线宽
        color='red',#线的颜色
        marker='',#标记样式
        markersize=5,  #标记的大小
        markeredgecolor='black',#标记边缘的颜色
        markeredgewidth=1,  #标记边缘的宽度
        markerfacecolor='none',#标记内部的颜色
        alpha=0.5#透明度
        )
plt.plot(x, y_cos, '-',
        label='cose Wave',#图例标签
        linewidth=1,#线宽
        color='blue',#线的颜色
        marker='',#标记样式
        markersize=5,  #标记的大小
        markeredgecolor='black',#标记边缘的颜色
        markeredgewidth=1,  #标记边缘的宽度
        markerfacecolor='none',#标记内部的颜色
        alpha=0.5#透明度
        )


#显示图例
plt.legend()
#显示图形
plt.show()