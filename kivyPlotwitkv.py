import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import matplotlib.pyplot as plt

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas


class PlotWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(PlotWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # create a plot and add some data
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4, 5], [2, 3, 1, 4, 2])

        # add the plot to the widget
        self.add_widget(FigureCanvas(fig))


class MyApp(App):
    def build(self):
        return PlotWidget()


if __name__ == '__main__':
    MyApp().run()
