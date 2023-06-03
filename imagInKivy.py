from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout

class MyLabel(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        image_url = 'output1.jpg'
        image = AsyncImage(source=image_url)
        self.add_widget(image)
        text = 'This is a label with an image'
        label = Label(text=text)
        self.add_widget(label)

class MyApp(App):
    def build(self):
        return MyLabel()

if __name__ == '__main__':
    MyApp().run()
