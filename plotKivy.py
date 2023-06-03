from kivy.app import App
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
import numpy as np


class MyApp(App):
    def build(self):
        # create a layout
        layout = BoxLayout(orientation='vertical')

        # create a figure and axis
        fig, ax = plt.subplots()

        # generate some data
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # plot the data
        ax.plot(x, y)

        # add the figure to the layout
        layout.add_widget(FigureCanvasKivyAgg(fig))

        return layout


if __name__ == '__main__':
    MyApp().run()
