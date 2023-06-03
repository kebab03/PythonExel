
from kivy.app import App
from kivy.lang import Builder

kv = """
BoxLayout:
    orientation: 'vertical'
    Label:
        font_size: 40  
        text: 'Literals: ∫ ∑ ∏ Ω ∞'
    Label:
        font_size: 40
        
        text: 'Unicode: \N{GREEK SMALL LETTER PI} \N{Integral} \N{Greek Capital Letter Sigma}'
    Label:
        font_size: 40
        font_name: 'Asana-Math.ttf'
        text: 'Asana: \N{GREEK SMALL LETTER PI} \N{Greek capital letter Omega} \N{Greek Capital Letter Sigma}'
"""


class TestSymbolApp(App):
    def build(self):
        return Builder.load_string(kv)


TestSymbolApp().run()