import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyBoxLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        #self.cols = 4
        #self.orientation='vertical'
        self.cols=2
        # Input widgets
        self.x_input = TextInput(text='0', multiline=False)
        self.y_input = TextInput(text='0', multiline=False)

        # Output widgets
        self.sum_label = Label(text='Sum: 0')
        self.product_label = Label(text='Product: 0')
        #,size_hint_y=None, height=10, font_size=50)

        # Add widgets to layout
        self.add_widget(Label(text='Enter x:', pos_hint ={'center_x':.7, 'center_y':.9}))
        self.add_widget(self.x_input)
        self.add_widget(Label(text='Enter y:'))
        self.add_widget(self.y_input)
        self.add_widget(self.sum_label)
        self.add_widget(self.product_label)

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        #self.add_widget(Label(text='=p'))
        #self.add_widget(Button(text='=', on_press=self.calculateN))
class BottonLayout(BoxLayout):
    def __init__(self, my_box_layou3t, **kwargs):
        super(BottonLayout, self).__init__(**kwargs)
        self.my_box_layout = my_box_layou3t
        self.add_widget(Button(text='=', on_press=self.calculateN))

    def calculate(self):
        # Get input values
        x = float(self.my_box_layout.x_input.text)
        y = float(self.my_box_layout.y_input.text)
        # Calculate sum and product
        s = x + y
        p = x * y
        # Update output labels
        self.my_box_layout.sum_label.text = 'Sum: {}'.format(s)
        self.my_box_layout.product_label.text = 'Product: {}'.format(p)

    def calculateN(self, button):
        # Get input values
        x = float(self.my_box_layout.x_input.text)
        y = float(self.my_box_layout.y_input.text)
        # Calculate sum and product
        s = x + y
        p = x * y
        # Update output labels
        self.my_box_layout.sum_label.text = 'Sum: {}'.format(s)
        self.my_box_layout.product_label.text = 'Product: {}'.format(p)


class MyApp(App):
    def build(self):
        main_layout = MainLayout(orientation='vertical')
        second_layout = MyBoxLayout()
        tird_layout = BottonLayout(second_layout)# cui sto passando  MyBoxLayout() che
        # in 40 row stiamo dando al init function di class BottonLayout(BoxLayout)
        # per

        


        # Add the second layout to the main layout
        main_layout.add_widget(second_layout)
        main_layout.add_widget(tird_layout)
        return main_layout


if __name__ == '__main__':
    MyApp().run()
#
# class BottonLayout(BoxLayout):
#         def __init__(self, **kwargs):
#             super(BottonLayout, self).__init__(**kwargs)
#             # self.add_widget(Label(text='=p'))
#             self.add_widget(Button(text='=', on_press=self.calculateN))
#
#         def calculate(self):
#         # Get input values
#             x = float(self.x_input.text)
#             y = float(self.y_input.text)
#         #print("x:",x)
#         # Calculate sum and product
#             s = x + y
#             p = x * y
#         #print("s:" ,s)
#         # Update output labels
#             self.sum_label.text = 'Sum: {}'.format(s)
#             self.product_label.text = 'Product: {}'.format(p)
#
#         def calculateN(self, button):
#     # Get input values
#             x = float(self.x_input.text)
#             y = float(self.y_input.text)
#     # Calculate sum and product
#             s = x + y
#             p = x * y
#     # Update output labels
#             self.sum_label.text = 'Sum: {}'.format(s)
#             self.product_label.text = 'Product: {}'.format(p)
#
# class MyApp(App):
#     def build(self):
#
#
#         main_layout= MainLayout(orientation='vertical')
#         second_layout= MyBoxLayout()
#         tird_layout = BottonLayout (MyBoxLayout)
#         # Add the second layout to the main layout
#         main_layout.add_widget(second_layout)
#         main_layout.add_widget(tird_layout)
#         return main_layout
#
#
# if __name__ == '__main__':
#     MyApp().run()
