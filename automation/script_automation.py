#IMPORTA AS BIBLIOTECAS
import os
import subprocess
import datetime as dt

path_read = '../scripts/'
path_files = os.listdir(path_read)

for cmd in path_files:
	atual_file = path_read+str(cmd)
	fl = open(atual_file, 'r')
	for line in fl:
		os.system(line)

	#ESCREVE O ARQUIVO DE LOG!
	path_write = '../log/'
	file_write = open(path_write + "log_file.txt", "a+")
	file_write.write('Script '+ str(cmd)+' rodado as: ' + str(dt.datetime.now()))
	file_write.write('\n\n')
	file_write.close()
