import os
import shutil


pat=r'C:\Users\PC\Desktop\pyhton\new'
os.chdir(pat)
i=20

for f in os.listdir():
	print(os.path.splitext(f)[1])
	print('ext:')
	ext=os.path.splitext(f)[1]
	print(ext)
	print('-------------')
	print(f)
	new_name='{}{}{}{}'.format("Pag_",str(i).zfill(3),'_',f)
	
	#new_name='{}{}{}'.format("Pag",str(i).zfill(3),ext)
	#.zfill(2)
	i +=1
	print(new_name)
	os.rename(f,new_name)
	cwd=os.getcwd()
	print(cwd)
	dst=r'C:\Users\PC\Desktop\pyhton'
##for f in os.listdir():
##	shutil.move(f,dst)
	
	
	
