from kivy.app import App
from kivy.garden.tex import Label as TexLabel

class MyApp(App):
    def build(self):
        return TexLabel(text=r'$\frac{1}{2}$')

if __name__ == '__main__':
    MyApp().run()
