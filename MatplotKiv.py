from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import  matplotlib.pyplot as plt
from kivy.lang import Builder
#https://www.youtube.com/watch?v=QDp9S0RWkRk&list=TLPQMjAwMjIwMjPVp7YUbmYasg&index=8
from kivy.uix.boxlayout import BoxLayout
from matplotlib.figure import Figure

x=[1,2,3,4]
y=[5,10,17,22]
# create a Figure instance
plt.plot(x,y)

plt.ylabel("y axis")
plt.ylabel("x axis")

class DemoMatplotlib(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box= self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

class MaiPl(App):
    def build(self):
        Builder.load_file("layout_yt.kv")
        return DemoMatplotlib()
MaiPl().run()


fig = Figure()


# add a subplot to the figure
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 30, 40])

# create a FigureCanvasKivyAgg instance
canvas = FigureCanvasKivyAgg(fig)

# create a BoxLayout widget and add the canvas to it
layout = BoxLayout()
layout.add_widget(canvas)

# add the layout to the canvas of a Kivy widget
kivy_widget.canvas.add(layout.canvas)
