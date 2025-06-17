###  Sucht Dateien mit der Endung _Zone.Identifier & Desktop.ini -Dateien & Dateien [otherFiles] der From .xxx_{a2n78cn5j5nv43lo9k}
		###  -->  durchsucht whole_filetree / alle subdirectories 
		###  -->  verschiebt alle gefundenen Files in gemeinsamen SammelOrdner 
		
#####################################################################################################################################


import glob
import os 
import shutil


###  INPUT_PATH
print("Quell-Pfad: ")
p = input()


###  OUTPUT_PATH
print("Ziel-Pfad: ")
op = input()


###  PATH_LIST 
p_list = glob.glob(p + '/**/*', recursive=True)


###  SUCHE & CUTTE												 		[+ PRINT & LOG] 

m = 0
d = 0																	# desktop.ini -Counter
print('\n\nEs wird durchsucht... und verschoben...\n')
for p_i in p_list:
	p_ext, ext = os.path.splitext(p_i)									# path+filename & extension
	try:
		### .IDENTIFIER  ###
		if ext == '.Identifier' and p_ext[-5:] == '_Zone' and os.path.isfile(p_i):		# tripleCheck
			print('\nZONE-IDENTIFIER')
			print(p_i)
			m = m + 1
			## LOG
			with open(op + '\___path_log.txt', "a", encoding="utf-8") as f1:
				f1.write('\n\nZONE-IDENTIFIER\n' + p_i)
			## MOVE
			if os.path.exists(op + '\\' + os.path.split(p_ext)[1] + ext):
				op_z = op + '\\' + os.path.split(p_ext)[1] + '_' + str(m) + ext
				shutil.move(p_i, op_z)
			else:
				shutil.move(p_i, op)
		###  DESKTOP.INI  ### 
		if ext.lower() == '.ini' and p_ext[-7:].lower() == 'desktop' and os.path.isfile(p_i): 			# tripleCheck
			print('\nDESKTOP-INI')
			print(p_i)
			m = m + 1
			d = d + 1
			## LOG
			with open(op + '\___path_log.txt', "a", encoding="utf-8") as f1:
				f1.write('\n\nDESKTOP-INI\n' + p_i)
			## MOVE	+ ReName
			fn = os.path.split(p_ext)[1]								# filename
			op_d = op + '\\' + fn + str(d) + ext						# renaming_variable
			shutil.move(p_i, op_d)
		###  OTHER_FILES  ### 
		if ext[0] == '.' and (ext[4] == '_' or ext[3] == '_' or ext[5] == '_') and os.path.isfile(p_i):		# für 3-, 2- & 4- Zeichen-Endungen
			print('\nOTHER-FILE')
			print(p_i)
			m = m + 1
			## LOG
			with open(op + '\___path_log.txt', "a", encoding="utf-8") as f1:
				f1.write('\n\nOTHER-FILE\n' + p_i)
			## MOVE
			if os.path.exists(op + '\\' + os.path.split(p_ext)[1] + ext):
				op_z = op + '\\' + os.path.split(p_ext)[1] + '_' + str(m) + ext
				shutil.move(p_i, op_z)
			else:
				shutil.move(p_i, op)
	except IndexError:
		#print('\nINDEX-ERROR')
		pass
	#except:
		#print('an Error occured')
		

print('\n\n' + str(m))
with open(op + '\___path_log.txt', "a", encoding="utf-8") as f1:
	f1.write('\n\n\n' + str(m))
