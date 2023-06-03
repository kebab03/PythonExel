# import required packages
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# get current working directory
base_path = os.getcwd()
print(base_path, "="*200)

# provide path to tesseract exe
# pytesseract.pytesseract.tesseract_cmd = os.path.join(base_path, "tesseract.exe")
pytesseract.pytesseract.tesseract_cmd = os.path.join(r"C:\Users\PC\AppData\Local\Tesseract-OCR\tesseract.exe")

# call the tk module
root = tk.Tk()

# it will close second window automatically
root.withdraw()

# it will auto focus on the opened pop up box
root.focus_force()

# show popup box asking for select the image    
file_path = filedialog.askopenfile(mode="r", parent=root, title="Select Image File")

# run the script as standalone
if __name__ == "__main__":
    # First it will open the image and then will convert to text
    txt = pytesseract.image_to_string(Image.open(file_path.name))
    print(txt)
    # write extracted text to text file
    with open(os.path.join(base_path, "tes1t.txt"), "w") as f:
        f.write(txt)
    # show popup box which shows where we have saved the file
    messagebox.showinfo("showinfo", "Text file has been written to {}".format(os.path.join(base_path, "test.txt")))
