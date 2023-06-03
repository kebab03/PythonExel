from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
from PIL import Image

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        # Create a button and add it to the layout
        self.my_button = Button(text="My Button")
        self.add_widget(self.my_button)

        # Load an image and create a Texture from it
        pil_img = Image.open("outfile.jpg")
        texture = Texture.create(size=pil_img.size)
        texture.blit_buffer(pil_img.tobytes(), colorfmt='rgb', bufferfmt='ubyte')

        # Set the Texture as the button's background
        self.my_button.background_normal = ''
        self.my_button.background_disabled_normal = ''
        self.my_button.background_color = [0, 0, 0, 0]
        self.my_button.canvas.before.add(
            Button.background_down, texture, self.my_button.texture_size)

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
