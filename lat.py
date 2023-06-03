from kivy.app import App
from kivy.uix.image import Image
from pylatexenc.latex2image import (
    get_default_latex_compiler,
    generate_filename_for_latex,
    latex2image,
)

class MyApp(App):
    def build(self):
        # Convert the LaTeX formula to an image file
        formula = r'\LaTeX{}'
        filename = generate_filename_for_latex(formula)
        latex2image(
            formula=formula,
            filename=filename,
            keep_file=True,
            latex_compiler=get_default_latex_compiler(),
        )
        
        # Load the image file into a Kivy Image widget
        img = Image(source=filename)
        
        # Return the Image widget as the root widget
        return img

if __name__ == '__main__':
    MyApp().run()

