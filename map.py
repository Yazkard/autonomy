import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA


def unit_vector(vector):
    return vector / np.linalg.norm(vector)


def angle_between(vector1, vector2):
    v1_u = unit_vector(vector1)
    v2_u = unit_vector(vector2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

xd, xd2 = [], []
for i in range(0, 100):
    xd.append(angle_between((0, 1), (-(i/10), 10-(i/10))))

print(np.power(0.25*np.pi, 2), np.power(0.5*np.pi, 2), np.power(0.75*np.pi, 2))
print(np.power(0.5*np.pi, 2) - np.power(0.25*np.pi, 2), np.power(0.75*np.pi, 2) - np.power(0.5*np.pi, 2))
print((np.power(0.5*np.pi, 2) - np.power(0.25*np.pi, 2))/np.power(0.75*np.pi, 2), (np.power(0.75*np.pi, 2) - np.power(0.5*np.pi, 2))/np.power(0.75*np.pi, 2))
print(np.power(2, 0.25*np.pi), np.power(2, 0.5*np.pi), np.power(2, 0.75*np.pi))
print(np.power(2, 0.5*np.pi) - np.power(2, 0.25*np.pi), np.power(2, 0.75*np.pi) - np.power(2, 0.5*np.pi))
print((np.power(2, 0.5*np.pi) - np.power(2, 0.25*np.pi))/np.power(2, 0.75*np.pi), (np.power(2, 0.75*np.pi) - np.power(2, 0.5*np.pi))/np.power(2, 0.75*np.pi))
print(np.power(0.25*np.pi, 0.25*np.pi), np.power(0.5*np.pi, 0.5*np.pi), np.power(0.75*np.pi, 0.75*np.pi))
print(np.power(0.5*np.pi, 0.5*np.pi) - np.power(0.25*np.pi, 0.25*np.pi), np.power(0.75*np.pi, 0.75*np.pi) - np.power(0.5*np.pi, 0.5*np.pi))
print((np.power(0.5*np.pi, 0.5*np.pi) - np.power(0.25*np.pi, 0.25*np.pi))/np.power(0.75*np.pi, 0.75*np.pi), (np.power(0.75*np.pi, 0.75*np.pi) - np.power(0.5*np.pi, 0.5*np.pi))/np.power(0.75*np.pi, 0.75*np.pi))


x = np.linspace(0, np.pi*0.8, num=100)
ax = host_subplot(111, axes_class=AA.Axes)
#plt.plot(x, xd)
ax.plot(x, np.power(x, 2), 'r')
ax.plot(x, np.power(2, x), 'b')
ax.plot(x, np.power(x, x), 'g')
#ax.plot(x, np.power(x*x, x), 'p')
ax.axis('tight')

ax2 = ax.twin()  # ax2 is responsible for "top" axis and "right" axis
ax2.set_xticks([0., 0.25*np.pi,.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi])
ax2.set_xticklabels(["$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
ax2.axis["right"].major_ticklabels.set_visible(False)
ax2.axis["top"].major_ticklabels.set_visible(True)

plt.show()
