import os
import subprocess
from pathlib import Path

directory = Path(__file__).parent

files = []
movies = []


for file_ in os.listdir(directory):
	if 'file_list' in file_:
		os.remove('file_list')
		
	if 'MOV' in file_:		
		files.append(file_)
		
clip_list = sorted(files)

with open('file_list','a') as concatenation_list:
	for line in clip_list:
		concatenation_list.write("file "+str(directory)+"/"+line+"\n")
concatenation_list.close()

file_name = input('Enter output file name: ')

command = ['ffmpeg','-f','concat','-safe','0','-i','file_list','-c','copy',str(file_name)+'.avi']

subprocess.run(command, shell = False) # concatenation
subprocess.run(fix_avi_index, shell = False)



