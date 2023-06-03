from PIL import Image
from kivy.uix.image import Image as KivyImage
import os

# Convert LaTeX equation to PNG image
equation = r'\frac{1}{2} \times \pi \times r^2'
with open('equation.tex', 'w') as f:
    f.write(r'\documentclass{article}\usepackage{amsmath}\pagestyle{empty}\begin{document}' + equation + r'\end{document}')
os.system('latex2png equation.tex')

# Display image in Kivy
img = Image.open('output1.jpg')
kivy_img = KivyImage(texture=img.texture)
