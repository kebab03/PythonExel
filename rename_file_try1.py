import os
import shutil


pat=r'C:\Users\PC\Desktop\pyhton\new'
os.chdir(pat)
i=27

for f in os.listdir():
    print(os.path.splitext(f)[1])
    print('ext:')
    ext=os.path.splitext(f)[1]
    print(ext)
    print('-------------')
    print(f)
    new_name='{}{}{}{}'.format("Pag_",str(i).zfill(3),'_',f)
    if 6 > 2 :
            print('f')
a = 200
b = 33
if b > a:
    
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
    
    
