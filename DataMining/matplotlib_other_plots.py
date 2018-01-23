import numpy as np 
import matplotlib.pyplot as plt 

def main():
	fig = plt.figure()
	# 散点图
	ax = fig.add_subplot(3, 3, 1)			# 获取子图句柄
	n = 128									# 数据		
	X = np.random.normal(0, 1, n)
	Y = np.random.normal(0, 1, n)
	T = np.arctan2(Y, X)					# 颜色数据
	plt.scatter(X, Y, s=25, c=T, alpha=0.5)	# 绘制散点
	plt.xlim(-1.5, 1.5), plt.xticks([])		# 横纵坐标
	plt.ylim(-1.5, 1.5), plt.yticks([])
	plt.title("Scatter")
	plt.xlabel("X")
	plt.ylabel("Y")

	# 柱状图
	ax = fig.add_subplot(332)
	n = 10
	X = np.arange(n)
	Y1 = (1 - X/float(n) * np.random.uniform(0.5, 1.0, n))
	Y2 = (1 - X/float(n) * np.random.uniform(0.5, 1.0, n))
	ax.bar(X, +Y1, facecolor="#9999ff", edgecolor="white")
	ax.bar(X, -Y2, facecolor="#ff9999", edgecolor="white")
	for x, y in zip(X,Y1):
		plt.text(x+0.4, y+0.05, "%.2f" %y, ha="center", va="bottom")
	for x, y in zip(X,Y2):
		plt.text(x+0.4, -y-0.05, "%.2f" %y, ha="center", va="top")	

	# 饼状图
	fig.add_subplot(333)
	n = 20
	Z = np.ones(n)
	Z[-1] = 2
	plt.pie(Z, explode=Z*0.05, colors=["%f" %(i/float(n)) for i in range(n)],
		labels=["%0.2f" %(i/float(n)) for i in range(n)])
	plt.gca().set_aspect("equal")
	plt.xticks([]), plt.yticks([])

	# 极坐标图
	fig.add_subplot(334, polar=True)
	n = 20
	theta = np.arange(0.0, 2*np.pi, 2*np.pi/float(n))
	radi = 10*np.random.rand(n)
	plt.plot(theta, radi)
	# plot.polar(theta, radi)

	# 热图
	fig.add_subplot(335)
	from matplotlib import cm
	data = np.random.rand(3, 3)
	cmap = cm.Blues
	map = plt.imshow(data, interpolation="nearest", cmap=cmap, aspect="auto",
		vmin=0, vmax=1)

	# 三维图
	from mpl_toolkits.mplot3d import Axes3D
	ax = fig.add_subplot(336, projection="3d")
	ax.scatter(1,1, s=50)

	# 热力图
	fig.add_subplot(313)
	def f(x, y):
		return (1 - x/2 + x**5 +y**3) * np.exp(-x**2 - y**2)
	n = 256
	x = np.linspace(-3, 3, n)
	y = np.linspace(-3, 3, n)
	X,Y = np.meshgrid(x, y)
	plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

	plt.show()
main()