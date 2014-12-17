from matplotlib import pyplot as plt
import numpy as np
from matplotlib.widgets import Button
from besie import *
#


t=np.linspace(0,1,100)
class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = []
        self.ys = []
        self.x  = []
        self.y  = []
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        #print('click', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.x.append(event.x)
        self.y.append(event.y)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()
        

    def create(self,event):
        xy = list(zip(self.xs,self.ys))
        converted = []
        for elem in xy:
            converted.append(np.array(elem))
        xy = converted
        res=[B(t[i],xy) for i in range(len(t))]
        #print(type(res))
        xy = list(zip(*res))
       # print(xy[0])
        x  = list(xy[0])
        y  = list(xy[1])
        self.line.set_data(x,y)
        #print(x)
        #print(y)
        self.line.figure.canvas.draw()

    def flush(self,event):
        self.line.set_data([0],[0])
        self.xs = []
        self.ys = []
        self.line.figure.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
b = Button(plt.axes([0.7, 0.02, 0.1, 0.035]),label='Create')
b2 = Button(plt.axes([0.4, 0.02, 0.1, 0.035]),label='Clear')

ax.set_title('click to build line segments')
line, = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)
b.on_clicked(linebuilder.create)
b2.on_clicked(linebuilder.flush)
plt.show()