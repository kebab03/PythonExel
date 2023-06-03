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
	if 'pag' in f:
            print('esite')
        else:
            i +=1
            print(new_name)
            os.rename(f,new_name)
	cwd=os.getcwd()
	print(cwd)
	dst=r'C:\Users\PC\Desktop\pyhton'
	with open("dog_breeds.txt", "w+") as file:
            #last_line = file.readlines()[-1]
            #print(last_line)
        file.writelines(str(i))
        file.close()
##for f in os.listdir():
##	shutil.move(f,dst)
	
	
	
