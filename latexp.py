import easylatex2image
from easylatex2image import latex_to_image

packages_and_commands = r"""\usepackage[parfill]{parskip}
\usepackage[german]{varioref}
\usepackage{url}
\usepackage{amsmath} 
\usepackage{dcolumn}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows}
\usetikzlibrary{intersections}
\usepackage[all,cmtip]{xy}
"""

content = r"""
\xymatrix{M \ar[d]_\kappa \ar[r]^f & A\\ K \ar[ur]_{f_K}}
"""
latex_code = r"$\frac{1}{2} + \frac{1}{4} = \frac{3}{4}$"
pmwe=r"""$\frac{a}{9}$"""
pmw=r"""$\sum_{i}^{∞}{ \frac{a}{9}}$"""
#pillow_image = latex_to_image(packages_and_commands,content,"output.jpg",dpi=500,img_type="JPEG")
pillow_image = latex_to_image(packages_and_commands,pmwe,"output5.jpg",dpi=500,img_type="JPEG")