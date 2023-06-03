from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from kivy.core.text import Label as CoreLabel

class MathLabel(Label):
    def __init__(self, **kwargs):
        super(MathLabel, self).__init__(**kwargs)

    def on_size(self, *args):
        self.texture_update()

    def texture_update(self, *args):
        # do some custom stuff here
        super().texture_update(*args)
        try:
            # create a core label to render the LaTeX formula
            label = CoreLabel(text=self.text, font_size=self.font_size,
                              font_name='Asana-Math.ttf')

            # render the label
            label.refresh()

            # get the texture
            tex = label.texture

            # set the texture size
            tex_size = list(tex.size)
            tex_size[0] *= 2
            tex_size[1] *= 2

            # create a new texture to resize the original texture
            new_tex = Texture.create(size=tuple(tex_size))

            # resize the original texture
            new_tex.blit_buffer(tex.pixels, colorfmt='rgba', bufferfmt='ubyte',
                                source_size=tex.size)

            # set the texture to the label
            self.texture = new_tex

        except Exception as e:
            print(e)

class MyLabelApp(App):
    def build(self):
        # create a label with a LaTeX formula
        label = MathLabel(text=r'$\frac{1}{2}$',
                          font_size=50, font_name='Asana-Math.ttf')
        return label

if __name__ == '__main__':
    MyLabelApp().run()
