###  Sucht Desktop.ini -Dateien & Dateien mit der Endung _Zone.Identifier 
		###  -->  durchsucht whole_filetree / alle subdirectories 
		###  -->  kopiert alle gefundenen Files in gemeinsamen SammelOrdner 
		###			(dort kann nochma drübergeschaut, gelöscht, gebackuppt werden) 



import glob
import os 


###  INPUT_PATH 

p = r'C:\Users\Dell\Desktop\Räume\Festplatte_nicht-erkannt\nachtrag\PC_Software\identify_files\test_files'
#print(p)
#print("Gebe StartOrdner-Pfad ein: ")									# Einfach Pfad aus der Adressleiste des Windows-Explorers kopieren und einfügen 
#p = input()


p_list = glob.glob(p + '/**/*', recursive=True)							# auchma mit 'walk' probiern? ; glob.glob aus: pathLength_get_v3_subFolder.py



###  SUCHE & CUTTE : _Zone.Identifier & desktop.ini & otherFiles 

n = 0
m = 0
#print('Es wird durschsucht... und verschoben...')
for p_i in p_list:
	#print(p_i)
	#ext = os.path.splitext(p_i)[0]										# extension ohne path+filename [0=>path+filename , 1=extension]  -> splitext gibt (Liste/)Tupel aus
	#split = os.path.splitext(p_i)											# same, und dann aber split[0] & split[1] zum Ansteuern
	p_ext, ext = os.path.splitext(p_i)										# same, aber mit beiden als Variablen
	#print(ext)
	n = n + 1
	#print(p_ext[-5:])
	try:																	# # because FM: "string index out of range"  (-> ext ist kürzer als bei OTHER_FILE erfragt, auch_mögl.bei p_ext kürzer '_Zone' (oder 'desktop'))
		if ext == '.Identifier' and p_ext[-5:] == '_Zone' and os.path.isfile(p_i): 	# tripleCheck=safer , letzen_5_Zeichen von path+filename == '_Zone' & isFile 
			print('\nZONE-IDENTIFIER')
			print(ext)
			print(p_i)
			m = m + 1
			#hier dann cut-Befehl
		#filename = os.path.split(p_ext)[1]									# splittet filename/name_nach_letztem_'\' vom path , p_ext[-7:] == 'desktop'  ist aber kürzer
		#print(filename)
		#print(p_ext[-7:])													# same, nur per splitext
		## ZUSAMMENFASSEN? : beide if-statements mit EINEM 'or' verbinden
		if ext == '.ini' and p_ext[-7:] == 'desktop' and os.path.isfile(p_i): 		# tripleCheck=safer   (TripleAbgleich)
			print('\nDESKTOP-INI')
			print(ext)
			print(p_i)
			m = m + 1
			#hier dann cut-Befehl
		#if ext == '.jpg_*':			# DOESNT_WORK, need wildcard
		if ext[0] == '.' and (ext[4] == '_' or ext[3] == '_' or ext[5] == '_') and os.path.isfile(p_i):		# ohne try/except: FM: string index out of range   (->für die ext die kürzeren Index haben)
			print('\nOTHER-FILE')
			print(ext)
			print(p_i)
			m = m + 1
			#hier dann cut-Befehl
	except IndexError:
		#print('\nINDEX-ERROR')											# printet & passes   (->desktop.ini & NORMAL-FILES)
		pass
	except: 															# 2.except für andere Fehler 
		print('an Error occured')
	# else:
		# print('no Error')												# wird bei desktop.ini nicht ausgeführt, da hier IndexErrors (die gepasst werden), ebenso bei allen NORMAL-FILES
		

            
	## VERSCHIEBEN : nach test_files_collect
		## siehe BackUp_DDHR

#print(len(p_list))														# Summe aller Pfade inkl.OrdnerPfade
#print(n)																# Vergleich: Wurden alle Pfade behandelt? -> Ja, auch die OrdnerPfade -> ext bleibt dann leer (=keineExtension)
print('\n\n' + str(m))																# Soll=28+3+3


##  isFile -> als TripleCheck bei jedem if  :  os.path.isfile(p_i)

##  strange(/other)Files-Endungen integrieren : .jpg_{a2n78cn5j5nv43lo9k}
	##  -> ".jpg_*" , ".pdf_*" , ".mp3_*"  -> fkt.mit WildCard? , oder ext[0:4] ist eine der drei
		##  (-> falls es weitere Extensions als diese 3 gibt müsste ich diese erstmal kennen) 
	##  -> separater _Zone.Identifier-Abgleich wäre dann teilweise redundant, aber mach dennoch 
		##  (weil Muster ".ext_" dort ebenfalls auftritt, allerdings würde split/-text sie nicht identifizieren, da .Identifier die eigentliche Extension ist) 
	##  -> Whrs.gibt es auch noch andere Endungen? -> .png_ , .tiff_ , .txt_ , ... ? 
		##  -> mit WildCards lösen? -> .***_... , .**_... , .****_... -> fkt.whrs.nich 
			##  -> checke tracklist_formatter 
		##  -> oder besser direkt über Indizes : ext[0] == '.' and (ext[4] == '_' or ext[3] == '_' or ext[5] == '_')
		##  -> Vlt.dies in separate Datei, weil so optische Abgleich einfacher ? 

##  TRY-EXCEPT_ERROR-HANDLING 

##  DELETE am Anfang um test_files_collect zu bereinigen? Muss vlt.nich...
##  ZURÜCK-KOPIEREN aus test_files_BU? dann auch nich...

##  ABGLEICH m vor&nach VERSCHIEBEN 

##  PFADE_loggen ? 
