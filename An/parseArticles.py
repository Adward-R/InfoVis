import os

fileName = open("namelist.txt", 'r')
totalName = fileName.read()
totalname = totalName.lower()
for ii in range(54):
	
#	lastName = totalname[0 : totalname.find("\t")] 
#	
#	totalname = totalname[totalname.find("\t") + 1 : ]
#	
#	if ii == 53:
#		firstName = totalname
#	else:
#		firstName = totalname[0 : totalname.find("\n")]
#		
#	currName = firstName + " " + lastName;
#	totalname = totalname[totalname.find("\n") + 1 : ]
#	
#	print currName
	currName = "isia";


	for i in range(844):
		
		file = str(i + 1) + '.txt'
		if not os.path.exists("trimmed/" + file):
			continue
		f = open("trimmed/" + file, 'r')
		strInFile = f.read()
		strinfile = strInFile.lower()
		if (strinfile.find(currName) >= 0):
			currDir = "name/" + currName + "/";
			if not os.path.exists(currDir):
				os.mkdir(currDir)
			fout = open(currDir + file, 'w')
			fout.write(strInFile)
			fout.close()
		f.close()
	

