import os
import shutil
import pytesseract
from PIL import Image
pat=r'C:\Users\PC\Desktop\pyhton\new'
os.chdir(pat)
i=0

pytesseract.pytesseract.tesseract_cmd = os.path.join(r"C:\Users\PC\AppData\Local\Tesseract-OCR\tesseract.exe")

##with open("dog_breeds.txt", 'r+') as file:
##        last_line = file.readlines()
##        print('last_line_--:',last_line)
                
for f in os.listdir():
##        if file.closed :
##                print("\nThe file is closed.")
        print(os.path.splitext(f)[1])
        print('ext-00--:',end='')
        ext=os.path.splitext(f)[1]
        print(ext)
        print('-------------')
        print(f)
        #new_name='{}'.format(f[:4]+str(i).zfill(3)+f[7:])
        new_name='{}'.format(str(i).zfill(3)+'_'+f[3:])
        if 'Pag' in f and f.endswith(".jpg"):
            print('---esite-----------')
        elif '.jpg' in f:
            print('esite_new')    
            i +=1
            print(new_name)
            os.rename(f,new_name)
        cwd=os.getcwd()
        print('cwd:',cwd)
        dst=r'C:\Users\PC\Desktop\pyhton\cal'
##        with open("dog_breeds.txt", 'r+') as file:
##for f in os.listdir():
##      shutil.move(f,dst)
##        
        
        
