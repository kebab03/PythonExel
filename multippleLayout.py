import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        # Create and add widgets to the main layout
        button1 = Button(text="Button 1")
        button2 = Button(text="Button 2")
        self.add_widget(button1)
        self.add_widget(button2)


class SecondLayout(GridLayout):
    def __init__(self, **kwargs):
        super(SecondLayout, self).__init__(**kwargs)

        # Create and add widgets to the second layout
        button3 = Button(text="Button 3")
        button4 = Button(text="Button 4")
        self.add_widget(button3)
        self.add_widget(button4)


class MyApp(App):
    def build(self):
        # Create the main layout and the second layout
        main_layout = MainLayout(orientation='vertical')
        second_layout = SecondLayout(cols=2)

        # Add the second layout to the main layout
        main_layout.add_widget(second_layout)

        return main_layout


if __name__ == '__main__':
    MyApp().run()
