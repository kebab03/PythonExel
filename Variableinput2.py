from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class InputScreen(Screen):
    input_number = ObjectProperty(None)

    def submit(self):
        number = int(self.input_number.text)
        app = App.get_running_app()
        app.root.get_screen('output').generate_input_boxes(number)
        app.root.current = 'output'


class OutputScreen(Screen):
    inputs_layout = ObjectProperty(None)

    def generate_input_boxes(self, number):
        self.inputs_layout.clear_widgets()
        for i in range(number):
            input_box = TextInput(hint_text=f'Input {i+1}')
            self.inputs_layout.add_widget(input_box)

        self.inputs_layout.add_widget(Label(text='Output:', size_hint=(1, None), height=50))
        self.result_label = Label(text='', size_hint=(1, None), height=50)
        self.inputs_layout.add_widget(self.result_label)

    def calculate_result(self):
        inputs = [float(child.text) for child in self.inputs_layout.children if isinstance(child, TextInput)]
        result = sum(inputs)
        self.result_label.text = f'The sum of the inputs is: {result}'


class WindowManager(ScreenManager):
    pass


kv = Builder.load_string('''
WindowManager:
    InputScreen:
    OutputScreen:

<InputScreen>:
    name: 'input'
    input_number: input_number_id
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter the number of input boxes:'
        TextInput:
            id: input_number_id
            multiline: False
        Button:
            text: 'Submit'
            on_press: root.submit()

<OutputScreen>:
    name: 'output'
    inputs_layout: inputs_layout_id
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Enter the input values:'
        ScrollView:
            BoxLayout:
                id: inputs_layout_id
                orientation: 'vertical'
        Button:
            text: 'Calculate Result'
            on_press: root.calculate_result()
''')

class MyApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyApp().run()
