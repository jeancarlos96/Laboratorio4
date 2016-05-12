def leertxt():
	archi=open('datos.txt','r')
	lin=archi.readline()
	print (lin)

	fr=lin.split(" ")
	print (fr)
	print (len(fr))
	archi.close()
#print (linea)
linea=leertxt()
