#IMPORTA AS BIBLIOTECAS
import os
import subprocess


fl = open('../scripts/file.txt', 'r')
for line in fl:
	os.system(line)
	
