import numpy as np 
import matplotlib.pyplot as plt

def main():
	"""matplotlib包中pyplot.line的使用"""
	# 数据准备
	x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
	c,s = np.cos(x),np.sin(x)
	# 新建空白图框
	plt.figure()
	# 绘图函数
	plt.plot(x, c, color="blue", linewidth=1, linestyle="-", label="COS", alpha=0.5)
	plt.plot(x, s, "r--", linewidth=1.0, label="SIN")
	# 标题
	plt.title("COS & SIN") 
	# 获取坐标周句柄
	ax = plt.gca()
	# 设置坐标线														
	ax.spines["right"].set_color("none")
	ax.spines["top"].set_color("none")
	ax.spines["left"].set_position(("data", 0))
	ax.spines["bottom"].set_position(("data", 0))
	# 设置坐标刻度
	ax.xaxis.set_ticks_position("bottom")
	ax.yaxis.set_ticks_position("left")
	plt.xticks([-np.pi, -np.pi/2.0, 0, np.pi/2, np.pi],
		[r'$-\pi$', r'$-\pi/2.0$', r'$0$', r'$+\pi/2.0$', r'$+\pi$'])
	plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
	for label in ax.get_xticklabels()+ax.get_yticklabels():
		label.set_fontsize(12)
		label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.2))
	# 设置坐标范围
	plt.axis([-np.pi, np.pi, -1, 1])
	# 添加图例
	plt.legend(loc="upper left")
	# 添加格网
	plt.grid()
	# 填充区域
	plt.fill_between(x, np.abs(x)<0.5, c, c>0.5, color="green", alpha=0.5)
	# 添加注释
	t = 1
	plt.plot([t, t],[0, np.cos(t)], "y", linewidth=1.0, linestyle="-.")
	plt.annotate("cos(1)", xy=(t, np.cos(1)), xycoords="data", xytext=(+10, +30),
		textcoords="offset points", arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=0.2"))
	# 显示图形
	plt.show()

main()