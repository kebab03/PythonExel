import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class FirstScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)

        # Create a button
        button = Button(text="Go to Second Screen")

        # Bind the button to a method
        button.bind(on_press=self.go_to_second_screen)

        # Add the button to the layout
        self.add_widget(button)

    def go_to_second_screen(self, instance):
        # Create an instance of the second screen
        second_screen = SecondScreen(variable="Hello, World!")

        # Set the app's root widget to the second screen
        app = App.get_running_app()
        app.root = second_screen


class SecondScreen(BoxLayout):
    def __init__(self, variable, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

        # Create a label with the passed variable
        label = Label(text=variable)

        # Add the label to the layout
        self.add_widget(label)


class MyApp(App):
    def build(self):
        # Create the first screen and set it as the root widget
        first_screen = FirstScreen()
        self.root = first_screen


if __name__ == '__main__':
    MyApp().run()
